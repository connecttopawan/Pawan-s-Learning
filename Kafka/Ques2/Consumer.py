# Consumer to check whether the data was written to the topic or not
from kafka import KafkaConsumer
import os 

def deserializer(data):
    return lambda data: str(data).decode('utf-8')
  
# Message count in a topic  
def topic_message_count(consumer):
    counter=0
    for i in consumer:
        counter+=1
    return counter

if __name__=='__main__':   
    consumer = KafkaConsumer(
        'topic_csv',
        bootstrap_servers=['localhost:9092'],
        # To read topic from begining
        auto_offset_reset='earliest',
        # To read topic from last read
        auto_offset_reset='latest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=deserializer(data))
    print("Message Count: ",topic_message_count(consumer))
     