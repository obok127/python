/*w3schools 테이블 구조
orders - 주문 아이디, 고객 아이디(foreign key), 선적 아이디(foreign key), 판매자 아이디(foreign key)
order_details - orderdetailId, productId, quantity, orderID(foreign key)
customers - 고객정보, customerID(primary key)
employees - employeeId(primary key)
products - productID(primary key)
shippers = shippedID(primary key)
suppliers - product에 묶임
categories - product에 묶임

inner join - 교집합
left outer join - 왼쪽 집합이 다 출력
right outer join - 오른쪽 집합이 다 출력
cross join - 카테시안곱, 조인조건이 없을 때 n by m (가짜 데이터 만들 때 사용)
self join - 자기 테이블끼리 조인을 한다
*/

use w3schools;
select * from customers;

-- 고객이름이 Handel 이라는 사람이 있고 이분의 주문 내용을 확인

select orderId, c.customerid, c.customername
from customers c
join orders o on c.customerid = o.customerID
where customername like '%Handel%';

-- 제품명 -> orders, products, orderdetails

desc orderdetails;

-- 위에 Handle 이라는 분이 주문한 상품명을 확인하고 싶을 때
select A.productID, quantity, productName, A.OrderID
from orderdetails A
join products B on A.productid = B.productid
where orderid in (
	select OrderID
	from customers c
	join orders o on c.customerid = o.customerID
	where customername like '%Handel%'
);

-- inner join 의 경우에는 from 절 테이블과 join절 테이블 구분 필요 없음
-- 다만 데이터의 개수가 좀 작은 테이블이 앞쪽에 오는 것이 좋다.(권고)
-- 조인 -for문, nested loop join -> hash join(검색속도가 빠르다, 메모리를 엄청 쓴다, where절로 검색 조건이 있을 때는 hash join을 사용할 필요가 없다)
-- where 조건절이 먼저 실행되어서 우선 데이터를 거른 다음에 조인을 한다.

-- left outer join : from 절에 가까운 테이블 내용이 다 나오길 원할 때
-- right outer join : from 절에 먼 테이블 내용이 다 나오길 원할 때
-- full outer join : 합집합,  ansi 표준은 있는데 mysql은 없음
-- cross join
select A.customerId, B.orderId
from customers A, orders B; -- 가짜 데이터 만들 때 활용, 평소에는 안 씀

-- self join emp 테이블 mgr 필드가 자기 상사의 사원번호임
-- 동일테이블을 조인한다고 해서 self join - 코드 테이블 만들 때

use mydb;

select * from emp;
-- emp A - mgr, emp B - empno
select A.ename, A.mgr, B.ename
from emp a
left outer join emp b on a.mgr = b.empno;
-- A에 있는 mgr값을 B에서 찾은 것

use w3schools;

SELECT O.OrderID, C.CustomerName
FROM Orders o
INNER JOIN Customers c ON O.CustomerID = C.CustomerID;



SELECT O.OrderID, C.CustomerName, S.ShipperName
FROM Orders o
INNER JOIN Customers c ON O.CustomerID = C.CustomerID
INNER JOIN Shippers s ON O.ShipperID = S.ShipperID;


SELECT O.OrderID, O.CustomerName, S.ShipperName
FROM
(
	SELECT O.OrderID, C.CustomerName, S.Shipperid
	FROM Orders o
	INNER JOIN Customers c ON O.CustomerID = C.CustomerID
) O
INNER JOIN shippers S on O.shipperID=S.shipperID;


Select A.orderid, b.customername, c.shippername
from orders a, customers b, shippers c
where a.customerid = B.customerid and a.shipperid = c.shipperid;

-- join이 일반적으로 subquery보다 빠르다

-- employees 테이블에 firstname이 king이라는 사람이 있다.
-- 이 사람이 판 주문 내역을 확인하고 싶다.(orderid, customerid,customername,shippername, productname)
SELECT e.lastname, e.firstname, o.orderid, c.customername, s.shippername, p.productname
FROM orders o
INNER JOIN employees e ON e.EmployeeID = o.EmployeeID
INNER JOIN Shippers s ON s.ShipperID = o.ShipperID
INNER JOIN customers c ON c.customerID = o.customerID
INNER JOIN orderdetails od ON o.OrderID = od.orderID
INNER JOIN products p ON p.ProductID = od.ProductID
where e.lastname = 'king';

