#Consumer
import boto3
import json
import time

sqs = boto3.client("sqs",region_name="us-east-1")
queue_url="arn_for_queue_created"

print(f"Kitchen Staff is waiting for Order")
while True:
    response= sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=5
    )
    if "Messages" in response:
        for message in response["Messages"]:
            order = json.loads(message['Body'])
            print(f"Cooking order: {order}")
            time.sleep(3)
            
            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=message["ReceiptHandle"]
            )
            print(f"Order Completed: {order}")
    else:
        print("No new Orders, kitchen is idle")
