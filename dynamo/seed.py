import boto3
from botocore.exceptions import ClientError

DYNAMODB_ENDPOINT = "http://localhost:8000"
TABLE_NAME = "test"

# Initialize DynamoDB resource
dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url=DYNAMODB_ENDPOINT,
    region_name='us-west-2',
    aws_access_key_id='dummy',
    aws_secret_access_key='dummy'
)

print(f"Creating Table {TABLE_NAME}")

# Create the table
try:
    table = dynamodb.create_table(
        TableName=TABLE_NAME,
        KeySchema=[
            {'AttributeName': 'Id', 'KeyType': 'HASH'}
        ],
        AttributeDefinitions=[
            {'AttributeName': 'Id', 'AttributeType': 'S'}
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    table.wait_until_exists()
    print(f"Table {TABLE_NAME} created.")
except ClientError as e:
    if e.response['Error']['Code'] == 'ResourceInUseException':
        print(f"Table {TABLE_NAME} already exists.")
        table = dynamodb.Table(TABLE_NAME)
    else:
        print(f"Unexpected error: {e}")
        exit(1)

print("Seeding data...")

# Seed data into the table
items = [
    {'Id': '1', 'Name': 'John Doe', 'Age': 30},
    {'Id': '2', 'Name': 'Jane Smith', 'Age': 25},
    {'Id': '3', 'Name': 'Alice Johnson', 'Age': 28}
]

with table.batch_writer() as batch:
    for item in items:
        batch.put_item(Item=item)

print("Seeding completed.")