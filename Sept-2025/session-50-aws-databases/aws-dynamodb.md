# AWS DynamoDB

- DynamoDB is a serverless, high performance No SQL database service in AWS
- best for app needing fast and scalable data access.

## Create DynamoDB from AWS Console

1. Login aws console
2. search for dynamodb --> open dashboard
3. create table --> name(Users) --> Partition Key (UserID) -- string
4. sort key its optional but if you want you can give like Email
5. table settings - default setting
6. click on cretae table
7. once its created --> click on Users
8. explore table items --> create items
9. insert data by adding attributes: Name: Sonam, Email: sonam@gmail.com, age:45
10. use appropriate data type like string or number
11. create
12. again go back to explore items and try to query also you can add filters.

## Run from CLI

```bash
aws dynamodb put-item \
    --table-name Users \
    --item '{
        "UserID":{"S":"u101"},
        "Name":{"S":"Sonam Soni"},
        "Email":{"S":"sonam@gmail.com"},
        "Age":{"N":"45"}
    }'
```

### Get Item
```bash
aws dynamodb get-item \
    --table-name Users \
    --key '{"UserID":{"S":"u101"}}'
```