use sakila;

-- actor_id, first_name, last_name
select *from actor limit 10;

select * from film limit 10;
-- 어떤 배우가 어떤 영화에 출연했는지 알고싶다.

select * from film_actor limit 10;

-- 영화 필름 기준으로 join
select title, description, actor_id
from film A
left outer join film_actor B on A.film_id=B.film_id;


select title, description, B.actor_id, C.first_name
from film A
left outer join film_actor B on A.film_id=B.film_id
left outer join actor C on B.actor_id=C.actor_id;

select title, description, B.actor_id,
concat(c.last_name, " ", C.first_name) actor_name
from film A
left outer join film_actor B on A.film_id=B.film_id
left outer join actor C on B.actor_id=C.actor_id;

-- category가 Comedy인 영화 목록만
-- 내 쿼리
select title, description, C.name
from film F
left outer join film_category FC on F.film_id = FC.film_id
left outer join category C on FC.category_id = C.category_id
where C.name = 'Comedy';

-- 강사님 쿼리
select title
from film A
left outer join film_category B on A.film_id=B.film_id
left outer join category C on B.category_id=C.category_id
where C.name = 'Comedy';

-- 문제1. 고객의 이름과 고객이 대여한 영화 제목을 모두 출력하시오.
select F.title,
concat(C.last_name, " ", C.first_name) customer_name
from customer C
left outer join rental R on  C.customer_id = R.customer_id
left outer join inventory I on  R.inventory_id = I.inventory_id
left outer join film F on F.film_id = I.film_id;

-- 강사님 풀이
select concat(A.last_name, A.first_name) name, D.title
from customer A
left outer join rental B on A.customer_id = B.customer_id
left outer join inventory C on B.inventory_id = C.inventory_id
left outer join film D on C.film_id = D.film_id;

-- 문제2. NICK WAHLNBERG 라는 배우가 출연한 영화의 제목 조회하기
select A.actor_id, F.title
from actor A
left outer join film_actor FA on A.actor_id = FA.actor_id 
left outer join film F on F.film_id = FA.film_id
where A.first_name = 'NICK' and A.last_name ='WAHLBERG';

select title
from actor A
inner join film_actor B on A.actor_id=B.actor_id
inner join film C on B.film_id = C.film_id
where A.first_name = 'NICK' and A.last_name = 'WAHLBERG';

select Count(distinct(title)) -- 개수 세고 싶을 때
from actor A
inner join film_actor B on A.actor_id=B.actor_id
inner join film C on B.film_id = C.film_id
where A.first_name = 'NICK' and A.last_name = 'WAHLBERG';

-- 문제3. 'London'도시의 고객 이름만 출력
select concat(A.last_name, A.first_name) customer_name
from customer A
join address B on A.address_id=B.address_id
join city C on B.city_id = C.city_id
where c.city ='London';

-- join 속도를 바르게 하려면, join 필드에 인덱스를 만들어줘야 한다.
-- 서브쿼리 : 서브쿼리는 주 쿼리 옆에서 주 쿼리보다 먼저 실행되어서 결과를 가져온 다음에 주쿼리가 실행되는 쿼리를 의미한다.
-- 서브쿼리는 select 절, from 절, where 절, order by절 등 다 가능하다.(실제로는 select랑 from절에 더 많이 쓴다.)
-- select 절 : 스칼라 서브 쿼리 (스칼라 연산 - 한번에 하나) , 결과값이 null이거나 한개만 가져오는 쿼리
-- join을 대체할 수 있다. 우리가 볼 때는 select절의 스칼라 서브쿼리가 더 편해보이지만, 조인이 일반적으로 더 빠르다. 
-- 가급적 join으로 해결하고 join이 안될 때 서브쿼리를 사용하자. 

use mydb; -- mydb로 사용 이동
-- 사원번호, 사원이름, 부서명을 가져오려고 한다.
select empno, ename, deptno -- 서브쿼리르 이용해 부서명을 가져오자
from emp;

select dname from dept where deptno = 10;

select empno, ename, deptno, 
(select dname from dept where dept.deptno = emp.deptno) as dname -- 한개의 필드만 가져올 수 있다. 스칼라 서브쿼리
from emp;

select empno, ename, deptno, 
(select dname from dept B where A.deptno = B.deptno) as dname -- aliasing
from emp A;

use sakila;
select first_name, last_name, B.film_id
from actor A
left outer join film_actor B on A.actor_id=B.actor_id;


select first_name, last_name, 
(select title from film C where B.film_id = C.film_id) as title -- title을 가져오는 서브쿼리
from actor A
left outer join film_actor B on A.actor_id=B.actor_id;


select first_name, last_name, 
(select title from film C where B.film_id = C.film_id) as title,
(select length from film C where B.film_id = C.film_id) as length -- length를 가져오는 서브쿼리
from actor A
left outer join film_actor B on A.actor_id=B.actor_id;

