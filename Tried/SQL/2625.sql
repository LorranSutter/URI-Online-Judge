-- Runtime error
-- UNDEFINED_FUNCTION: Function does not exist.

select SUBSTRING(cpf,1,3) + 
       '.' + 
       SUBSTRING(cpf,4,6) + 
       '.' +
       SUBSTRING(cpf,7,9) + 
       '-' +
       SUBSTRING(cpf,10,11)
       AS CPF
from natural_person