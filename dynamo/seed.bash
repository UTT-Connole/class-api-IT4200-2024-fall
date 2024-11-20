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

# --------------------------
# Table for storing travel data (for /travel endpoint)
TRAVEL_TABLE_NAME="travel"
echo "Creating Table $TRAVEL_TABLE_NAME"

aws dynamodb create-table \
    --table-name $TRAVEL_TABLE_NAME \
    --attribute-definitions AttributeName=ID,AttributeType=S \
    --key-schema AttributeName=ID,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --endpoint-url $DYNAMODB_ENDPOINT

echo "Waiting for $TRAVEL_TABLE_NAME to be created..."
aws dynamodb wait table-exists --table-name $TRAVEL_TABLE_NAME --endpoint-url $DYNAMODB_ENDPOINT

echo "Table $TRAVEL_TABLE_NAME created."
echo "Seeding data for travel table..."

# Insert all travel data items
aws dynamodb put-item \
    --table-name $TRAVEL_TABLE_NAME \
    --item '{"ID": {"S": "1"}, "destination": {"S": "Paris, France"}, "duration": {"S": "9h 50m"}, "continent": {"S": "Europe"}, "best_season": {"S": "Spring"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TRAVEL_TABLE_NAME \
    --item '{"ID": {"S": "2"}, "destination": {"S": "Rome, Italy"}, "duration": {"S": "13hr 30m"}, "continent": {"S": "Europe"}, "best_season": {"S": "Summer"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TRAVEL_TABLE_NAME \
    --item '{"ID": {"S": "3"}, "destination": {"S": "London, England"}, "duration": {"S": "9hr 30m"}, "continent": {"S": "Europe"}, "best_season": {"S": "Fall"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TRAVEL_TABLE_NAME \
    --item '{"ID": {"S": "4"}, "destination": {"S": "Tokyo, Japan"}, "duration": {"S": "13hr 40m"}, "continent": {"S": "Asia"}, "best_season": {"S": "Spring"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TRAVEL_TABLE_NAME \
    --item '{"ID": {"S": "5"}, "destination": {"S": "Barcelona, Spain"}, "duration": {"S": "12hr 30m"}, "continent": {"S": "Europe"}, "best_season": {"S": "Spring"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TRAVEL_TABLE_NAME \
    --item '{"ID": {"S": "6"}, "destination": {"S": "New York City, New York"}, "duration": {"S": "4hr 35m"}, "continent": {"S": "North America"}, "best_season": {"S": "Winter"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TRAVEL_TABLE_NAME \
    --item '{"ID": {"S": "7"}, "destination": {"S": "Los Angeles, California"}, "duration": {"S": "2hr"}, "continent": {"S": "North America"}, "best_season": {"S": "Fall"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TRAVEL_TABLE_NAME \
    --item '{"ID": {"S": "8"}, "destination": {"S": "Dublin, Ireland"}, "duration": {"S": "11hr 30m"}, "continent": {"S": "Europe"}, "best_season": {"S": "Fall"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TRAVEL_TABLE_NAME \
    --item '{"ID": {"S": "9"}, "destination": {"S": "Cairo, Egypt"}, "duration": {"S": "15hr 15m"}, "continent": {"S": "Africa"}, "best_season": {"S": "Winter"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TRAVEL_TABLE_NAME \
    --item '{"ID": {"S": "10"}, "destination": {"S": "Sydney, Australia"}, "duration": {"S": "18hr 15m"}, "continent": {"S": "Australia"}, "best_season": {"S": "Summer"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TRAVEL_TABLE_NAME \
    --item '{"ID": {"S": "11"}, "destination": {"S": "Sacramento, California"}, "duration": {"S": "1hr 45m"}, "continent": {"S": "North America"}, "best_season": {"S": "Spring"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TRAVEL_TABLE_NAME \
    --item '{"ID": {"S": "12"}, "destination": {"S": "Salt Lake, Utah"}, "duration": {"S": "0hr 0m"}, "continent": {"S": "North America"}, "best_season": {"S": "Anytime"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TRAVEL_TABLE_NAME \
    --item '{"ID": {"S": "13"}, "destination": {"S": "Denver, Colorado"}, "duration": {"S": "1hr 35m"}, "continent": {"S": "North America"}, "best_season": {"S": "Summer"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $TRAVEL_TABLE_NAME \
    --item '{"ID": {"S": "14"}, "destination": {"S": "Santa Cruz, California"}, "duration": {"S": "2hr"}, "continent": {"S": "North America"}, "best_season": {"S": "Fall"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

echo "Seeding completed for $TRAVEL_TABLE_NAME."

# --------------------------
# Table for storing fortunes (for /fortune endpoint)
FORTUNE_TABLE_NAME="fortunes"
echo "Creating Table $FORTUNE_TABLE_NAME"

aws dynamodb create-table \
    --table-name $FORTUNE_TABLE_NAME \
    --attribute-definitions AttributeName=ID,AttributeType=S \
    --key-schema AttributeName=ID,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --endpoint-url $DYNAMODB_ENDPOINT

echo "Waiting for $FORTUNE_TABLE_NAME to be created..."
aws dynamodb wait table-exists --table-name $FORTUNE_TABLE_NAME --endpoint-url $DYNAMODB_ENDPOINT

echo "Table $FORTUNE_TABLE_NAME created."
echo "Seeding data for fortune table..."

# Insert fortune data
aws dynamodb put-item \
    --table-name $FORTUNE_TABLE_NAME \
    --item '{"ID": {"S": "1"}, "fortune": {"S": "You will find a fortune."}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $FORTUNE_TABLE_NAME \
    --item '{"ID": {"S": "2"}, "fortune": {"S": "A fresh start will put you on your way."}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $FORTUNE_TABLE_NAME \
    --item '{"ID": {"S": "3"}, "fortune": {"S": "Fortune favors the brave."}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $FORTUNE_TABLE_NAME \
    --item '{"ID": {"S": "4"}, "fortune": {"S": "Good news will come to you by mail."}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $FORTUNE_TABLE_NAME \
    --item '{"ID": {"S": "5"}, "fortune": {"S": "A beautiful, smart, and loving person will be coming into your life."}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $FORTUNE_TABLE_NAME \
    --item '{"ID": {"S": "6"}, "fortune": {"S": "A soft voice may be awfully persuasive."}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2

aws dynamodb put-item \
    --table-name $FORTUNE_TABLE_NAME \
    --item '{"ID": {"S": "7"}, "fortune": {"S": "All your hard work will soon pay off."}}' \
    --endpoint-url $DYNAMODB_ENDPOINT \
    --region us-west-2


echo "Seeding completed for $NAMES_TABLE_NAME."

# Table for storing meals data (for /meal/<meal_id> endpoint)
MEALS_TABLE_NAME="meals"
echo "Creating Table $MEALS_TABLE_NAME"

aws dynamodb create-table \
    --table-name $MEALS_TABLE_NAME \
    --attribute-definitions AttributeName=id,AttributeType=S \
    --key-schema AttributeName=id,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --endpoint-url $DYNAMODB_ENDPOINT

echo "Waiting for $MEALS_TABLE_NAME to be created..."
aws dynamodb wait table-exists --table-name $MEALS_TABLE_NAME --endpoint-url $DYNAMODB_ENDPOINT

echo "Table $MEALS_TABLE_NAME created."
echo "Seeding data for meals table..."

# Insert meals data
aws dynamodb put-item \
    --table-name $MEALS_TABLE_NAME \
    --item '{"id": {"S": "1"}, "name": {"S": "Classic Meal"}, "pizza": {"S": "Pepperoni"}, "soda": {"S": "Coca Cola"}, "size": {"S": "2 Liter"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT

aws dynamodb put-item \
    --table-name $MEALS_TABLE_NAME \
    --item '{"id": {"S": "2"}, "name": {"S": "Vegan Meal"}, "pizza": {"S": "Vegan"}, "soda": {"S": "Sprite"}, "size": {"S": "Personal"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT

aws dynamodb put-item \
    --table-name $MEALS_TABLE_NAME \
    --item '{"id": {"S": "3"}, "name": {"S": "Family Meal"}, "pizza": {"S": "Cheese"}, "soda": {"S": "Mountain Dew"}, "size": {"S": "2 Liter"}}' \
    --endpoint-url $DYNAMODB_ENDPOINT

echo "Seeding completed for $MEALS_TABLE_NAME."