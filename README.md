# python-django-all-in-one

~ RDBMS = Relational Database Management System

~ Database ভার্টিকাল (vartical) স্কেলিং করা হয় মানে storage এর capacity বৃদ্ধি করা

~ Database shard: Horizontal : (https://aws.amazon.com/what-is/database-sharding/#:~:text=Database%20sharding%20splits%20a%20single,original%20database's%20schema%20or%20design.)

~ NoSQL ভিত্তিক হরাইজন্টাল স্কেলিং করা হয় মানে সার্ভারের Capacity বৃদ্ধি করার পরিবর্তে নতুন সার্ভার যোগ করাই হল হরাইজন্টাল স্কেলিং।

~ ACID database= atomicity, consistency, isolation, and durability (https://www.mongodb.com/basics/acid-transactions#:~:text=ACID%20is%20an%20acronym%20that,the%20event%20of%20unexpected%20errors.) (https://www.databricks.com/glossary/acid-transactions)

~ how database indexing work : (https://codemacaw.com/2023/04/04/database-indexing-makes-db-query-faster/)

~ What is B-tree & B+ tree in DBMS? : (https://codemacaw.com/2023/06/24/what-is-b-tree-b-tree-in-dbms/)

~ why: SELECT DISTINCT সম্ভব হলে avoid করা।

~ why: WHERE ব্যবহার করা HAVING এর পরিবর্তে।

~ how: Complex Query এর জন্য Stored Procedure ব্যবহার করা। এতে করে আমরা Network Traffic কমাতে পারি।

~ how: WHERE clause এর ভিতর Scaler Function ব্যবহার না করা। WHERE clause এর ভিতর Scaler Function ব্যবহার করলে Query Optimizer, Index কে ব্যবহার করতে পারে না।

~ why: n+1 query execute না করা।

~ connection pool: 

~ lru-cache: (https://realpython.com/lru-cache-python/)
