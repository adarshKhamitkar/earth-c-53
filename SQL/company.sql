/*
Amber's conglomerate corporation just acquired some new companies. Each of the companies follows this hierarchy: 

Given the table schemas below, write a query to print the company_code, founder name, total number of lead managers, total number of senior managers, total number of managers, and total number of employees. Order your output by ascending company_code.

Note:

The tables may contain duplicate records.
The company_code is string, so the sorting should not be numeric. For example, if the company_codes are C_1, C_2, and C_10, then the ascending company_codes will be C_1, C_10, and C_2.
*/

select c.company_code,c.founder,COUNT(distinct(l.lead_manager_code)),COUNT(distinct(s.senior_manager_code)),COUNT(distinct(m.manager_code)),COUNT(distinct(e.employee_code))
from Company c join Lead_manager l on c.company_code=l.company_code
                            join Senior_manager s on c.company_code=s.company_code and l.lead_manager_code=s.lead_manager_code
                            join Manager m on c.company_code=m.company_code and l.lead_manager_code=m.lead_manager_code and s.senior_manager_code = m.senior_manager_code
                            join Employee e on c.company_code=e.company_code and l.lead_manager_code=e.lead_manager_code and s.senior_manager_code = e.senior_manager_code and m.manager_code=e.manager_code
group by c.company_code,c.founder
order by c.company_code
