# Read “test.csv” file and convert each line to json and load the data to a Kafka topic.
from time import sleep
from json import dumps
from kafka import KafkaProducer
import os 
from csv import DictReader 

# csv file
file= "/path/file.csv"

def serializer(data):
    return json.dump(data).encode('utf-8')

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer= serializer)
                         
if __name__=='__main__':
    with open(file,'r') as f:
        data=f.read()
        csv_dict_read = DictReader(data)
        for row in csv_dict_read:
            producer.send('topic_json',row)
                     