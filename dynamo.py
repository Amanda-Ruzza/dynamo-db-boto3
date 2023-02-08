import boto3

# Getting the service resource
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table named MUSICIANS.
table = dynamodb.create_table(
    TableName='musicians',
    KeySchema=[
        {
            'AttributeName': 'instrument',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'musician_name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'instrument',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'musician_name',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.wait_until_exists()

# Print out some data about the table.
print(table.item_count)


