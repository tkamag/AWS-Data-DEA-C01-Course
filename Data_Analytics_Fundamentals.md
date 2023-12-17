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