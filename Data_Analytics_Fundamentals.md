# Introduction to data analysis solutions
https://ecotrust-canada.github.io/markdown-toc/
- [Introduction to data analysis solutions](#introduction-to-data-analysis-solutions)
  - [A-Lesson 1: Introduction to data analysis solutions](#a-lesson-1-introduction-to-data-analysis-solutions)
    - [A.1-Benefits of data analytics on a big scale](#a1-benefits-of-data-analytics-on-a-big-scale)
    - [A.2 Characteristics of big data](#a2-characteristics-of-big-data)
    - [A.3 Components of a data analysis solution](#a3-components-of-a-data-analysis-solution)
  - [B Lesson 2: Volume - Data Storage](#b-lesson-2-volume---data-storage)
    - [B.1 Exponential growth of business data](#b1-exponential-growth-of-business-data)
    - [B.2 Introduction to Amazon S3](#b2-introduction-to-amazon-s3)
      - [B.2.1 Amazon S3 concepts](#b21-amazon-s3-concepts)
      - [B.2.2-Accessing your content](#b22-accessing-your-content)
    - [B.3 Introduction to data lakes](#b3-introduction-to-data-lakes)
      - [B.3.1 Benefits of a data lake on AWS](#b31-benefits-of-a-data-lake-on-aws)
      - [B.3.2 Amazon EMR and data lakes](#b32-amazon-emr-and-data-lakes)
      - [B.4 AWS Lake Formation](#b4-aws-lake-formation)
    - [B.4 Introduction to data storage methods](#b4-introduction-to-data-storage-methods)
      - [B.4.1 Data marts](#b41-data-marts)
      - [B.4.2 Amazon Redshift benefits](#b42-amazon-redshift-benefits)
      - [B.4.3 Comparing data warehouses and data lakes](#b43-comparing-data-warehouses-and-data-lakes)
    - [B.5 Amazon EMRFS](#b5-amazon-emrfs)
  - [C Lesson 3: Velocity – data processing](#c-lesson-3-velocity--data-processing)
    - [C.1 Introduction to data processing methods](#c1-introduction-to-data-processing-methods)
    - [C.2 Attributes of batch and stream processing](#c2-attributes-of-batch-and-stream-processing)
    - [C.2 Introduction to batch data processing](#c2-introduction-to-batch-data-processing)
      - [C.2.1 Batch processing architecture](#c21-batch-processing-architecture)
      - [C.2.2 Batch processing use cases](#c22-batch-processing-use-cases)
    - [C.3 Introduction to stream data processing](#c3-introduction-to-stream-data-processing)
      - [C.3.1 Processing big data streams](#c31-processing-big-data-streams)
      - [C.3.2 Benefits of stream processing](#c32-benefits-of-stream-processing)
      - [C.3.3 Stream processing architecture](#c33-stream-processing-architecture)
      - [C.3.4 Stream processing use cases](#c34-stream-processing-use-cases)
  - [D Lesson 3: Variety – data structure and types](#d-lesson-3-variety--data-structure-and-types)
    - [D.1 Introduction to source data storage](#d1-introduction-to-source-data-storage)
      - [D.1.1 Data source types](#d11-data-source-types)
> Organizations spend **millions** of dollars on data storage. The problem isn’t **finding** the data—the problem is **failing** to do anything with it. 
## A-Lesson 1: Introduction to data analysis solutions
### A.1-Benefits of data analytics on a big scale

* Customer Personalization
* Fraud Detection
* Security Threat Detection
* User behavior
* Financial Modeling and Forecasting
* Real-Time Alerting

> **Effective** data analysis solutions require both storage and the ability to analyze data **in near real time**, with **low latency** while yielding **high-value returns.**

### A.2 Characteristics of big data

The **volume** and **velocity** of data are only two factors you should consider in  a data analytics solution
* Volume
* Velocity
* Variety
* Veracity
* Value

### A.3 Components of a data analysis solution

* **Ingest/Collect** : Assemble data from many sources
* **Store** : Hold data in repositories
* **Process Analyze** : Manipulate data into needed forms
* **Consume Visualize** : Extract key information from the data

## B Lesson 2: Volume - Data Storage
> When businesses have **more data** than they are able to **process and analyze**, they have a **volume problem**..
### B.1 Exponential growth of business data
There are three broad classifications of data source types:

* **Structured data** is organized and stored in the form of values that are grouped into rows and columns of a table.
* **Semi-structured data** is often stored in a series of key-value pairs that are grouped into elements within a file.
* **Unstructured data** is not structured in a consistent way. Some data may have structure similar to semi-structured data but others may only contain metadata.

### B.2 Introduction to Amazon S3
``Amazon S3`` is object storage built to store and retrieve any amount of data from anywhere.

#### B.2.1 Amazon S3 concepts

To get the most out of Amazon S3, you need to understand a few simple concepts. First, ``Amazon S3`` stores data as objects within buckets.

An **object** is composed of a file and any metadata that describes that file. To store an object in Amazon S3, you upload the file you want to store into a bucket. When you upload a file, you can set permissions on the object and add any metadata.

**Buckets** are logical containers for objects. You can have one or more buckets in your account and can control access for each bucket individually. You control who can create, delete, and list objects in the bucket. You can also view access logs for the bucket and its objects and choose the geographical region where Amazon S3 will store the bucket and its contents.

#### B.2.2-Accessing your content
Once objects have been stored in an ``Amazon S3`` bucket, they are given an **object key**. Use this, along with the bucket name, to access the object.

![Alt text](fig/01.png)

### B.3 Introduction to data lakes
> A data lake is a **centralized repository** that allows you to store **structured, semistructured, and unstructured** data at any scale.
``Data lakes`` promise the ability to store all data for a business in a single repository. You can leverage data lakes to store large volumes of data instead of persisting that data in data warehouses. ``Data lakes``, such as those built in ``Amazon S3``, are generally less expensive than specialized big data storage solutions.
* Single source of truth
* Store any type of data, regardless f structure
* Can be analyzed using artificial intelligence (AI) and machine learning.

#### B.3.1 Benefits of a data lake on AWS
* **Cost-effective data storage solution**
* Implement industry-leading **security and compliance**.
* Allow you to take advantage of **many different data collection and ingestion tools** to ingest data into your data lake.
* **Categorize and manage your data** simply and efficiently.
* Help you turn data into **meaningful insights**.

#### B.3.2 Amazon EMR and data lakes
``Apache Hadoop`` and ``Spark`` are both supported by ``Amazon EMR``, which has the ability to help businesses easily, quickly, and cost-effectively implement data processing solutions based on ``Amazon S3`` data lakes.

#### B.4 AWS Lake Formation 
``AWS Lake Formation`` makes it easy to **ingest, clean, catalog, transform, and secure** your data and make it available for analysis and machine learning. ``Lake Formation`` gives you a central console where you can discover data sources, set up transformation jobs to move data to an ``Amazon S3`` data lake, remove duplicates and match records, catalog data for access by analytic tools, configure data access and security policies, and audit and control access from AWS analytic and machine learning services.

``Lake Formation`` automatically configures underlying AWS services to ensure compliance with your defined policies. If you have set up transformation jobs spanning AWS services, ``Lake Formation`` **configures the flows, centralizes their orchestration, and lets you monitor the processing of your jobs**.

### B.4 Introduction to data storage methods
``Data Lakes`` and ``Data warehouses`` are two different storage systems. ``Data Lakes`` are not a replacement for ``data warehouses``.
> A ``data warehouse`` is a **central repository** of structured data from many data sources. This data is **transformed, aggregated, and prepared** for business reporting and analysis.
>
> ![Alt text](fig/02.png)

A ``data warehouse`` is a **central repository of information coming from one or more data sources**. Data flows into a data warehouse from transactional systems, relational databases, and other sources. These data sources can **include structured, semi-structured, and unstructured data**. 
> **These data sources are transformed into structured data before they are stored in the data warehouse.**

**Data is stored within the data warehouse using a schema**. A schema defines how data is stored within tables, columns, and rows. The schema enforces constraints on the data to ensure integrity of the data. The transformation process often involves the steps required to make the source data conform to the schema. Following the first successful ingestion of data into the data warehouse, the process of ingesting and transforming the data can continue at a regular cadence.

Business analysts, data scientists, and decision makers access the data through business intelligence (BI) tools, SQL clients, and other analytics applications. Businesses use reports, dashboards, and analytics tools to extract insights from their data, monitor business performance, and support decision making. These reports, dashboards, and analytics tools are powered by data warehouses, which store data efficiently to minimize I/O and deliver query results at blazing speeds to hundreds and thousands of users concurrently.

#### B.4.1 Data marts
Data warehouses can be massive. Analyzing these huge stores of data can be confusing. Many organizations **need a way to limit the tables to those that are most relevant to the analytics users will be performing**.
> A subset of data from a data warehouse is called a **data mart**. Data marts only focus on one subject or functional area

#### B.4.2 Amazon Redshift benefits

This is where ``Amazon Redshift`` comes in. ``Amazon Redshift`` overcomes all of these negatives by providing a cloud-based, scalable, secure environment for your data warehouse. ``Amazon Redshift`` is easy to set up, deploy, and manage and provides up to 10 times faster performance than other data warehousing solutions.

#### B.4.3 Comparing data warehouses and data lakes

**Analyzing a Data Warehouse**:

For analysis to be most effective, it should be performed on data that has been processed and cleansed. This often means implementing an ETL operation to collect, cleanse, and transform the data. This data is then placed in a data warehouse. It is very common for data from many different parts of the organization to be combined into a single data warehouse.

Amazon Redshift is a data warehousing solution specially designed for workloads of all sizes. Amazon Redshift Spectrum even provides the ability to query data that is housed in an Amazon S3 data lake.

**Analyzing a Data Lakes**

Data lakes extend data warehouses

Data lakes provide customers a means for including unstructured and semi-structured data in their analytics. Analytic queries can be run over cataloged data within a data lake. This extends the reach of analytics beyond the confines of a single data warehouse.

Businesses can securely store data coming from applications and devices in its native format, with high availability, durability, at low cost, and at any scale. Businesses can easily access and analyze data in a variety of ways using the tools and frameworks of their choice in a
high-performance, cost-effective way without having to move large amounts of data between storage and analytics systems.

**AWS: Data Lakes and Analytics**

AWS provides a comprehensive portfolio of services that enable customers to build their data lakes in the cloud and analyze all their data with the broadest set of analytical approaches, including machine learning.

> So now what we’ve got is ``Amazon S3`` that can host a data lake and ``Amazon Redshift`` that can host a data warehouse, but what if I need to query across both spaces?
>
> ``Amazon Redshift Spectrum`` **allows you to combine your data lake and data warehouse as if it were a single source of data**. No data movement, no crazy query logic, just clean queries of all your data. 
>
### B.5 Amazon EMRFS

``Amazon EMR`` provides an alternative to ``HDFS``: the ``EMR File System (EMRFS)``. EMRFS can help ensure that there is a persistent "source of truth" for HDFS data stored in Amazon S3. When implementing EMRFS, there is no need to copy data into the cluster before transforming and analyzing the data as with HDFS. EMRFS can catalog data within a data lake on Amazon S3. The time that is saved by eliminating the copy step can dramatically improve performance of the cluster.

* ``Data warehouses`` provide storage for highly structured data sets that serve as the single source of truth for analytical queries.

* ``Data lakes`` allow content of any form to be stored. This content may not be curated and serves all forms of querying.

* ``OLTP databases`` serve as a structured store for new and frequently updated data. They may not perform well when analytical queries are run frequently.

* ``Hadoop clusters`` provide extremely fast and reliable ingestion and processing of data.

## C Lesson 3: Velocity – data processing
> When businesses **need rapid insights** from the data they are collecting, **but the systems in place simply cannot meet the need, there's a velocity problem.**

**Data processing** means the collection and manipulation of data to produce meaningful information. 

**Data collection** is divided into two parts:
* **Data collection**: Gathering data from multiple source for single source storage and analysis.
* **Data processing**: Formatting, organizing and controlling data. 

### C.1 Introduction to data processing methods
``Data processing`` may only need to **be performed once a day**, making results available the following morning, or it may need to be performed and made available immediately. This variance in the speed at which data processing must occur can be broken down into four categories.

Two types of data processing: 
* **Batch processing** (processing content in batches at certain intervals). Used to get deep insights from complex analytics.
* **Stream processing** (processing data in a stream—in other words, processing data that’s generated continuously, in small datasets). Used to get initial insights and real-time feedback.

![Alt text](fig/03.png)

* Rapid collection of data followed by the rapid processing of data is another common challenge ==> **Stream processing system.**

* Slower collection of data followed by a rapid processing requirement is a common challenge ==> **Batch processing system.**

### C.2 Attributes of batch and stream processing
The table below highlights the difference between batch and stream processing: 
![Alt text](fig/04.png)

![Alt text](fig/05.png)

![Alt text](fig/06.png)

### C.2 Introduction to batch data processing
![Alt text](fig/07.png)

``Batch processing`` is often thought of as a slow process. This is not the case. ``Batch processing`` must quickly and efficiently consume a huge amount of data all at once. This poses challenges that do not exist with ``stream processing``.

``Batch data processing`` provides companies with the ability to dive deep into the data they have collected to produce complex analytics that simply cannot be achieved using ``streaming analytics``.

> ``Batch processing`` is the processing of a series of programs, or jobs, on one or more computers without manual intervention.

Data is collected into batches asynchronously. Each batch is sent to a processing system when specific conditions are met, such as a specified time of day. The results of the processing job are then sent to a storage location to be queried later as needed.

You can run them **when less expensive capacity is available**. With modern architectures, you can optimize ``batch processing`` systems to the frequency and size of the batches you’re processing. This avoids the idling compute resources and under-used storage capacity often associated with traditional on-premises systems.

``Amazon EMR`` has mitigated the problem of **imbalanced processing jobs** by decoupling the collection system from the processing system. This is accomplished by implementing one of two common frameworks: ``Hadoop`` or ``Apache Spark``. Both frameworks process high-velocity data but they do it in different ways.

Both ``Hadoop`` and ``Spark support`` general **batch processing, streaming analytics, machine learning, graph databases, and ad hoc queries**.
#### C.2.1 Batch processing architecture
Batch processing can be performed in different ways using AWS services. In the following architecture,
![Alt text](fig/08.png)

The architecture diagram below depicts the same data flow as above but uses ``AWS Glue`` **for aggregated ETL (heavy lifting, consolidated transformation, and loading engine)**. 
> ``AWS Glue`` is a fully managed service, as opposed to ``Amazon EMR``, which requires management and configuration of all of the components within the service.

![Alt text](fig/09.png)

#### C.2.2 Batch processing use cases
* **Log analytics**: ``Amazon EMR`` can be used to process logs generated by web and mobile applications. 
* **Unified view of data across multiple data stores**: You can use the ``AWS Glue Data Catalog`` to quickly discover and search across multiple AWS data sets without moving the data. 
* **Predictive analytics**: ``Apache Spark`` on ``EMR`` includes MLlib for scalable machine learning algorithms, or you can use your own libraries.
* **Queries against an Amazon S3 data lake**: ``Data lakes`` are an increasingly popular way to store and analyze both structured and unstructured data.

> ``AWS Lambda`` is a serverless compute service that can **be used to initiate processing operations in a batch processing system.**

### C.3 Introduction to stream data processing
![Alt text](fig/10.png)
``Stream data processing`` is one of the fastest growing areas of processing. 
> With ``stream processing`` solutions, **the amount of data being transferred and the size of the data packets is not always consistent.**
#### C.3.1 Processing big data streams
* With streaming solutions, **the collection system (producer**) and **the processing system (consumer)** are always separate.
* Streaming data uses what are called **data producers**. Each of these producers can write their data to the same endpoint, **allowing multiple streams of data to be combined into a single stream for processing**. 
* Another huge advantage is **the ability to preserve client ordering of data and the ability to perform parallel consumption of data**. This allows multiple users to work simultaneously on the same data.

#### C.3.2 Benefits of stream processing
![Alt text](fig/11.png)

#### C.3.3 Stream processing architecture
![Alt text](fig/12.png)


**Combined processing architecture**

![Alt text](fig/13.png)

It is important to remember that **streaming analytics is very limited**. Due to the size of each data packet and the speed the data is moving, **you are limited to simple analytics such as aggregating and filtering the data**. Due to this limitation, **it is common for businesses to incorporate batch analytics to produce deeper insights into the data before producing dashboards and reports on the data.**

In this architecture, 
* Sensor data is being collected in the form of a stream. The streaming data is being collected from the sensor devices by ``Amazon Kinesis Data Firehose``. 
* This service is configured to send the data to be processed using ``Amazon Kinesis Data Analytics``. 
* This service **filters the data for relevant records** and send the data into another ``Kinesis Data Firehose`` process, which places the results into an ``Amazon S3 bucket`` at the serving layer.
* Using ``Amazon Athena``, the data in the ``Amazon S3`` bucket can now be queried. ``Amazon QuickSight`` can be used to produce dashboards that include content from both Amazon Athena and the first Amazon S3 bucket where the raw streaming data was loaded.

**Combined processing architecture**

![Alt text](fig/14.png)

#### C.3.4 Stream processing use cases
* **Build video analytics applications**
* **Evolve from batch to real-time analytics**
* **Analyze IoT device data**

## D Lesson 3: Variety – data structure and types
> When your business becomes **overwhelmed** by the **sheer number of data sources** to analyze and you **cannot find systems** to perform the analytics, you know you have a **variety** problem.
### D.1 Introduction to source data storage

**Transactional databases** experience heavy write and update operations, while **analytical databases** experience heavy read operations.

#### D.1.1 Data source types

**Structured data** is stored in a tabular format, often within a database management system (DBMS). This data is organized based on a relational data model, which defines and standardizes data elements and their relation to one another. Data is stored in rows, with each row representing a single instance of a thing (for example, a customer). These rows are well understood due to the table schema, which explains what each field in the table represents. This makes structured data easy to query.
> **The downside to structured data is its lack of flexibility.**
> 
**Examples of structured data applications** include Amazon RDS, Amazon Aurora, MySQL, MariaDB, PostgreSQL, Microsoft SQL Server, and Oracle.
>
**Semi-structured data** is stored in the form of elements within a file. This data is organized based on elements and the attributes that define them. It doesn't conform to data models or schemas. **Semi-structured** data is considered to have a self-describing structure. Each element is a single instance of a thing, such as a conversation. The attributes within an element define the characteristics of that conversation. Each conversation element can track different attributes. This makes semi-structured data quite flexible and able to scale to meet the changing demands of a business much more rapidly than structured data.

**Examples of semi-structured data** stores include CSV, XML, JSON, Amazon DynamoDB, Amazon Neptune, and Amazon ElastiCache.

**Unstructured data** is stored in the form of files. This data doesn't conform to a predefined data model and isn't organized in a predefined manner. Unstructured data can be text-heavy, photographs, audio recordings, or even videos. Unstructured data is full of irrelevant information, which means the files need to be preprocessed to perform meaningful analysis. This can be done in many ways. For example, services can add tags to the data based on rules defined for the types of files. The data can also be cataloged to make it available to query services.

**Examples of unstructured data** include emails, photos, videos, clickstream data, Amazon S3, and Amazon Redshift Spectrum.

> **Structured data** is hot, **immediately ready** to be analyzed. 

> **Semi structured data** is lukewarm, some data will be ready to go and other data **may need to be cleansed** or preprocessed. 

> **Unstructured data** is the **frozen** ocean—full of **exactly what you need** but separated by all kinds of **stuff you don’t need**.

