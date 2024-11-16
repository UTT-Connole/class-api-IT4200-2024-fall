#!/bin/bash

DYNAMODB_ENDPOINT="http://localhost:8000"

TABLE_NAME="test"
echo "Creating Table $TABLE_NAME"

aws dynamodb create-table \
    --table-name $TABLE_NAME \
    --attribute-definitions AttributeName=Id,AttributeType=S \
    --key-schema AttributeName=Id,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --endpoint-url $DYNAMODB_ENDPOINT

echo "Waiting for table to be created..."
aws dynamodb wait table-exists --table-name $TABLE_NAME --endpoint-url $DYNAMODB_ENDPOINT

echo "Table $TABLE_NAME created."
echo "Seeding data..."

aws dynamodb put-item \
    --table-name $TABLE_NAME \
    --item '{"Id": {"S": "1"}, "Name": {"S": "John Doe"}, "Age": {"N": "30"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TABLE_NAME \
    --item '{"Id": {"S": "2"}, "Name": {"S": "Jane Smith"}, "Age": {"N": "25"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TABLE_NAME \
    --item '{"Id": {"S": "3"}, "Name": {"S": "Alice Johnson"}, "Age": {"N": "28"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

echo "Seeding completed for $TABLE_NAME."

# --------------------------
# Table for storing items data (for /items endpoint)
ITEMS_TABLE_NAME="items"
echo "Creating Table $ITEMS_TABLE_NAME"

aws dynamodb create-table \
    --table-name $ITEMS_TABLE_NAME \
    --attribute-definitions AttributeName=ID,AttributeType=S \
    --key-schema AttributeName=ID,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --endpoint-url $DYNAMODB_ENDPOINT

echo "Waiting for $ITEMS_TABLE_NAME to be created..."
aws dynamodb wait table-exists --table-name $ITEMS_TABLE_NAME --endpoint-url $DYNAMODB_ENDPOINT

echo "Table $ITEMS_TABLE_NAME created."
echo "Seeding data for items table..."

# Insert items data
aws dynamodb put-item \
    --table-name $ITEMS_TABLE_NAME \
    --item '{"ID": {"S": "1"}, "Name": {"S": "Item One"}, "Description": {"S": "A sample item."}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $ITEMS_TABLE_NAME \
    --item '{"ID": {"S": "2"}, "Name": {"S": "Item Two"}, "Description": {"S": "Another sample item."}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $ITEMS_TABLE_NAME \
    --item '{"ID": {"S": "3"}, "Name": {"S": "Item Three"}, "Description": {"S": "Yet another item."}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

echo "Seeding completed for $ITEMS_TABLE_NAME."
