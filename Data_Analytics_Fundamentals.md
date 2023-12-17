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