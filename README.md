# Reddit End-to-End Data Engineering Project

## 📌 Introduction

This project demonstrates a complete end-to-end data engineering pipeline using Reddit's public API. It extracts meme-related posts from the Reddit `r/memes` subreddit, stores them in Amazon S3, processes and transforms the data using AWS Lambda, and finally makes it queryable using **Snowflake** (previously Athena). The entire pipeline is built using serverless and cloud-native tools, making it scalable and cost-effective.

---

## 📊 Architecture

![pipeline](https://github.com/user-attachments/assets/ea3eced0-3700-4e6a-9f55-2917179ca03a)

* **Extract**: Triggered by AWS CloudWatch, a Lambda function fetches data from Reddit API and stores it in the raw S3 bucket.
* **Transform**: Another Lambda function is triggered on object creation in the raw S3 bucket. It cleans and transforms the data, then stores it in a separate S3 path for processed data.
* **Load**: The transformed data is automatically ingested into Snowflake using Snowpipe. A defined file format, stage, and pipe handle the loading process. The data is then available for querying in a structured table.

---

## 🔍 About the API/Dataset

The Reddit API allows developers to programmatically access data from various subreddits. In this project, we extract the top 10 hot posts from the `r/memes` subreddit, including:

* Post ID
* Title
* Author
* Score (upvotes)
* Number of Comments
* Time of Creation
* Post URL

📚 **Reddit API Documentation**
👉 [https://www.reddit.com/dev/api/](https://www.reddit.com/dev/api/)

---

## 🛠️ AWS & Snowflake Services Used

* **AWS Lambda**: For both data extraction and transformation.
* **Amazon S3**: Storage for raw and transformed data.
* **Amazon CloudWatch**: Scheduled trigger for the extraction Lambda.
* **Amazon SNS/S3 Trigger**: Event-based trigger for Snowpipe.
* **Snowflake**: Cloud data warehouse used to store and query the final dataset.

  * **Storage Integration**: Connects Snowflake securely to S3.
  * **File Format**: Defines how Snowflake reads the CSV files.
  * **External Stage**: Points to the S3 path for transformed data.
  * **Snowpipe**: Automatically loads new data from S3 into the target table.
  * **Data Table**: Stores the Reddit data in a queryable format.

---

## 🧪 Example Snowflake Queries

```sql
-- Total number of posts
SELECT COUNT(*) FROM reddit.public.data;

-- Top 10 most upvoted posts
SELECT Title, Author, Score
FROM reddit.public.data
ORDER BY Score DESC
LIMIT 10;

-- Posts per day
SELECT DATE_TRUNC('DAY', Time_of_Creation) AS Post_Date, COUNT(*) AS Total_Posts
FROM reddit.public.data
GROUP BY Post_Date
ORDER BY Post_Date;
```

---

## 📦 Install Packages (for local development or packaging Lambda layer)

```
pip install praw pandas
```

