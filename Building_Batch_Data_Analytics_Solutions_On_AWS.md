# A- Building  Batch Data Analytics Solutions on AWS
- [A- Building  Batch Data Analytics Solutions on AWS](#a--building--batch-data-analytics-solutions-on-aws)
  - [A.1 Module A: Overview of Data Analytics and the Data Pipeline](#a1-module-a-overview-of-data-analytics-and-the-data-pipeline)
  - [A.2 Module 1: Introduction to Amazon EMR](#a2-module-1-introduction-to-amazon-emr)
    - [A.1.1 Benefits of Hadoop on Amazon EMR](#a11-benefits-of-hadoop-on-amazon-emr)
  - [A.2 Amazon EMR cluster architecture](#a2-amazon-emr-cluster-architecture)
  - [A.2.1 Single Leader node](#a21-single-leader-node)
  - [A.2.1 Three Leader node](#a21-three-leader-node)

## A.1 Module A: Overview of Data Analytics and the Data Pipeline
<figure>
  <img src="./fig/48.png" alt=".." title="Optional title" width="55%" height="70%"/>
</figure>

* Data analytics use cases
* Using the data pipeline for analytics
  * Ingesting and storing data for analytics
  * Storage architectures
  * Storage architectures

Best practice is to optimize for data querying:
* File Format
* File Partitioning
* File Compression
## A.2 Module 1: Introduction to Amazon EMR
<figure>
  <img src="./fig/49.png" alt=".." title="Optional title" width="55%" height="70%"/>
</figure>

### A.1.1 Benefits of Hadoop on Amazon EMR
* Speed and agility
* Flexible capacity
* Integration with AWS services
* Pay for clusters only when you use them
* Improved availability and disaster recovery
* Fully managed

## A.2 Amazon EMR cluster architecture
## A.2.1 Single Leader node
<figure>
  <img src="./fig/50_.png" alt=".." title="Optional title" width="55%" height="70%"/>
</figure>

> **One cluster equal EMR instance** and one ``EMR`` instance can have **multiple nodes within it called nodes**
>
> By default ``Hadoop`` is using ``HDFS`` as it main storage component and ``EBS`` volume are use inside ``EMR`. 

``EMR`` architecture have three important nodes(collection of ``EC2`` instances).
* **Primary node**: Define where to store and process **thing**. 
  * It also responsible of ``HDFS Name Node`` with is going to **process and manage resources tasks** so that we can coordinate data operation within a cluster sas well.
* **Core node**: Doing both storage and processing. 
  * It host the ``YARN Node Manager`` and ``HDFS Data Node``. This is to perform **read or write operations into a HDFS**. ``Data Node`` is responsible of **writing and reading to EBS volume**
  * It also responsible of running task and handle all processing part.
* **Task node**: Only for transforming data. 
  * It add additional compute  resource for processing the job.
  * Don't read or write to ``HDFS``

The are two types of clusters;
* **Persistent cluster**:
* **Transient cluster**:  Shutdown automatically after it given jobs is completed. It's most cost effective approach. Any **data store in HDFS will automatically been deleted** as well.

## A.2.1 Three Leader node
<figure>
  <img src="./fig/51.png" alt=".." title="Optional title" width="55%" height="70%"/>
</figure>