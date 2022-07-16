select customer_id, count(*) as count_no_trans
from visits v left join transactions t
on v.visit_id = t.visit_id
where amount is null
group by customer_id;
