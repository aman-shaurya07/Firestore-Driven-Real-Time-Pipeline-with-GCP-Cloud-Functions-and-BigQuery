# Firestore-Driven Real-Time Pipeline with GCP Cloud Functions and BigQuery

This project demonstrates a real-time data processing pipeline on Google Cloud Platform (GCP) using **Firestore** as the entry point. The pipeline ingests sales data, processes and transforms it using Cloud Functions, and stores the transformed data in Cloud Storage for analytics via BigQuery.

---

## **Architecture Overview**

1. **Mock Data Generator**: Simulates real-time sales data ingestion directly into Firestore.
2. **Firestore**: Serves as the NoSQL database to store raw sales data.
3. **Cloud Function**: Processes Firestore data changes, transforms the data, and stores it in Cloud Storage.
4. **Cloud Storage**: Stores transformed JSON files for further analysis.
5. **BigQuery**: Queries the transformed data in Cloud Storage for insights.

---

### **Architecture Flow**

```plaintext
          +---------------------------+
          |    Mock Data Generator    |
          | (Python Script writing to |
          |  Firestore directly)      |
          +---------------------------+
                     |
                     v
          +---------------------------+
          |      Firestore DB          |
          |  (Stores raw sales data)   |
          +---------------------------+
                     |
                     v
          +---------------------------+
          |     Cloud Function         |
          | (Triggered by Firestore    |
          |  document changes)         |
          +---------------------------+
                     |
                     v
          +---------------------------+
          |      Cloud Storage         |
          | (Stores transformed data) |
          +---------------------------+
                     |
                     v
          +---------------------------+
          |        BigQuery            |
          | (Queries transformed data)|
          +---------------------------+



## Setup Instructions

### Prerequisites
1. Google Cloud SDK installed and authenticated.
2. Python 3.9 or later installed.
3. Enabled the following GCP APIs:
    - Cloud Functions
    - Firestore
    - Cloud Storage
    - BigQuery



### Deployment Steps

#### Step 1: Set Up Firestore
```bash
bash setup_scripts/create_firestore.sh
```


#### Step 2: Set Up Cloud Storage
```bash
bash setup_scripts/create_storage.sh
```

#### Step 3: Deploy the Cloud Function
```bash
bash setup_scripts/deploy_cloud_function.sh
```

#### Step 5: Set Up BigQuery
```bash
bash setup_scripts/create_bigquery_table.sh
```

#### Step 6: Generate Mock Data
```bash
python3 mock_data_generator/mock_data_generator.py
```
