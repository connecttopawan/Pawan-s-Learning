#Spark Dataframe to read from queue
# Batch Processing
df = spark \
  .read \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "host1:port1,host2:port2") \
  .option("subscribe", "JdbcTopic") \
  .option("startingOffsets", "earliest") \
  .option("endingOffsets", "latest") \
  .load()

# Stream Processing  
df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "host1:port1,host2:port2") \
  .option("subscribe", "topic1") \
  .load()