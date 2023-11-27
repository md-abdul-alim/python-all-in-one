# SYSTEM DESIGN
## Database
* [SQL](#sql)
  * [Relational database management system (RDBMS)](#relational-database-management-system-rdbms)
    * [Replication](#replication)
      * [Master-Slave](#master-slave)
      * [Master-Master](#master-master)
      * [Synchronous vs Asynchronous replication](#synchronous-vs-asynchronous-replication)
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

* [Indexes](#indexes)
  * [Dense Index](#dense-index)
  * [Sparse Index](#sparse-index)

* [Normalization and Denormalization](#normalization-and-denormalization)
  * [Normalization](#normalization)
  * [Denormalization](#denormalization)

* [ACID and BASE consistency models](#acid-and-base-consistency-models)
  * [ACID](#acid)
  * [BASE](#base)

* [Transactions](#transactions)
  * [Distributed Transactions](#distributed-transactions)

* [Consistent Hashing](#consistent-hashing)

* [SQL vs NoSQL](#sql-vs-nosql)
  * [When to use SQL or NoSQL?](#when-to-use-sql-or-nosql)
  * [Graph Database vs Relational Database](#graph-database-vs-relational-database)
  * [Relational vs non-relational](#relational-vs-non-relational)

* [Time Series Databases](#time-series-databases)
  * [Pinterest Time Series Database](#pinterest-time-series-database)
  * [Uber Time Series DB](#uber-time-series-db)
  * [Time Series Relational DB](#time-series-relational-db)
  * [Facebook Gorilla Time Series DB](#facebook-gorilla-time-series-db)

* [A nice cheat sheet of different databases in cloud services](#a-nice-cheat-sheet-of-different-databases-in-cloud-services)
* [8 Data Structures That Power Your Databases](#8-data-structures-that-power-your-databases)
* [How is an SQL statement executed in the database?](#how-is-an-sql-statement-executed-in-the-database)
* [CAP theorem-Availability vs consistency](#cap-theorem-availability-vs-consistency)
  * [CP-consistency and partition tolerance](#cp-consistency-and-partition-tolerance)
    * [Consistency patterns](#consistency-patterns)
  * [AP-availability and partition tolerance](#ap-availability-and-partition-tolerance)
    * [Availability patterns](#availability-patterns)
* [PACELC Theorem](#pacelc-theorem)
* [Types of Memory and Storage](#types-of-memory-and-storage)
* [Visualizing a SQL query](#visualizing-a-sql-query)
* [SQL language](#sql-language)
--------------------------------------

## Cache
* [Client caching](#client-caching)
* [CDN caching](#cdn-caching)
* [Web server caching](#web-server-caching)
* [Database caching](#database-caching)
* [Application caching](#application-caching)
* [Caching at the database query level](#caching-at-the-database-query-level)
* [Caching at the object level](#caching-at-the-object-level)
* [Top 5 Caching Patterns](#top-5-caching-patterns)
* [Cache invalidation-When to update the cache](#cache-invalidation-when-to-update-the-cache)
    * [Cache-aside](#cache-aside)
    * [Write-through](#write-through)
    * [Write-behind (write-back)](#write-behind-write-back)
    * [Refresh-ahead](#refresh-ahead)
* [Eviction policies](#eviction-policies)
* [Distributed Cache](#distributed-cache)
* [Global Cache](#global-cache)
* [Redis-In Memory Database](#redis-in-memory-database)
  * [Redis Official Documentation](#redis-official-documentation)
  * [Learn Redis through Redis University](#learn-redis-through-redis-university)
  * [Redis Open Source Repo](#redis-open-source-repo)
  * [Redis Architecture](#redis-architecture)
  * [YouTube Video](#youtube-video)
* [Data is cached everywhere](#data-is-cached-everywhere)
* [Why is Redis so fast?](#why-is-redis-so-fast)
* [How can Redis be used?](#how-can-redis-be-used)
* [Top caching strategies](#top-caching-strategies)
* [Use cases](#use-cases)
* [Advantages](#advantages)


--------------------------------------

## Architectural Design
* [Software Architecture](#software-architecture)
  * [MVC, MVP, MVVM, MVVM-C, and VIPER](#mvc-mvp-mvvm-mvvm-c-and-viper)
  * [18 Key Design Patterns](#18-key-design-patterns)
  * [Hexagonal Architecture](#hexagonal-architecture)
  * [Hexagonal architecture (Alistair Cockburn)](#hexagonal-architecture-alistair-cockburn)
  * [The Clean Code by Robert C. Martin (Uncle Bob)](#the-clean-code-by-robert-c-martin-uncle-bob)
  * [CQRS](#cqrs)
  * [Domain Driven Design](#domain-driven-design)

* [Microservice architecture](#microservice-architecture)
  * [Monolith Architecture](#monolith-architecture)
  * [Monoliths vs Microservices](#monoliths-vs-microservices)
  * [Uber Nano services antipattern](#uber-nano-services-antipattern)
  * [Uber Domain oriented microservice](#uber-domain-oriented-microservice)
  * [What does a typical microservice architecture look like?](#what-does-a-typical-microservice-architecture-look-like)
  * [Microservice Best Practices](#microservice-best-practices)
  * [What tech stack is commonly used for microservices?](#what-tech-stack-is-commonly-used-for-microservices)
  * [Why is Kafka fast?](#why-is-kafka-fast)
* [Event Driven Architectures](#event-driven-architectures)
  * [Martin Fowler-Event Driven Architecture](#martin-fowler-event-driven-architecture)
  * [Event Driven Architecture](#event-driven-architecture)

  
--------------------------------------

## Server and Network Design

--------------------------------------
--------------------------------------


## Database
## SQL
### Relational database management system (RDBMS)
* [Ref](https://github.com/donnemartin/system-design-primer#relational-database-management-system-rdbms)

> #### Replication

* [Ref 1](https://github.com/lahin31/system-design-bangla/tree/master#section-18-database-replication)
* [Ref 2](https://github.com/karanpratapsingh/system-design#database-replication)

#### Master-Slave
* [Ref 1](https://github.com/donnemartin/system-design-primer#master-slave-replication)
* [Ref 2](https://github.com/karanpratapsingh/system-design#master-slave-replication)

#### Master-Master
* [Ref 1](https://github.com/donnemartin/system-design-primer#master-master-replication)
* [Ref 2](https://github.com/karanpratapsingh/system-design#master-master-replication)

#### Synchronous vs Asynchronous replication
* [Ref](https://github.com/karanpratapsingh/system-design#synchronous-vs-asynchronous-replication)


> #### Federation
* [Ref 1](https://github.com/donnemartin/system-design-primer#federation)
* [Ref 2](https://github.com/karanpratapsingh/system-design#database-federation)

> #### Sharding
* [Ref 1](https://github.com/donnemartin/system-design-primer#sharding)
* [Ref 2](https://github.com/lahin31/system-design-bangla/tree/master#section-17-database-sharding)
* [Ref 3](https://github.com/karanpratapsingh/system-design#sharding)
* [Ref 4](https://github.com/Jeevan-kumar-Raj/Grokking-System-Design/blob/master/basics/sharding.md#sharding--data-partitioning)

> #### De-normalization
* [Ref](https://github.com/donnemartin/system-design-primer#denormalization)

> #### SQL tuning
* [Ref](https://github.com/donnemartin/system-design-primer#sql-tuning)


## NoSQLCP-consistency and partition tolerance
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


## Indexes
#### [Ref](https://github.com/karanpratapsingh/system-design#indexes)
> #### Dense Index
  * [Ref](https://github.com/karanpratapsingh/system-design#dense-index)

> #### Sparse Index
  * [Ref](https://github.com/karanpratapsingh/system-design#sparse-index)


## Normalization and Denormalization
#### [Ref](https://github.com/karanpratapsingh/system-design#normalization-and-denormalization)
> #### Normalization
  * [Ref](https://github.com/karanpratapsingh/system-design#normalization)

> #### Denormalization
  * [Ref](https://github.com/karanpratapsingh/system-design#denormalization)


## ACID and BASE consistency models
#### [Ref 1](https://github.com/karanpratapsingh/system-design#acid-and-base-consistency-models)
#### [Ref 2](https://github.com/Jeevan-kumar-Raj/Grokking-System-Design/blob/master/basics/cap-theorem.md#cap-theorem)
> #### ACID
  * [Ref 1](https://github.com/karanpratapsingh/system-design#acid)
  * [Ref 2](https://redis.com/glossary/acid-transactions/)
> #### BASE
  * [Ref](https://github.com/karanpratapsingh/system-design#base)


## Transactions
#### [Ref](https://github.com/karanpratapsingh/system-design#transactions)
> #### Distributed Transactions
  * [Ref](https://github.com/karanpratapsingh/system-design#distributed-transactions)

## Consistent Hashing
#### [Ref 1](https://tom-e-white.com/2007/11/consistent-hashing.html)
#### [Ref 2](https://arpitbhayani.me/blogs/consistent-hashing/)
#### [Ref 3](https://www.paperplanes.de/2011/12/9/the-magic-of-consistent-hashing.html)
#### [Ref 4](https://github.com/karanpratapsingh/system-design#consistent-hashing)
#### [Ref 5](https://github.com/Jeevan-kumar-Raj/Grokking-System-Design/blob/master/basics/consistent-hashing.md#consistent-hashing)



## SQL vs NoSQL
#### [Ref](https://github.com/donnemartin/system-design-primer#sql-or-nosql)
> #### When to use SQL or NoSQL?
  * [Ref](https://github.com/lahin31/system-design-bangla/blob/master/sections/database/README.md)
> #### Graph Database vs Relational Database
  * [Ref](https://memgraph.com/blog/graph-database-vs-relational-database)
> #### Relational vs non-relational
  * [Ref](https://www.altexsoft.com/blog/comparing-database-management-systems-mysql-postgresql-mssql-server-mongodb-elasticsearch-and-others/)


## Time Series Databases

> #### Pinterest Time Series Database
  * [Ref](https://medium.com/pinterest-engineering/goku-building-a-scalable-and-high-performant-time-series-database-system-a8ff5758a181)
> #### Uber Time Series DB
  * [Ref](https://eng.uber.com/aresdb/)
> #### Time Series Relational DB
  * [Ref](https://www.timescale.com/blog/time-series-data-why-and-how-to-use-a-relational-database-instead-of-nosql-d0cd6975e87c/)
> #### Facebook Gorilla Time Series DB
  * [Ref](https://www.vldb.org/pvldb/vol8/p1816-teller.pdf)

### A nice cheat sheet of different databases in cloud services
* [Ref](https://github.com/ByteByteGoHq/system-design-101#a-nice-cheat-sheet-of-different-databases-in-cloud-services)

### 8 Data Structures That Power Your Databases
* [Ref](https://github.com/ByteByteGoHq/system-design-101#8-data-structures-that-power-your-databases)

### How is an SQL statement executed in the database?
* [Ref](https://github.com/ByteByteGoHq/system-design-101#how-is-an-sql-statement-executed-in-the-database)

### CAP theorem-Availability vs consistency
* [Ref 1](https://github.com/ByteByteGoHq/system-design-101#cap-theorem)
* [Ref 2](https://github.com/donnemartin/system-design-primer/tree/master#cap-theorem)
* [Ref 3](https://github.com/karanpratapsingh/system-design#cap-theorem)

> #### CP-consistency and partition tolerance
  * [Ref](https://github.com/donnemartin/system-design-primer/tree/master#cp---consistency-and-partition-tolerance)
> #### Consistency patterns
  * [Ref](https://github.com/donnemartin/system-design-primer/tree/master#consistency-patterns)
> #### AP-availability and partition tolerance
  * [Ref](https://github.com/donnemartin/system-design-primer/tree/master#ap---availability-and-partition-tolerance)
> #### Availability patterns
  * [Ref](https://github.com/donnemartin/system-design-primer/tree/master#availability-patterns)

### PACELC Theorem
* [Ref](https://github.com/karanpratapsingh/system-design#pacelc-theorem)

### Types of Memory and Storage
* [Ref](https://github.com/ByteByteGoHq/system-design-101#types-of-memory-and-storage)

### Visualizing a SQL query
* [Ref](https://github.com/ByteByteGoHq/system-design-101#visualizing-a-sql-query)

### SQL language
* [Ref](https://github.com/ByteByteGoHq/system-design-101#sql-language)

-----------------------------------
## Cache
* [Ref 1](https://github.com/donnemartin/system-design-primer#cache)
* [Ref 2](https://medium.com/must-know-computer-science/system-design-caching-acbd1b02ca01)

> ### Client caching
  * [Ref](https://github.com/donnemartin/system-design-primer#client-caching)

> ### CDN caching
  * [Ref](https://github.com/donnemartin/system-design-primer#cdn-caching)

> ### Web server caching
  * [Ref](https://github.com/donnemartin/system-design-primer#web-server-caching)

> ### Database caching
  * [Ref](https://github.com/donnemartin/system-design-primer#database-caching)

> ### Application caching
  * [Ref](https://github.com/donnemartin/system-design-primer#application-caching)

> ### Caching at the database query level
  * [Ref](https://github.com/donnemartin/system-design-primer#caching-at-the-database-query-level)

> ### Caching at the object level
  * [Ref](https://github.com/donnemartin/system-design-primer#caching-at-the-object-level)
> ### Top 5 Caching Patterns
  * [Ref](https://newsletter.systemdesign.one/p/caching-patterns)

> ### Cache invalidation-When to update the cache
  * [Ref 1](https://github.com/donnemartin/system-design-primer#when-to-update-the-cache)
  * [Ref 2](https://github.com/Jeevan-kumar-Raj/Grokking-System-Design/blob/master/basics/caching.md#cache-invalidation)

> #### Cache-aside
  * [Ref 1](https://github.com/donnemartin/system-design-primer#cache-aside)
  * [Ref 2](https://github.com/karanpratapsingh/system-design#write-around-cache)

> #### Write-through
  * [Ref 1](https://github.com/donnemartin/system-design-primer#write-through)
  * [Ref 2](https://github.com/karanpratapsingh/system-design#write-through-cache)

> #### Write-behind (write-back)
  * [Ref 1](https://github.com/donnemartin/system-design-primer#write-behind-write-back)
  * [Ref 2](https://github.com/karanpratapsingh/system-design#write-back-cache)

> #### Refresh-ahead
  * [Ref](https://github.com/donnemartin/system-design-primer#refresh-ahead)


> ### Eviction policies
  * [Ref 1](https://github.com/karanpratapsingh/system-design#eviction-policies)
  * [Ref 2](https://github.com/Jeevan-kumar-Raj/Grokking-System-Design/blob/master/basics/caching.md#cache-eviction-policies)
> ### Distributed Cache
  * [Ref 1](https://github.com/karanpratapsingh/system-design#distributed-cache)
  * [Ref 2](https://github.com/Jeevan-kumar-Raj/Grokking-System-Design/blob/master/basics/caching.md#distributed-cache)
  * [Ref 3](https://redis.com/glossary/distributed-caching/)
> ### Global Cache
  * [Ref 1](https://github.com/karanpratapsingh/system-design#global-cache)
  * [Ref 2](https://github.com/Jeevan-kumar-Raj/Grokking-System-Design/blob/master/basics/caching.md#global-cache)
> ### Redis-In Memory Database
  * [Ref](https://redis.io/)

> #### Learn Redis through Redis University
  * [Ref](https://university.redis.com/)
> #### Redis Official Documentation
  * [Ref](https://medium.com/pinterest-engineering/goku-building-a-scalable-and-high-performant-time-series-database-system-a8ff5758a181)
> #### Learn Redis through Redis University
  * [Ref](https://university.redis.com/)
> #### Redis Open Source Repo
  * [Ref](https://github.com/redis/redis)
> #### Redis Architecture
  * [Ref](https://medium.com/opstree-technology/redis-cluster-architecture-replication-sharding-and-failover-86871e783ac0)
> #### YouTube Video
  * [Ref](https://www.youtube.com/watch?v=Vx2zPMPvmug&t=4074s)

> ### Data is cached everywhere
  * [Ref](https://github.com/ByteByteGoHq/system-design-101#data-is-cached-everywhere)

> ### Why is Redis so fast?
  * [Ref](https://github.com/ByteByteGoHq/system-design-101#why-is-redis-so-fast)

> ### How can Redis be used?
  * [Ref](https://github.com/ByteByteGoHq/system-design-101#how-can-redis-be-used)

> ### Top caching strategies
  * [Ref](https://github.com/ByteByteGoHq/system-design-101#top-caching-strategies)

> ### Use cases
  * [Ref](https://github.com/karanpratapsingh/system-design#use-cases)

> ### Advantages
  * [Ref](https://github.com/karanpratapsingh/system-design#advantages-2)


## Architectural Design
> ### Software Architecture

  #### MVC, MVP, MVVM, MVVM-C, and VIPER
  * [Ref](https://github.com/ByteByteGoHq/system-design-101#mvc-mvp-mvvm-mvvm-c-and-viper)
  #### 18 Key Design Patterns
  * [Ref](https://github.com/ByteByteGoHq/system-design-101#18-key-design-patterns-every-developer-should-know)
  #### Hexagonal Architecture
  * [Ref](https://netflixtechblog.com/ready-for-changes-with-hexagonal-architecture-b315ec967749)
  #### Hexagonal architecture (Alistair Cockburn)
  * [Ref](https://alistair.cockburn.us/hexagonal-architecture/)
  #### The Clean Code by Robert C. Martin (Uncle Bob)
  * [Ref](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
  #### CQRS
  * [Ref](https://martinfowler.com/bliki/CQRS.html)
  #### Domain Driven Design
  * [Ref](https://martinfowler.com/bliki/DomainDrivenDesign.html)



> ### Microservice architecture
  #### Monolith Architecture
  * [Ref](https://buttercms.com/books/microservices-for-startups/should-you-always-start-with-a-monolith/)
  #### Monoliths vs Microservices
  * [Ref](https://buttercms.com/books/microservices-for-startups/should-you-always-start-with-a-monolith/)
  #### Uber Nano services antipattern
  * [Ref](https://www.youtube.com/watch?v=kb-m2fasdDY)
  #### Uber Domain oriented microservice
  * [Ref](https://eng.uber.com/microservice-architecture/)
  #### What does a typical microservice architecture look like?
  * [Ref](https://github.com/ByteByteGoHq/system-design-101#what-does-a-typical-microservice-architecture-look-like)
  #### Microservice Best Practices
  * [Ref](https://github.com/ByteByteGoHq/system-design-101#microservice-best-practices)
  #### What tech stack is commonly used for microservices?
  * [Ref](https://github.com/ByteByteGoHq/system-design-101#what-tech-stack-is-commonly-used-for-microservices)
  #### Why is Kafka fast?
  * [Ref](https://github.com/ByteByteGoHq/system-design-101#why-is-kafka-fast)

> ### Event Driven Architectures
  #### Martin Fowler-Event Driven Architecture
  * [Ref](https://www.youtube.com/watch?v=STKCRSUsyP0)
  #### Event Driven Architecture
  * [Ref](https://martinfowler.com/articles/201701-event-driven.html)