-- 강사님 풀이
select A.orderId, c.customername, f.ShipperName, e.ProductName
from orders A
inner join employees B on A.EmployeeID = B.EmployeeID
inner join customers C on A.customerID = C.customerID
inner join orderdetails D on A.orderId = D.orderID
inner join products E on D.productID = E.productID
inner join shippers F on A.shipperID = F.shipperID
where B.lastname like 'King%'; -- 여기서 배달업자별로 

-- cross join 가짜 데이터로 튜닝할 때 사용함
-- self join 

-- union, union all 단순 합하기, 데이터 덧붙이기
-- union 의 경우 중복 배제, union all은 중복을 배제하지 않는다.
/*
select column1, column2 from table1
union all
select column1, column2 from table2
필드개수와 타입만 맞으면 된다.
행 -> 열로 바꿔야 할 때alter
1
2
3
4
  1  2  3  4
포털, 국가 기관 검색어로 검색하면 각 테이블로부터 검색한 내용을 전부 union 해서 가져온다.
*/

use mydb;

select empno, ename from emp
union all
select deptno, dname from dept;

select count(*) from emp
union all
select count(*) from dept; -- table row 수 샐 때 사용, db에 덜 갔다 오는 수단으로 사용할 수 있다.

use w3schools;

SELECT City, Country FROM Customers
WHERE Country='Germany'
UNION ALL
SELECT City, Country FROM Suppliers
WHERE Country='Germany'
ORDER BY City;

-- 나라별로 몇 명의 고객이 있는가?
-- 그룹함수 중에 null값 처리부분이 조금씩 다르다
-- count(필드명) 에 null값이 존재하면 카운트 하지 않는다. count(*) : 그 중에 가장 긴 애를 카운트한다.

select count(*) -- 전체 고객 수 
from customers;

select country, count(*) -- 나라 별로 몇 명의 고객이 있는가
from customers
group by country; -- group by 절에 있던 필드만 select절에 올 수 있다.


select country, count(*) 
from customers
group by country
order by count(*) desc; -- 그룹 함수가 order by절에 올 수 있다. group by의 영향을 받음

-- 배달업체 별로 주문 개수
select shippername, count(*) -- 주문 개수
from orders A
join shippers B on A.shipperID = B.shipperID -- join이 되는지 먼저 확인
group by shippername; -- 배달업체 별

-- 주문번호, 배달업체, 배달업체 카운트
select orderid, shippername, count(*) -- 주문 개수
from orders A
join shippers B on A.shipperID = B.shipperID -- join이 되는지 먼저 확인
group by shippername;
-- error : SELECT list is not in GROUP BY clause and contains nonaggregated column 'w3schools.A.OrderID' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by

-- 주문번호, 배달업체, 배달업체 카운트
select AA.*, B.orderid
from
(
select count(*) cnt, A.ShipperID
from orders A
join shippers B on A.shipperID = B.shipperID 
group by ShipperID
) AA
inner join orders B on B.shipperid=AA.shipperid;

-- 카운터가 정렬해서 3개만 -> 분석함수(윈도우 함수) - 오라클
select count(*) cnt, A.ShipperID
from orders A
join shippers B on A.shipperid = B.shipperid
group by shipperid
order by count(*) desc
limit 2;


-- 주문번호, 배송업체 번호, 카운트
select orderid, b.shipperid, cnt
from orders A
inner join (
select A.shipperid, count(*) cnt
from orders A
join shippers B on a.shipperid=b.shipperid
group by shipperid
order by count(*) desc
limit 2
) b on a.shipperid = b.shipperid;

select orderid, shipperid,
(select count(*) from orders B where A.shipperid=b.shipperid) as cnt
from orders a;

-- DB접속
-- select * from orders; 쿼리실행
-- 디비 연결 끊음
-- for order in orders
-- 	 	DB접속
-- 		select count(*) from orders where shipperid=order 
-- 		DB연결 끊음
-- 이렇게 하면 안됨

SELECT A.SupplierName
FROM Suppliers A
WHERE EXISTS (
SELECT 1 FROM Products B
WHERE B.SupplierID = A.supplierID AND B.Price < 20
);
-- exists 의 장점 : 서브쿼리의 모든 수행을 기다리지 않고 뭔가 하나 찾으면 바로 끝남
-- 서브쿼리의 수행 결과셋 존재 유무만 파악

