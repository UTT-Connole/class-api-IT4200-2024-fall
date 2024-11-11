#!/bin/bash

echo "Getting list of tables..."
tables=$(aws dynamodb list-tables --endpoint-url http://localhost:8000 --query "TableNames[]" --output text --region us-west-2)

echo "Deleting tables..."
for table in $tables; do
    echo "Deleting table: $table"
    aws dynamodb delete-table --table-name $table --endpoint-url http://localhost:8000 --region us-west-2
done

echo "All tables have been deleted."