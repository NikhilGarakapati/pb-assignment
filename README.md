# pb-assignment

#### 1.1 Booking time is defined as the time taken from the leadcreation until the booking status changes to COMPLETED. For each of the cities 'Gurgaon' and 'Noida’, calculate average booking time (in days) for each product for all completed bookings within the last 30 days.
&nbsp;<br>
#### The result should have 3 columns: city_name, product_name, average_booking_time.
```
select cm.city_name, pm.product_name, avg(datediff(bd.completed_at, bd.created_at)) avg_booking_time
from lead_details ld
left join booking_details bd on bd.lead_id = ld.id
left join customer_registration_details crd on crd.id = ld.customer_id
left join product_master pm on pm.id = ld.product_id
left join cities_master cm on cm.id = city_id
where bd.status = 'COMPLETED' and cm.city_name in ('Gurgaon', 'Noida')
and bd.completed_at > (curdate() - interval 30 day)
group by cm.id, pm.id
```
&nbsp;<br>

#### 1.2 For each city (Gurgaon and Noida) and each day of the week, determine the percentage of registrations on a particular day that resulted in a successful lead generation within 24 hours of the user registration.

#### Consider only the first 7 days of 2021 for user-registration.
&nbsp;<br>
#### The result should have 4 columns: city_name, date, total_registrations, percentage_lead_generated.

```
select cm.city_name, date(bd.created_at) created_at,
count(crd.id) total_registrations,
(count(case when db.status = 'COMPLETED' then crd.id else null end)/count(crd.id))*100 percentage_lead_generated
from lead_details ld
left join booking_details bd on bd.lead_id = ld.id
left join customer_registration_details crd on crd.id = ld.customer_id
left join product_master pm on pm.id = ld.product_id
left join cities_master cm on cm.id = city_id
where cm.city_name in ('Gurgaon', 'Noida') and date_format(bd.created_at) between '2021-01-01' and '2021-01-07'
group by date, cm.id