-- Any : 서브쿼리에서 오는 조건 중에 하나라도 만족하는 항목이 있을 경우 부등호 or 부등호 or 부등호 or
-- All : 부등호 and 부등호 and 부등호 and
-- in : 등호 or 등호 or 등호 or

-- 프로그래밍 언어 mysql script가 있어서 함수도 프로시저도 만들 수 있다.
-- mysql 만들었던 언어가 함수와 프로시저
-- 함수는 반드시 반환값이 있다. 프로시저는 반환값이 없다.
-- mysql의 내장함수 
select now(); -- 현재 날짜와 시간을 주는 함수
-- 대부분의 DBMS들은 select절은 from절 못 빠짐
-- 오라클 같은 경우에는 dummy tale 이 있다. 
-- select sysdate from dummy(가짜테이블); 다른 DBMS는 이런 dummy를 붙여야 sysdate 출력이 가능한데
-- 근데 mysql은 from 절을 따로 안 써도 됨.

-- 함수도 표준이 없어서 DBMS마다 다르다

select now() from customers; -- customers 테이블의 데이터 개수만큼 호출된다.

select * from customers 
where customername like '%Around%';

select concat("Tom","is", "a student") as sentence; -- 필드명을 새로 준다.

SELECT CONCAT(Address, " ", PostalCode, " ", City) AS Address
FROM Customers;

select concat(address, " ", PostalCode, " ", City) as address
from customers;
/*
select * from
delete from -- delete는 행을 삭제하기 때문에 *이 필요없다. 
*/

desc customers;

select ltrim("    hello    ") a, "***" b;
select rtrim("    hello    ") a, "***" b;
select trim("    hello    ") a, "***" b;
-- 대부분의 dbms가 문자열 인덱스를 1부터 시작한다.
select substr("Hello mysql", 7,5) c;

select substr("2025-05-20", 1, 4) year,
	   substr("2025-05-20", 6, 2) month,
	   substr("2025-05-20", 9, 2) day; -- 행사의 경우에 어떤 달에 어떤 걸 했는지가 문자열로 들어가 있는 경우가 있다.
       -- 그럴 때 substr로 추출해냄

-- sql sin cos tan
-- 교촌 치킨 위치가 DB에 위도 경도로 다 들어가 있으면
-- 우리집 좌표 gps기반으로 마크하는 것: 유클리드로 거리계산

-- CEIL : 올림함수 데이터 개수가 231개 -> page 개수 계산할 때 
-- floor : 내림함수(소수점 이하 다 버림)

-- 마감일이 얼마나 남았나, 언제 이걸 오픈해야 하는가 ex. 멜론티켓
-- interval은 간격을 의미함
SELECT ADDDATE("2017-06-15", INTERVAL 10 DAY) as day;
SELECT ADDDATE("2017-07-27", INTERVAL 6 DAY) as day; -- 윤년도 알아서 계산해줌
SELECT ADDDATE("2025-12-27", INTERVAL 10 DAY) as day;  -- 2017.6.15일에 10일 후는 몇일이냐

SELECT ADDDATE("2017-06-15 09:34:21", INTERVAL 15 MINUTE);

SELECT DATEDIFF("2017-06-25", "2017-06-15") date; -- 날짜와 날짜 사이에 얼마나 간격이 있는가

SELECT DATEDIFF("2025-05-20", "2025-09-25") date;

use mydb;
desc dept;
select * from dept;

-- 테이블 구조가 간단할 경우에는 필드명을 생략할 수 있다.
-- desc에 나온 필드 목록하고 동일한 구조로 저장해야 한다.
insert into dept values(50, '개발1부', '서울');
select * from dept;

insert into dept(deptno, dname) values(60, '개발2부'); -- deptno는 primary key
select * from dept;-- 구조를 안맞추면 null값이 들어간다.

desc emp;

insert into emp(empno) values(9000);

-- 규칙에 위배되는 데이터를 삭제하자
delete from emp where sal is null;
-- delete는 행 삭제, delete 명령어 안전장치가 되어 있는 DBMS가 있다. 오라클(트랜지션) rollback하면 막을 수 있다.

