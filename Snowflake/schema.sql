create database reddit;

create or replace file format reddit.public.csv_fileformat
    type=csv 
    field_delimiter=','
    skip_header=1
    null_if=('','NULL','null')
    trim_space=true
    empty_field_as_null=true
    field_optionally_enclosed_by='"';

create or replace stage reddit.public.aws_stage
    url='s3://reddit-etl-project-vikas02/transformed_data/reddit_data/'
    storage_integration=s3_connect
    file_format=reddit.public.csv_fileformat;

create or replace table reddit.public.data(
    Id string,
    Title string,
    Author string,
    Score int,
    Number_of_Comments int,
    Time_of_Creation timestamp_tz,
    URL string
);