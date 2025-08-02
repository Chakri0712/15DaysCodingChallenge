-- Last updated: 02/08/2025, 14:42:23
# Write your MySQL query statement below
select employee_id, 
case when name like 'M%' or name like 'm%' then 0
else
  employee_id % 2 * salary
end  
as bonus
from Employees
order by employee_id;