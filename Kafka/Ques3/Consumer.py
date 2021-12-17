# Kafka consumer that will read data from multiple topics.
from kafka import KafkaConsumer
import os 

def deserializer(data):
    return lambda data: str(data).decode('utf-8')
  

if __name__=='__main__':   
    consumer = KafkaConsumer(
        bootstrap_servers=['localhost:9092'],
        # To read topic from begining
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=deserializer(data))
     
    consumer.subscribe([topic1,topic2])
                         