#!/bin/bash
# Create Cloud Storage bucket
gcloud storage buckets create gs://aws-style-bucket \
    --location=us-central1

# Enable versioning (optional)
gcloud storage buckets update gs://aws-style-bucket --versioning
