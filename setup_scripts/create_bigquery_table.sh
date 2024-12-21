#!/bin/bash
# Create BigQuery dataset
bq mk --dataset --location=us-central1 aws_style_dataset

# Create BigQuery external table
bq mk --external_table_definition=aws_style_table \
    format=JSON \
    uris=gs://aws-style-bucket/orders/*.json \
    aws_style_dataset.aws_style_table
