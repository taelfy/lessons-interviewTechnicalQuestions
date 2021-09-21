select
  *
from
  (
    select
      sales_id
      ,sum(amount) as total_amount
    from
      sales
    where
      to_char(sales_date,'yyyy-01-01') = '2020-01-01'
    group by
      sales_id
  ) a
where
  a.total_amount =
  (
    select
      max(b.total_amount)
    from
      (
        select
          sales_id
          ,sum(amount) as total_amount
        from
          sales
        where
          to_char(sales_date,'yyyy-01-01') = '2020-01-01'
        group by
          sales_id
      ) b
  )