## Python woth boto3 and DynamoDB

- create file name python-boto3.py
- add below code
```python
import boto3

# Create DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
# Reference the table
table = dynamodb.Table('Users')

#  Insert (Put Item)
table.put_item(
    Item={
        'UserID': '101',
        'Name': 'Alice',
        'Email': 'alice@example.com',
        'Age': 25
    }
)

print("Item inserted successfully.")

# Get (Read Item)
response = table.get_item(
    Key={
        'UserID': '101'
    }
)
print("Retrieved Item:", response.get('Item'))

# Update Item
table.update_item(
    Key={'UserID': '101'},
    UpdateExpression="set Age = :age",
    ExpressionAttributeValues={':age': 26}
)
print("Item updated successfully.")

# Scan All Items
response = table.scan()
print(" All Items:", response['Items'])

# Delete Item
table.delete_item(Key={'UserID': '101'})
print("Item deleted successfully.")
```
- save the file and then set up virtual environment
- run below commands in bash
```bash
python3 -m venv myenv
source myenv/bin/activate
pip install boto3
python3 python-boto3.py
```
- check your output
- deactivate virtual environment
```bash
deactivate
```