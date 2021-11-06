import boto3
import logging
import json
import pickle

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_s3_client(access_key, secret_key) -> boto3.client:
    """
    Creates and returns a S3 client object

    :param access_key: AWS access key
    :param secret_key: AWS secret key
    :return: S3 client object
    """
    return boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)


def get_s3_resource(access_key, secret_key) -> boto3.resource:
    """
    Creates and returns a S3 resource object
    :param access_key: AWS access key
    :param secret_key: AWS secret key
    :return: S3 resource object
    """
    return boto3.resource('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)


def get_file_index(s3res, bucket, prefix):
    """
    Returns a dictionary of file names and their corresponding keys

    :param s3res: S3 resource object
    :param bucket: S3 bucket name
    :param prefix: S3 prefix
    :return: List of file names in the given bucket and prefix
    """
    return [obj.key for obj in s3res.Bucket(bucket).objects.filter(Prefix=prefix)]


def load_pickle(s3client, bucket, key) -> pickle:
    """
    Create and load the pickle file from S3
    :param s3client: S3 Client object
    :param bucket: S3 bucket name
    :param key: Pickle file path
    :return: pickle file
    """
    response = s3client.get_object(Bucket=bucket, Key=key)
    return pickle.loads(response['Body'].read())


def download_s3_file(s3client, bucket, key, file_name):
    """
    Download the file from S3
    :param s3client: S3 Client object
    :param bucket: S3 bucket name
    :param key: S3 File path
    :param file_name: Destination File Name
    :return: Boolean
    """
    try:
        s3client.download_file(bucket, key, file_name)
    except Exception as e:
        logger.error(e)
        return False
    return True

def save_obj_as_pickle(s3_client, obj, name, bucket, prefix) -> str:
    """
    Save the object as pickle file in S3
    :param obj: Object to be saved
    :param name: Name of the object
    :param bucket: S3 bucket name
    :param prefix: S3 prefix
    :return: Saved file path
    """
    output_file = prefix + name + '.pickle'
    serialized = pickle.dumps(obj)
    s3_client.put_object(Bucket=bucket, Key=output_file, Body=serialized)
    return output_file

def get_log_lines(logFile, startByte, endByte):
    """
    Get the log lines from the given log file
    :param logFile: Log file
    :param startByte: Start byte
    :param endByte: End byte
    :return: List of log lines
    """
    print("Start | End")
    print(startByte, endByte)
    with open(logFile, 'rb') as f:
        f.seek(startByte)
        return f.read(endByte - startByte).decode('utf-8').split('\n')