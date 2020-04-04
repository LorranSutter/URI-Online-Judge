-- Wrong answer 100%

select C.id, C.name
from customers C
left join locations L
on C.id = L.id_customers