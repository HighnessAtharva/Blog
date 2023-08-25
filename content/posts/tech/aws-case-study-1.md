---
title: "AWS Security Scenario Case Study - S3 Migration"
date: 2023-08-20T15:18:34+05:30
draft: true
cover: 
    image: blog/aws/.webp
    alt: A Personal AWS Cheatsheet Dump
    caption:  A Personal Cheatsheet Dump
description: "AWS Security Scenario Case Study - S3 Migration"
tags: ["aws"]
---

## Case Study Scenario

Analytica Soft Pty Ltd (ASPT) - analyticasoft.com.au is a global analytics company with its head office in Australia. ASPT is planning to migrate its static website hosting to AWS Cloud in the first phase. One of the requirements is to setup a storage service on the cloud to store documents and videos. These documents will be available to the registered users as Presigned URLs. As part of the cloud team, your task is to analyze and recommend suitable AWS cloud services to meet ASPT's requirements. You need to prepare report for the following tasks.

Your task is to answer the following five questions:

### a. Cloud Service model recommendation. Consider factors to choose a region. (3 marks)

ASPT needs ready-to-use software applications without installation or maintenance.

1. Evaluate and recommend whether Platform as a Service (PaaS) or Software as a Service (SaaS) would be more suitable for their cloud implementation.
2. Discuss the benefits and limitations of each model, considering ASPT's specific needs.
3. Additionally, elaborate on the factors ASPT should consider when choosing an AWS region for a specific service deployment that is not available in both Melbourne and Sydney regions.
Justify your answer by giving an explanation and diagram(s) (if any).

### b. AWS Service(s) Selection (3 marks)

1. Select the most appropriate AWS service(s) for ASPT's requirement to store documents and videos accessible to registered users as pre-signed URLs.
2. Justify your choice by comparing different AWS storage services, considering scalability, performance, cost, security, and ease of implementation.
3. As ASPT head office is in Australia, what is the best AWS region to choose for S3 and IAM resources.
Support your answer with relevant explanations and diagrams (if any).

### c. AWS Cloud Interaction Strategy & sequence of creation of cloud resources (3 marks)

ASPT should follow AWS best practices to interact with AWS services.

1. Outline the various ways ASPT can interact with the AWS cloud, such as AWS Management Console, AWS Command Line Interface (CLI), and AWS Software Development Kits (SDKs).
2. For each role (Admin, Billing, Data Scientist, DB Admin, Dev Power User, Network Admin, Security Auditor, Support User, System Admin, and View Only Users), recommend the most suitable interaction method in a tabular form.
3. Additionally, propose the sequence of creation for AWS users (IAM User, IAM Groups, IAM Roles, and IAM Policies).
Justify your approach with a clear explanation and diagrams (if any).

### d. Storage Class Selection & Storage services identification (3 marks)

Considering ASPT storage needs as mentioned in Case-1.

1. If you recommend Amazon S3 as the storage option for ASPT. Which storage class would you suggest considering cost-saving, given their business need for only one availability zone in the Melbourne region?
2. Evaluate the various storage classes available in Amazon S3 and provide a detailed explanation for your choice.
3. Additionally, identify other AWS storage services, and explain why they were not suitable for
Justify your answer by giving an explanation and diagram(s) (if any).

### e. Software Development Methodology Recommendation (3 marks)

ASPT is evaluating software development methodologies.

1. Recommend an appropriate software development methodology for ASPT based on commonly used methodologies (e.g., Agile, Waterfall, DevOps, Lean etc.).
2. Justify your suggestion with appropriate reasoning, considering ASPT's business environment, project requirements, and goals.
3. Highlight the advantages and potential challenges of the recommended methodology.

## Solutions

### a. Cloud Service model recommendation. Consider factors to choose a region

**i) PaaS vs. SaaS Recommendation.** **Software as a Service (SaaS)** is more suitable since the requirement is hosting a static website and setting up a storage service for documents and videos. ASPT can consider Amazon S3 (Simple Storage Service) as a SaaS model. It has scalable object storage with high availability, durability, and security features. It also generates pre-signed URLs for registered users to access the stored documents and videos.

**ii) Benefits and Limitations**

- **PaaS Benefits.** Solutions like AWS Elastic Beanstalk abstract away the complexity of infrastructure management. They can focus on their application code and business logic. It offers automatic scaling based on traffic and usage. This simplifies application management and deployment.
- **PaaS Limitations.** Customization and control over the underlying infrastructure are limited compared to IaaS. It will not have the same level of flexibility for granular control over the environment.
- **SaaS Benefits.** Amazon S3 as a SaaS solution has high durability. It comes with built-in security features. It fulfills the use case of hosting documents and videos perfectly. Pre-signed URLs get generated for secure, time-limited access.
- **SaaS Limitations.** Advanced data processing and analytics require add-on services or integration. The setup and configuration are complex compared to PaaS. Requires operational overhead and attention to detail since ASPT will provision everything.

