import json
import base64
import logquery_pb2
import logquery_pb2_grpc
import boto3
import pickle
from loglib import utils
import os
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)


BUCKET_NAME = "441-log-bucket"
PICKLE_PATH = "pickle/"
LOGS_PATH = "logs/"

def get_serialized_response(status):
    response = logquery_pb2.LogQueryResponse(isAvailable=status)
    serialized = response.SerializeToString()
    return serialized.decode()
    
def lambda_handler(event, context):
    
    accessKey = os.environ.get('accessKeyId')
    secretAccessKey = os.environ.get('secretAccessKey')

    if accessKey is None or secretAccessKey is None:
        print("AccessKey/Secret AccessKey is None")
        return {'statusCode': 500, 'body': json.dumps('AccessKey/Secret AccessKey is None')}
    print("Event Type", type(event))
    
    content = base64.b64decode(event['body'])
    logQuery = logquery_pb2.LogQueryRequest()
    logQuery.ParseFromString(content)
    time = logQuery.time
    date = logQuery.date

    s3 = utils.get_s3_client(accessKey, secretAccessKey)
    s3r = utils.get_s3_resource(accessKey, secretAccessKey)
    
    pickleFile = PICKLE_PATH + 'LogFileGenerator.{}.log.pickle'.format(date)
    
    pickleFiles = utils.get_file_index(s3r, BUCKET_NAME, PICKLE_PATH)
    print("Pickle Files: ", pickleFiles)
    
    print("TimeStamp: {} | Window: {} | Date: {}".format(logQuery.time, logQuery.window, logQuery.date))

    if pickleFile not in pickleFiles:
        logger.info("Date not found in pickle files")
        return {'statusCode': 404, 'body':get_serialized_response(False)}

    pickleData = utils.load_pickle(s3, BUCKET_NAME, pickleFile)
    
    print(pickleData.keys())
    if time not in pickleData:
        logger.info("TimeStamp not found in pickle index")
        return {'statusCode': 404, 'body': get_serialized_response(False)}
    logger.info("TimeStamp found in pickle index")
    

    return {'statusCode': 200, 'body': get_serialized_response(True)}
