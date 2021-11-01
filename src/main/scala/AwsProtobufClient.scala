package com.laxmena

import scalaj.http.Http
import HelperUtil.{CreateLogger, ObtainConfigReference}

import logquery.{LogQueryRequest, LogQueryResponse}

/**
 * <h1>AWS Protobuf Client</h1>
 *
 *  This class is responsible for creating the AWS Protobuf Client.
 *
 *  <h3>Functionality</h3>
 *  <p>
 *    AWS Lambda by default doesnt provide support to gRPC connection. So we emulate the behaviour of gRPC by using
 *    Protobuf Serialization, and transfer it over .
 *  </p>
 *  <ul>
 *    <li>Encodes the LogQueryRequest into bytes and sends </li>
 *
 *  @author laxmena
 *  @version 1.0
 */
class AwsProtobufClient
object AwsProtobufClient {
  val logger = CreateLogger(classOf[AwsProtobufClient])
  val config = ObtainConfigReference("logQuery") match {
    case Some(c) => c.getConfig("logQuery")
    case None => throw new Exception("Unable to obtain configuration reference")
  }
  logger.info("Config: ", config)

  val grpcConfig = config.getConfig("grpc")
  logger.info("Grpc Config: ", grpcConfig)

  val grpcHost = grpcConfig.getString("host")
  val grpcPort = grpcConfig.getInt("port")
  val contentType = grpcConfig.getString("contentType")
  val accept = grpcConfig.getString("acceptType")
  val grpcChannel = s"$grpcHost:$grpcPort"
  val awsGrpcChannel = s"$grpcHost"

  def run(logQuery: LogQueryRequest): Boolean = {
    logger.info("Starting AWS Protobuf Client")
    val request = Http(awsGrpcChannel)
                    .headers(Map(
                      "Content-Type" -> contentType,
                      "Accept" -> contentType
                    ))
                    .timeout(connTimeoutMs = 10000, readTimeoutMs = 10000)
                    .postData(logQuery.toByteArray)

    val response = request.asBytes.body
    logger.info(s"req: ${request.asBytes}")
    logger.info(s"Response: ${response}")
    val logQueryRes: LogQueryResponse = LogQueryResponse.parseFrom(response)
    logger.info(s"LogQueryResponse: $logQueryRes")

    logQueryRes.isAvailable
  }
}