**iii) Factors for AWS Region Choice**

ASPT should consider factors such as availability in Melbourne and Sydney regions when selecting an AWS region for a specific service deployment.

1. **Proximity to Users.** Choose a region closest to ASPT's audience. This will reduce latency and improve the user experience. Consider the geographical location and potential user traffic patterns.
1. **Data sovereignty and compliance**. Different regions have varying data protection and compliance regulations. Ensure that the chosen region aligns with ASPT's legal and regulatory requirements.
1. **Service Availability.** Check if the required AWS service is available in the desired region. Each service is not guaranteed.
1. **Performance.** Test the network performance and availability of other AWS services that ASPT might use in conjunction with the chosen service.
1. **Redundancy and Disaster Recovery**: Consider the region's redundancy and disaster recovery capabilities. ASPT should aim for high availability and data durability.
1. **Costs.** Compare pricing across regions. Factor in the data transfer costs, storage costs, and other relevant expenses.
1. **Support and SLA** Review AWS support options and service level agreements (SLAs) for the chosen region.
1. **Future Growth.** ASPT should have room to expand without significant operational changes. Plan based on scalability and the potential for future growth in the chosen region.
1. **Resource Availability.** Assess the availability of skilled personnel and resources in the chosen region for managing and supporting the AWS services.

![Availability Zones in Australia](/blog/aws-case-study/1.webp "Availability Zones in Australia")

### b. AWS Service(s) Selection

**i) Most Appropriate AWS Service**

Amazon S3 (Simple Storage Service) is an obvious choice. As discussed above it has high durability to store large-scale data with pre-signed URLs. This means good scaling and security.

**ii) Justification and Comparison of AWS Storage Services**

- **Scalability.** Amazon S3 provides virtually unlimited scalability. allowing ASPT to store and retrieve any amount of data. It scales to accommodate growing storage needs. S3 maintains 11 9's data durability for objects over a span of one year.
- **Performance.** It is optimized for large-scale data storage and can handle a wide range of workloads. S3 offers excellent performance for data storage and retrieval, with low latency and high throughput.
- **Cost**: Amazon S3 offers a cost-effective storage solution with a pay-as-you-go pricing model. Storage classes, such as Standard, Intelligent-Tiering, Glacier, etc., will help ASPT pick a class based on data access patterns and cost requirements.
- **Security.** S3 Bucket policies and IAM (Identity and Access Management) policies take care of access controls. Pre-signed URLs are secure and will keep sensitive information within the organization's perimeter. They also time-limit the duration of object access. Data remains encrypted (both in transit and rest).
- **Ease of Implementation**: Setting up and configuring Amazon S3 is straightforward. Integration with other AWS services and applications is also seamless. ASPT only must create buckets to store their objects.

**iii) Best AWS Region for S3 and IAM Resources**

The best AWS region to choose for S3 and IAM resources would be the Sydney (ap-southeast-2) region.

- **Proximity.** Always go for a region geographically close to the head office (Australia). Users accessing the stored documents and videos will experience the lowest latency this way.
- **Compliance.** The Sydney region is compliant with Australian data protection and privacy regulations. This aligns with ASPT's location-specific legal requirements.
- **Availability.** This AZ offers high availability and redundancy, contributing to data durability and disaster recovery.
- **Data Residency.** Data residency requirements are met for sensitive documents and videos. The provisioned AZ and head office are in the same geographical area.
- **Local Support.** Local AWS support will support ASPT in the event of any issues.

![AWS S3 Architechture and Use Case](/blog/aws-case-study/2.webp "AWS S3 Architechture and Use Case")

### c. AWS Cloud Interaction Strategy & sequence of creation of cloud resources

**i) Ways to Interact with AWS Cloud:**

ASPT can interact with the AWS cloud using [steps outlined here](https://docs.aws.amazon.com/rekognition/latest/dg/setup-awscli-sdk.html) through:

1. **AWS Management Console** is a web-GUI to handle AWS resources. User-friendly and suitable for non-IT employees at ASPT.
1. **AWS Command Line Interface (CLI)**. It provides scripting capabilities and is efficient for repetitive tasks. All interactions are done via the terminal.
1. **AWS Software Development Kits (SDKs)** gets integrated into programming languages. This means ASPT engineers can make custom apps that invoke AWS services.

**ii)**

|**Role**|**Suggested Interaction Method**|
| :-: | :-: |
|Admin|Console, CLI, SDKs|
|Billing|Console, CLI|
|Data Scientist|CLI, SDKs|
|DB Admin|Console, CLI, SDKs|
|Dev Power User|CLI, SDKs|
|Network Admin|Console, CLI, SDKs|
|Security Auditor|Console, CLI|
|Support User|Console, CLI|
|System Admin|Console, CLI, SDKs|
|View Only Users|Console|

