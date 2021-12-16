# Consumer to read files from ftp server and load to topic.
from time import sleep
from json import dumps
from kafka import KafkaProducer
import os 

# ftp server path
source_directory= "/path"

def serializer(data):
    return lambda data: str(data).encode('utf-8')

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer= serializer)
                         
if __name__=='__main__':
    # Reading files from ftp server.
    for file in os.listdir(source_directory):
        with open(file,'r') as f:
            data=f.read()
            # Segregating csv files.
            if (re.search('\.csv',file)
                producer.send('topic_csv',data)
                sleep(5)
            # Segregating json files.
            if (re.search('\.json',file)
                producer.send('topic_json',data)
                sleep(5)
                         