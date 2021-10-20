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
  value.converter=org.apache.kafka.connect.converters.ByteArrayConverter
  
  
## 2. Reading Data from S3 bucket, process the data with spark on EMR and storing it back to S3.
