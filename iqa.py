"""
1. What is serializer?
=> Serializer is a process of converting complex data structures or objects into a linear format that can be easily
    stored, transfer or manipulated. Like XML(eXtensible Markup Language, JSON(JavaScript Object Notation).
2. What is deserializer?
=> Deserializer takes serialized data and reconstructs the original data structure or object.

3. Why should we use serializer?
=> When we need to transmit data over a network, serialization is used to package the data into a format that can be
    transmitted efficiently.
=> For API service serialization is used to exchanged data between clients and servers.

4. Tell me about some serialization formats.
=> JSON(JavaScript Object Notation): Lightweight human read-able
=> XML(eXtensible Markup Language): Text-based markup language used for describing data.
=> Binary: More compact but less human-readable format.
=> Protocol Buffers(protobuf): Binary serialization format developed by Google that is both efficient and extensible.
    extensible means?
=> MessagePack: Binary format that is more compact and faster to serialize and deserialize than other formats.

5. When we should use which serialization format? Which is more efficient format?
=> JSON: needs when human-readable for debugging or manual inspection. JSON is not the best choice
    for large data payload. Because
        ~ lots of structural character like braces, colons and quotation marks
        ~ include fields name with every data item.
        ~ allow indentation and line breaks to improve human readability.
        ~~ above all increase the size of the payload. This can be a reason why this is not the best choice.
=> XML: needs when we need hierarchical structure with metadata and attributes.
    XML is the best choice for
        ~ documents, configuration files
    XML is not the best choice for large data payload. Because
        ~ lots of element names, metadata, attribute, whitespace
        ~~ above all increase the size of the payload.
=> Binary: Needs when high efficiency is important for both data size and serialization/ deserialization speed.
    high efficiency increase the high-performance. Not the best choice for human read-able.
=> Protocol Buffers(protobuf):
        ~ highly efficient and compact binary format.
        ~ the best choice for high-performance application, microservices
        ~ well-suited for cross-language compatibility and has build-in schema evolution support.
=> MessagePack: compact binary format space-efficient than JSON/XML
==> Note: For web API - JSON. For high-performance: Binary

6. For high-performance and large payload which serialization format is best?
=> Binary format is the best choice for efficiency in terms of both data size and serialization/deserialization speed.
=> There are two type of binary format.
    ~ Protocol buffers
    ~ MessagePack

7. between Protocol Buffers and MessagePack which is faster?
=> MessagePack is often considered to be slightly faster than Protocol Buffers in terms of
    serialization/ deserialization speed. It achieves this speed advantage because of its simpler binary format.
    Because it less structured than Protocol Buffers.
=> Protocol Buffers is more structured with schema support, schema evolution.
    ~ schema support: schema includes data type, fields name and their relationships.
    ~ Schema evolution: This provided field rules like 'optional', 'required' and 'repeated'.
==> Note: MessagePack doesn't support schema support and schema evolution like Protocol Buffers.

8. What is the difference between REST API serializer and graphQL serializer?
=> Both convert data object to suitable JSON/XML format. But they are different for bellow reason.
    ~ Serialization:
        ~ REST API - Manual Serialization: Need to write serialization class
        ~ GraphQL - Auto-Generated Serialization: Don't need to write extra serialization class. It will generate auto.
    ~ Data Shape:
        ~ REST API - Client have less control over the data shape. Data shape is fixed.
        ~ GraphQL - Client have more control over the data shape. Client can send single query specifying the data they
            want to receive.
        ~~ NOTE: GraphQL reduce data over-fetching and under-fetching.
    ~ API Endpoint:
        ~ REST API: Typically have fixed end point for different resource.
        ~ GraphQL: Single end point for all resource.
    ~ Data Over-fetching/Under-fetching:
        ~ REST API: Client some time receive more data (over-fetching) or not enough data (under-fetching) compared to
            what they need.
        ~ GraphQL: Client only receive the data they request by queries.

9. What is data over-fetching/ under-fetching?
=> Client some time receive more data (over-fetching) or not enough data (under-fetching) compared to what they need.

9. What is schema
"""