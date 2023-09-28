---
title: "AWS Security Best Practices: A Case Study on IAM"
date: 2023-09-25T15:19:34+05:30
draft: false
cover: 
    image: blog/aws/iam-case-study.webp
    alt: IAM Case Study
    caption: "Master AWS security with insights into responsibilities, IAM, access, and protection" 
description: "Learn AWS security best practices, including customer responsibilities, IAM risks, secure access to services, root account safeguarding, and credential management."
tags: ["aws"]
---

## Case Study Scenario

Aus Global Financial Services (AGFS) is a renowned financial service provider with a 50-year legacy, operating in 20 countries with multiple currencies. AGFS is currently setting up its dynamic website on AWS using EC2 instances running under a Load Balancer. All critical documents will be stored in the S3 bucket named "agfs-docs-bucket." Considering Sydney as multi- availability zone AWS region, for fail-over point of view, at least one EC2 instance is recommended to use in every availability zone in Sydney region (ap-southeast-2). AGFS emphasizes security and is committed to implementing robust security measures before migrating to the cloud. As an AWS professional working for AGFS, your task is to address the following questions, which will challenge your critical thinking and self-reflection skills.
You task is to answer the following questions:

### a. AWS and Customer Responsibilities

The shared responsibility model is a crucial concept in AWS cloud security. Analyse AGFS's business needs and critically assess the division of responsibilities between AWS and AGFS for the following 6 points individually.

1. Data should be encrypted on the client side.
2. Data should be protected in transit.
3. Hardware should be safe.
4. All Edge locations should be secure.
5. Guest operating system and application should be patched properly.
6. AGFS employees must be trained on AWS skills.
Present your recommendations in tabular form.

### b. IAM Best Practices and Cross-Account Access

IAM plays a pivotal role in cloud security and allows you to control access to your AWS resources.

1. Evaluate the significance of IAM in managing access control and fostering a security-centric culture at AGFS for managing IAM users, groups, roles, and policies.
2. Self-reflect on the challenges that AGFS might encounter while implementing IAM best practices across multiple AWS accounts (Production, UAT, and Development), where Production AWS account is the consolidated account.
3. Propose innovative solutions for granting cross-account access while ensuring the principle of least privilege.
Support your response with real-world examples, self-reflection, and diagrams.

### c. Securely Accessing AWS Services

Security in the AWS cloud is AGFS’s high priority.

1. Examine various methods AGFS web developers can use his access keys to interact with AWS services.
2. Critically assess the potential risks associated with each approach and reflect on the trade-offs between convenience and security.
3. As an AWS professional, propose advanced strategies for securely providing AWS credentials to web servers deployed on EC2 instances with a load balancer across multiple availability zones in Sydney region.
Support your response with self-reflection, cutting-edge practices, and relevant diagrams.

### d. Safeguarding Root Account and Admin Roles

AGFS has users with various roles.

1. Reflect on the significance of protecting the AWS root account and Admin roles (Console users) to maintain the highest level of security at AGFS.
2. Do AGFS needs to create access keys for a root user, if so do the need to rotate the access keys.? 3. What are the key differences between IAM roles and IAM users, and in what scenarios would you use one over the other for Admin roles?
Support your response with a deep understanding of security principles, self-reflection, and relevant diagrams (if any).

### e. IAM Access and Credential Management

AGFS is storing all critical documents on S3.

1. Critically evaluate AGFS's approach to configure the "agfs-docs-bucket" S3 bucket as a static website hosting.
2. Reflect on the implications of granting IAM access to different AWS Accounts (Pro, UAT, and Dev).
3. Differentiate Credential files and Credential profiles, which one you recommend AGFS to access different AWS accounts (mentioned in ii) in the company.
Support your response with self-reflection, innovative solutions, and relevant examples including diagrams (if any).

## Solutions

### a. AWS and Customer Responsibilities

|**Security Point**|**AWS Responsibilities**|**AGFS Responsibilities**|
| :-: | :-: | :-: |
|Encrypt data on client side|Provide tools and services for encryption and key management.|Achieve client-side encryption using appropriate tools and manage encryption keys. Use AWS Key Management Service.|
|Data should be protected in transit.|Provide encryption options for data in transit between services.|Set encryption settings and protocols for data in transit.|
|Hardware should be safe.|Ensure physical security of data centers and server hardware.|Implement access controls, firewalls, and physical security measures for EC2 instances and other assets.|
|Secure all Edge locations.|Secure and maintain the edge locations and CDN infrastructure.|Configure security settings and firewall rules for AGFS's applications and services deployed at edge locations.|
|Patch Guest OS and application.|Provide patches and updates for underlying infrastructure.|Regularly apply patches and updates to the operating system and applications running on EC2 instances.|
|AGFS employees must be trained on AWS skills.|Offer AWS training resources, certifications, and documentation.|<p>Ensure AGFS employees undergo training to understand AWS services, security practices, and best practices for cloud usage.  <https://docs.aws.amazon.com/>, <https://aws.amazon.com/certification/></p>|

