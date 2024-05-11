/*
How can we generate a unique session id for click stream data by using Spark(Scala) dataframes with following two conditions?

Session expires after 30 minutes of inactivity (Means no click stream data within 30 minutes)
Session remains active for a total duration of 2 hours. After 2 hours, renew the session.

Given Data:

userId clickTime
U1 2019-01-01T11:00:00Z
U1 2019-01-01T11:15:00Z
U1 2019-01-01T12:00:00Z
U1 2019-01-01T12:20:00Z
U1 2019-01-01T15:00:00Z
U2 2019-01-01T11:00:00Z
U2 2019-01-02T11:00:00Z
U2 2019-01-02T11:25:00Z
U2 2019-01-02T11:50:00Z
U2 2019-01-02T12:15:00Z
U2 2019-01-02T12:40:00Z
U2 2019-01-02T13:05:00Z
U2 2019-01-02T13:20:00Z
*/

/* SimpleApp scala */
import org.apache.spark.sql._
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.expressions._
import org.apache.spark.sql.functions._
import org.apache.log4j.Logger
import org.apache.log4j.Level

object Sessions {
  def main(args: Array[String]) {
    Logger.getLogger("org").setLevel(Level.WARN)
    val sampleFile = "src/main/resources/dataset.txt"
    val spark = SparkSession.builder.master("local").appName("Simple Application").getOrCreate()
    import spark.implicits._

    val sampleData = spark.read.textFile(sampleFile).cache()

    sampleData.map(_.replaceAll("Given Dataset:",""))
      .map(_.replaceAll("Timestamp",""))
      .map(_.replaceAll("User_id",""))
      .map(_.replaceAll(" ",",")).na.drop().write.csv("src/main/resources/inputCSVData2")


    val inputDF = spark.read.option("delimiter",",").csv("src/main/resources/inputCSVData/*.csv").na.drop()
      .withColumn("temp",split(col("_c0"),","))
      .select($"temp".getItem(0).as("Click_Timestamp"),$"temp".getItem(1).as("User_id"))
      .select(col("Click_Timestamp").cast("timestamp"),col("User_id").cast("string"))
      .na.drop().orderBy("User_id")


    val validSessionsDF = inputDF
      .withColumn("lagClickTime",lag(col("Click_Timestamp"),1).over(Window.partitionBy("User_id").orderBy("Click_Timestamp")))
      .withColumn("timeDiff30",(col("Click_Timestamp").cast("long")-col("lagClickTime").cast("long"))/(60*30))
      .na.fill(0)
      .withColumn("isNewSession",when(col("timeDiff30")>1,1).otherwise(0))
      .withColumn("sumSessions30",sum("isNewSession").over(Window.partitionBy("User_id").orderBy("Click_Timestamp")))
      .withColumn("firstClickTime",first(col("Click_Timestamp")).over(Window.partitionBy("User_id","sumSessions30").orderBy("Click_Timestamp")))
      .withColumn("timeDiff120",((col("Click_Timestamp").cast("long")-col("firstClickTime").cast("long"))/(60*60*2)).cast("int"))
      .withColumn("sessions_ids",(col("sumSessions30")+col("timeDiff120")+1))
        
    validSessionsDF.createOrReplaceTempView("final_sessions")

    val sessionDF = spark.sql("select Click_Timestamp as Timestamp,User_id as User_id,concat(User_id,'_s',sessions_ids) as Session_id from final_sessions")
    sessionDF.createOrReplaceTempView("user_sessions")

    sessionDF.write.parquet("src/main/resources/sessions2")

    val numberOfSessions = spark.sql("select date(Timestamp) as session_date,Session_id,count(*) from user_sessions group by date(Timestamp),Session_id order by date(Timestamp)")
    numberOfSessions.write.parquet("src/main/resources/numberOfSessionsPerDay2")

    val totalTimeSpent = spark.sql("select User_id, ((Max(Timestamp) over(partition by User_id order by Timestamp)) - (Min(Timestamp) over (partition by User_id order by Timestamp))) as total_time_spent from user_sessions")
    totalTimeSpent.write.parquet("src/main/resources/totalTimeSpentByUser2")


    //val numAs = logData.filter(line => line.contains("e")).count()
    //val numOs = logData.filter(line => line.contains("o")).count()
    //println(s"Lines with a: $numAs, Lines with b: $numOs")
    spark.stop()
  }
}
