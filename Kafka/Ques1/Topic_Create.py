### START THE KAFKA ENVIRONMENT
$ bin/zookeeper-server-start.sh config/zookeeper.properties
$ bin/kafka-server-start.sh config/server.properties

### CREATE A TOPIC
$ bin/kafka-topics.sh --create \
                      --topic topic_csv \
                      --bootstrap-server ['localhost:9092'] \
                      --zookeeper <Server name> \
                      --replication-factor 3 \
                      --partitions 3
					  
$ bin/kafka-topics.sh --create \
                      --topic topic_json \
                      --bootstrap-server ['localhost:9092'] \
                      --zookeeper <Server name> \
                      --replication-factor 3 \
                      --partitions 3