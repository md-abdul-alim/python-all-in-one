# SYSTEM DESIGN
## Database
* [SQL](#sql)
  * [Relational database management system (RDBMS)](#relational-database-management-system-rdbms)
  * [Database Scaling](#database-scaling)
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

* [Normalization and De-normalization](#normalization-and-de-normalization)
  * [Normalization](#normalization)
  * [De-normalization](#de-normalization)

* [ACID and BASE consistency models](#acid-and-base-consistency-models)
  * [ACID](#acid)
  * [BASE](#base)

* [Transactions](#transactions)
  * [Distributed Transactions](#distributed-transactions)

* [Eventual vs Strong Consistency in Distributed Databases](#eventual-vs-strong-consistency-in-distributed-databases)

* [Consistency Patterns](#consistency-patterns)

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
* [Data Redundancy](#data-redundancy)
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
* [Backend Caching Strategies](#backend-caching-strategies)
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
  * [Microservices Architecture](#microservices-architecture)
  * [Circuit Breaker Pattern](#circuit-breaker-pattern)
  * [Netflix Microservices](#netflix-microservices)
  * [Monolith Architecture](#monolith-architecture)
  * [Monoliths vs Microservices](#monoliths-vs-microservices)
  * [Uber Nano services anti-pattern](#uber-nano-services-anti-pattern)
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
* [Client-Server Communication](#client-server-communication)
* [Content Delivery Network (CDN)](#content-delivery-network-cdn)
* [Latency vs Throughput](#latency-vs-hroughput)
* [Rate Limiting](#rate-limiting)
* [Batch Processing vs Stream Processing](#batch-processing-vs-stream-processing)
* [Proxy Server](#proxy-server)
* [Domain Name System (DNS)](#domain-name-system-dns)
* [Message Queues](#message-queues)
* [WebSockets](#websockets)
* [API Gateway](#api-gateway)
--------------------------------------
# System Design Interview Problems

## Easy
* [Design Leaderboard](#design-leaderboard)
* [Design URL Shortener like TinyURL](#design-url-shortener-like-tinyurl)
* [Design Text Storage Service like Pastebin](#design-text-storage-service-like-pastebin)
* [Design Content Delivery Network (CDN)](#design-content-delivery-network-cdn)
* [Design Parking Garage](#design-parking-garage)
* [Design Vending Machine](#design-vending-machine)
* [Design Distributed Key-Value Store](#design-distributed-key-value-store)
* [Design Distributed Cache](#design-distributed-cache)
* [Design Distributed Job Scheduler](#design-distributed-job-scheduler)
* [Design Authentication System](#design-authentication-system)
* [Design Unified Payments Interface (UPI)](#design-unified-payments-interface-upi)
* [Design type-ahead search or autocomplete](#design-type-ahead-search-or-autocomplete)
* [Design a Load Balancer or Dropbox Bandaid](#design-a-load-balancer-or-dropbox-bandaid)
* [Fraud Detection with Semi-supervised Learning](#fraud-detection-with-semi-supervised-learning)
* [Design Online Judge](#design-online-judge)

## Medium
* [Design Instagram](#design-instagram)
* [Design Tinder](#design-tinder)
* [Design WhatsApp](#design-whatsapp)
* [Design Facebook](#design-facebook)
* [Facebook Newsfeed](#facebook-newsfeed)
* [Design Twitter](#design-twitter)
* [Twitter Search](#twitter-search)
* [Design Reddit](#design-reddit)
* [Design Netflix](#design-netflix)
* [Design YouTube](#design-youtube)
* [Design Google Search](#design-google-search)
* [Design E-commerce Store like Amazon](#design-e-commerce-store-like-amazon)
* [Design Spotify](#design-spotify)
* [Design TikTok](#design-tiktok)
* [Design Shopify](#design-shopify)
* [Design Airbnb](#design-airbnb)
* [Design Autocomplete for Search Engines](#design-autocomplete-for-search-engines)
* [Design Rate Limiter](#design-rate-limiter)
* [Design Distributed Message Queue like Kafka](#design-distributed-message-queue-like-kafka)
* [Design Flight Booking System](#design-flight-booking-system)
* [Design Online Code Editor](#design-online-code-editor)
* [Design Stock Exchange System](#design-stock-exchange-system)
* [Design an Analytics Platform (Metrics & Logging)](#design-an-analytics-platform-metrics--logging)
* [Design Notification Service](#design-notification-service)
* [Design Payment System](#design-payment-system)
* [Designing payment webhook](#designing-payment-webhook)
* [Design Paypal Payment System](#design-paypal-payment-system)
* [Design Pinterest](#design-pinterest)

## Hard
* [Design Slack](#design-slack)
* [Design Live Comments](#design-live-comments)
* [Design Distributed Counter](#design-distributed-counter)
* [Design Location Based Service like Yelp](#design-location-based-service-like-yelp)
* [Design Uber](#design-uber)
* [Uber Backend](#uber-backend)
* [Design Food Delivery App like Doordash](#design-food-delivery-app-like-doordash)
* [Design Google Docs](#design-google-docs)
* [Design Google Maps](#design-google-maps)
* [Design Zoom](#design-zoom)
* [Design File Sharing System like Dropbox](#design-file-sharing-system-like-dropbox)
* [Design Ticket Booking System like BookMyShow](#design-ticket-booking-system-like-bookmyshow)
* [Design Distributed Web Crawler](#design-distributed-web-crawler)
* [Design Code Deployment System](#design-code-deployment-system)
* [Design Distributed Cloud Storage like S3](#design-distributed-cloud-storage-like-s3)
* [Design Distributed Locking Service](#design-distributed-locking-service)
* [Cloud Design Patterns](#cloud-design-patterns)
--------------------------------------


## Database
## SQL
### Relational database management system (RDBMS)
* [Ref](https://github.com/donnemartin/system-design-primer#relational-database-management-system-rdbms)

### Database Scaling
* [Ref](https://thenewstack.io/techniques-for-scaling-applications-with-a-database/)
> #### Replication
* [Ref 1](https://github.com/lahin31/system-design-bangla/tree/master#section-18-database-replication)
* [Ref 2](https://github.com/karanpratapsingh/system-design#database-replication)
* [Ref 3](https://redis.com/blog/what-is-data-replication/)

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
* [Ref 5](https://www.mongodb.com/features/database-sharding-explained)

> #### De-normalization
* [Ref](https://github.com/donnemartin/system-design-primer#de-normalization)

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


## Indexes
#### [Ref 1](https://github.com/karanpratapsingh/system-design#indexes)
#### [Ref 2](https://www.progress.com/tutorials/odbc/using-indexes)
> #### Dense Index
  * [Ref](https://github.com/karanpratapsingh/system-design#dense-index)

> #### Sparse Index
  * [Ref](https://github.com/karanpratapsingh/system-design#sparse-index)


## Normalization and De-normalization
#### [Ref](https://github.com/karanpratapsingh/system-design#normalization-and-denormalization)
> #### Normalization
  * [Ref](https://github.com/karanpratapsingh/system-design#normalization)

> #### De-normalization
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

## Eventual vs Strong Consistency in Distributed Databases
#### [Ref](https://hackernoon.com/eventual-vs-strong-consistency-in-distributed-databases-282fdad37cf7)

## Consistency Patterns
#### [Ref](https://systemdesign.one/consistency-patterns/)

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
* [Ref 4](https://www.bmc.com/blogs/cap-theorem/)

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

### Data Redundancy
* [Ref](https://www.egnyte.com/guides/governance/data-redundancy)
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
  * [Ref 1](https://github.com/donnemartin/system-design-primer#cdn-caching)
  * [Ref 2](https://github.com/Jeevan-kumar-Raj/Grokking-System-Design/blob/master/basics/caching.md#content-distributed-network-cdn)

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
> ### Backend Caching Strategies
  * [Ref](https://www.linkedin.com/feed/update/urn:li:activity:7136700953629450240/)

> ### Cache invalidation-When to update the cache
  * [Ref 1](https://github.com/donnemartin/system-design-primer#when-to-update-the-cache)
  * [Ref 2](https://github.com/Jeevan-kumar-Raj/Grokking-System-Design/blob/master/basics/caching.md#cache-invalidation)
  * [Ref 3](https://github.com/Jeevan-kumar-Raj/Grokking-System-Design/blob/master/basics/caching.md#cache-invalidation)

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
  * [Ref 1](https://github.com/ByteByteGoHq/system-design-101#mvc-mvp-mvvm-mvvm-c-and-viper)
  * [Ref 2](https://www.linkedin.com/posts/ginacostag_developer-software-python-activity-7134888640513495040-oARO?utm_source=share&utm_medium=member_desktop)
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
  #### Microservices Architecture
  * [Ref](https://medium.com/hashmapinc/the-what-why-and-how-of-a-microservices-architecture-4179579423a9)
  #### Circuit Breaker Pattern
  * [Ref](https://medium.com/geekculture/design-patterns-for-microservices-circuit-breaker-pattern-276249ffab33)
  #### Netflix Microservices
  * [Ref](https://newsletter.systemdesign.one/p/netflix-microservices)
  #### Monolith Architecture
  * [Ref](https://buttercms.com/books/microservices-for-startups/should-you-always-start-with-a-monolith/)
  #### Monoliths vs Microservices
  * [Ref](https://buttercms.com/books/microservices-for-startups/should-you-always-start-with-a-monolith/)
  #### Uber Nano services anti-pattern
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
---------------------------------

## Server and Network Design
#### Client-Server Communication
  * [Ref](https://github.com/Jeevan-kumar-Raj/Grokking-System-Design/blob/master/basics/client-server-communication.md#client-server-communication)
#### Content Delivery Network (CDN)
  * [Ref](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)
#### Latency vs Throughput
  * [Ref](https://aws.amazon.com/compare/the-difference-between-throughput-and-latency/)
#### Rate Limiting
  * [Ref](https://www.imperva.com/learn/application-security/rate-limiting/)
#### Batch Processing vs Stream Processing
  * [Ref 1](https://atlan.com/batch-processing-vs-stream-processing/)
  * [Ref 2](https://github.com/puncsky/system-design-and-architecture/blob/master/en/137-stream-and-batch-processing.md)
#### Proxy Server
  * [Ref](https://www.fortinet.com/resources/cyberglossary/proxy-server)
#### Domain Name System (DNS)
  * [Ref](https://www.cloudflare.com/learning/dns/what-is-dns/)
#### Message Queues
  * [Ref](https://medium.com/must-know-computer-science/system-design-message-queues-245612428a22)
#### WebSockets
  * [Ref](https://www.pubnub.com/guides/websockets/)
#### API Gateway
  * [Ref](https://www.nginx.com/learn/api-gateway/)
---------------------------------
## System Design Interview Problems
> ### Easy
  #### Design Leaderboard
  * [Ref](https://systemdesign.one/leaderboard-system-design/)
  #### Design URL Shortener like TinyURL
  * [Ref 1](https://www.youtube.com/watch?v=fMZMm_0ZhK4&themeRefresh=1)
  * [Ref 2](https://github.com/Jeevan-kumar-Raj/Grokking-System-Design/blob/master/designs/short-url.md)
  * [Ref 3](https://github.com/puncsky/system-design-and-architecture/blob/master/en/84-designing-a-url-shortener.md)
  #### Design Text Storage Service like Pastebin
  * [Ref 1](https://www.youtube.com/watch?v=josjRSBqEBI)
  * [Ref 2](https://github.com/Jeevan-kumar-Raj/Grokking-System-Design/blob/master/designs/pastebin.md)
  #### Design Content Delivery Network (CDN)
  * [Ref](https://www.youtube.com/watch?v=8zX0rue2Hic)
  #### Design Parking Garage
  * [Ref](https://www.youtube.com/watch?v=NtMvNh0WFVM)
  #### Design Vending Machine
  * [Ref](https://www.youtube.com/watch?v=D0kDMUgo27c)
  #### Design Distributed Key-Value Store
  * [Ref](https://www.youtube.com/watch?v=rnZmdmlR-2M)
  #### Design Distributed Cache
  * [Ref](https://www.youtube.com/watch?v=iuqZvajTOyA)
  #### Design Distributed Job Scheduler
  * [Ref](https://towardsdatascience.com/ace-the-system-design-interview-job-scheduling-system-b25693817950)
  #### Design Authentication System
  * [Ref](https://www.youtube.com/watch?v=uj_4vxm9u90)
  #### Design Unified Payments Interface (UPI)
  * [Ref](https://www.youtube.com/watch?v=QpLy0_c_RXk)
  #### Design type-ahead search or autocomplete
  * [Ref](https://github.com/puncsky/system-design-and-architecture/blob/master/en/179-designing-typeahead-search-or-autocomplete.md)
  #### Design a Load Balancer or Dropbox Bandaid
  * [Ref](https://github.com/puncsky/system-design-and-architecture/blob/master/en/182-designing-l7-load-balancer.md)
  #### Fraud Detection with Semi-supervised Learning
  * [Ref](https://github.com/puncsky/system-design-and-architecture/blob/master/en/136-fraud-detection-with-semi-supervised-learning.md)
  #### Design Online Judge
  * [Ref](https://tianpan.co/notes/243-designing-online-judge-or-leetcode)

> ### Medium
  #### Design Instagram
  * [Ref 1](https://www.youtube.com/watch?v=VJpfO6KdyWE)
  * [Ref 2](https://github.com/Jeevan-kumar-Raj/Grokking-System-Design/blob/master/designs/instagram.md)
  #### Design Tinder
  * [Ref](https://www.youtube.com/watch?v=tndzLznxq40)
  #### Design WhatsApp
  * [Ref](https://www.youtube.com/watch?v=vvhC64hQZMk)
  #### Design Facebook
  * [Ref 1](https://www.youtube.com/watch?v=9-hjBGxuiEs)
  * [Ref 2](https://github.com/puncsky/system-design-and-architecture/blob/master/en/49-facebook-tao.md)
  * [Ref 3](https://github.com/puncsky/system-design-and-architecture/blob/master/en/121-designing-facebook-photo-storage.md)
  #### Facebook Newsfeed
  * [Ref](https://github.com/Jeevan-kumar-Raj/Grokking-System-Design/blob/master/designs/facebook-newsfeed.md)
  #### Design Twitter
  * [Ref 1](https://www.youtube.com/watch?v=wYk0xPP_P_8)
  * [Ref 2](https://github.com/Jeevan-kumar-Raj/Grokking-System-Design/blob/master/designs/twitter.md)
  #### Twitter Search
  * [Ref](https://github.com/Jeevan-kumar-Raj/Grokking-System-Design/blob/master/designs/twitter-search.md)
  #### Design Reddit
  * [Ref](https://www.youtube.com/watch?v=KYExYE_9nIY)
  #### Design Netflix
  * [Ref 1](https://www.youtube.com/watch?v=psQzyFfsUGU)
  * [Ref 2](https://github.com/puncsky/system-design-and-architecture/blob/master/en/38-how-to-stream-video-over-http.md)
  #### Design YouTube
  * [Ref 1](https://www.youtube.com/watch?v=jPKTo1iGQiE)
  * [Ref 2](https://github.com/Jeevan-kumar-Raj/Grokking-System-Design/blob/master/designs/youtube.md)
  #### Design Google Search
  * [Ref](https://www.youtube.com/watch?v=CeGtqouT8eA)
  #### Design E-commerce Store like Amazon
  * [Ref](https://www.youtube.com/watch?v=EpASu_1dUdE)
  #### Design Spotify
  * [Ref](https://www.youtube.com/watch?v=_K-eupuDVEc)
  #### Design TikTok
  * [Ref](https://www.youtube.com/watch?v=Z-0g_aJL5Fw)
  #### Design Shopify
  * [Ref](https://www.youtube.com/watch?v=lEL4F_0J3l8)
  #### Design Airbnb
  * [Ref](https://www.youtube.com/watch?v=YyOXt2MEkv4)
  #### Design Autocomplete for Search Engines
  * [Ref](https://www.youtube.com/watch?v=us0qySiUsGU)
  #### Design Rate Limiter
  * [Ref](https://www.youtube.com/watch?v=mhUQe4BKZXs)
  #### Design Distributed Message Queue like Kafka
  * [Ref](https://www.youtube.com/watch?v=iJLL-KPqBpM)
  #### Design Flight Booking System
  * [Ref](https://www.youtube.com/watch?v=qsGcfVGvFSs)
  #### Design Online Code Editor
  * [Ref](https://www.youtube.com/watch?v=07jkn4jUtso)
  #### Design Stock Exchange System
  * [Ref 1](https://www.youtube.com/watch?v=dUMWMZmMsVE)
  * [Ref 2](https://github.com/puncsky/system-design-and-architecture/blob/master/en/161-designing-stock-exchange.md)
  * [Ref 3](https://github.com/puncsky/system-design-and-architecture/blob/master/en/162-designing-smart-notification-of-stock-price-changes.md)
  #### Design an Analytics Platform (Metrics & Logging)
  * [Ref 1](https://www.youtube.com/watch?v=kIcq1_pBQSY)
  * [Ref 2](https://github.com/puncsky/system-design-and-architecture/blob/master/en/61-what-is-apache-kafka.md)
  #### Design Notification Service
  * [Ref](https://www.youtube.com/watch?v=CUwt9_l0DOg)
  #### Design Payment System
  * [Ref](https://www.youtube.com/watch?v=olfaBgJrUBI)
  #### Designing payment webhook
  * [Ref](https://github.com/puncsky/system-design-and-architecture/blob/master/en/166-designing-payment-webhook.md)
  #### Design Paypal Payment System
  * [Ref](https://github.com/puncsky/system-design-and-architecture/blob/master/en/167-designing-paypal-money-transfer.md)
  #### Design Pinterest
  * [Ref](https://github.com/puncsky/system-design-and-architecture/blob/master/en/2016-02-13-crack-the-system-design-interview.md#design-pinterest)

> ### Hard
  #### Design Slack
  * [Ref](https://systemdesign.one/slack-architecture/)
  #### Design Live Comments
  * [Ref](https://systemdesign.one/live-comment-system-design/)
  #### Design Distributed Counter
  * [Ref](https://systemdesign.one/distributed-counter-system-design/)
  #### Design Location Based Service like Yelp
  * [Ref 1](https://www.youtube.com/watch?v=M4lR_Va97cQ)
  * [Ref 2](https://github.com/Jeevan-kumar-Raj/Grokking-System-Design/blob/master/designs/yelp.md)
  #### Design Uber
  * [Ref 1](https://www.youtube.com/watch?v=umWABit-wbk)
  * [Ref 2](https://github.com/puncsky/system-design-and-architecture/blob/master/en/120-designing-uber.md)
  #### Uber Backend
  * [Ref](https://github.com/Jeevan-kumar-Raj/Grokking-System-Design/blob/master/designs/uber-backend.md)
  #### Design Food Delivery App like Doordash
  * [Ref](https://www.youtube.com/watch?v=iRhSAR3ldTw)
  #### Design Google Docs
  * [Ref](https://www.youtube.com/watch?v=2auwirNBvGg)
  #### Design Google Maps
  * [Ref](https://www.youtube.com/watch?v=jk3yvVfNvds)
  #### Design Zoom
  * [Ref](https://www.youtube.com/watch?v=G32ThJakeHk)
  #### Design File Sharing System like Dropbox
  * [Ref 1](https://www.youtube.com/watch?v=U0xTu6E2CT8)
  * [Ref 2](https://github.com/Jeevan-kumar-Raj/Grokking-System-Design/blob/master/designs/dropbox.md)
  #### Design Ticket Booking System like BookMyShow
  * [Ref](https://www.youtube.com/watch?v=lBAwJgoO3Ek)
  #### Design Distributed Web Crawler
  * [Ref 1](https://www.youtube.com/watch?v=BKZxZwUgL3Y)
  * [Ref 2](https://github.com/Jeevan-kumar-Raj/Grokking-System-Design/blob/master/designs/web-crawler.md)
  #### Design Code Deployment System
  * [Ref](https://www.youtube.com/watch?v=q0KGYwNbf-0)
  #### Design Distributed Cloud Storage like S3
  * [Ref](https://www.youtube.com/watch?v=UmWtcgC96X8)
  #### Design Distributed Locking Service
  * [Ref](https://www.youtube.com/watch?v=v7x75aN9liM)
  #### Cloud Design Patterns
  * [Ref](https://learn.microsoft.com/en-us/azure/architecture/patterns/)
