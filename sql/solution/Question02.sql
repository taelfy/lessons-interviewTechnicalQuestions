select
  id
  ,amount
  ,customer_id
  ,load_datetime
from
  (
    select
      id
      ,amount
      ,customer_id
      ,load_datetime
      ,row_number() over (PARTITION BY id order by load_datetime desc) as row_number_rank
    from
      customer_sales
  ) a
where
  row_number_rank = 1;