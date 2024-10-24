# PATIENT ALERT ETL 
![th](https://github.com/user-attachments/assets/22cfb8fe-21fd-4d04-b631-8e55753030c2)

## Healthcare IoT Real-Time Alert System
### This project demonstrates the development of a Real-Time Alert Notification System for monitoring vital health parameters using data pipelines. It leverages streaming data from IoT devices in hospitals and health centers to trigger real-time alerts when patients' vital signs (such as body temperature, heartbeat, blood pressure, etc.) fall outside predefined thresholds. The solution utilizes a combination of Apache Kafka, Apache Spark, Hive, HBase, Sqoop, and Amazon SNS for end-to-end data processing and alerting.

## Project Overview
### The rise of IoT in healthcare has enabled continuous monitoring of patient vitals in real-time. This repository contains the implementation of a robust and scalable data pipeline designed to capture, store, and process high-velocity IoT data. The system monitors patient data and sends alerts to medical professionals whenever vitals deviate from normal ranges, ensuring timely interventions and improved patient care.

## Features:
1.  Real-time Data Ingestion: Stream patient vital signs from IoT devices using Apache Kafka.
2.  Stream Processing & Analytics: Use Apache Spark (PySpark) to process real-time data and compare it with reference thresholds.
3.  Reference Data Storage: Store threshold values for vital signs in HBase for quick lookups during stream processing.
4.  Data Storage: Store processed and raw data in Hive for historical analysis and reporting.
5.  Alert Notifications: Trigger email notifications via Amazon SNS when vitals exceed normal ranges.
6.  Data Import/Export: Use Apache Sqoop to move data between RDBMS and Hadoop/Hive ecosystems.

## Architecture
![338f6aac-9db0-44e6-bfb9-8f891d9dc992-Capture1](https://github.com/user-attachments/assets/30f943fa-854b-4157-b769-5ad9f17f43ba)
### IoT Data Ingestion: IoT devices continuously push vital signs data (e.g., temperature, heart rate, BP) into Kafka topics.
Real-Time Stream Processing: Spark Streaming reads data from Kafka, processes the stream, and checks whether vitals cross the thresholds stored in HBase.
Alerts: If any vital parameter exceeds its threshold, the system triggers an alert notification to the registered email using Amazon SNS.
Data Storage: Processed records are saved in Hive for long-term storage and batch analysis.
Data Management: Sqoop is used to import/export patient data between relational databases (RDS/MySQL) and the Hadoop ecosystem.

## Technologies Used:
Apache Kafka: Distributed streaming platform for real-time data ingestion.
Apache Spark (PySpark): Real-time data processing and analytics.
Apache HBase: NoSQL database for storing reference threshold data.
Hive: Data warehouse system for structured data storage and querying.
Sqoop: Tool for data import/export between RDBMS and Hadoop.
Amazon SNS: Simple Notification Service for sending email alerts.
HDFS: Distributed file system for storing large volumes of data.
## Installation and Setup

### Prerequisites:
#### Java 8 or higher, Python 3.x, Apache Kafka, Apache Spark, Hadoop (HDFS), Hive, HBase, Sqoop, AWS Account for SNS, MySQL (or any RDBMS for patient records)

### Steps to Set Up:
->   Kafka Setup:
      1.  Install and configure Kafka.
      2.  Create Kafka topics for vital signs data.
->   HBase Setup:
      1.  Install HBase and create a table for storing threshold reference data.
->   Spark Streaming Setup:
      1.  Install Spark and set up streaming jobs to read from Kafka and process data.
->  Hive Setup:
      1.  Set up Hive to store patient vital data.
->  Sqoop Setup:
      1.  Install Sqoop to import/export data between MySQL and Hive.
->  SNS Setup:
      1.  Configure AWS SNS for sending alert notifications via email.

## Usage
  ### Start Kafka Producer: Send simulated patient data to Kafka.
  ### Run Spark Streaming Job: Process the incoming data stream and monitor vital signs.
  ### Monitor Alerts: Receive real-time alerts for abnormal vitals via email.
  ### Query Hive: Analyze stored patient data in Hive for trends and historical insights.

## Contributing
### Contributions are welcome! If you have suggestions for improvements or new features, feel free to create an issue or submit a pull request.

## FINAL OUTPUT ACHIEVED:
![image](https://github.com/user-attachments/assets/92c5bb00-f129-4258-9da6-50ffda61dc0b)

License
This project is licensed under the MIT License - see the LICENSE file for details.

