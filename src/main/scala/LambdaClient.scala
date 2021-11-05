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

  /**
   Main method, recieves the following arguments:
   <ol>
   <li> Date in the format YYYY-MM-DD </li>
   <li> Time in the format HH:MM:SS </li>
   <li> Window size in minutes </li>
   <ol>

   <b>Functionality:</b>
   <p>Creates a Protobuf message with the given parameters and sends it to the Lambda function.
   The response(isAvailable) is printed to the console.</p>

   @param args Date, Time, Window Size

  **/

  def main(args: Array[String]): Unit = {
    logger.info("LambdaClient started")
    val date = args(0)
    val time = args(1)
    val window = args(2).toInt
    logger.info(s"date: $date, time: $time, window: $window")
    val logQuery = LogQueryRequest(date = date, time = time, window = window)
    AwsProtobufClient.run(logQuery)
  }

}
