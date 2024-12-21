#!/bin/bash
# Deploy Cloud Function
gcloud functions deploy aws-style-function \
    --runtime python39 \
    --trigger-event providers/cloud.firestore/eventTypes/document.create \
    --trigger-resource projects/your-project-id/databases/(default)/documents/aws_style_sales/{documentId} \
    --entry-point transform_sales_data \
    --region us-central1 \
    --source ../cloud_function
