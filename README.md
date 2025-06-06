# Reddit End-to-End Data Engineering Project

## 📌 Introduction
This project demonstrates a complete end-to-end data engineering pipeline using Reddit's public API. It extracts meme-related posts from the Reddit `r/memes` subreddit, stores them in Amazon S3, processes and transforms the data using AWS Lambda, and finally makes it queryable using AWS Athena. The entire pipeline is built using serverless services, making it scalable and cost-effective.

---

## 📊 Architecture
![pipeline](https://github.com/user-attachments/assets/ea3eced0-3700-4e6a-9f55-2917179ca03a)


- **Extract**: Triggered by AWS CloudWatch, a Lambda function fetches data from Reddit API and stores it in the raw S3 bucket.
- **Transform**: Another Lambda function is triggered on object creation in the raw S3 bucket. It cleans and transforms the data, then stores it in a separate S3 path for processed data.
- **Load**: AWS Glue Crawler detects schema and creates tables in the Data Catalog. Athena is used to query the transformed data.

---

## 🔍 About the API/Dataset

The Reddit API allows developers to programmatically access data from various subreddits. In this project, we extract the top 10 hot posts from the `r/memes` subreddit, including:

- Post ID
- Title
- Author
- Score (upvotes)
- Number of Comments
- Time of Creation
- Post URL

### 📚 Reddit API Documentation  
You can learn more about the Reddit API here:  
👉 [https://www.reddit.com/dev/api/](https://www.reddit.com/dev/api/)

---

## 🛠️ AWS Services Used

- **AWS Lambda**: For both data extraction and transformation.
- **Amazon S3**: Storage for raw and transformed data.
- **Amazon CloudWatch**: Scheduled trigger for the extraction Lambda.
- **AWS Glue**: Crawler to create schema and table metadata.
- **AWS Athena**: Query engine to analyze the data.

---

## 📦 Install Packages (for local development or packaging Lambda layer)
```
- pip install praw pandas
```
