import os
import boto3
import pickle
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create AWS Lambda Function that Triggers on S3 Object Creation and reads file and hashes it
def lambda_handler(event, context):
    logger.info('Event: {}'.format(event))

    # Load accessKey and secretKey from the environment variables
    accessKeyId = os.environ['accessKeyId']
    secretAccessKey = os.environ['secretAccessKey']

    pickleKeyPrefix = 'pickle/'
    eventObj = event['Records'][0]['s3']
    bucket = eventObj['bucket']['name']
    key = eventObj['object']['key']
    fileName = key.split('/')[-1]

    logger.info("Bucket: " + bucket)
    logger.info("Key: " + key)

    # Download file from S3 bucket to tmp
    tmp_file = '/tmp/' + fileName
    s3_client = boto3.client('s3', aws_access_key_id=accessKeyId, aws_secret_access_key=secretAccessKey)
    s3_client.download_file(bucket, key, tmp_file)
    logger.info("Downloaded file to: " + tmp_file)

    # Map to store TimeStamp and FileName, Start & length
    map = {}
    
    print(os.path.getsize(tmp_file))
    
    # Load downloaded file into memory
    with open(tmp_file, 'r') as f:
        data = f.read()
        prevTimeStamp, startByte, byteCounter = "", 0, 0
        # Iterate through each line and extract timestamp in logfile
        for line in data.splitlines():
            fullTimeStamp = line.split(' ')[0]
            timeStamp = fullTimeStamp.split('.')[0]
            if prevTimeStamp != timeStamp:
                map[prevTimeStamp] = (bucket, key, startByte, byteCounter)
                prevTimeStamp = timeStamp
                startByte = byteCounter
            byteCounter += len(line.encode('utf-8')) + len('\r\n'.encode('utf-8'))
        map[prevTimeStamp] = (bucket, key, startByte, byteCounter) 

    # Save map pickle file in S3 bucket
    output_file = pickleKeyPrefix + fileName + '.pickle'
    serialized = pickle.dumps(map)
    s3_client.put_object(Bucket=bucket, Key=output_file, Body=serialized)
    logger.info("Saved map pickle file to: " + output_file)
