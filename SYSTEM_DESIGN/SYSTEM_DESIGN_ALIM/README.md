# SYSTEM DESIGN
## Database Design
* [SQL](#sql)
  * [Relational database management system (RDBMS)](#relational-database-management-system-rdbms)
    * [Replication](#replication)
      * [Master-Slave](#master-slave)
      * [Master-Master](#master-master)
    * [Federation](#federation)
    * [Sharding](#sharding)
    * [De-normalization](#de-normalization)
    * [SQL tuning](#sql-tuning)
  
* [NoSQL](#nosql)
  * [Key-value store](#key-value-store)
  * [Document store](#document-store)
  * [Wide column store](#wide-column-store)
  * [Graph database](#graph-database)
  * [Database Internal](#database-internal)
    * [Cassandra Architecture](#cassandra-architecture)
    * [Google BigTable Architecture](#google-bigtable-architecture)
    * [Amazon Dynamo DB](#amazon-dynamo-db)
    * [Design Patterns in Amazon Dynamo DB](#design-patterns-in-amazon-dynamo-db)
  * [Database Algorithms](#database-algorithms)
    * [Hyperloglog](#hyperloglog)
    * [Log Structured Merge Tree](#log-structured-merge-tree)
    * [Sorted String Tables and Compaction Strategies](#sorted-string-tables-and-compaction-strategies)
    * [Leveled Compaction Cassandra](#leveled-compaction-cassandra)
    * [Scylla DB Compaction](#scylla-db-compaction)
    * [Indexing In Cassandra](#indexing-in-cassandra)

* [SQL vs NoSQL](#sql-vs-nosql)
  * [When to use SQL or NoSQL?](#when-to-use-sql-or-nosql)
  * [Graph Database vs Relational Database](#graph-database-vs-relational-database)

* [Time Series Databases](#time-series-databases)
  * [Pinterest Time Series Database](#pinterest-time-series-database)
  * [Uber Time Series DB](#uber-time-series-db)
  * [Time Series Relational DB](#time-series-relational-db)
  * [Facebook Gorilla Time Series DB](#facebook-gorilla-time-series-db)

* [In Memory Database-Redis](#in-memory-database-redis)
  * [Redis Official Documentation](#redis-official-documentation)
  * [Learn Redis through Redis University](#learn-redis-through-redis-university)
  * [Redis Open Source Repo](#redis-open-source-repo)
  * [Redis Architecture](#redis-architecture)
--------------------------------------

## Software Architectural Design

## Code Base Design

## Server Side Design


## Database Design
## SQL
### Relational database management system (RDBMS)
* [Ref](https://github.com/donnemartin/system-design-primer#relational-database-management-system-rdbms)

> #### Replication

* [Ref](https://github.com/lahin31/system-design-bangla/tree/master#section-18-database-replication)

#### Master-Slave
* [Ref](https://github.com/donnemartin/system-design-primer#master-slave-replication)

#### Master-Master
* [Ref](https://github.com/donnemartin/system-design-primer#master-master-replication)

> #### Federation
* [Ref](https://github.com/donnemartin/system-design-primer#federation)

> #### Sharding
* [Ref](https://github.com/donnemartin/system-design-primer#sharding)
* [Ref](https://github.com/lahin31/system-design-bangla/tree/master#section-17-database-sharding)

> #### De-normalization
* [Ref](https://github.com/donnemartin/system-design-primer#denormalization)

> #### SQL tuning
* [Ref](https://github.com/donnemartin/system-design-primer#sql-tuning)


## NoSQL
> #### Key-value store
* [Ref](https://github.com/donnemartin/system-design-primer#key-value-store)

> #### Document store
* [Ref](https://github.com/donnemartin/system-design-primer#document-store)

> #### Wide column store
* [Ref](https://github.com/donnemartin/system-design-primer#wide-column-store)

> #### Graph database
* [Ref](https://github.com/donnemartin/system-design-primer#graph-database)

> #### Database Internal

#### Cassandra Architecture
* [Ref](https://docs.datastax.com/en/archived/cassandra/3.0/cassandra/architecture/archIntro.html)

#### Google BigTable Architecture
* [Ref](https://static.googleusercontent.com/media/research.google.com/en//archive/bigtable-osdi06.pdf)

#### Amazon Dynamo DB
* [Ref](https://www.allthingsdistributed.com/2007/10/amazons_dynamo.html)

#### Design Patterns in Amazon Dynamo DB
* [Ref](https://docs.datastax.com/en/archived/cassandra/3.0/cassandra/architecture/archIntro.html)
* [Ref](https://www.youtube.com/watch?v=HaEPXoXVf2k)
* [Ref](https://www.youtube.com/watch?v=yvBR71D0nAQ)


> #### Database Algorithms

#### Hyperloglog
* [Ref](https://odino.org/my-favorite-data-structure-hyperloglog/)

#### Log Structured Merge Tree
* [Ref](https://www.cs.umb.edu/~poneil/lsmtree.pdf)

#### Sorted String Tables and Compaction Strategies
* [Ref](https://github.com/scylladb/scylladb/wiki/SSTable-compaction-and-compaction-strategies)

#### Leveled Compaction Cassandra
* [Ref](https://www.datastax.com/blog/leveled-compaction-apache-cassandra)

#### Scylla DB Compaction
* [Ref](https://github.com/scylladb/scylladb/wiki/SSTable-compaction-and-compaction-strategies)

#### Indexing In Cassandra
* [Ref](https://www.bmc.com/blogs/cassandra-clustering-columns-partition-composite-key/)


## SQL vs NoSQL
#### [Ref](https://github.com/donnemartin/system-design-primer#sql-or-nosql)
> #### When to use SQL or NoSQL?
  * [Ref](https://github.com/lahin31/system-design-bangla/blob/master/sections/database/README.md)
> #### Graph Database vs Relational Database
  * [Ref](https://memgraph.com/blog/graph-database-vs-relational-database)


## Time Series Databases

> #### Pinterest Time Series Database
  * [Ref](https://medium.com/pinterest-engineering/goku-building-a-scalable-and-high-performant-time-series-database-system-a8ff5758a181)
> #### Uber Time Series DB
  * [Ref](https://eng.uber.com/aresdb/)
> #### Time Series Relational DB
  * [Ref](https://www.timescale.com/blog/time-series-data-why-and-how-to-use-a-relational-database-instead-of-nosql-d0cd6975e87c/)
> #### Facebook Gorilla Time Series DB
  * [Ref](https://www.vldb.org/pvldb/vol8/p1816-teller.pdf)


## In Memory Database-Redis

> #### Redis Official Documentation
  * [Ref](https://medium.com/pinterest-engineering/goku-building-a-scalable-and-high-performant-time-series-database-system-a8ff5758a181)
> #### Learn Redis through Redis University
  * [Ref](https://university.redis.com/)
> #### Redis Open Source Repo
  * [Ref](https://github.com/redis/redis)
> #### Redis Architecture
  * [Ref](https://medium.com/opstree-technology/redis-cluster-architecture-replication-sharding-and-failover-86871e783ac0)