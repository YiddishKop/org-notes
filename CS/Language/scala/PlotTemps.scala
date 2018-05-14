package standardscala

import scalafx.application.JFXApp
import scalafx.collections.ObservableBuffer
import scalafx.scene.Scene
import scalafx.scene.chart.{ NumberAxis, ScatterChart, XYChart }

import scalafx.application.JFXApp
import scalafx.scene.Scene
import scalafx.scene.chart.ScatterChart
import scalafx.collections.ObservableBuffer
import scalafx.scene.chart.NumberAxis
import scalafx.scene.chart.XYChart

// import swiftvis2.plotting
// import swiftvis2.plotting.Plot
// import swiftvis2.plotting.renderer.FXRenderer
// import swiftvis2.plotting.ColorGradient

object PlotTemps extends JFXApp {
  // sourceFromFile
  val source = scala.io.Source.fromFile("MN212142_9392.csv")

  // Iterator[String]
  val lines = source.getLines().drop(1)

  // each line map to a TempData case object
  val data = lines.flatMap{
    line => {
      val p = line.split(",")
      if (p(7)=="."||p(8)=="." || p(9)==".") Seq.empty else
                                                         Seq(TempData(p(0).toInt,
                                                                      p(1).toInt,
                                                                      p(2).toInt,
                                                                      p(4).toInt,
                                                                      TempData.toDoubleOrNeg(p(5)),
                                                                      TempData.toDoubleOrNeg(p(6)),
                                                                      p(7).toDouble,
                                                                      p(8).toDouble,
                                                                      p(9).toDouble))
    }
  }.toArray
  source.close()

  // scalaFx is verbose but very stable
  stage = new JFXApp.PrimaryStage{
    title = "Temp Plot"
    scene = new Scene(500, 500){
      /* draw temperature against the day of the year
       2 ways to put things in a scene or another grouping node
       1. root
       2. content
      */
      val xAxis = NumberAxis()
      val yAxis = NumberAxis()
      val pData = XYChart.Series[Number, Number]("Temps",
                                                 ObservableBuffer(data.map(td => XYChart.Data[Number, Number](td.doy, td.tmax)):_*))
      val plot = new ScatterChart(xAxis, yAxis, ObservableBuffer(pData))
      root = plot

    }
  }

}
