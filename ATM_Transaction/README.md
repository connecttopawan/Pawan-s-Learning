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
    We need to below arguments to create cluster.
      --name: Provide name to the cluster, It is an identifier.
      --release-label: It specifies which version of EMR to use. It is recomended to use latest version.
      --applications: It tells EMR which type of application we will be using on our cluster. To create a Spark cluster, use Name=Spark.
      --instance-type: It specifies which type of EC2 instance you want to use for our cluster.
      --bootstrap-actions: It allows us to specify what packages we want to be installed on all of your cluster’s nodes. This step is only necessary if your application uses non-builtin Python packages other than pyspark. To use such packages, create our emr_bootstrap.sh file using the example below as a template, and add it to your S3 bucket. Include --bootstrap-actions Path=s3://your-bucket/emr_bootstrap.sh in the aws emr create-cluster command.
      --steps: tells our cluster what to do after the cluster starts. Be sure to replace s3://your-bucket/pyspark_job.py in the --steps argument with the S3 path to your Spark application. We can also put your application code on S3 and pass an S3 path.
  ###### Run spark submit cmd to created cluster.

## 3. Copying data from S3 to AWS Redshift through AWS Glue. 
#### Creating table in Redshift.
#### Creating Glue job through management console.
   ###### Add classifiers to identify JSON, csv or XML files (here we provide headings, delimeter etc.)
   ###### Create crawler to create metadata of S3 files (source) in Data Catalog.
   ###### Add connection to establish connection to Amazon Redshift.
   ###### Create crawler to create metadata of Redshift table (target) in Data Catalog.
   ###### Add Job and provide spark script.
