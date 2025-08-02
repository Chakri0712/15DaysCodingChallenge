-- Last updated: 02/08/2025, 14:42:38
# Write your MySQL query statement below

select Customers.name as Customers from Customers where Customers.id not in (select customerId from Orders);
