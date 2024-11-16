import boto3
from botocore.exceptions import ClientError

DYNAMODB_ENDPOINT = "http://localhost:8000"
REGION_NAME = "us-west-2"
TABLE_NAME = "test"
FACTS_TABLE_NAME = "facts"

# Initialize DynamoDB resource
dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url=DYNAMODB_ENDPOINT,
    region_name=REGION_NAME,
    aws_access_key_id='dummy',
    aws_secret_access_key='dummy'
)

print(f"Creating Table {TABLE_NAME}")

# Create the test table
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
    table.meta.client.get_waiter('table_exists').wait(TableName=TABLE_NAME)
    print(f"Table {TABLE_NAME} created successfully.")
except ClientError as e:
    if e.response['Error']['Code'] == 'ResourceInUseException':
        print(f"Table {TABLE_NAME} already exists.")
    else:
        print(f"Unexpected error: {e}")
        exit(1)

print("Seeding data...")

# Seed data into the test table
items = [
    {'Id': '1', 'Name': 'John Doe', 'Age': 30},
    {'Id': '2', 'Name': 'Jane Smith', 'Age': 25},
    {'Id': '3', 'Name': 'Alice Johnson', 'Age': 28}
]

table = dynamodb.Table(TABLE_NAME)

with table.batch_writer() as batch:
    for item in items:
        batch.put_item(Item=item)

print("Seeding completed.")

# Create the facts table
print(f"Creating Table {FACTS_TABLE_NAME}")

try:
    facts_table = dynamodb.create_table(
        TableName=FACTS_TABLE_NAME,
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
    facts_table.meta.client.get_waiter('table_exists').wait(TableName=FACTS_TABLE_NAME)
    print(f"Table {FACTS_TABLE_NAME} created successfully.")
except ClientError as e:
    if e.response['Error']['Code'] == 'ResourceInUseException':
        print(f"Table {FACTS_TABLE_NAME} already exists.")
        facts_table = dynamodb.Table(FACTS_TABLE_NAME)
    else:
        print(f"Unexpected error: {e}")
        exit(1)

# Seed data into the facts table
facts = [
    {"Id": "1", "Category": "basketball", "Fact": "Michael Jordan has won six NBA championships."},
    {"Id": "2", "Category": "basketball", "Fact": "Kareem Abdul-Jabbar is the all-time leading scorer in NBA history."},
    {"Id": "3", "Category": "basketball", "Fact": "The NBA was founded in New York City on June 6, 1946."},
    {"Id": "4", "Category": "basketball", "Fact": "Wilt Chamberlain scored 100 points in a single game."},
    {"Id": "5", "Category": "basketball", "Fact": "The Boston Celtics have the most NBA titles with 17 championships."},
    {"Id": "6", "Category": "basketball", "Fact": "Basketball was invented in 1891 by Dr. James Naismith."},
    {"Id": "7", "Category": "studying", "Fact": "The Pomodoro Technique helps improve focus by working in 25-minute intervals."},
    {"Id": "8", "Category": "studying", "Fact": "Exercise before studying can enhance learning and memory."},
    {"Id": "9", "Category": "studying", "Fact": "Short, frequent study sessions are more effective than long, infrequent ones."},
    {"Id": "10", "Category": "studying", "Fact": "Taking handwritten notes improves memory more than typing."},
    {"Id": "11", "Category": "studying", "Fact": "Sleep plays a crucial role in memory consolidation after studying."}
]

print(f"Seeding data into {FACTS_TABLE_NAME}")

with facts_table.batch_writer() as batch:
    for fact in facts:
        batch.put_item(Item=fact)

print("Seeding completed.")