**iii) Sequence of Creation for AWS Users (IAM User, IAM Groups, IAM Roles, and IAM Policies)**

![User Creation Flow](/blog/aws-case-study/3.webp "User Creation Flow")

1. Define IAM policies first. They establish a clear and controlled permission structure. Permissions are well-defined and can be managed and audited.
2. Then IAM Group should be set up. Permissions are assigned at the group level rather than individually. Post this ASPT can grant or revoke access for specific roles.
3. Third step is to define IAM users and associate them with groups. They will automatically inherit the appropriate permissions based on their roles. It also simplifies the onboarding and offboarding processes.
4. IAM roles are created after IAM users and groups. It requires a detailed understanding of the user and group structure and hence should be the last step. They are often used for specific applications, services, or cross-account access.  

ASPT can establish a structured, efficient access control mechanism, manage permissions efficiently, and align access with users' roles and responsibilities by following this sequence.

### d. Storage Class Selection & Storage services identification

**i) Recommended Amazon S3 Storage Class**

Documents and videos are to be stored only in one availability zone (Melbourne). Hence, the most cost-effective storage class is **S3 One Zone-IA" (Infrequent Access)**.

![Storage Class Options](/blog/aws-case-study/4.webp "Storage Class Options")

**ii) Evaluation and Explanation of Storage Class Choice**

The choice of storage class depends on the frequency of access and availability. In this case, One Zone-IA is suitable because:

1. **Cost-Saving**. The storage costs are lower compared to other classes like S3 Standard or Intelligent Tiering. Since ASPT specifies only one availability zone, using this storage class means better cost savings.
2. **Availability Consideration**. Data replication inside the availability zone ensures durability even when the data is in a single zone. The risk is that, in comparison to classes that replicate over many zones, this class is more susceptible to data loss in the event of an AZ failure.
3. **Infrequent Access**. Suitable for data that is rarely accessed but requires quick retrieval when needed. Because ASPT requires registered users to have pre-signed URLs, S3 One Zone-IA balances cost reductions with tolerable access times.

**iii) Other AWS Storage Services and Their Suitability for Case-1**

- **Amazon Glacier** is applicable for archived data. It is one of the cheapest storage services designed for long-term data retention. When compared to other storage types, retrieval times are longer. Amazon Glacier is not the greatest fit for ASPT since it does not offer the required pre-signed URLs and quick access.
- **EBS (Elastic Block Store)** has block-level storage volumes that can be attached to EC2 instances. For storing data directly accessed by EC2 instances, it is practical. Not the best fit for pre-signed URLs.
- **EFS (Elastic File System)** offers scalable and managed file storage for use with EC2 instances. It's designed for applications that need shared file storage. Not optimal for ASPT’s use case.

One Zone-IA is a cost-saving storage solution suitable for documents and videos, offering rapid retrieval and pre-signed URLs. It fulfills ASPT's requirement for a single availability zone.

### e. Software Development Methodology Recommendation

**i) Recommended Software Development Methodology**

Agile is most suitable to migrate ASPT's static website hosting to AWS Cloud in the first phase.

**ii) Justification**

- [Agile promotes a methodical, incremental approach to development](https://ccaps.umn.edu/story/agile-methodology-advantages-and-disadvantages). This is appropriate for the strategy of gradual migration. Component migration must be carried out in small, manageable phases.
- It places a strong emphasis on flexibility and adaptability to shifting needs. Based on the changing cloud environment and technical factors, ASPT may need to modify its strategy.
- Encourage team members to communicate and work together continuously. This is essential for handling any difficulties that might emerge throughout the migration procedure.
- ASPT can clearly observe the progress being made toward finishing the migration phases. This promotes openness and upholds stakeholder trust.
- Early risk detection and minimization are possible with Agile. Potential issues will be resolved in real time by ASPT. Minimizes the likelihood of serious issues during the relocation.

![Suggested Agile Workflow for ASPT](/blog/aws-case-study/5.webp "Suggested Agile Workflow for ASPT")

**iii)**

**Advantages of Agile**

- Agile's incremental methodology guarantees the delivery of useful components sooner.
- It promotes routine reflection. ASPT can refine the migration process by learning from each iteration.
- Stakeholder collaboration and communication on a regular basis improves alignment and satisfaction.
- ASPT can adjust to changing conditions, technological improvements, and evolving business requirements. This is the fundamental idea.

**Potential Challenges**

- For team members who are inexperienced with Agile, training, and changes are necessary.
- Due to the iterative nature of projects, proper scope management is required to avoid "scope creep" and guarantee project objectives are met.
- All project stakeholders must actively participate and collaborate according to this process. This results in an increase in managerial workload.
