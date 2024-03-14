# A. Designing Event-Driven Architectures
- [A. Designing Event-Driven Architectures](#a-designing-event-driven-architectures)
  - [A.1 Thinking Serverless](#a1-thinking-serverless)
  - [A.2 Serverless Event Submission Patterns](#a2-serverless-event-submission-patterns)
  - [A.3 Workflow orchestration with AWS Step Functions](#a3-workflow-orchestration-with-aws-step-functions)
  - [A.4 Patterns for Communicating Status Updates](#a4-patterns-for-communicating-status-updates)
  - [A.5 Serverless Data Processing Patterns](#a5-serverless-data-processing-patterns)
    - [A.5.2 Kinesis Data Streams and Kinesis Data Firehose](#a52-kinesis-data-streams-and-kinesis-data-firehose)
    - [A.5.3 Amazon SNS filtering, fan-out, and nested serverless applications](#a53-amazon-sns-filtering-fan-out-and-nested-serverless-applications)
    - [A.5.4 Streaming or messaging for data processing](#a54-streaming-or-messaging-for-data-processing)
  - [A.6 Failure Management in Event-Driven Architectures](#a6-failure-management-in-event-driven-architectures)
  - [A.7 Failure management across your application](#a7-failure-management-across-your-application)
  - [A.8 Failure management with dead-letter queues](#a8-failure-management-with-dead-letter-queues)
    - [A.9 AWS Event Fork Pipelines](#a9-aws-event-fork-pipelines)
  - [A.10 Distributed tracing with AWS X-Ray](#a10-distributed-tracing-with-aws-x-ray)
## A.1 Thinking Serverless
> The term ``serverless`` represents abstracting your computing infrastructure to the point that you have no responsibilities for the servers on which your code runs. This means when your application isn't running, you're not paying for idle server time.

> ``Event-driven`` architectures **use events to communicate between and invoke decoupled services**. These events are simple changes, or updates, to a state such as an item being placed in a shopping cart on an e-commerce website.

## A.2 Serverless Event Submission Patterns
As discussed in the previous lesson, **using an asynchronous pattern can be more beneficial for some workloads than synchronous patterns**. This is because of potential downstream issues, the need for immediate responses, and no built-in retries.

By introducing the ``SQS queue`` in front of ``Lambda``, **you can create an asynchronous connection between the API request and Lambda**. This allows you to satisfy the API request without regard for how long the Lambda function (or other backend services) will run.
* The message is stored on the SQS queue durably.  
* The Lambda service ``polls`` the ``Amazon SQS queue``. The Lambda service uses long polling to poll the SQS queue, waiting for messages to appear.
* If Lambda finds new messages, **it invokes the Lambda function the queue is connected to, passing the message as a parameter and including the message ID for identifying the message**. The Lambda service reads messages in batches and invokes your Lambda function once per batch.
> By default, ``Lambda`` **reads up to five batches at a time** and sends each batch to an invocation of your function. Each invocation of the Lambda function gets an event object that contains the messages in a batch.
* The messages in that batch become hidden to other consumers for the duration of the queue’s visibility timeout setting
* When your Lambda function successfully processes a batch, the Lambda service deletes that batch of messages from the queue.  If your function returns an error or doesn’t respond, the messages in that batch become visible again.
* If any of the messages in the batch fail, all items in the batch become visible on the queue again. This means that some messages will be processed more than once. You want to include code in your Lambda functions to handle this kind of partial failure. Your Lambda function should delete each message from the queue after successfully processing it. That way if the batch fails, only the unsuccessful messages reappear in the queue.
* When a message continues to fail, send it to a dead-letter queue. A dead-letter queue is another SQS queue that you use to process failed messages. This is optional, but recommended.
* Make sure that you configure the dead-letter queue on the source queue versus configuring the dead-letter queue option on the Lambda function.
* Amazon SQS supports both standard and First-In-First-Out (FIFO) queues, but currently only standard queues can be used as Lambda event sources. 
* Standard queues provide much higher throughput, but order is not guaranteed. Also, messages may be delivered more than once, so you need to write idempotent functions that can process the same message multiple times without unexpected results.

| **Characteristic**  | **Standard**  | **FIFO**  |
|---|---|---|
| **Record Order**  | Order is not guaranteed  | Order is guaranteed per group ID  |
| **Delivery**  | Messages may be delivered more than once  | Messages are delivered only once. There are no duplicate messages introduced to the queue  |
| **Transaction Throughput**  | Nearly unlimited messages per second  | FIFO queues support up to 300 messages per second, per API action without batching, or 3,000 with batching  |

**Additional resources: documentation**
* [Amazon SQS Overview](https://aws.amazon.com/sqs/)
* [Amazon SQS Developer](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
* [Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-limits.html)
* [Using AWS Lambda with Amazon SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html)

**Additional resources: blog posts**
* [AWS News Blog: AWS Lambda Adds Amazon SQS to Supported Event Sources](https://aws.amazon.com/blogs/aws/aws-lambda-adds-amazon-simple-queue-service-to-supported-event-sources/)
* [AWS Lambda Supports Amazon SQS FIFO (First-In-First-Out) as an Event Source](https://aws.amazon.com/about-aws/whats-new/2019/11/aws-lambda-supports-amazon-sqs-fifo-event-source/)

## A.3 Workflow orchestration with AWS Step Functions
``AWS Step Functions`` can coordinate the distributed components of your application and keep the need for orchestration out of your code. It automatically launches and tracks each step, and can retry steps when there are errors. 

**Step Functions Express Workflows**

Step Functions Express Workflows are an alternative to the Standard Workflows described in the video. Express Workflows are designed for high-volume, short-duration use cases. Review the following resources to learn if Express Workflows suit your use case:

* AWS News Blog: [AWS Step Functions Express Workflows: High Performance and Low Cost](https://aws.amazon.com/blogs/aws/new-aws-step-functions-express-workflows-high-performance-low-cost/)
* AWS Step Functions Developer Guide: [Standard vs. Express Workflows](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html)

**Recap**

* Don't **use Amazon API Gateway as an event source for ``AWS Lambda``.**, **use a standard ``Amazon Simple Queue Service (Amazon SQS)`` queue as an event source for ``AWS Lambda``** instead.
* ``Step Functions`` is a good option for managing the integration with the legacy system because it can control the flow of tasks and wait for a response from the legacy system without adding additional logic or increasing the duration of your Lambda function.

**Additional resources: Courses**
* [Introduction to Step Functions](https://explore.skillbuilder.aws/pages/55/learner-dashboard?ctl231=se-%22Introduction%20to%20Step%20Functions%22)
* [How AWS Step Functions Work](https://explore.skillbuilder.aws/pages/55/learner-dashboard?ctl231=se-%22How%20AWS%20Step%20Functions%20Work%22)
* [Observability for AWS Step Functions](https://explore.skillbuilder.aws/pages/55/learner-dashboard?ctl231=se-%22Observability%20for%20AWS%20Step%20Functions%22)
* [Developer Tooling for AWS Step Functions](https://explore.skillbuilder.aws/pages/55/learner-dashboard?ctl231=se-%22Developer%20Tooling%20for%20AWS%20Step%20Functions%22)
* [Design Patterns for AWS Step Functions](https://explore.skillbuilder.aws/pages/55/learner-dashboard?ctl231=se-%22Design%20Patterns%20for%20AWS%20Step%20Functions%22)


**Additional resources: Documentation**

* [AWS Step Functions Developer Guide](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
* [AWS Step Functions Overview](https://aws.amazon.com/step-functions/)
* [AWS Step Functions Quotas](https://docs.aws.amazon.com/step-functions/latest/dg/limits.html)
* [Supported AWS Service Integrations for Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/connect-supported-services.html)

**Additional resources: Online videos and workshops**

* [Introduction to AWS Step Functions](https://youtu.be/Dh7h3lkpeP4)
* [Build on Serverless: Breaking the Monolith with Step Functions](https://youtu.be/CFelZoLjF50)
* [The AWS Step Functions Workshop](https://catalog.workshops.aws/stepfunctions/en-US)

**Additional resources: Tutorials and samples**
* [Tutorial: Create a Serverless Workflow](https://aws.amazon.com/getting-started/tutorials/create-a-serverless-workflow-step-functions-lambda/)
* [Builder Session: Create a State Machine that Implements the Saga Pattern](https://github.com/aws-samples/aws-step-functions-long-lived-transactions)

## A.4 Patterns for Communicating Status Updates

**Three patterns for communicating status updates**

In an architecture in the previous lesson, the client service submitted an order, and the SQS queue gave a response to API Gateway with the message ID. Then Lambda pulled the message from the queue and handed it off to Step Functions to complete the order process and update the job status as it moved through the workflow.

The next thing you need to consider is how to provide the status to the calling client. The method you choose depends on your use case. The next set of videos looks at three potential approaches:

* **Client polling**: Client polling provides a solution with minimal rework but does have potential for latency between polling.
* **Webhooks!** with Amazon Simple Notification Service (Amazon SNS): If you have an internal service, you can use trusted webhooks to provide results data to the client without the need for polling.
* **WebSockets with AWS AppSync**: WebSockets with AWS AppSync lets clients receive status updates as they occur and is a good option when data drives the user interface.


**Additional resources: Documentation**

* [AWS AppSync Overview](https://aws.amazon.com/appsync/)
* [AWS AppSync Developer Guide](https://docs.aws.amazon.com/appsync/latest/devguide/welcome.html)

**Additional resources: Blog posts**
* [AWS Architecture Blog: How to Architect APIs for Scale and Security](https://docs.aws.amazon.com/appsync/latest/devguide/welcome.html)

## A.5 Serverless Data Processing Patterns
> **One of the ways serverless services helps you focus on your business is by facilitating quick reactions to critical data.**
>
> ### A.5.1 Amazon Kinesis Data Streams

Clickstream data from mobile apps, application logs, and home security camera feeds are common examples where traditional batch processing would not give you the responsiveness you need to make data actionable. The stream also provides an asynchronous data buffer for downstream processing. To learn more, choose each numbered marker.

When it comes to Kinesis, you need to understand the difference between producers and consumers. To learn about each, choose the appropriate tab.

**Producers**
Producers add data records to the stream. Producers can be created with the following: 
* Kinesis Producer Library (KPL)
* AWS SDK
* Third-party tools

**Consumers**
Consumers get records and process them. Consumer can be any of the following:
* Lambda functions
* Other streams
* Applications created with Kinesis Client Library (KCL)

**Kinesis Data Streams capacity limits (per shard)**

Kinesis Data Streams scales horizontally by adding shards. 
> **Each shard has a uniquely identified sequence of data records, and each data record has a sequence number assigned by Kinesis.** 
The following table compares the different rate and data limits for both writes and reads.


|   | **Writes (Putting Data on the Stream)**  | **Reads(Consuming Data off the Stream)**  |
|---|---|---|
| **Rate Limit**  | 1,000 records per second  | 5 transactions per second, up to 10,000 records  |
| **Data Limit**  | 1 MB per second  | 2 MB per second  |
|   |   |   |

### A.5.2 Kinesis Data Streams and Kinesis Data Firehose

In any of the patterns we’ve looked at, you might use Kinesis Data Streams rather than Kinesis Data Firehose if it is better suited to your use case. To learn more about the differences between Kinesis Data Streams and Kinesis Data Firehose, choose the play button.

| **Kinesis Data Streams**  | **Kinesis Data Firehose**  |   
|---|---|
| You write custom consumers, with more targets   | The use case of transforming and storing streaming data is simplified  |   
| Order delivery and exactly-once delivery are guaranteed  | Order not guaranteed; messages could be delivered more than once  |  
| Failing messages block the shard until it succeeds or expires  | Retry mechanisms are available for each delivery target  |  
| You set the number of shards  | You set the data volume and the service manages the number of shards  |  
| Multiple consumers and multiple types of consumers are used  | Stream is associated with a single destination  |  


### A.5.3 Amazon SNS filtering, fan-out, and nested serverless applications

Another serverless data processing pattern you can use is messaging, instead of streaming. ``Amazon Simple Notification Service (Amazon SNS)`` uses a publication/subscription, or pub/sub, model, which means that a single published message can have multiple consumers.

**Amazon SNS message filtering**

In the ``Amazon SNS`` message filtering pattern, the subscriber assigns a filter policy to the topic subscription. The filter policy contains attributes that define which messages that subscriber receives, and Amazon SNS compares message attributes to the filter policy for each subscription. If the attributes don’t match, the message doesn’t get sent to that subscriber.

**Nested serverless applications**

Tasks like data backup or indexing data for search or analytics repeat across your larger applications. You can build these recurring patterns as smaller serverless applications and reuse them.

**Amazon EventBridge**

Amazon EventBridge is a serverless event bus that facilitates connection of applications together using AWS services and data from your own applications, as well as integrated software-as-a-service (SaaS) applications.

**Additional resources:**

* [Amazon SNS Subscription Filter Policies](https://docs.aws.amazon.com/sns/latest/dg/sns-subscription-filter-policies.html)
* [Amazon EventBridge Content-Based Filtering with Event Patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/content-filtering-with-event-patterns.html)
### A.5.4 Streaming or messaging for data processing

Now that you understand how streaming and messaging can be used for data processing, let's compare the two. Which option you select really depends on the nature of the data you are collecting and the type and timing of processing you need to do.


**Messaging**
* The core entity is an individual message, and message rates vary.
* Messages are deleted when they’ve been consumed.
* Configure retries and dead-letter queues for failures.

**Streaming**
* You look at the stream of messages together, and the stream is generally continuous.
* Data remains on the stream for a period of time. Consumers must maintain a pointer.
* A message is retried until it succeeds or expires. You must build error handling into your function to bypass a record.


* **Kinesis Data Firehose** is ideal for ingesting data for storage. It can also transform data using an AWS Lambda function before storing it.

* **Kinesis Data Firehose** streams can only be associated with a single consumer, and the target must be Amazon S3, Amazon Redshift, Amazon OpenSearch Service, or Splunk.

* **Messaging services like Amazon Simple Queue Service (Amazon SQS) or Amazon Simple Notification Service (Amazon SNS)** would be better suited for processing and responding to individual messages than processing a stream of data.

* **Kinesis Data Firehose has built-in retries**. Amazon Kinesis Data Streams does not, but order is not guaranteed with Kinesis Data Firehose.

**Additional resources: Kinesis documentation**

* [Amazon Kinesis Data Streams Terminology and Concepte](https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html)
* [Kinesis Data Streams Developer Guide](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)
* [Kinesis Data Firehose Developer Guide](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html)
* [Amazon Kinesis Data Firehose Data Transformatioe](https://docs.aws.amazon.com/firehose/latest/dev/data-transformation.html)
* [Amazon Kinesis Data Analytics for SQL Applications Developer Guide](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/what-is.html)
* [Kinesis Data Analytics: Preprocessing Data Using a Lambda Functioe](https://docs.aws.amazon.com/en_pv/kinesisanalytics/latest/dev/lambda-preprocessing.html)

**Additional resources: Kinesis blog posts**
* [AWS News Blog: Amazon Kinesis Data Analytics for Jave](https://aws.amazon.com/blogs/aws/new-amazon-kinesis-data-analytics-for-java/)

**Additional resources: Online videos and workshops**
* [Serverless Bytes: Building a Serverless Data Processing App](https://youtu.be/ohXgbcbYH7U)

## A.6 Failure Management in Event-Driven Architectures

You are setting up an Amazon Simple Queue Service (Amazon SQS) queue as an event source to an AWS Lambda function that takes an average of 3 minutes to process each message. What are the most appropriate configuration options as a starting point?

* Your batch size must allow all the messages in a batch to process within the Lambda timeout. That means (batch size * 3 minutes) < 15 minutes.
* It is a best practice to set the visibility timeout on your SQS queue to 6x the Lambda function timeout to allow for retries if the function is getting throttled.
* It is also a best practice to configure a dead-letter queue.
* The IteratorAge metric is helpful for monitoring streaming data, but is not relevant for queues.

**Additional resources: Developer guide pages** 

* [Error Handling and Automatic Retries in AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/retries-on-errors.html)
* [Configuring Error Handling for Asynchronous Invocation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-errors)
* [Handle Lambda Errors in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/handle-errors-in-lambda-integration.html)
* [Amazon API Gateway Quotas and Important Notes](https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html)
* [Amazon SNS Message Delivery Retries](https://docs.aws.amazon.com/sns/latest/dg/sns-message-delivery-retries.html)
* [Using AWS Lambda with Amazon Kinesis: Error Handling](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#services-kinesis-errors)
* [Kinesis Data Streams: Changing the Data Retention Period](https://docs.aws.amazon.com/streams/latest/dev/kinesis-extended-retention.html)
* [Amazon SQS Visibility Timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html)

**Additional resources: Built-in CloudWatch metrics pages**
* [Lambda Metrics](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions-metrics.html)
* [API Gateway Metrics](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-metrics-and-dimensions.html)
* [Amazon SNS Metrics](https://docs.aws.amazon.com/sns/latest/dg/sns-monitoring-using-cloudwatch.html)
* [Kinesis Data Streams Metrics](https://docs.aws.amazon.com/streams/latest/dev/monitoring-with-cloudwatch.html)
* [Amazon SQS Metrics](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.html)
* [Step Functions Metrics](https://docs.aws.amazon.com/step-functions/latest/dg/procedure-cw-metrics.html)

## A.7 Failure management across your application
Whenever possible, you should use Step Functions to minimize the amount of custom retry and backoff code you write in your Lambda functions. Step Functions were introduced earlier as a way of visualizing and orchestrating your workflow, and they are useful for managing failures.

This section focuses on ways that these four AWS services can provide failure management across your application:
* AWS Step Functions
* Amazon SQS
* Amazon SNS
* AWS X-Ray


**Additional resources: Developer guide pages**

* [Handling Error Conditions Using a State Machine](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-handling-error-conditions.html)
* [Error Handling: Examples Using Retry and Using Catch](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html#error-handling-examples)
* [Handle Lambda Service Exceptions](https://docs.aws.amazon.com/step-functions/latest/dg/bp-lambda-serviceexception.html)
* [Distributed Data Management](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/distributed-data-management.html)

**Additional resources: Whitepapers**
 [Implementing Microservices on AWS](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/microservices-on-aws.pdf)

 ## A.8 Failure management with dead-letter queues

You can turn on dead-letter queues and create dedicated dead-letter queue resources using Amazon SNS or Amazon SQS for individual Lambda functions that are invoked by asynchronous event sources. To learn more, choose the play button.

**This table compares the differences between dead-letter queues for Lambda functions and for SQS source queues.**

| **Dead-Letter Queue on Lambda Function**  | **Dead-Letter Queue on SQS Source Queue  | 
|---|---|
| Dead-letter queue is configured as part of the function.  | Dead-letter queue is part of the queue policy.  |   
| Messages that error out after two built-in retries are routed to the dead-letter queue.  | The policy describes how many retries before an item is moved to the dead-letter queue.  |   
| Both need a mechanism to redrive messages back to the original source for processing.  | Both need a mechanism to redrive messages back to the original source for processing.  |   

### A.9 AWS Event Fork Pipelines 

AWS Event Fork Pipelines are prebuilt applications, available in the [AWS Serverless Application Repositora](https://aws.amazon.com/serverless/serverlessrepo/), that you can use in your serverless applications.

The Event Replay Pipeline buffers events from the given Amazon SNS topic into an Amazon SQS queue, so it can replay these events back to another pipeline in a disaster recovery scenario.

**Additional resources
* [Amazon SQS Dead-Letter Queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)
* [Amazon SNS Dead-Letter Queues](https://docs.aws.amazon.com/sns/latest/dg/sns-dead-letter-queues.html)
* [AWS Lambda Function Dead-Letter Queues](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-dlq)

## A.10 Distributed tracing with AWS X-Ray

Another important best practice for event-driven, decoupled applications is the use of distributed tracing to give you insight into issues or bottlenecks across your distributed architecture. To learn more, choose the play button.


**Additional resources: Documentation
* [AWS X-Ray Developer Guide](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
* [Tracing Lambda-Based Applications with AWS X-Ray](https://docs.aws.amazon.com/lambda/latest/dg/using-x-ray.html)
* [Viewing the Service Map](https://docs.aws.amazon.com/xray/latest/devguide/xray-console.html#xray-console-servicemap)

Additional resources: Blog posts
* [AWS Developer Blog: Deep Dive into AWS X-Ray Groups and Use Cases](https://aws.amazon.com/blogs/developer/deep-dive-into-aws-x-ray-groups-and-use-cases/)
* [AWS Developer Blog: Analyze and Debug Distributed Applications Interactively Using X-Ray Analytics](https://aws.amazon.com/blogs/developer/new-analyze-and-debug-distributed-applications-interactively-using-aws-x-ray-analytics/)

**Additional resources**

Join the serverless community

Probably the easiest thing you can do today to start thinking serverless is to get connected to the serverless community. This is an evolving topic, and there are lots of resources to help you stay abreast of the latest updates. Between blog posts, tutorials, use case examples, and Twitch channels, you will find lots of resources to take you deeper! Here are a few things to review:


**Webpages and whitepapers**

* [AWS landing page for serverless computing](https://aws.amazon.com/serverless/)
* [Whitepaper: Serverless Application Lens: AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html)
**Blogs**

* [AWS Architecture Blog: Ten Things Serverless Architects Should Know](https://aws.amazon.com/blogs/architecture/ten-things-serverless-architects-should-know/)
* [AWS Compute Blog: AWS Lambda](https://aws.amazon.com/blogs/compute/category/compute/aws-lambda/)
* [AWS Compute Blog: Amazon API Gateway](https://aws.amazon.com/blogs/compute/category/application-services/amazon-api-gateway-application-services/)

**Online serverless workshops**

* [Build on Serverless: Season 2](https://www.youtube.com/playlist?list=PLJV9303TMVKzFk1CNV_bStVZd3ZhW8dNz)
]()Recorded live series in which Specialist Solutions Architect Heitor Lessa and guests build a serverless airline web booking application episode by episode.
* [BuildOn | Rendering Websites at the Edge with Lambda@Edge](https://www.youtube.com/watch?v=RF7x4HcQ8lM)
Recorded live hands-on session using Lambda@Edge and Amazon CloudFront to deliver high-performance and personalized experiences to global internet users.
* [Live Coding with AWS: Well-Architected Solutions](https://www.youtube.com/playlist?list=PLhr1KZpdzukf1ERxT2lJnkpsmTPyG0_cC)
]()Recorded live hands-on sessions addressing implementing the Well-Architected Framework.

**Recorded talks**

* [2021 re:Invent playlist for serverless breakout sessions](https://aws.amazon.com/lambda/resources/customer-talks/)
Recordings of 2021 re:Invent sessions focused on serverless topics.
* [AWS Lambda Customer Talks](https://aws.amazon.com/lambda/resources/customer-talks/)
Recorded customer presentations focused on how companies solved business challenges with AWS Lambda.
* [AWS Lambda Technical Talks](https://aws.amazon.com/lambda/resources/webinars-and-talks/)
Recorded talks on developing and running serverless applications built with AWS Lambda or Amazon API Gateway. The main categories are Getting Started, Use Cases, Security, Best Practices, and Development Practices.