package com.laxmena

import org.scalatest.flatspec.AnyFlatSpec
import org.scalatest.matchers.should.Matchers
import com.laxmena.HelperUtil.{ObtainConfigReference, Constants}
import com.typesafe.config.{Config, ConfigFactory}

class TestSuite extends AnyFlatSpec with Matchers {
  behavior of "Configuration parameters module"
  // App Config Tests
  var config = ObtainConfigReference(Constants.LOGQUERY) match {
    case Some(value) => value.getConfig(Constants.LOGQUERY)
    case None => throw new RuntimeException("Cannot obtain reference to the Config data")
  }

  // GRPC Config Tests
  it should "Contain grpc configuration" in {
    assert(config.hasPath(Constants.GRPC))
  }

  var grpcConfig = config.getConfig(Constants.GRPC)

  it should "Contain grpc host configuration" in {
    assert(grpcConfig.hasPath(Constants.HOST))
  }

  it should "contain grpc port" in {
    assert(grpcConfig.hasPath(Constants.PORT))
  }

  it should "contain content type" in {
    assert(grpcConfig.hasPath(Constants.CONTENT_TYPE))
  }

  it should "contain accept type" in {
    assert(grpcConfig.hasPath(Constants.ACCEPT_TYPE))
  }

  // REST Config Tests

  it should "Contain rest configuration" in {
    assert(config.hasPath(Constants.REST))
  }

  var restConfig = config.getConfig(Constants.REST)

  it should "Contain rest host configuration" in {
    assert(restConfig.hasPath(Constants.HOST))
  }

  it should "contain rest URI" in {
    assert(restConfig.hasPath(Constants.URI))
  }

  it should "contain rest port" in {
    assert(restConfig.hasPath(Constants.PORT))
  }

  it should "contain rest content type" in {
    assert(restConfig.hasPath(Constants.CONTENT_TYPE))
  }

  it should "contain rest accept type" in {
    assert(restConfig.hasPath(Constants.ACCEPT_TYPE))
  }

  it should "contain rest search pattern" in {
    assert(restConfig.hasPath(Constants.PATTERN))
  }

}