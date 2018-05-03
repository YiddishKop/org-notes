import Dependencies._

val scalacOptions = taskKey[Seq[String]]("Options for the Scala compiler.")
val update = taskKey[UpdateReport]("Resolves and optionally retrieves dependencies, producing a report.")
val clean = taskKey[Unit]("Deletes files produced by the build, such as generated sources, compiled classes, and task caches.")


ThisBuild / concurrentRestrictions := Seq(
  Tags.limitAll(1)
)

val sampleStringTask = taskKey[String]("A sample string task.")

lazy val root = (project in file(".")).
  settings(
    name := "hello",
    organization := "com.example",
    scalaVersion := "2.12.4",
    version := "0.1.0-SNAPSHOT",
    scalacOptions := List("-encoding", "utf8", "-Xfatal-warnings", "-deprecation", "-unchecked"),
    sampleStringTask := System.getProperty("user.home"),
    scalacOptions := {
      val old = scalacOptions.value
      scalaBinaryVersion.value match {
        case "2.12" => old
        case _      => old filterNot (Set("-Xfatal-warnings", "-deprecation").apply)
      }
    }
  )
