-- Wrong answer 100%

select P.id, P.name
from products P
join( 
      select id
      from categories
      where name like '%super'
    ) C on C.id = P.id