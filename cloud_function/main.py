from google.cloud import storage
import json

# Initialize Cloud Storage client
storage_client = storage.Client()

def transform_sales_data(event, context):
    """Process Firestore changes, transform the data, and store it in Cloud Storage."""
    # Extract Firestore document data
    sales_record = event['value']['fields']

    # Transform the data
    transformed_data = {
        'orderid': sales_record['orderid']['stringValue'],
        'product_name': sales_record['product_name']['stringValue'],
        'quantity': int(sales_record['quantity']['integerValue']),
        'price': float(sales_record['price']['doubleValue']),
        'total': int(sales_record['quantity']['integerValue']) * float(sales_record['price']['doubleValue'])
    }

    # Save transformed data to Cloud Storage
    bucket = storage_client.bucket('aws-style-bucket')
    blob = bucket.blob(f"orders/{transformed_data['orderid']}.json")
    blob.upload_from_string(json.dumps(transformed_data))
    print(f"Processed and stored: {transformed_data}")
