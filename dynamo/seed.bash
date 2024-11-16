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

# --------------------------
# Table for storing names data (for /generateName endpoint)
NAMES_TABLE_NAME="names"
echo "Creating Table $NAMES_TABLE_NAME"

aws dynamodb create-table \
    --table-name $NAMES_TABLE_NAME \
    --attribute-definitions AttributeName=gender,AttributeType=S AttributeName=name,AttributeType=S \
    --key-schema AttributeName=gender,KeyType=HASH AttributeName=name,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --endpoint-url $DYNAMODB_ENDPOINT

echo "Waiting for $NAMES_TABLE_NAME to be created..."
aws dynamodb wait table-exists --table-name $NAMES_TABLE_NAME --endpoint-url $DYNAMODB_ENDPOINT

echo "Table $NAMES_TABLE_NAME created."
echo "Seeding data for names table..."

# Insert names data
aws dynamodb put-item \
    --table-name $NAMES_TABLE_NAME \
    --item '{"gender": {"S": "male"}, "name": {"S": "John"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $NAMES_TABLE_NAME \
    --item '{"gender": {"S": "female"}, "name": {"S": "Jane"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $NAMES_TABLE_NAME \
    --item '{"gender": {"S": "male"}, "name": {"S": "Michael"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

echo "Seeding completed for $NAMES_TABLE_NAME."

# Pokefishing endpoint table
TABLE_NAME="pokefishing"
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
    --item '{"Id": {"S": "1"}, "catch": {"S": "a regular ol' Magikarp"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TABLE_NAME \
    --item '{"Id": {"S": "2"}, "catch": {"S": "a calico pattern Magikarp"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TABLE_NAME \
    --item '{"Id": {"S": "3"}, "catch": {"S": "a orange two-tone pattern Magikarp"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TABLE_NAME \
    --item '{"Id": {"S": "4"}, "catch": {"S": "a pink dapple pattern Magikarp"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TABLE_NAME \
    --item '{"Id": {"S": "5"}, "catch": {"S": "a gray diamond pattern Magikarp"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TABLE_NAME \
    --item '{"Id": {"S": "6"}, "catch": {"S": "a purple patches pattern Magikarp"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TABLE_NAME \
    --item '{"Id": {"S": "7"}, "catch": {"S": "a apricot tiger pattern Magikarp"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TABLE_NAME \
    --item '{"Id": {"S": "8"}, "catch": {"S": "a brown stripes pattern Magikarp"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TABLE_NAME \
    --item '{"Id": {"S": "9"}, "catch": {"S": "a orange forehead pattern Magikarp"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TABLE_NAME \
    --item '{"Id": {"S": "10"}, "catch": {"S": "a blue raindrops pattern Magikarp"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TABLE_NAME \
    --item '{"Id": {"S": "11"}, "catch": {"S": "a shiny Magikarp"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TABLE_NAME \
    --item '{"Id": {"S": "12"}, "catch": {"S": "a... Oh no, it'\''s a Gyarados!!"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TABLE_NAME \
    --item '{"Id": {"S": "13"}, "catch": {"S": "a Goldeen and it'\''s the biggest you'\''ve ever seen"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TABLE_NAME \
    --item '{"Id": {"S": "14"}, "catch": {"S": "nothing... But you did see a Mudkip riding on a Lotad"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

echo "Seeding completed for $TABLE_NAME."