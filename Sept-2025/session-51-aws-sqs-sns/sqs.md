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