# Types of system tables and views
There are several types of system tables and views:
* **SVV** views contain information about database objects with references to transient STV tables.
* **SYS** views are used to monitor query and workload usage for provisioned clusters and serverless workgroups.
* **STL** views are generated from logs that have been persisted to disk to provide a history of the system.
* **STV** tables are virtual system tables that contain snapshots of the current system data. They are based on transient in-memory data and are not persisted to disk-based logs or regular tables.
* **SVCS** views provide details about queries on both the main and concurrency scaling clusters.
* **SVL** views provide details about queries on main clusters.
# Cluster Resize
As your Amazon Redshift capacity or performance changes throughout its lifecycle, you may find yourself needing to resize in order to make the best use of your cluster
* **Elastic Resize** is the optimal and fastest way to quickly add or remove nodes or change node types from an existing cluster. It automates the steps of taking a snapshot, creating a new cluster, deleting the old cluster and renaming the new cluster into a simple, quick and familiar operation. The elastic resize operation can be run at any time or can be scheduled to run at a future time.
* **Classic resize** is the manual approach to resizing your cluster and is the predecessor to **Elastic Resize**.
* **Concurrency scaling** is a cost-effective way to pay only for additional capacity during large workload spikes, as opposed to adding persistent nodes in the cluster that will incur extra costs during downtime.
# Querying your data lake
Amazon Redshift provides SQL capability designed for fast online analytical processing (OLAP) of very large datasets that are stored in both Amazon Redshift clusters and Amazon S3 data lakes. You can query data in many formats, including Parquet, ORC, RCFile, TextFile, SequenceFile, RegexSerde, OpenCSV, and AVRO. 
* To define the structure of the files in Amazon S3, you create external schemas and tables. 
* Then, you use an external data catalog such as AWS Glue or your own Apache Hive metastore. Changes to either type of data catalog are immediately available to any of your Amazon Redshift clusters.
* After your data is registered with an AWS Glue Data Catalog and enabled with AWS Lake Formation, you can query it by using Redshift Spectrum.
* Redshift Spectrum resides on dedicated Amazon Redshift servers that are independent of your cluster. 
* Redshift Spectrum pushes many compute-intensive tasks, such as predicate filtering and aggregation, to the Redshift Spectrum layer. 
* Redshift Spectrum also scales intelligently to take advantage of massively parallel processing.

You can partition the external tables on one or more columns to optimize query performance through partition elimination. 
* You can query and join the external tables with Amazon Redshift tables. 
* You can access external tables from multiple Amazon Redshift clusters and query the Amazon S3 data from any cluster in the same AWS Region.
* When you update Amazon S3 data files, the data is immediately available for queries from any of your Amazon Redshift clusters.
# Distribution styles
* **AUTO distribution**: With **AUTO distribution**, Amazon Redshift assigns an optimal distribution style based on the size of the table data. For example, if AUTO distribution style is specified, Amazon Redshift initially assigns the ALL distribution style to a small table. When the table grows larger, Amazon Redshift might change the distribution style to KEY, choosing the primary key (or a column of the composite primary key) as the distribution key. If the table grows larger and none of the columns are suitable to be the distribution key, Amazon Redshift changes the distribution style to EVEN. The change in distribution style occurs in the background with minimal impact to user queries.

    * To view actions that Amazon Redshift automatically performed to alter a table distribution key, see SVL_AUTO_WORKER_ACTION. 
    * To view current recommendations regarding altering a table distribution key, see SVV_ALTER_TABLE_RECOMMENDATIONS.
    * To view the distribution style applied to a table, query the PG_CLASS_INFO system catalog view.
  
*  **EVEN distribution**: The leader node distributes the rows across the slices in a round-robin fashion, regardless of the values in any particular column. EVEN distribution is appropriate when a table doesn't participate in joins. It's also appropriate when there isn't a clear choice between KEY distribution and ALL distribution.

* **KEY distribution**: The rows are distributed according to the values in one column. The leader node places matching values on the same node slice. If you distribute a pair of tables on the joining keys, the leader node collocates the rows on the slices according to the values in the joining columns. This way, matching values from the common columns are physically stored together.

* **ALL distribution**:  A copy of the entire table is distributed to every node. Where EVEN distribution or KEY distribution place only a portion of a table's rows on each node, ALL distribution ensures that every row is collocated for every join that the table participates in.

# Vacuum
Re-sorts rows and reclaims space in either a specified table or all tables in the current database. Users can access tables while they are being vacuumed. You can perform queries and write operations while a table is being vacuumed, but when data manipulation language (DML) commands and a vacuum run concurrently, both might take longer. If you run UPDATE and DELETE statements during a vacuum, system performance might be reduced. VACUUM DELETE temporarily blocks update and delete operations.
**VACUUM [ FULL | SORT ONLY | DELETE ONLY | REINDEX | RECLUSTER ]**

**AUTO** distribution and **interleaved sort keys** ==> Thinks **(re-)Indexing**.
# Loading data from an Amazon DynamoDB table
When the COPY command reads data from the Amazon DynamoDB table, the resulting data transfer is part of that table's provisioned throughput.
To avoid consuming excessive amounts of **provisioned read throughput**, we recommend that you not load data from Amazon DynamoDB tables that are in production environments. If you do load data from production tables, 
* We recommend that you set the READRATIO option much lower than the average percentage of unused provisioned throughput. 
* A low READRATIO setting will help minimize throttling issues. 
* To use the entire provisioned throughput of an Amazon DynamoDB table, set READRATIO to 100.
# EBS Volumes
EBS volumes are are off-instances volumes. Data on these volumes persist post the EC2 instances is stopped or terminated or if any drive failure. When EBS volumes are attached to an EC2 instances, default behavior for root volumes is deleted when the instance is terminated. For non-root EBS volumes, by default are not deleted when Amazon EC2 instances are terminated. This default behavior can be changed by setting the flag **DeleteOnTermination** while attaching  EBS volumes to an EC2 instances.

> The root volume is where the OS and applications normally live. The user volume is meant for your users to store their data in. In the case of a rebuild of the WorkSpace the root volume gets reverted back to default whereas the users data is persistent, at least as much as its last snapshot, normally every 12 hours.
# S3 Object Lambda
S3 Object Lambda, a new capability that allows you to add your own code to process data retrieved from S3 before returning it to an application. S3 Object Lambda works with your existing application.
S3 Object Lambda allows you to modification and process of data before it is read from S3 buckets. Its add AWS Lambda function code for S3 GET, HEAD and LIST request to process the data. Using S3 Object Lambda eliminates the needs to create a copy of data in the S3 bucket to process for different requirements. It's a fully managed solution which can be implemented with least operational work.