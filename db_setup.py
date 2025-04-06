from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ImageProcessing").getOrCreate()
schema = "request_id STRING, status STRING"
spark.createDataFrame([], schema=schema).write.format("delta").saveAsTable("image_processing_requests")