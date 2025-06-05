use mydb;

-- emp 테이블의 정보를 확인하고 primary key가 존재하면 삭제하려고 한다
select * from emp limit 10;
desc emp; -- empno가 primary key
insert into emp(empno, ename) values(8000, '장길산'); -- empno에 8000이 존재하기 때문에 insert가 안된다.
alter table emp drop primary key; -- primary key를 삭제한다.
desc emp; -- key값이 없어짐.

select * from emp; -- 8000번이 두번 들어가 있어서 empno를 primary key 지정할 수 없음. : empno 필드값이 이미 중복상태(에러)
alter table emp add constraint pk_emp primary key(empno); -- Duplicate entry로 나옴
delete from emp where empno = 8000 and ename = '장길산';