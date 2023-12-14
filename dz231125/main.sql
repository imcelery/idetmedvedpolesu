-- 16
SELECT ps.name,
	count(*) as count
from Passenger as ps
	join Pass_in_trip as pt on ps.id = pt.passenger
GROUP by ps.name
Order by count(*) DESC,
	ps.name

-- 17
Select member_name,
	status,
	Sum(pm.amount * pm.unit_price) as costs
from FamilyMembers
	join Payments as pm on pm.family_member = member_id
where YEAR(date) = 2005
GROUP by member_name,
	status

-- 18
SELECT member_name
from familymembers
Where YEAR(birthday) = (
		SElect MIN(YEAR(birthday))
		from familyMembers
	)

-- 19
Select status
from FamilyMembers
Where member_id in (
		SELECT family_member
		from Payments
		where good in (
				select good_id
				from Goods
				where good_name = "potato"
			)
	)

-- 20
select l1.status,
	l1.member_name,
	sum(l2.amount * l2.unit_price) as costs
from FamilyMembers as l1
	join Payments as l2 on l2.family_member = l1.member_id
	join Goods as gods on gods.good_id = l2.good
	join goodTypes as gt on gt.good_type_id = gods.type
where gt.good_type_name = "entertainment"
GROUP by l1.status,
	l1.member_name

-- 21
select good_name
from Goods
	join Payments on Payments.good = goods.good_id
GROUP by Payments.good
HAVING COUNT(Payments.good) > 1;

-- 22
SELECT member_name
from FamilyMembers
where status = "mother"

-- 23
select Goods.good_name,
	Payments.unit_price
from Goods
	join GoodTypes on GoodTypes.good_type_id = Goods.type
	join Payments on Payments.good = Goods.good_id
where GoodTypes.good_type_name = "delicacies"
GROUP by Goods.good_name,
	Payments.unit_price
limit 1

-- 24
SELECT fm.member_name,
	SUM(pm.amount * pm.unit_price) as costs
from FamilyMembers as fm
	join Payments as pm on pm.family_member = fm.member_id
Where YEAR(pm.date) = 2005
	and MONTH(pm.date) = 06
GROUP by fm.member_name

-- 25
select g.good_name
from Goods as g
	left join (
		select *
		from Payments
		where YEAR(date) = 2005
	) as pm on pm.good = g.good_id
where pm.good is null
GROUP by g.good_name

-- 26
select good_type_name
from GoodTypes
WHERE good_type_id not in (
		select g.type
		from Goods as g
			join (
				select *
				from Payments
				where YEAR(date) = 2005
			) as pm on pm.good = g.good_id
		GROUP by g.good_name
	)

-- 27
select gt.good_type_name,
	sum(pm.unit_price * pm.amount) as costs
from GoodTypes as gt
	join Goods as gs on gs.type = gt.good_type_id
	join Payments as pm on pm.good = gs.good_id
Where YEAR(pm.date) = 2005
GROUP by gt.good_type_name

-- 28
SELECT COUNT(*) as count
from trip
where town_to = "Moscow"
	and town_from = "Rostov"

-- 29
select name
from passenger
Where id in (
		SELECT passenger
		from Pass_in_trip
		where trip in (
				SELECT id
				from trip
				where plane = "TU-134"
					and town_to = "Moscow"
			)
	)

-- 30
Select tr.id as trip,
	COUNT(pt.passenger) as count
from trip as tr
	join Pass_in_trip as pt on pt.trip = tr.id
GROUP by trip
ORDER by COUNT(pt.passenger) DESC

-- 31
Select *
from FamilyMembers
Where member_name like "%Quincey"

-- 32
Select FLOOR(AVG(YEAR(CURDATE()) - YEAR(birthday))) as age
from FamilyMembers

-- 33
SElect AVG(pm.unit_price) as cost
from Payments as pm
	Join Goods as gd On pm.good = gd.good_id
Where good_name = "red caviar"
	or good_name = "black caviar"

-- 34
select Count(name) as COUNT
from class
where name like "10%"

-- 35
Select Count(date) as Count
from Schedule
Where date = "2019-09-02"

-- 36
Select *
from student
Where address like "%ul. Pushkina%"

-- 37
Select min(TIMESTAMPDIFF(Year, birthday, CURDATE())) as year
from Student

-- 38
Select Count(id) as count
from student
Where first_name = "Anna"

-- 39
Select COUNT(sc.student) as count
from Student_in_class as sc
	join Class as cl on cl.id = sc.class
Where name = "10 B"

-- 40
Select su.name as subjects
from subject as su
	join Schedule as sc on sc.subject = su.id
	join Teacher as te on te.id = sc.teacher
Where te.last_name = "Romashkin"
	and te.first_name like "P%"
	and te.middle_name like "P%"

-- 41
Select start_pair
from Timepair
where id = 4

-- 42
Select DISTINCT TIMEDIFF(
		(
			Select end_pair
			from Timepair
			where id = 4
		),
		(
			Select start_pair
			from Timepair
			where id = 2
		)
	) as time
from Timepair

-- 43
Select last_name
from teacher as te
	join Schedule as sc on sc.teacher = te.id
	Join subject as su on su.id = sc.subject
Where su.name = "Physical Culture"
ORDER by last_name

-- 44
Select MAX(TIMESTAMPDIFF(YEAR, birthday, CURDATE())) as max_year
from student as st
	Join Student_in_class as sc on sc.student = st.id
	join class as cl on cl.id = sc.class
Where cl.name like "10 %"

-- 45
select classroom
from Schedule
group by classroom
HAVING count(classroom) = (
		select count(classroom)
		from Schedule
		GROUP by classroom
		ORDER by count(Class) DESC
		limit 1
	)

-- 46
select DISTINCT name
from Class as cl
	join Schedule as sc on sc.class = cl.id
	join Teacher as tc on tc.id = sc.teacher
where tc.last_name = "Krauze"

-- 47
select count(*) as count
from Schedule as sc
	join Teacher as te on sc.teacher = te.id
where te.last_name = "Krauze"
	and sc.date = "2019-08-30"

-- 48
select cl.name,
	count(sc.student) as count
from class as cl
	join Student_in_class as sc on sc.class = cl.id
group by cl.name
ORDER by count desc

-- 49
select count(student) * 100 / (
		select count(student)
		from Student_in_class
	) as percent
from Student_in_class as sc
	join class as cl on cl.id = sc.class
where cl.name = "10 A"

-- 50
select floor(
		count(id) * 100 / (
			select count(id)
			from Student
		)
	) as percent
from Student as st
where year(st.birthday) = "2000"