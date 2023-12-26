# A- Building Data Lakes on AWS

- [A- Building Data Lakes on AWS](#a--building-data-lakes-on-aws)
  - [A.1 Module 1 Introduction to Data Lakes](#a1-module-1-introduction-to-data-lakes)
  - [A.2 Module 2 Data Ingestion, cataloging, and preparation](#a2-module-2-data-ingestion-cataloging-and-preparation)
    - [A.2.1 Data Lake storage](#a21-data-lake-storage)
    - [A.2.2 Data Injection](#a22-data-injection)
      - [A.2.2.1 Transactional Data Ingestion](#a221-transactional-data-ingestion)
      - [A.2.2.2 Files and object ingestion](#a222-files-and-object-ingestion)
      - [A.2.2.3 STreaming data ingestion](#a223-streaming-data-ingestion)
    - [A.2.3 Crawl and catalog data](#a23-crawl-and-catalog-data)
## A.1 Module 1 Introduction to Data Lakes
## A.2 Module 2 Data Ingestion, cataloging, and preparation

### A.2.1 Data Lake storage
``Data lakes`` uses ``Amazon S3`` as it **primary storage location** and this allows a decoupling storage from compute.

To optimize the **storage costs**:
* You can use the multiple **tiers that are currently available in S3**, **S3 intelligent tiering service** for example.
* You can also use **lifecycle management** or integrated **storage class analysis**.
* Transform data into **columnar, compressed and files formats**
  


![Alt text](fig/29.png)

![Alt text](fig/30.png)
### A.2.2 Data Injection
Data Ingestion services are multiples and include:
* **DMS** with ``AWS DMS``
* **Batch ou Bulkloading** of files
* **Streaming Data** with ``AWS Kinesis`` family and so on
* ...


![Alt text](fig/31_.png)

If data are coming from **transactional source** like a database, **the most likely response** in term of ingestion, would be ``AWS DMS``.

With ``AWS DMS``,
* No downtime, **database still accessible during the time of migration**( one of multiple raison that we need to separate storage to compute)
  
#### A.2.2.1 Transactional Data Ingestion
![Alt text](fig/32.png)
#### A.2.2.2 Files and object ingestion
![Alt text](fig/33.png)
* ``Storage Gateway``
* ``Direct Connect``
* ``Data Sync``: **Online** data transfer service that actually automate, simplify and therefore accelerate  and moving data across storage systems.
* * ``Amazon AppFlow : Fully manged integration service that allows you to exchange data between ``SaaS`application and  ``AWS services``

#### A.2.2.3 STreaming data ingestion
![Alt text](fig/34.png)

### A.2.3 Crawl and catalog data
![Alt text](fig/36.png)

Once we get our data into a ``Data Lake``, the question is **what do we have to do with then**? The next step would be the creation and maintenance of the ``Glue data catalog``starting by configuring the ``Glue data crawler``.

The ``Glue data crawler`` identify certain characteristics of data itself and uses those characteristics to **build a metadata structure** which is the ``Glue data catalog`` and that data can be sooner or later being ETL into some format for analytic purpose.









