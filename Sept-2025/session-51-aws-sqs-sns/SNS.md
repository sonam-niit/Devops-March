# SNS: Simple Notification Service
## Fully Managed pub/sub messaging service

### Key points

1. Pub-sub model
    - publisher sends message to topic
    - subscribers to that topic (email, SMS, Lambda, SQS) automatically receives message
2. Fan-out Architecture:
    - one message -> delivered to many endpoints

3. Delivery Options:
    - Email Notifications
    - SMS (Text messages)
    - Push notifications (google)
    - AWS Lambda functions
    - SQS queues

#### Send Email with SNS

1. Console --> SNS --> Create topic --> OrderUpdates --> Create topic
2. Add Subscription --> ARN-orderupdates --> enter your email --> create
3. go to the topic --> publish message --> write subject
4. set message body --> Publish
5. you wit get the email instantly.

### Publish message
```bash
aws sns publish \
> --topic-arn <enter_your_arn_here> \
> --subject "Class Demo" \
> --message "Hello Everyone! this is the Test Email From Sonam"
```


- Link for python SDK: [text](https://docs.aws.amazon.com/code-library/latest/ug/python_3_sns_code_examples.html)