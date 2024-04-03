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