package com.laxmena

import HelperUtil.{CreateLogger, ObtainConfigReference}

import logquery.LogQueryRequest

import java.lang.Iterable
import scala.collection.JavaConverters._
import scala.util.matching.Regex

/**
 * <h1>LambdaClient</h1>
 * <p>
 *   LambdaClient is a Scala client for the AWS Lambda service.
 * </p>
 * <h3>Usage</h3>
 * <p>
 *   The following command shows how to compile and run the LambdaClient:
 *   <pre>
 *     sbt clean compile
 *     sbt assembly
 *     sbt run
 *   </pre>
 */
class LambdaClient
object LambdaClient {
  val logger = CreateLogger(classOf[LambdaClient])
  val config = ObtainConfigReference("logQuery") match {
    case Some(c) => c.getConfig("logQuery")
    case None => throw new Exception("Unable to obtain configuration reference")
  }

  def main(args: Array[String]): Unit = {
    logger.info("LambdaClient started")
    print("args", args)

    val logQuery = LogQueryRequest(timeStamp = "10:21:12", window = 1)
    val logAvailable = AwsProtobufClient.run(logQuery)
    logger.info("logAvailable", logAvailable)

  }

}
