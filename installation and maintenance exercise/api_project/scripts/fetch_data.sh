#!/bin/bash

echo "Fetching and processing user data..."

API_URL="https://jsonplaceholder.typicode.com/users?_limit=5"
OUTPUT_FILE="../data/user_summary.json"

curl -s "$API_URL" | jq '[.[] | {id, name, email}]' > $OUTPUT_FILE

echo "Data saved to $OUTPUT_FILE"

