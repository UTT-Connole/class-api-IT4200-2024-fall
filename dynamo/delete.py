import boto3
from botocore.exceptions import ClientError

DYNAMODB_ENDPOINT = "http://localhost:8000"
REGION_NAME = "us-west-2"

# Initialize DynamoDB client
dynamodb = boto3.client(
    "dynamodb",
    endpoint_url=DYNAMODB_ENDPOINT,
    region_name=REGION_NAME,
    aws_access_key_id="dummy",
    aws_secret_access_key="dummy",
)

print("Getting list of tables...")

try:
    response = dynamodb.list_tables()
    tables = response.get("TableNames", [])
    if not tables:
        print("No tables to delete.")
        exit(0)
except ClientError as e:
    print(f"Error listing tables: {e}")
    exit(1)

print("Deleting tables...")
for table_name in tables:
    print(f"Deleting table: {table_name}")
    try:
        dynamodb.delete_table(TableName=table_name)
        # Wait until the table is deleted
        waiter = dynamodb.get_waiter("table_not_exists")
        waiter.wait(TableName=table_name)
    except ClientError as e:
        print(f"Error deleting table {table_name}: {e}")

print("All tables have been deleted.")