-- from 절에서 : 다중행을 반환한다. 다중행 서브쿼리, 인라인뷰
use mydb;

-- select *from emp where deptno in(10,20) 에서 사원이름, 부서명

select A.ename, dname
from(
select * from emp where deptno in (10,20)
) as A
join dept B on A.deptno = B.deptno;

use sakila;

-- film_id in field list is ambiguous 
select A.film_id, title, length, actor_id
from film A
left outer join film_actor B on A.film_id=B.film_id; 

select first_name, last_name, title
from actor A
left outer join (
select A.film_id, title, length, actor_id
from film A
left outer join film_actor B on A.film_id=B.film_id
-- inline view
) B on A.actor_id =  B.actor_id;

-- where 절
use mydb;

-- emp 테이블에 smith 라는 사람의 부서와 같은 부서에 있는 사람들의 정보
select deptno from emp where ename = 'SMITH';
-- where 조건절에 오는 서브쿼리가 데이터가 여러 개일 때가 있고, 단일행인 경우가 있다.
-- 단일행인 경우와 다중행인 경우 처리방법이 다르다.
select * from emp where deptno=20;

select * from emp 
where deptno=(select deptno from emp where enmae ='SMITH');

-- smith 가 근무하는 부서의 급여 평균보다 급여를 받는 사람들 정보를 확인하고자 한다
select avg(sal) from emp where deptno = (select deptno from emp where ename='SMITH');

select ename, sal from emp
where sal > (select avg(sal) 
from emp where deptno = (select deptno from emp where ename='SMITH'));

-- 부서 평균 급여보다 급여가 많은 사원 조회
select * from emp
where sal > ( select avg(sal) from emp);


-- 가장 높은 급여를 받는 사원 정보 조회하기
select * from emp 
where sal = (select max(sal) from emp);


-- 강사님 풀이
select * from emp
where sal >= (select max(sal) from emp);

-- 매니저가 존재하는 사원만 조회MGR
-- 내 풀이
select * from emp 
where MGR is not null; -- MGR의 값이 NULL이 아닌, 상사가 지정되어 있는 사원만 선택

select * from emp 
where MGR in (select distinct MGR from emp where MGR is not null); -- MGR의 값이 다른 직원의 MGR 값 중 하나인 직원들만 조회

--  강사님 풀이
select * from emp; -- mgr 필드에 자기 상관 정보가 있다.
-- 나의 mgr 필드가 emp 테이블에 존재하느냐
select * from emp where mgr in (select empno from emp); -- mgr 값이 emp 테이블의 empno(직원번호) 값 중 하나인 경우만 조회

-- 상관쿼리 : 외부 쿼리의 값을 내부쿼리에서 참조하는 서브쿼리를 말한다.
-- 외부 쿼리의 각 행마다 내부쿼리가 실행되는 구조
-- exists, any, all, in 등이 있다.
-- exists - 서브쿼리의 실행결과가 하나라도 있으면 True, 한개도 없으면 False 반환, 서브쿼리의 실행결과가 한 건이라도 있으면 실행된다.
-- any - 조건을 만족하는 게 하나라도 있으면 수행, 부등호 or 부등호 or 부등호 or 부등호
-- all - 모든 조건을 만족하는 부등호 and 부등호 and 부등호
-- in - 등호 or 등호 or 등호

-- 부서별 평균 급여보다 높은 급여를 받는 사원 조회
-- 부서별 평균 값이 필요

select avg(sal) from emp where deptno=10;
select avg(sal) from emp where deptno=20;
select avg(sal) from emp where deptno=30;
select avg(sal) from emp where deptno=40;

select empno, sal, deptno from emp;
 
 -- 부서번호 10이 서브쿼리의 외부쿼리에서 가져와야 한다.(=상관쿼리)
 select empno, sal, deptno from emp
 where sal > (select avg(sal) from emp where deptno=10);

-- 외부의 A의 deptno와 서브쿼리(내부쿼리)의 deptno가 서로 관계가 있다. (상관쿼리)
 select empno, sal, deptno from emp A
 where sal > (select avg(sal) from emp B where B.deptno=A.deptno);
 
-- exists - 매니저가 존재하는 사원만 조회
select empno, ename, mgr from emp;

select ename from emp where mgr = 7902;
-- 서브쿼리의 실행결과가 하나라도 있으면 외부쿼리를 실행한다.
-- 서브쿼리의 결과 유무만 따진다.
-- select *from emp where exists (서브쿼리)

select empno, ename, mgr from emp A 
where exists (select 1 from emp B where A.mgr=B.empno -- A의 상사번호가 B의 직원번호에 존재하는지 확인
);

use sakila;
--  문제1. 고객의 이름과 고객이 대여한 영화 제목을 모두 출력하시오.

