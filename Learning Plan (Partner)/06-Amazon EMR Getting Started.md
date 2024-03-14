# A. Amazon EMR Getting Started
- [A. Amazon EMR Getting Started](#a-amazon-emr-getting-started)
  - [A.1 Introduction to Amazon EMR](#a1-introduction-to-amazon-emr)
  - [A.2 Amazon EMR Serverless Architecture and Use Cases](#a2-amazon-emr-serverless-architecture-and-use-cases)
    - [A.1.1 What are the core concepts of Amazon EMR Serverless?](#a11-what-are-the-core-concepts-of-amazon-emr-serverless)
    - [A.1.2 Amazon EMR Serverless use cases](#a12-amazon-emr-serverless-use-cases)
    - [A.1.3 What else should I keep in mind when using Amazon EMR Serverless?](#a13-what-else-should-i-keep-in-mind-when-using-amazon-emr-serverless)
  - [A.2 Amazon EMR Cluster Architecture and Use Cases](#a2-amazon-emr-cluster-architecture-and-use-cases)
    - [A.2.1 How is Amazon EMR used to architect a cloud solution using clusters?](#a21-how-is-amazon-emr-used-to-architect-a-cloud-solution-using-clusters)
    - [A.2.2 What data sources do EMR clusters support?](#a22-what-data-sources-do-emr-clusters-support)
    - [A.2.3 How else can I customize EMR clusters?](#a23-how-else-can-i-customize-emr-clusters)
  - [A.3 What are typical use cases for Amazon EMR clusters?](#a3-what-are-typical-use-cases-for-amazon-emr-clusters)
  - [A.4 What else should I keep in mind about Amazon EMR clusters?](#a4-what-else-should-i-keep-in-mind-about-amazon-emr-clusters)
- [B. Using Amazon EMR Serverless](#b-using-amazon-emr-serverless)
  - [B.1 How Do I Create AWS Resources for Use with Amazon EMR Serverless?](#b1-how-do-i-create-aws-resources-for-use-with-amazon-emr-serverless)
- [C. How can I learn more about Amazon EMR?](#c-how-can-i-learn-more-about-amazon-emr)

## A.1 Introduction to Amazon EMR
What are the differences in deployment options for Amazon EMR?

``Amazon EMR`` provides **four different ways for you to deploy applications**. To learn more the deployment options and when are they suitable for customers, choose the following four tabs.
*  ``Amazon EMR Serverless``: The ``Amazon EMR Serverless`` option **helps data analysts and engineers run open-source big data analytics frameworks without configuring, managing, and scaling clusters or servers**. You get all the features and benefits of ``Amazon EMR`` without the need for experts to plan and manage clusters.
> ``Amazon EMR Serverless`` is suitable for customers who want to avoid managing and operating clusters and prefer to run applications using open-source frameworks. 

* ``Amazon EMR On Amazon EC2``: The closest deployment environment to a YARN-based Hadoop platform supporting various open-source frameworks. ``Amazon EMR on Amazon EC2`` clusters **are suitable for customers who need maximum control and flexibility over running their applications**. With ``Amazon EMR on Amazon EC2`` clusters, customers can choose the EC2 instance type to meet application-specific performance needs and customize the Linux AMI and EC2 instance configuration. They can also customize and extend open-source frameworks and install additional custom software on cluster instances.

* ``Amazon EMR On Amazon EKS``: This option runs applications on an ``Amazon EKS`` cluster that offers the benefits of both ``Amazon EMR and Kubernetes``. ``Amazon EMR on EKS`` is **suitable for customers who want to standardize on ``Amazon EKS`` to manage clusters across applications or use different versions of an open-source framework on the same cluster``.

* ``Amazon EMR On Amazon Outposts``: This fully managed service offers the same AWS infrastructure and services, APIs, and tools **to virtually any data center, co-location space, or on-premises facility for a consistent hybrid experience.** ``Amazon EMR on AWS Outposts`` is for customers who want to run ``Amazon EMR`` closer to their data center, within an Outpost.

## A.2 Amazon EMR Serverless Architecture and Use Cases
``Amazon EMR Serverless`` **automatically provisions, configures, and scales compute and memory resources required at each stage of your data-processing application**. 
> With ``Amazon EMR Serverless``, **your jobs run faster because it includes the performance-optimized** ``Amazon EMR`` runtime for Apache Spark, Hive, Presto, and other technologies. 

Additionally, ``Amazon EMR Serverless`` integrates with EMR Studio to provide an interactive development experience using notebooks and familiar open-source tools. Such tools include **Spark UI and Tez UI** to help you develop, visualize, and debug your applications.

As soon as the ``Amazon EMR`` application is created, `**users can start submitting their Apache Spark jobs**. There are multiple ways to submit Apache Spark jobs. For example, you can use Apache Airflow, Step Functions, EMR Studio notebook, the AWS CLI, AWS SDK, or custom-built pipelines. ``Amazon EMR Serverless`` automatically provisions workers required for data processing jobs in the ``Amazon EMR`` service account. These interact with resources in your AWS account to run the jobs.


### A.1.1 What are the core concepts of Amazon EMR Serverless?

With ``Amazon EMR Serverless``, the behind-the-scenes architecture remains similar to ``Amazon EMR running on Amazon EC2 and Amazon EMR on EKS``. However, the core concepts you work with shift from nodes to application, jobs, workers, and pre-initialized workers.

**Application**: You can create one or more applications that use open-source analytics frameworks by specifying the framework that you want to use (for example, Apache Spark or Apache Hive), the ``Amazon EMR`` release version, and the name of your application.

**Jobs:** A job is a request submitted to an ``Amazon EMR Serverless`` application that runs asynchronously and is tracked through completion. **You can run multiple jobs concurrently in an application**. Jobs are run in a single Availability Zone to avoid cross-AZ network communication. If there is an Availability Zone failure, jobs are retried in a healthy AZ.

**Workers:** ``Amazon EMR Serverless`` applications use workers internally to run jobs. Depending on the open-source framework, it uses a default number of vCPU, memory, and local storage per worker. You can override these defaults for your application.

**Pre-initializers Workers**: With ``Amazon EMR Serverless``, **you can pre-initialize workers when your applications start up, so that those workers are warmed up and ready to process requests immediately when a job is submitted to the application**. This optional setting is useful when you need a sub-second response to start processing requests.

### A.1.2 Amazon EMR Serverless use cases   
* Apache Spark ETL Jobs
* Large-scale SQL queries using Hive
* Interactive analysis using jupyter notebooks with EMR studio
* Ad-hoc analysis using Presto
* Building real-time streaming data pipelines
* Running AI/ML workloads onAmazon EMR

### A.1.3 What else should I keep in mind when using Amazon EMR Serverless?

There are multiple aspects to consider while designing workloads to run on Amazon EMR. To learn more about Amazon EMR Serverless considerations, expand each of the following three sections.

* Fine-grained auto-scalling with no need to guess cluster size
* Resilience to Availability zones failures
* Different Amazon EMR deployment options

* [Getting Started with Amazon EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/getting-started.html)
To learn more about getting started with Amazon EMR Serverless when you deploy a sample Spark or Hive workload, choose the following button.

* [Run Big Data Applications without Managing Servers](https://aws.amazon.com/blogs/big-data/announcing-amazon-emr-serverless-preview-run-big-data-applications-without-managing-servers/) 
To learn more about using Amazon EMR Serverless, choose the following button.

## A.2 Amazon EMR Cluster Architecture and Use Cases

### A.2.1 How is Amazon EMR used to architect a cloud solution using clusters?
The central component of ``Amazon EMR** is **the cluster**. A cluster is a collection of Amazon EC2 instances.

Each instance in the cluster is called a **node**, and every node has a role (or node type) within the cluster. ``Amazon EMR`` also installs different software components on each node type, giving each node a role in a distributed application, such as Apache Spark. 
> **The three types of nodes are primary, core, and task**.

* The **primary node**managed the cluster by running software components to coordinate the distribution of data and tasks amont other node for processing. It also track the status of tasks and monitor the cluster's health.

* The **Core node** runs tasks and store data in the HDFS of your cluster. **Multi-node cluster have at least one core node**

* The **task node** hos software components that only runs tasks. It does not store data in HDFS. **Tasks nodes are optional**

### A.2.2 What data sources do EMR clusters support?

``Amazon EMR`` **supports virtually unlimited storage capacity through the EMRFS backed by Amazon S3**, which can be shared across multiple EMR clusters or Amazon EMR Serverless. As a standard storage choice in Hadoop, **Amazon EMR also provides the Hadoop Distributed File System (HDFS) option, which stores your data with three copies by default, across local disks in your cluster**. You can use HDFS along with Amazon S3 to improve your data durability, security, and I/O performance. 
> **Amazon EMR clusters process data from the native HDFS as well as from the EMRFS (Amazon S3).**


**HDFS**
The primary and core nodes use the HDFS for caching the results produced by intermediate job-flow steps. Instance store and Amazon EBS volume storage is used for HDFS data and for buffers, caches, scratch data, and other temporary content that some applications may “spill” to the local file system. Amazon EBS works differently within Amazon EMR than it does with regular Amazon EC2 instances, and the EBS volumes attached to EMR clusters are ephemeral.

**EMRGS**
EMRFS is an implementation of the Hadoop file system used for reading and writing regular files from Amazon EMR directly to Amazon S3. EMRFS provides the convenience of storing persistent data in Amazon S3 for use with Hadoop, while also providing features like Amazon S3 server-side encryption, read-after-write consistency, and list consistency.

Amazon EMR is a large Spark and Hadoop service provider and the Release Guide gives details of all the open-source applications that are bundled with Amazon EMR. You can also use a bootstrap action to install additional software, or customize the configuration of cluster instances. Bootstrap actions are scripts that run on a cluster after Amazon EMR launches the instance using the Linux Amazon Machine Image (AMI).

### A.2.3 How else can I customize EMR clusters?

Customizing clusters helps to optimize for cost and performance based on workload requirements. Lake Formation and Apache Ranger bring fine-grain access control, while integration with Step Functions and Amazon MWAA help with orchestrating your data pipelines. Tools such as EMR Studio, EMR notebooks, and Apache Zeppelin provide an integrated development environment (IDE) that can help data scientists and data engineers develop, visualize, and debug data engineering and data science applications written in R, Python, Scala, and PySpark. 

You can monitor Amazon EMR using CloudWatch, Ganglia, and CloudTrail for metrics and logs specific to Amazon EMR.

* [EMRFS Release Guide](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-fs.html)
To learn more about EMRFS with Amazon EMR, choose the following button.

* [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/connect-emr.html)
To learn more about Step Functions with Amazon EMR, choose the following button.

* [Amazon MWAA]https://docs.aws.amazon.com/mwaa/latest/userguide/samples-emr.html() 
To learn more about using Amazon EMR and Amazon MWAA, choose the following button.

## A.3 What are typical use cases for Amazon EMR clusters?

* **Perform Big-Data Analytics**: Run large-scale data processing and what-if analysis using statistical algorithms and predictive models to uncover hidden patterns, correlations, market trends, and customer preferences.

* **Build Scalable Data Pipelines**: Extract data from a variety of sources, process it at petabyte scale, and make it available for applications and users.
  
* **Process Real-Time Data Streams**: Analyze events from streaming data sources in real time to create long-running, highly available, and fault-tolerant streaming data pipelines.

* **Analyse Data and ML Adoption**: Analyze data using open-source ML frameworks such as Apache Spark MLlib, TensorFlow, and Apache MXNet. Connect to Amazon SageMaker Studio for large-scale model training, analysis, and reporting.

## A.4 What else should I keep in mind about Amazon EMR clusters?

* **Job Orchestration**:  AWS Step functions, Apache Airflow, Apache Oozie
* **Auto scalling on Amazon EMR on Amazon EC2**
* **Spot instances**
* **Long running and transient clusters**
* **Direct connect EMR cluster from Amazon Sagemaker Studio**
* **External Hive Metastore**: ``AWS Glue Data Catalog`` and ``Amazon RDS or Amazon Aurora``
* **Security using Lake Formation or Apache Ranger**
* **Transferring data between HDFS and EMRFS**: Using ``S3DistCp``
* **Storage options on Amazon EMR**
* **Amazon EMR on AMazon EKS uses Kubernetes as cluster manager**

* [Using AWS Glue Data Catalog as the Metastore for Hive](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hive-metastore-glue.html)
To learn more about configuring Hive to use the AWS Glue Data Catalog as its metastore, choose the following button.

* [Using an External MySQL Database or Amazon Aurora](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hive-metastore-external.html)
To learn more on using an external MySQL database or Amazon Aurora as your Hive metastore, choose the following button.

# B. Using Amazon EMR Serverless
## B.1 How Do I Create AWS Resources for Use with Amazon EMR Serverless?

# C. How can I learn more about Amazon EMR?
To learn more information about Amazon EMR, choose from the following links.

* [Amazon EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless.html)
To learn more about Amazon EMR Serverless, choose the following button.

* [Amazon EMR FAQs](https://aws.amazon.com/emr/faqs/?nc=sn&loc=5)
To view frequently asked questions about Amazon EMR, choose the following button.

* [Amazon EMR with AWS Lake Formation](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-lf-terms.html)
To learn more about how Amazon EMR works with AWS Lake Formation, choose the following button.

* [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
To learn more about creation of infrastructure as code, choose the following button.

* [AWS Step Functions with Amazon EMR ](https://aws.amazon.com/blogs/big-data/orchestrate-an-amazon-emr-on-amazon-eks-spark-job-with-aws-step-functions/)
To learn about using Step Functions to orchestrate Amazon EMR Workloads, choose the following button.

* [Use AWS Glue Data Catalog as Spark SQL metastore](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-glue.html)
To learn more about using AWS Glue Data Catalog as a persistent metastore for Spark SQL, choose the following button.

* [Amazon EMR integration with Apache Ranger](https://aws.amazon.com/blogs/big-data/introducing-amazon-emr-integration-with-apache-ranger/)
To learn more about the Amazon EMR integration with Apache Ranger, choose the following button.

* [Amazon EMR on EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks.html)
To learn more about running Amazon EMR on Amazon EKS clusters, choose the following button

* [Overview of Amazon EMR Serverless](https://aws.amazon.com/emr/serverless/)
For an overview about Amazon EMR Serverless, choose the following button.

* [AWS course](https://aws.amazon.com/training/classroom/building-data-lakes/)
To learn how to build Data Lakes on AWS, choose the following button.

* [ETL on Amazon EMR Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/c86bd131-f6bf-4e8f-b798-58fd450d3c44/en-US)
To deploy an Amazon EMR cluster on AWS using AWS Cloud9 IDE, choose the following button.