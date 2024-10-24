# Import Spark Libraries
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Creating Spark Session
spark = SparkSession  \
        .builder  \
        .appName("HealthAlert System")  \
        .config("spark.sql.warehouse.dir", "/user/hive/warehouse") \
 	      .config("spark.sql.hive.metastore.jars", "builtin") \
   	    .config("hive.metastore.uris", "thrift://ip-172-31-84-72.ec2.internal:9083") \
 	      .enableHiveSupport() \
        .getOrCreate()

spark.sparkContext.setLogLevel('ERROR')

# Define schema for vital information
vitals_schema = StructType([
    StructField("heartBeat", IntegerType(), True),
    StructField("bp", IntegerType(), True),
    StructField("customerId", IntegerType(), True),
    StructField("message_time", TimestampType(), True)
])

# Define paths for input and checkpoint directory
checkpoint_dir = "hdfs://ip-172-31-84-72.ec2.internal:8020/user/hadoop/health-alert/checkpoint/"

# Read the vital information table from HDFS
patient_vital_info = spark.readStream \
                           .format("parquet") \
                           .option("maxFilesPerTrigger", "1") \
                           .schema(vitals_schema) \
                           .load("hdfs://ip-172-31-84-72.ec2.internal:8020/user/hadoop/health-alert/patients-vital-info")


# Read the patients contact information table from Hive
patient_contact_info = spark.sql("select * from health.patients_contact_info")

#Comparison of HDFS data and hive data
patient_complete_data = patient_vital_info.join(patient_contact_info, patient_vital_info.customerId == patient_contact_info.patientid, 'left_outer')

patient_complete_data.createOrReplaceTempView("patient_complete_data_tbl")

bp = spark.sql("""
    SELECT a.patientname, a.age, a.patientaddress, a.phone_number, a.admitted_ward, a.bp, a.heartbeat, a.message_time, b.alert_message 
    FROM patient_complete_data_tbl a, health.threshold_ref_hive b 
    WHERE b.attribute = 'bp' 
      AND (a.age >= b.low_age_limit AND a.age <= b.high_age_limit) 
      AND (a.bp >= b.low_range_value AND a.bp <= b.high_range_value) 
      AND b.alert_flag = 1
""")

heartBeat = spark.sql("""
    SELECT a.patientname, a.age, a.patientaddress, a.phone_number, a.admitted_ward, a.bp, a.heartbeat, a.message_time, b.alert_message 
    FROM patient_complete_data_tbl a, health.threshold_ref_hive b 
    WHERE b.attribute = 'heartBeat' 
      AND (a.age >= b.low_age_limit AND a.age <= b.high_age_limit) 
      AND (a.heartBeat >= b.low_range_value AND a.heartBeat <= b.high_range_value) 
      AND b.alert_flag = 1
""")

alert_df = bp.union(heartBeat).withColumnRenamed("message_time", "input_message_time")

alert_final_df = alert_df.selectExpr("to_json(struct(*)) AS value")

# Final output
output = alert_final_df \
        .writeStream  \
        .outputMode("append")  \
        .format("kafka")  \
        .option("kafka.bootstrap.servers", "44.215.14.94:9092")  \
        .option("topic", "PatientHealthNotification")  \
        .option("checkpointLocation", checkpoint_dir)  \
        .start()

output.awaitTermination()