-- emp table에서 alter table에서 조건 변경
desc emp;
-- 테이블을 수정했음 sal 필드와 ename 필드를 not null로 하기로
-- insert into emp(empno) values(9000); 에러가 남 왜냐면 sal필드랑 ,ename필드가 not null 이니까
insert into emp(empno, ename, sal)
values(8000, '홍길동', 3300); -- 최소한 3개의 필드는 넣어줘야 돌아간다.
select * from emp;

-- 한번에 여러명 넣기 
insert into emp(empno, ename, sal)
values(8001,'둘리', 3200),
	  (8002,'도우너', 3200),
	  (8003,'또치', 3200);

-- 데이터에 '가 들어가야 할 때 ==> ''
-- 'Toms'family' ==> 'Tom''s family'
-- 'Jane' ==> '''Jane'''

insert into emp(empno,ename, sal)
values (8004, 'Tom''s',3200),
(8005,'''jane''',3200);

select * from emp;
-- 액시스? 는 ms에서 만든 DBMS

-- 서버 : 서비스를 제공하는 측(하드웨어 또는 소프트웨어)
-- 클라이언트 : 서비스를 제공받는 측(하드웨어 또는 소프트웨어) workbench, mysql, 웹브라우저
-- 서비스(ms), daemon 데몬(리눅스) : 백그라운드에서 돌아가는 프로그램, 화면 ui 제공 안하고 조용히 작동중 DB

-- 테이블을 만들기, 테이블 복사 명령어가 없음
-- create table 테이블명(컬럼1 타입, 컬럼2 타입,,,);
create table emp2 as select* from emp;
-- 복사 명령어 없이 서브쿼리를 써서 테이블을 복사할 수 있다.
-- 제약조건은 안 데려감(primary key, foreign key는 버림 , not null은 들고옴)
desc emp2;
select * from emp2;

-- 구조만 복사하기 : 운영중인 DB를 쿼리 테스트나 빠르게 확인하고자 할 때
create table emp3 as select * from emp where 1=0; -- 해당 조건을 만족하는 데이터가 없으면 따라갈 데이터가 없어서 구조복사만 됨.
select * from emp3;

-- 일부만 복사해서 가져오기
create table emp4 as
select empno,ename, sal
from emp where deptno in (10,20);
select * from emp4;

insert into emp3 (empno, ename, sal) 
select empno, ename, sal 
from emp; -- 서브쿼리로 특정 필드만 복사도 가능
select * from emp3;

use w3schools;
-- 문제1. customers 테이블의 구조를 복사한 후 customers2로 만들고 고객 아이디 중에 3,23,21,45,67,89,54 복사하기

-- 내 풀이
create table customers2 as
select customerid
from customers where customerid in (3,23,21,45,67,89,54);

select * from customers2;

-- 강사님 풀이 : git 확인
create table customers2 as 
select * from customers where 1=0;

desc customers;
insert into customers2 (CustomerID,cusotmername,contactname, address, city, postalcode, country)
select * from customers
where customerid in (3,23,21,45,67,89,54);

-- 문제2. 고객아이디 중에 4,5,11,33,42,43,56,57,58번을 이동하기 customers-> customers2로 
create table customers3 as 
select * from customers 
where customerid in (4,5,11,33,42,43,56,57,58); -- 해당 조건을 만족하는 데이터가 없으면 따라갈 데이터가 없어서 구조복사만 됨.
select * from customers3;

-- 강사님 풀이 : git 확인
insert into customers3 (customerid, customername, contactname,address,city, postalcode,country)
select * from customers
where customerid in (4,5,11,33,42,43,56,57,58);
-- foreign key를 제거하고 삭제해야 한다.
-- 현재 삭제 안됨

-- 문제3. 제품 가격이 100$를 넘는 제품을 구매한 고객 리스트
select customerName as over_100$
from customers c
join orders o on o.customerid = c.customerid
join orderdetails od on od.orderid = o.orderid
join products p on p.productid = od.productid
where p.price >100;

-- 강사님 풀이
select A.orderid, D.customername, price
from orders A
inner join orderdetails B on A.orderid=B.orderid
inner join products C on B.productid=C.productid
inner join customers D on A.customerid = D.customerid
where price > 100;

