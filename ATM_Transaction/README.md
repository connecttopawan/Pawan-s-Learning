This Project is to track financial transactions of a bank.
The pipeline of the project is:	 

![image](https://user-images.githubusercontent.com/40576094/138065098-67c884f9-0993-4d3f-805d-a44a10c0db90.png)

As per the above pipeline, we can divide our work in below steps:
## 1. Ingesting file from log server to S3 through Kafka:
  In this stage we are moving transaction log which are in JSON format from SFTP to AWS S3 bucket.
  We are using kafka connects. Kafka Connect is a framework for connecting Kafka with external systems. It is having 2 components source connectors and sink connectors.
  ### JSON Source Connector:
  The Kafka Connect JSON Source connector is used to stream JSON files from an SFTP directory while also converting the data based on the schema supplied in the configuration. If the schema is not supplied in the configuration then the connector can also auto generate the key.schema and value.schema at run time when schema.generation.enabled is true.
    connector.class=io.confluent.connect.sftp.SftpJsonSourceConnector
  #### Other Connectors are:
  connector.class=io.confluent.connect.sftp.SftpCsvSourceConnector
  ### S3 Sink Connector:
    connector.class=io.confluent.connect.s3.s3sinkconnector
  ### Worker Config:
    Finally, we have to configure the Connect worker, which will integrate our two connectors and do the work of reading from the source connector and writing to the sink connector.
  
  
## 2. Reading Data from S3 bucket, process the data with spark on EMR and storing it back to S3.
  ### Create S3 bucket to store processed data
  We can create through aws management console or CLI. Here we are creating through CLI.
  
  ### Create a pyspark code and store it to a S3 bucket.
  File Name: ATM-Transaction.py
  
  ### Open putty and submit pyspark code here.
  ###### Configure it with private key file.
  ###### EMR will be launched.
  ###### Create EMR cluster:
    This can be created from management console or CLI. Here we are using CLI.
  ###### Run spark submit cmd to created cluster.

## 3. Copying data from S3 to AWS Redshift through AWS Glue. 
