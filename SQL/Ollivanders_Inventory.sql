select w.id,p.age,w.coins_needed,w.power
from Wands w join wands_property p on w.code=p.code
where p.is_evil=0 and w.coins_needed = (select min(a.coins_needed)
                                                                    from Wands a join wands_property b on a.code=b.code
                                                                    where p.age=b.age and w.power=a.power)
order by w.power desc,p.age desc;
