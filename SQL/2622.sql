select C.name
from customers C
join legal_person LP
  on LP.id_customers = C.id