-- 강사님 풀이
select concat(A.last_name, A.first_name) name, 
(select title from film D where C.film_id=D.film_id) as title
from customer A
left outer join rental B on A.customer_id = B.customer_id
left outer join inventory C on B.inventory_id = C.inventory_id;

select concat(A.last_name, A.first_name) name,
(select title from film D where C.film_id=D.film_id) as title
from customer A
left outer join rental B on A.customer_id = B.customer_id
left outer join inventory C on B.inventory_id = C.inventory_id;

-- 문제2. NICK WAHLBERG라는 배우가 출연한 영화의 제목 조회하기

-- 강사님 풀이
select (select title from film C where B.film_id=C.film_id) title
from actor A
left outer join film_actor B on A.actor_id = B.actor_id 
where A.first_name = 'NICK' and A.last_name ='WAHLBERG';


use w3schools;

select *from customers limit 10;

-- 주문번호, 고객이름, 판매자이름
select  o.*, c.customername,
concat(e.lastname," ",e.firstname) as employeename
from orders o
join customers c on c.CustomerID = o.CustomerID
join employees e on o.EmployeeID = e.EmployeeID;


-- 강사님 풀이
desc orders;
select A.*, B.customername,
concat(c.lastname," ",c.firstname) as employeename
from orders A
join customers B on A.customerID=B.customerID
join employees C on A.employeeID=c.employeeID;

-- join 안 쓰고 subquery로 바꾸기
-- 내풀이
select o.*,(select customername from customers c where c.CustomerID = o.CustomerID) customername,
concat(e.lastname, " ", e.firstname) as employeename
from orders o
join employees e on o.EmployeeID = e.EmployeeID;

-- 강사님 풀이
select orderid,
(select customerName from customers B 
where A.customerid=B.customerid) as customerName
,
(select concat(C.lastname, " ", C.firstname) from employees C
where A.EmployeeID = C.EmployeeID) as employeeName
from orders A;

-- 주의사항, linux mysql은 필드명이나 테이블명의 대소문자를 따진다.

-- 그룹함수, avb, max, min, count, sum...
use mydb;
-- ename, sal 필드는 데이터 개수만큼 나오고 avg(sal)은 값이 1개 나오기 때문에 같이 쓸 수 없다.
-- select ename, sal, avg(sal) from emp; -- 에러남

select ename, sal, (select avg(sal) from emp) avg_sal -- 이럴 때 서브쿼리를 쓴다.
from emp;

-- 부분합, 그룹별로 묶는 게 가능
-- 각 부서별로 급여 평균을 확인하고 싶다.
-- 그룹함수는 group by 절에 온 필드는 사용가능
select deptno, avg(sal)
from emp
group by deptno;

-- 이름과 부서번호 급여 부서별 평균
select ename, deptno, sal, (select avg(sal) from emp B where A.deptno = B.deptno) dept_sal -- 이럴 때 서브쿼리, 즉, 통계쿼리를 만들 때 서브쿼리가 필요하다
from emp A;

-- 서브쿼리와 join 합치키
select ename, A.deptno, sal, dept_sal
from emp A
left outer join(
select deptno, avg(sal) dept_sal
from emp
group by deptno) B
on A.deptno = B.deptno;

select ename, A.deptno, sal, dept_sal, sum_sal, max_sal, min_sal
from emp A
left outer join(
select deptno, avg(sal) dept_sal, sum(sal) sum_sal, max(sal) max_sal, min(sal) min_sal
from emp
group by deptno) B
on A.deptno = B.deptno;


-- 문제 orders 테이블에서 고객별 주문 개수 구하고 정렬을 주문수가 많은 고객부터 내림차순 desc
-- 고객 이름, 주문 카운트
use w3schools;
-- 내풀이 : 고객별 제품 구매 수량 카운트
select c.customerID, c.customername, count_order
from orders o
inner join customers c on c.customerID=o.customerID
left outer join(
select orderID, count(quantity) count_order
from orderdetails
group by  orderID) od
on o.OrderID=od.OrderID
order by count_order desc;

-- 강사님 풀이 : 주문 수 카운트

select customerId, count(customerID)
from orders
group by customerID
order by count(customerID) desc;
-- where 절에는 group 함수 사용못함
-- 구매 개수 5개 이상만 출력

select c.customerID, c.customername, count(c.customerID)
from orders o
inner join customers c on c.customerID=o.customerID
group by c.customerId
having count(c.customerId) >=5 -- where절은 그룹함수 사용 못함. having 써야함.
order by count(c.customerID) desc;

-- 오늘의 과제
-- 1. 주문이 한번도 업는 고객의 이름을 조회하기
-- 2. 가장 주문 건수가 많은 판매자 이름 구하기
-- 3. 판매건수가 5건 이상인 판매자 인원 수 구하기


use w3schools

show tables;