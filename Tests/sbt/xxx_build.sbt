lazy val foo = settingKey[Int]("")
lazy val bar = settingKey[Int]("")

lazy val projX = (project in file("x"))
  .settings(
    unmanagedBase := baseDirectory.value / "yiddishkop",
    foo := {
      (Test / bar).value + 1
    },
    Compile / bar := 1
  )
