import sbt.Keys.libraryDependencies

name := "AWS-Lambda-with-gRPC-Rest"

version := "0.1"

scalaVersion := "2.13.4"

idePackagePrefix := Some("com.laxmena")
val logbackVersion = "1.3.0-alpha10"
val sfl4sVersion = "2.0.0-alpha5"
val typesafeConfigVersion = "1.4.1"
val apacheCommonIOVersion = "2.11.0"
val scalacticVersion = "3.2.9"

resolvers += Resolver.jcenterRepo

assembly / assemblyMergeStrategy := {
  case PathList("META-INF", xs @ _*) => MergeStrategy.discard
  case x => MergeStrategy.first
}


libraryDependencies ++= Seq(
  "ch.qos.logback" % "logback-core" % logbackVersion,
  "ch.qos.logback" % "logback-classic" % logbackVersion,
  "org.slf4j" % "slf4j-api" % sfl4sVersion,
  "com.typesafe" % "config" % typesafeConfigVersion,
  "commons-io" % "commons-io" % apacheCommonIOVersion,
  "org.scalactic" %% "scalactic" % scalacticVersion,
  "org.scalatest" %% "scalatest" % scalacticVersion % Test,
  "org.scalatest" %% "scalatest-featurespec" % scalacticVersion % Test,
  "com.typesafe" % "config" % typesafeConfigVersion,
  "org.scalatest" %% "scalatest" % "3.0.8" % "test",
  "com.thesamet.scalapb" %% "scalapb-runtime-grpc" % scalapb.compiler.Version.scalapbVersion,
  "org.scalaj" %% "scalaj-http" % "2.4.2",
)
libraryDependencies += "org.scala-lang.modules" %% "scala-parser-combinators" % "1.1.2"
libraryDependencies += "com.twitter" %% "finagle-http" % "21.9.0"

Compile / PB.targets := Seq(
  scalapb.gen() -> (sourceManaged in Compile).value
)
