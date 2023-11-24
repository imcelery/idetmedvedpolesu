SELECT town_to
from Trip
where id in (
		select trip
		from Pass_in_trip
		where passenger in (
				SELECT id
				from Passenger
				where name = "Bruce Willis"))


SELECT time_in from Trip
JOIN Pass_in_trip ON Pass_in_trip.trip = Trip.id
JOIN Passenger ON Passenger.id = Pass_in_trip.passenger
Where name = "Steve Martin" 
AND town_to = "London"
