-- 백업 : mysql -u root -p DB명 > ... sql 백업
-- mysql -u root -p < /경로/사킬라/sakila-schema.sql
-- mysql -u root -p < /경로/사킬라/sakila-data.sql
-- desc actor; 테이블을 description
-- select *from actor limit 0, 10; limit 옵셋, 개수(0번부터 10개)
select count(*) from actor;

use sakila;
-- [기초 조회]
-- 1. 모든 배우(Actor)의 이름과 성을 조회하시오.
SELECT first_name, last_name FROM sakila.actor;

-- 2. 배우 테이블에서 성(last_name)이 ‘DAVIS’인 사람을 모두 찾으시오.
SELECT * FROM sakila.actor
where last_name ='DAVIS'; -- 이중 따옴표 못 씀

-- 3. 고객(Customer)의 이메일 목록을 알파벳 순서로 조회하시오.
SELECT email FROM sakila.customer
order by email;

desc customer; -- 필드명 확인하기(데이터 몇 건인지 모르거나 필드명을 모를 때)
select *
from customer 
order by email;

-- 4. 영화(film)의 제목과 대여 요금(rental_rate)을 조회하시오.
SELECT title, rental_rate 
FROM film;

-- 5. 고객(Customer)의 이름, 성, 이메일을 각각 출력하시오.
SELECT first_name, last_name, email 
FROM customer;

-- 6. 카테고리(category)별 이름과 ID를 출력하시오. 
SELECT c.category_id, c.name
FROM category c;

-- [조건과 정렬]
-- 7. 길이가 180분 이상인 영화 제목을 조회하시오.
SELECT * FROM film
where length >= 180;

-- 8. ‘Comedy’ 카테고리에 속한 영화 제목을 모두 조회하시오. 
-- 최소한 두 개이상의 테이블을 조인해야 한다.
SELECT f.title
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name = 'Comedy';


-- 9. 대여 요금이 4.99 이상인 영화 중에서 제목(title)과 요금(rental_rate)을 내림차순 정렬하시오.
SELECT title, rental_rate 
FROM film
where rental_rate>= 4.99
order by title desc;

-- 10. 대여(rental) 중 2005년에 이루어진 기록만 조회하시오.
SELECT * FROM sakila.rental
where year(rental_date) = 2005;
-- 문자열을 자르는 함수 substring
select rental_date, substring(rental_date, 1, 4) from rental;

select * from rental
where substring(rental_date, 1,4) = '2005';


-- python 이나 java 0부터 시작된다. 디비는 1부터
-- substing (시작위치, 개수) 1번부터

-- 11. 고객 중 이름이 'S'로 시작하는 고객의 이름을 조회하시오.
SELECT first_name, last_name 
FROM sakila.customer
where last_name like 'S%';

-- 12. 배우(actor) 테이블에서 이름이 5글자인 배우만 찾으시오.
SELECT * FROM sakila.actor
where length(first_name) = 5;

-- 