-- 문제4. orderdetails 테이블의 quantity가 제품을 구매한 수량이고 products 테이블에 있는 price가 단가이다.
-- 구매한 고객의 이름과, 제품명, 제품 전체 가액을 구하시오
-- ex. 홍길동 가구 quantity * price

select c.customerName, p.productName,
(select (quantity*price) from products p where  p.productid = od.productid) as total_price
from customers c
join orders o on o.customerid = c.customerid
join orderdetails od on od.orderid = o.orderid
join products p on p.productid = od.productid;


-- 강사님 풀이
select D.customername, C.productname, C.price*B.quantity
from orders A
inner join orderdetails B on A.orderid=B.orderid
inner join products C on B.productid=C.productid
inner join customers D on A.customerid = D.customerid;



-- 문제5. 핀란드에 있는 공급자 리스트 가져오기(Finland)
-- disticnt 뒤에 나오는 필드값의 주복을 배제하는 명령어, 단일 필드로 바꿀 때만 사용
-- 옛날 데이터를 새로운 데이터로 옮기는 것 migration 
-- select distinct country, suppliername from suppliers;
-- distinct는 country와 suppliername 을 조합해서 유일한 데이터를 가져온다.(사용범위가 매우 제한됨)
select distinct country from suppliers; -- 값 확인시 활용

select *
from suppliers
where country like "%Finland%";

-- 강사님 풀이
select suppliername from suppliers where country = 'Finland';
-- 외부에서 검색할 때 제목+내용  : 이때 like와 와일드카드%를 같이 사용



-- 문제6. 카테고리 제품이 seafood 인 제품의 구매자 리스트를 조회하시오.
select c.CustomerName as bgt_seafood 
from customers c
join orders o on o.customerid = c.customerid
join orderdetails od on od.orderid = o.orderid
join products p on p.productid = od.productid
join categories ct on ct.categoryid = p.categoryid
where CategoryName like "%seafood%";

-- 강사님 풀이
select customername
from orders A
inner join orderdetails B on A.orderid = B.orderid
inner join products C on B.productid= C.productid
inner join customers d on A.customerid =D.customerid
inner join categories E on C.categoryid = E.categoryid
where lower(E.categoryname) = 'seafood';

-- 오늘의 과제
-- 1. customers 테이블에서 나라가 Germany인 나라의 정보 전체
select * 
from customers c
where country = 'germany';
 
-- 2. customers 테이블에서 나라가 Austria, USA, 
select * 
from customers c
where country in ('austria', 'usa', 'poland','denmark')
order by country; 

-- 3. 각자 나라별로 고객이 몇명씩 있는지 확인
select country, count(customerid) as count
from customers c
group by country;

-- 4. 나라별로 고객이 5명 이상인 나라 목록만 조회
select c.country as over_5
from customers c
group by country
having count(c.CustomerID) >=5;

-- 5. 나라이름이 B로 시작하는 나라들의 고객 전체 합
select count(customerID) 
from customers c
where country like 'B%';

-- 6. 나라는 Mexico 도시명은 Mexico City('México D.F.'??) 에 있는 고객들 이름 목록
select customername, city
from customers c
where country = 'uk'and city = 'LONDON';

-- 7. 주문 날짜가 '1996-07-01'~'1996-09-30'일까지의 주문아이디와 고객이름
select o.orderId, c.customername
from orders o
join customers c on c.customerid = o.customerid
where orderdate >= '1996-07-01' and orderdate<='1996-09-30';


-- 8. 위의 7번 문제를 고객이름 오름차순으로 정렬하여 출력하기
select o.orderId, c.customername
from orders o
join customers c on c.customerid = o.customerid
where orderdate >= '1996-07-01' and orderdate<='1996-09-30'
order by c.customername;


-- 9. 배달자가 federal shipping인 경우의 상품명 가격 수량
select p.productname, p.price, od.quantity
from orders o
join shippers sh on sh.shipperid = o.shipperid
join orderdetails od on od.orderid = o.orderid
join products p on p.productid = od.productid
where shippername = 'federal shipping';










SELECT Shippers.ShipperName, COUNT(Orders.OrderID) 
AS NumberOfOrders 
FROM Orders
LEFT JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID
GROUP BY ShipperName;


SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country;


