import json
import os
import boto3
import praw
from datetime import datetime, timezone

def lambda_handler(event, context):
    reddit_client_id = os.environ.get('reddit_client_id')
    reddit_client_secret = os.environ.get('reddit_client_secret')
    reddit_user_agent = os.environ.get('reddit_user_agent')

    reddit = praw.Reddit(
        client_id=reddit_client_id,
        client_secret=reddit_client_secret, 
        user_agent=reddit_user_agent
    )

    subreddit = reddit.subreddit('memes') 
    post_list = []

    for post in subreddit.hot(limit=100):
        created_time = datetime.fromtimestamp(post.created_utc, tz=timezone.utc)
        created_at = created_time.strftime('%Y-%m-%d %H:%M:%S UTC')
        post_element = {
            'id': post.id, 
            'Title': post.title,
            'Author': str(post.author),
            'Score': post.score,
            'Number of Comments': post.num_comments,
            'Time of Creation': created_at,
            'URL': post.url
        }
        post_list.append(post_element)
    
    s3 = boto3.client('s3')
    file_name = 'reddit_raw_'+datetime.now().strftime('%Y%m%d%H%M%S')+'.json'
    s3.put_object(
        Bucket='reddit-etl-project-vikas02',
        Key='raw_data/to_process/' + file_name,
        Body=json.dumps(post_list)  
    )
    
