# SQS (Simple Queue Service): fully managed messaged queuing service

## Key Points

1. Message Queueing
2. Types
    - Standard
        - Unlimited transactions per seconds
        - Best-effort ordering
        - At-least Once Delivery
    - FIFO Queue
        - First-in-first-out delivery
        - Guarantees message order
        - Exactly-once Processing

## Use Cases

1. Order Processing System: Order go to SQS queue -> service workers
    pick them one by one.
2. Decouple Microservices: A frontend service sends task to queue 
    --> Backend service process it Async
3. Async Workloads: video uploads trigger encoding jobs via queue

## AWS SQL Using Console

1. Open SQS in console
2. Create Queue
3. select type: standard or fifo
    - if its fifo the name must ends with .fifo
4. Leave all fields as default
5. Keep access policy and others fieds default values
6. create queue.

## Check Queue from CLI

--------------------- List Queues ---------------
```bash
 aws sqs list-queues
```

--------------------- Send Message ---------------
```bash
aws sqs send-message \ 
--queue-url <queue_url> \
--message-body "Hello From CLI"
```
--------------------- Receive Message -------------
```bash
aws sqs receive-message \ 
--queue-url <queue_url>
```

#### You can also try this by using from Console there is option so send and receive messages

1. Send message
    ```json
    {
        "order_id":1, 
        "item":"Pizza", 
        "quantity":2
    }
    ```
2. Poll For message as well.

## Connect SQS with lambda for Message processing 

Let's Create Lambda Function:

1. AWS Console --> Lambda
2. Create function --> name (sqs-message-processor)
3. create
4. IAM --> Roles --> Select --> Lambda role --> attach policy
5. AWSLambdaSQSQueueExecutionRole --> update it
6. In lambda --> click Add Trigger
7. select sqs --> select created sqs queue
8. in Lambda add below lines of code:

```python
def lambda_handler(event, context):
    for record in event['Records']:
        message = record['body']
        print(f"New Message received: {message}")
    return {
        'statusCode': 200,
        'body': "Messages Processed Successfully"
    }
```

9. Once code added click on deploy
10. go back to your sqs queue and try to send some messages.
11. To watch those logs
12. cloudwatch --> loggroup --> open your lambda log-group and 
13. check logs




