use mydb;

-- emp 테이블의 정보를 확인하고 primary key가 존재하면 삭제하려고 한다
select * from emp limit 10;
desc emp; -- empno가 primary key
insert into emp(empno, ename) values(8000, '장길산'); -- empno에 8000이 존재하기 때문에 insert가 안된다.
alter table emp drop primary key; -- primary key를 삭제한다.
-- edit - preference - sql editor - safe updates 체크 해제하고 재실행
-- 기본적으로 update del
desc emp; -- key값이 없어짐.

select * from emp; -- 8000번이 두번 들어가 있어서 empno를 primary key 지정할 수 없음. : empno 필드값이 이미 중복상태(에러)
alter table emp add constraint pk_emp primary key(empno); -- Duplicate entry로 나옴
delete from emp where empno = 8000 and ename = '장길산';

-- 외부키(foreign key)
desc dept;
/*
alter table 테이블명
add constraint 외부키이름
foreign key(필드명)
references 참조테이블명(참조필드명)
on delete cascade -- 부모 레코드 삭제 시 자식도 삭제
on update cascade -- 부모키값 변경시 자식도 자동으로 변경
*/
-- 1. 참조하는 테이블(dept)의 deptno가 반드시 primary 거나 unique조건을 만족해야 한다
-- 2. 데이터 타입이 동일해야 한다.
alter table emp add constraint fk_emp_dept
foreign key(deptno) 
references dept(deptno);
desc emp;

-- 테이블 상호간에 제약조건이 발생한다
select *from dept;
delete from dept where deptno=10; -- a foreign key constraint fails : 외부키 때문에 삭제 불가
select *from emp; -- 아직 홍길동한테 부서번호가 없다.
update emp set deptno =50 where empno =8000; -- foreign key constraint fails : 외부키 때문에 업데이트가 안됨.alter

-- join은 inner, outer, full - ansi 표준
/* emp 테이블에는 부서번호
dept 테이블에는 부서번호와 부서명
두 개 이상의 테이블을 하나로 묶어서 새로운 ㄴ정보를 창출한다
아래의 쿼리는 표준 아님, 다른 DBMS에서는 에러가 날 수 있다. (oracle, mysql)
*/
select A.empno, A.ename, A.deptno, B.dname
from emp A, dept B
where A.deptno=B.deptno; -- join 조건이 동등조건(equal)

-- 표준조인
select A.empno, A.ename, A.deptno, B.dname
from emp A
inner join dept B on A.deptno = B.deptno;

-- 회원번호가 7369, 7892, 9000, 7900, 7902
select A.empno, A.ename, A.deptno, B.dname
from emp A, dept B
where A.deptno = B.deptno and
A.empno in (7369, 7892, 8000, 7900, 7902) ;
-- 이 방식의 단점 : 조인조건과 검색 조건이 구분이 되질 않음. 그래서 조인이 여러번 이루어질 경우 보기 좋지 않다.

select A.empno, A.ename, A.deptno, B.dname
from emp A
inner join dept B on A.deptno = B.deptno
where A.empno in (7369, 7892, 8000, 7900, 7902) ;

-- inner join은 양쪽 테이블에 값이 존재할 때 된다.

-- outer join : left, right
-- from 절에 가까운 테이블이 left(left 테이블 다 출력)
-- from 절로부터 먼 테이블이 right(right 테이블 다 출력)

select A.empno, A.ename, A.deptno, B.dname
from emp A
left outer join dept B on A.deptno = B.deptno;

-- 중복성 배제
select distinct deptno from emp;

select A.empno, A.ename, A.deptno, B.dname
from emp A
right outer join dept B on A.deptno = B.deptno;