### b. IAM Best Practices and Cross-Account Access

i) [Identity and Access Management](https://aws.amazon.com/iam/resources/best-practices/) manages access control and fosters a security-centric culture. AGFS needs it for:

- **Granular Access Control.** AGFS can define fine-grained permissions for users, groups, and roles. This guarantees that each entity only has access to the resources and actions required for fulfilling its function. decreases the possibility of unauthorized access or unintentional data leakage.
- **Principle of least privilege.** IAM ensures that individuals and programs have the bare minimum of access necessary to do their tasks. By doing this, the potential harm from a security breach or configuration error is reduced.
- **Audit and Accountability.** With logging and monitoring via IAM, AGFS can keep track of who used which resources and when. Investigating security incidents is made easier by this.
- **Centralized Management.** IAM is a unified control point for security policies. AGFS can centrally manage access across a variety of AWS services and accounts.
- **Security Culture.** It encourages employees to adopt secure access practices and reinforces the importance of data protection.

![IAM and Security Implementation](/blog/aws-case-study/6.webp "IAM and Security Implementation")

ii) It might be difficult to implement IAM best practices across several  AWS accounts, particularly in the case of consolidated production accounts.

- It is challenging to manage IAM roles and policies across multiple accounts. increased chance of errors or oversights.
- Planning is necessary to coordinate access across several accounts (such as development and production) while retaining the separation of roles.
- Consistency in IAM policies and practices might lead to security flaws or inconsistent behaviors.
- It takes time to manage users and roles across many accounts while ensuring appropriate access and permissions.

iii) To grant cross-account access while adhering to the principle of least privilege, AGFS should:

- Group accounts together with **AWS Organizations** into a hierarchy. To enforce consistent security standards across accounts, use service control policies (SCPs).
- Trusted entities from one account can take on roles in another thanks to **cross-account roles**. For further security, use external IDs.
- Grant access based on user attributes and conditions using **attribute-based access control**. Choose permissions that are more dynamic and context-sensitive.
- Use **AWS SSO** to manage access to numerous accounts and applications from a single location User provisioning and access management are made easier as a result.
- **Tools or scripts** for automating the creation and management of cross-account IAM roles on demand. Reduce manual labor and maintain uniformity.
- Apply **MFA requirements** for cross-account access to increase security.

A cross-account role can be used by the AGFS development team to gain temporary access to resources in use, guaranteeing restricted rights and limited permissions. To maintain security and compliance and to strike a balance between operational effectiveness and security, IAM policies across accounts must undergo regular audits and reviews.

### c. Securely Accessing AWS Services

i) AGFS web developers can use access keys to interact with AWS services through -

- Developers instantly include access keys into the software code. The ability to connect to AWS services is made possible by this.
- Set access keys as environment variables on the server where the program is running. The software then reads these variables to authenticate with AWS.
- To interact with AWS services, developers need SDKs (Software Development Kits). Using the SDKs, access keys can be configured programmatically or using configuration files.
- EC2 instances can be given IAM roles. This provides programs running on the instance with temporary credentials without requiring access keys to be controlled directly.

ii) Potential risks and trade-offs associated with:

|**Access Method**|**Risk Level**|**Notes**|
| :-: | :-: | :-: |
|Hardcoding Keys|High|Easily exposed if code is shared or leaked|
|Environment Variables|Moderate|Slightly better, still susceptible|
|AWS SDK|Moderate|More secure than hardcoding, still vulnerable|
|Instance Profiles|Lower|Eliminates direct key management, EC2 risk|

iii) Advanced strategies for securely providing AWS credentials to web servers deployed on EC2 instances in the Sydney region:

- **AWS Secrets Manager.** The application retrieves credentials from Secrets Manager when needed. Reduced exposure and ensured regular rotation of keys.
- **IAM Roles with Short Durations**. Instead of using instance profiles, use IAM roles with short-duration sessions. This limits the time an application has access to AWS services, reducing the attack surface.
- **Temporary Security Tokens**. Security Token Service (STS) generates temporary security tokens for web servers. They have a limited lifespan and can be obtained using instance metadata or an identity broker.
- **SSO and Identity Federation**. It allows web servers to assume roles in multiple accounts without the need for long-lived access keys.

