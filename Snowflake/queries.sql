-- Total Rows
SELECT COUNT(*) FROM reddit.public.data;

-- Top 10 most upvoted posts
select title, author, score from reddit.public.data
order by score desc
limit 10;

-- Three most commented posts
select title, number_of_comments from reddit.public.data
order by number_of_comments desc
limit 3;

-- Top authors by total score
select author, sum(score) total_score from reddit.public.data
group by author
order by total_score desc;


-- Posts per day
select day(time_of_creation) day,count(*) total_posts from reddit.public.data
group by day
order by day;


-- Posts containing specific keywords like 'you'
select * from reddit.public.data
where title ilike '%you%';