	from pyspark.sql import SparkSession
  
  if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("File Streaming Demo") \
        .master("local[3]") \
        .getOrCreate()
	
	spark.sparkContext
     .hadoopConfiguration.set("fs.s3a.access.key", "awsaccesskey value")
service)
 // Replace Key with your AWS secret key (You can find this on IAM 
spark.sparkContext
     .hadoopConfiguration.set("fs.s3a.secret.key", "aws secretkey value")
spark.sparkContext
      .hadoopConfiguration.set("fs.s3a.endpoint", "s3.amazonaws.com")
	  
df = spark.read.json("s3a://source")
df.printSchema()
df.show(false)
// Perform required data processing 
	.
	.
	.
df.write.mode('overwrite').format('parquet').save("s3a://ATM-Transaction")
