import boto3
import json
import psycopg2

s3_client = boto3.client('s3')

# database connection setup
connection = psycopg2.connect(
                database="dvdrental",
                user="postgres",
                password="****")
connection.autocommit = True
cursor = connection.cursor()

# Get all the table names from the database
query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 
'public' and table_type = 'BASE TABLE';"
cursor.execute(query)
table_names = cursor.fetchall()
table_names_list = [row[0] for row in table_names]

# Get the contents of each table in json format and move it to the s3 bucket
for name in table_names_list:
  query2 = "SELECT array_to_json(array_agg(row_to_json(n_alias))) from (select * 
  from {}) n_alias;".format(name)
  cursor.execute(query2)
  file_content = cursor.fetchall()
  data = json.dumps(file_content).encode('UTF-8')
  s3_client.put_object(Body=data, Bucket='dvdrentalbucket', 
  Key='{}.json'.format(name))



# closing database connection.
cursor.close()
connection.close()
print("PostgreSQL connection is closed")
