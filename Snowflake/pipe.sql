create or replace pipe reddit.pipes.data_pipe
auto_ingest=true 
as 
copy into reddit.public.data
from @reddit.public.aws_stage;

desc pipe reddit.pipes.data_pipe;

create or replace schema reddit.pipes;

create or replace pipe reddit.pipes.data_pipe
auto_ingest=true 
as 
copy into reddit.public.data
from @reddit.public.aws_stage;

desc pipe reddit.pipes.data_pipe;