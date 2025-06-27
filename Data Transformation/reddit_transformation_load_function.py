import json
import boto3
from datetime import datetime
import pandas as pd
from io import StringIO

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = 'reddit-etl-project-vikas02'
    prefix = 'raw_data/to_process/'


    raw_files = [
        obj['Key']
        for obj in s3.list_objects(Bucket=bucket, Prefix=prefix)['Contents']
        if obj['Key'].endswith('.json')
    ]

    s3_resource = boto3.resource('s3')
    processed_prefix = 'raw_data/processed/'

    for file_key in raw_files:

        response = s3.get_object(Bucket=bucket, Key=file_key)
        content = response['Body'].read().decode('utf-8')
        post_list = json.loads(content)


        post_df = pd.DataFrame(post_list)
        post_df['Time of Creation'] = pd.to_datetime(post_df['Time of Creation'])

        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        transformed_key = f'transformed_data/reddit_data/reddit_transformed_{timestamp}.csv'
        csv_buffer = StringIO()
        post_df.to_csv(csv_buffer, index=False)
        s3.put_object(
            Bucket=bucket,
            Key=transformed_key,
            Body=csv_buffer.getvalue()
        )


        copy_source = {'Bucket': bucket, 'Key': file_key}
        processed_key = processed_prefix + file_key.split('/')[-1]
        s3_resource.meta.client.copy(copy_source, bucket, processed_key)
        s3_resource.Object(bucket, file_key).delete()