As an AWS professional, I emphasize the need for a balance between developer convenience and security. Convenient methods like hardcoding and environment variables can introduce security risks. Modern AWS services like Secrets Manager can enhance AGFS's cloud infrastructure, and regular security assessments and continuous education are crucial.

![EC2 Protection with AWS Security Services](/blog/aws-case-study/7.webp "EC2 Protection with AWS Security Services")

### d. Safeguarding Root Account and Admin Roles

i) Safeguarding the AWS root account and Admin roles (Console users) is of paramount importance for maintaining the [highest level of security](https://docs.aws.amazon.com/accounts/latest/reference/best-practices-root-user.html) at AGFS:

- **Root Account Protection.** The root account has unrestricted access to all AWS resources and services. If compromised, it could lead to a complete compromise of the entire AWS environment. Enforce multi-factor authentication (MFA), limit root account usage, and delegate day-to-day tasks to individual IAM users or roles for maximum protection.
- **Admin Role Security.** These roles grant significant permissions within the AWS environment. Only authorized personnel can make critical changes and access sensitive resources. Proper role separation, least privilege principles, and regular review of permissions are good security strategies to prevent unauthorized access.

ii) AGFS should not create access keys for the root user. AWS strongly recommends not using access keys for the root account due to the high level of privilege associated with it. Access keys are long-term credentials that can be easily compromised. Using them with the root account increases the attack surface and potential impact of a security breach.

If access keys were inadvertently created for the root user, it is advisable to rotate them regularly. These are the best practices for access key management.

iii) Key differences between [IAM roles and IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html)

- **IAM Users**
  - Individual identities with distinct permissions.
  - Suitable for users who require long-term access to AWS resources. E.g., developers, administrators, or other personnel.
  - Often used for human users who need console access and programmatic access.
- **IAM Roles:**
  - These are credentials for temporary security that reputable entities can use. E.g., EC2 instances, AWS services.
  - Suitable for granting permissions to applications, services, or processes that need to interact with AWS resources without the need for long-lived credentials.
  - Applicable for serverless applications, EC2 instances, Lambda functions, or cross-account access scenarios.

IAM users with well-defined and restricted rights are more suitable for Admin jobs. For admins who need console access, IAM users provide more granularity. IAM roles, on the other hand, prove useful for temporary access where credentials are needed for a particular action or scenario. Examples include app deployment or data processing.

As an AWS professional, I would prioritize securing root account and Admin roles, adhering to best practices, monitoring permissions, and following the principle of least privilege to maintain a secure AWS environment.

### e. IAM Access and Credential Management

i) **Configuring "agfs-docs-bucket" S3 Bucket as a Static Website Hosting**

AGFS's approach to configuring the S3 bucket as a static website hosting for [https://www.agfs.com.au](https://www.agfs.com.au/) is a secure and cost-effective method. With S3's static hosting, AGFS can serve the website directly from the S3 bucket. Benefits of S3 (high availability, scalability, and reduced operational overhead) carry over. Web hosting architecture is simplified and there is no need for traditional web server management.

Bucket object permissions need to be set to private. Access controls will prevent unauthorized access to sensitive documents. Implementing IAM and bucket policies will restrict access to only authorized users or roles. Non-internal entities won't be able to access bucket objects even with the public URL.

ii) **Implications of Granting IAM Access to Different AWS Accounts**

- While this may allow AGFS to segregate environments and manage permissions well, it also presents challenges.
- It might be difficult to manage IAM roles and permissions across many accounts. requiring careful coordination and uniform rules.
- Harder to ensure effective governance and auditing of access and permissions when managing many accounts.
- IAM roles permit safe cross-account access, but their setup and management demand careful configuration.

iii) **Credential Files vs. Credential Profiles**

1. **Credential Files** are JSON-formatted files that store AWS credentials, including access keys, secret access keys, and session tokens. AWS CLI and SDKs use it to authenticate requests to AWS services.
1. **Credential Profiles** are named configurations within credential files. They allow users to store multiple sets of credentials for different AWS accounts or regions. Each profile can contain different access keys, secret access keys, and session tokens.

For accessing various AWS accounts, I would recommend using **credential profiles within credential files**. Developers will transition between accounts and environments without changing their code or scripts. Transient session tokens acquired via IAM roles improve overall security. Since AGFS configures S3 static website hosting and focuses on strict access, bucket objects cannot be set to public. A more practical and systematic method of controlling access to various accounts is provided by credential profiles within credential files.
