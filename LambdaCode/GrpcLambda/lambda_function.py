import json
import base64
import logquery_pb2
import logquery_pb2_grpc

def lambda_handler(event, context):
    content = base64.b64decode(event['body'])
    logQuery = logquery_pb2.LogQueryRequest()
    logQuery.ParseFromString(content)
    
    print("TimeStamp: {} | Window: {}".format(logQuery.timeStamp, logQuery.window))

    response = logquery_pb2.LogQueryResponse(isAvailable=True)
    serialized = response.SerializeToString()

    result = {
        'statusCode': 200,
        'body': serialized.decode(),
    }
    
    return result
