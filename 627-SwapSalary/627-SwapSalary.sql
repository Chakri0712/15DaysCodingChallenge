-- Last updated: 02/08/2025, 14:42:29
# Write your MySQL query statement below
update Salary set sex = case 
    when sex = 'm' then 'f'
    when sex = 'f' then 'm'
    end