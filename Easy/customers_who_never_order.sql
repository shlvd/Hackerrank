select name as Customers
from Customers left join orders on Customers.ID = Orders.CustomerId
where Customers.Id not in (select Customers.Id
from Customers join orders on Customers.ID = Orders.CustomerId);
