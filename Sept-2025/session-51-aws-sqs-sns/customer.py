## Producer
import boto3
import json

#inialize SQS Client
sqs = boto3.client("sqs",region_name="us-east-1")

queue_url="arn_for_queue_created"

orders=[
    {"order_id":1,"item":"pizza","quantity":2},
    {"order_id":2,"item":"burger","quantity":2},
    {"order_id":3,"item":"cheeze","quantity":3},
    {"order_id":4,"item":"milk","quantity":4},
]

#Send them to SQS
for order in orders:
    response= sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(order)
    )
    print(f"order sent: {order} | MessageId: {response['MessageId']}")
