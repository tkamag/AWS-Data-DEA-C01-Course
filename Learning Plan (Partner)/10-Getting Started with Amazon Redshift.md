# A. Getting Started with Amazon Redshift
- [A. Getting Started with Amazon Redshift](#a-getting-started-with-amazon-redshift)
  - [A.1 Architecture and Use Cases](#a1-architecture-and-use-cases)
    - [A.1.1 How is Amazon Redshift used to architect a cloud solution?](#a11-how-is-amazon-redshift-used-to-architect-a-cloud-solution)
    - [A.1.2 What are the basic technical concepts of Amazon Redshift?](#a12-what-are-the-basic-technical-concepts-of-amazon-redshift)
    - [A.1.3 What else should I keep in mind about Amazon Redshift?](#a13-what-else-should-i-keep-in-mind-about-amazon-redshift)
  - [A.2 Using Amazon Redshift](#a2-using-amazon-redshift)
    - [A.2.1 How Do I Configure a Cluster in Amazon Redshift?](#a21-how-do-i-configure-a-cluster-in-amazon-redshift)
  - [A.3 Learn More](#a3-learn-more)
  - [A.4 Additional reading material](#a4-additional-reading-material)
  - [A.5 Course Resources](#a5-course-resources)

* [AWS Pricing Calculator](https://calculator.aws/#/createCalculator/Redshift)
To estimate the cost of Amazon Redshift, choose the Go to Calculator button.

* [Amazon Redshift pricing](https://aws.amazon.com/redshift/pricing/)
For additional details about Amazon Redshift pricing, choose the Go to Webpage button.

## A.1 Architecture and Use Cases
### A.1.1 How is Amazon Redshift used to architect a cloud solution?
``Amazon Redshift`` **uses SQL to analyze structured and semi-structured data** across data warehouses, operational databases, and data lakes. Hardware designed by AWS and ML combine to help deliver price performance at any scale. In other words, ``Amazon Redshift`` can play a key role in a modern data architecture.

The following architecture diagram describes how to use Amazon Redshift and key features, such as the following, to build out a modern cloud data warehouse.

* **Redshift Spectrum**
* **Federated queries**
* **Amazon Redshift Data API**
* **Data sharing**
* **Amazon Redshift ML**

### A.1.2 What are the basic technical concepts of Amazon Redshift?

Amazon Redshift achieves efficient storage and optimum query performance through a combination of MPP; columnar data storage; and very efficient, targeted data compression encoding schemes.

* **MPP**: ``Amazon Redshift`` **distributes the rows of a table to the compute nodes so that data can be processed in parallel**. With ``MPP``, **you can quickly run queries that operate on large amounts of data**. Multiple compute nodes handle all query processing. **This leads to final-result aggregation, with each core of each node running the same compiled query segments on portions of the entire data**. 
>>> By **selecting an appropriate distribution key for each table**, you can optimize the distribution of data to balance the workload and minimize movement of data from node to node.

* **Columnnar strorage**: ``Amazon Redshift`` **uses columnar storage, which is optimal for analytical processing**, where each data block stores values of a single column for multiple rows. ``Amazon Redshift`` transparently **converts data to columnar storage for each column**. 
>>> **Columnar storage optimizes analytic query performance by significantly reducing overall disk I/O requirements** and the amount of data required to be loaded into memory from disk. 
Additionally, **when data is stored in columnar fashion, compression algorithms work more efficiently**. This further reduces disk space and I/O because each block holds the homogeneous type of data.

* **Data ingestion**: There are several ways to load data into an ``Amazon Redshift`` database. 
  * Using the ``COPY`` command: This is a best practice for loading data into Amazon Redshift. The ``COPY`` command **loads data in parallel** from ``Amazon S3, Amazon EMR, Amazon DynamoDB``, or from multiple data sources on any remote hosts accessible through an SSH connection. 
>>>> The ``COPY`` command **appends the new input data to any existing rows in the target table**. The command can load data from ``Amazon S3 for Avro, CSV, JSON, and text file formats`` and for **columnar format files such as ORC and Parquet**.
>
  * Using ``AWS Glue``: When moving data to a Redshift cluster, ``AWS Glue`` **jobs issue COPY statements against Amazon Redshift to achieve maximum throughput.**
  
  * Integration with third-party ETL tools: ``Amazon Redshift`` `**integrates with several ETL tools to load data into databases** 

* **Data access**: You can connect to your Redshift cluster in various ways.

### A.1.3 What else should I keep in mind about Amazon Redshift?

As you design workloads to run on ``Amazon Redshift``, keep in mind some primary considerations. To explore these, expand each of the following five categories.

* **Amazon Redshift nodes types**: ``Amazon Redshift`` offers two node types to choose from, depending on the required performance, data size, and growth. 
  * ``DC2 nodes`` **for compute-intensive data warehouses with local solid-state drive (SSD) with local storage included**. For datasets under 1 TB uncompressed, we recommend DC2 node types for the best performance at the lowest price. 
  >>> **Choose the number of nodes that you need based on data size and performance requirements.**
  * With ``RA3 nodes`` with managed storage, **you can optimize your data warehouse by scaling and paying for compute and managed storage independently**.
  >>> **Choose the number of nodes based on your performance requirements and pay only for the managed storage that you use**.

  ``Redshift Managed Storage (RMS)`` uses large, high-performance SSDs in each RA3 node for fast local storage and Amazon S3 for longer-term durable storage.
    * If **the data in a node grows beyond the size of the large local SSDs, RMS automatically offloads that data to Amazon S3**. You pay the same low rate for ``RMS`` regardless of whether the data resides in high-performance SSDs or in Amazon S3. 
   * For workloads that require ever-growing storage, **you can use managed storage to automatically scale your data warehouse storage capacity without adding and paying for additional nodes**.

* **Query acceleration  with AQUA**: ``Advanced Query Accelerator (AQUA)`` is a new distributed and hardware-accelerated cache. With ``AQUA, Amazon Redshift`` **can run eligible queries with LIKE and SIMILAR_TO up to 10 times faster than other enterprise cloud data warehouses**. ``AQUA`` uses ``AWS designed processors with AWS Nitro chips`` and a scale-out architecture to automatically add more capacity as storage needs grow. ``AQUA`` is available on ``RA3`` clusters at no additional charge and requires no code changes to your queries.

* **Automate optimization and maintenance**: ``Amazon Redshift`` automates many tasks that typically require user intervention. This includes features ranging from automatic table tuning using advanced ML approaches to features minimizing administrative overhead. 
  * **Automatic table optimization (ATO)** is a self-tuning capability that automatically optimizes the design of tables by applying sort and distribution keys without the need for administrator intervention.
  * **Automatic workload management (Auto WLM)**:  Uses ML to dynamically manage memory and concurrency to help maximize query throughput.
  * **Short query acceleration (SQA)** speeds up short-running queries such as reports, dashboards, and interactive analysis.
  * **Amazon Redshift Advisor** helps you improve the performance and decrease operating costs for your Redshift cluster by offering specific recommendations about changes to make.
  * **Automatic analyze** updates the statistical metadata that the query planner uses to choose optimal plans.
  * **Auto vacuum** delete reclaims disk space occupied by rows that were marked for deletion by previous UPDATE and DELETE operations.
  * **Automatic table sort** provides an efficient, automated way to maintain sort order of the data in Amazon Redshift tables to continuously optimize query performance.
* **Monitoring**: Metrics for compute utilization, storage utilization, and read/write traffic to your ``Amazon Redshift`` data warehouse cluster are available at no additional cost. ``Amazon Redshift`` also provides information about query and cluster performance through the AWS Management Console.
* **Built-in cost controls**: The ``Amazon Redshift`` console provides cost controls that you can quickly configure, which limit the usage of certain features, such as concurrency scaling and ``Amazon Redshift Spectrum``.

* [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html)
For more information about Amazon Redshift, refer to the Amazon Redshift by choosing the Go to User Guide button.

## A.2 Using Amazon Redshift
### A.2.1 How Do I Configure a Cluster in Amazon Redshift?

## A.3 Learn More

* [Building Data Analytics Solutions Using Amazon Redshift training](https://aws.amazon.com/training/classroom/building-data-analytics-solutions-using-amazon-redshift/)
Learn the current thinking in building and operating data analytics pipelines using Amazon Redshift. Enroll in this instructor-led course to get your questions answered in real time from an AWS instructor and to learn from your peers. 

* [Amazon Redshift Deep Dive Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/380e0b8a-5d4c-46e3-95a8-82d68cf5789a/en-US)
Exercise the different features of Amazon Redshift with the help of this self-directed Workshop. 

## A.4 Additional reading material

To learn more about Amazon Redshift, explore each resource by choosing the following buttons.

* [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
Account activity monitoring and recording across your  infrastructure

* [AWS Glue](https://aws.amazon.com/glue/)
Serverless data integration service

* [Amazon Kinesis Data Firehouse](https://aws.amazon.com/kinesis/data-firehose/)
Extract, transform, and load (ETL) service for streaming data

* [Amazon QuickSight](https://aws.amazon.com/quicksight/)
Business intelligence tool

* [Amazon Redshift FAQs](https://aws.amazon.com/redshift/faqs/)
Frequently asked questions

* [Amazon SageMaker](https://aws.amazon.com/pm/sagemaker/)
Managed environment to build, train, and deploy machine learning models

* [Amazon S3](https://aws.amazon.com/s3/)
Object storage service

## A.5 Course Resources

* [Amazon Redshift best practices](https://docs.aws.amazon.com/redshift/latest/dg/best-practices.html)
Learn about Amazon Redshift best practices in the Database Developer Guide by choosing the Go to Guide button.

* [Amazon Redshift ML](https://aws.amazon.com/redshift/features/redshift-ml/)
Learn how to create, train, and deploy ML models using familiar SQL commands by choosing the Go to Webpage button.

* [Amazon Redshift pricing](https://aws.amazon.com/redshift/pricing/)
Learn more about Amazon Redshift pricing by choosing the Go to Webpage button.

* [Amazon Redshift RSQL](https://docs.aws.amazon.com/redshift/latest/mgmt/rsql-query-tool.html)
Learn about Amazon Redshift RSQL by choosing the Go to Guide button.

* [AWS Pricing Calculator](https://calculator.aws/#/createCalculator/Redshift)
Access the AWS Pricing Calculator by choosing the Go to Calculator button.

* [COPY](https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html)
Learn how to use the COPY command by choosing the Go to Guide button.

* [Overview of managing clusters in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-operations.html)
Get an overview of how to manage clusters in Amazon Redshift by choosing the Go to Guide button.

* [Sharing data access clusters in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/datashare-overview.html)
Learn how to share data access clusters in Amazon Redshift by choosing the Go to Guide button.

* [SQL reference](https://docs.aws.amazon.com/redshift/latest/dg/cm_chap_SQLCommandRef.html)
Learn about SQL reference in the Database Developer Guide by choosing the Go to Guide button.

* [SUPER type](https://docs.aws.amazon.com/redshift/latest/dg/r_SUPER_type.html)
Learn how to use SUPER type by choosing the Go to Webpage button.

* [Working with concurrency scaling](https://docs.aws.amazon.com/redshift/latest/dg/concurrency-scaling.html)
Learn more about working with concurrency scaling by choose the Go to Guide button.