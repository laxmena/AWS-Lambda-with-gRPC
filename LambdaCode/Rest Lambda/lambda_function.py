import boto3
import os, re
import logging
import json
from loglib import utils
import hashlib

logger = logging.getLogger()
logger.setLevel(logging.INFO)

BUCKET_NAME = "441-log-bucket"
PICKLE_PATH = 'pickle/'
LOGS_PATH = 'logs/'

def lambda_handler(event, context):
    logger.info("Received event: " + json.dumps(event, indent=2))

    accessKey = os.environ.get('accessKeyId')
    secretAccessKey = os.environ.get('secretAccessKey')

    if accessKey is None or secretAccessKey is None:
        print("AccessKey/Secret AccessKey is None")
        return {'statusCode': 500, 'body': json.dumps('AccessKey/Secret AccessKey is None')}
    print("Event Type", type(event))
    
    if event['httpMethod'] == "GET":
        body = event["queryStringParameters"]
        print(body, type(body))
        date = body['date']
        timeStamp = body['timeStamp']
        window = body['window']
        pattern = re.compile(body['pattern'])
    else:
        body = json.loads(event['body'])
        date = body['date']
        timeStamp = body['timeStamp']
        window = body['window']
        pattern = re.compile(body['pattern'])
    
    logger.info("Date: {} | Timestamp: {} | Window: {} | Pattern: {}".format(date, timeStamp, window, pattern))
    s3 = utils.get_s3_client(accessKey, secretAccessKey)
    s3r = utils.get_s3_resource(accessKey, secretAccessKey)

    pickleFile = PICKLE_PATH + 'LogFileGenerator.{}.log.pickle'.format(date)
    
    pickleFiles = utils.get_file_index(s3r, BUCKET_NAME, PICKLE_PATH)
    print("Pickle Files: ", pickleFiles)
    
    logger.info('Requesting PickleFile: {}'.format(pickleFile))
    
    if pickleFile not in pickleFiles:
        logger.info("Date not found in pickle files")
        return {'statusCode': 404, 'body': json.dumps({'isAvailable': False, 'message':'Logs for given Date not found'})}

    logger.info("Date found in pickle files")

    # Load the pickle index for the date 
    pickleData = utils.load_pickle(s3, BUCKET_NAME, pickleFile)
    
    print(pickleData.keys())
    if timeStamp not in pickleData:
        logger.info("TimeStamp not found in pickle index")
        return {'statusCode': 404, 'body': json.dumps({'isAvailable': False, 'message':'No Logs for given Timestamp found'})}
    logger.info("TimeStamp found in pickle index")

    # Load the log file for the timestamp
    dataPoint = pickleData[timeStamp]
    logBucket, logFileName, startByte, endByte = pickleData[timeStamp] 


    
    logger.info("Log Bucket: {}, Log File: {}".format(logBucket, logFileName))
    
    temp_file = "/tmp/op.log"
    logFile = utils.download_s3_file(s3, logBucket, logFileName, temp_file)
    logger.info("LogFile: {}".format(temp_file))

    # Get the log lines for the timestamp
    matchedLines = []

    logLines = utils.get_log_lines(temp_file, startByte, endByte)
    print("logLines: {}".format(len(logLines)), logLines)
    # Find strings that match the pattern in logLines
    for line in logLines:
        result = re.search(pattern, line)
        if result:
            print("Pattern Matched: ", line)
            matchedLines.append(hashlib.md5(line.encode('utf-8')).hexdigest())
    
    print("Matched Lines Hash: ", matchedLines)
    return {
        'statusCode': 200,
        'body': json.dumps({'isAvailable': len(matchedLines) > 0, 'matchHashes': matchedLines}, default=str)
    }
