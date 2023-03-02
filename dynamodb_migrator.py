import boto3

from my_poc.settings import DB_ENDPOINT, DB_TABLE

dynamodb=boto3.resource('dynamodb',endpoint_url=DB_ENDPOINT)
table= dynamodb.Table('employees')
table.put_item(
    Item={
        'firstName':'Hangover',
        'lastName':'up',
        'empId':1
    }
)
# print(table.item_count)

# def create_table(dynamodb=None):
#     if not dynamodb:
#         dynamodb=boto3.resource('dynamodb',endpoint_url=DB_ENDPOINT)
#
#     table = dynamodb.create_table(
#         TableName=DB_TABLE,
#         KeySchema=[
#             {'AttributeName': 'firstName', 'KeyType': 'HASH'},  # Partition key
#             # {'AttributeName': 'lastName', 'KeyType': 'RANGE'}  # Sort key
#         ],
#         AttributeDefinitions=[
#             {'AttributeName': 'firstName', 'AttributeType': 'S'},
#             # {'AttributeName': 'lastName', 'AttributeType': 'S'}
#         ],
#         ProvisionedThroughput={'ReadCapacityUnits': 10, 'WriteCapacityUnits': 10}
#     )
#     return table
#
#
#
# if __name__=='__main__':
#     movie=create_table()
#     movie.meta.client.get_waiter('table_exists').wait(TableName=DB_TABLE)
#     print(movie.item_count)