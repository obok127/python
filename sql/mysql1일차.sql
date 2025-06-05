-- emp 테이블의 내용을 다 보여줌 - 14건
select * from emp;

-- 데이터 전체 몇 건일까?
select count(*) from emp;

-- * : 아스테리스크 모든 필드
select empno, ename, job from emp;

-- aliasing : 별명 테이블명을 수정해서 부를 수 있다.
select empno, ename, job
from emp as e;

-- information_schema : DB에 사용자가 만드는 테이블 정보가 저장된다. aliasing 안 쓰면 저 DB가 다 검색해서 정보를 읽어오고, aliasing을 하면 캐시를 해서 DB정보를 메모리에 불러놓고 작업을 해서 작업 속도가 유리하다 
select e.empno, e.ename, e.job
from emp as e;

-- as 생략가능 count(필드명) dbms는 null값이 있을 경우 count를 하지 않음
-- count(*) - 필드 중에 null값이 아에 없는 필드를 기준으로 제일 많은 데이터count를 가져와라
select count(e.comm) from emp e;

/*
null값? 알 수 없는, python의 None, 수학적으로 무한대의 의미를 갖는다
null + 1 -> null(무한대)
null - 1 -> null(무한대)
수학 연산 다 가능(=,-,*,/,sin,cosin, tan, round......)
null값에 연산을 하면 결과는 null
파이썬의 if문, 함수를 써서 처리가능
DBMS의 쿼리는 ANSI표존이 있어서 비슷한데 함수는 각자 다르다
NVL - 오라클, ISNULL, IFNULL

IFNULL(필드명, 기본값)만일 필드명에서 값이 NULL이 아닌 값이 오면 그 값을 주고 NULL이면 기본값을 부여한다.
*/
SELECT SAL+COMM FROM EMP;

-- 연산을 통해서 새로운 컬럼을 만들었음, 수식이 필드명으로 나옴
-- 필드명도 aliasing을 통해서 다시 부여할 수 있다.
select empno,sal, comm, sal+ifnull(comm,0) as total_sal 
from emp;

-- 홍길동의 급여는 얼마입니다. 
select concat(ename, "님의 급여는", sal, "입니다.") as title
from emp;
-- 조건절
/*
select 필드들
from 테이블명
where 조건절 		해당 조건에 만족하는 데이터 = != < > <= >= 논리연산자 and, or, not
*/

select * from emp;

-- 이름이 smith인 사람

select *from emp where ename = 'SMITH';
select *from emp where ename = 'smith';

-- 이름이 smith이거나 ford 인 사람
select *from emp where ename = 'SMITH' or enmae = 'Ford';

-- 급여가 3000원 이상인 사원의 이름과 급여를 조회하시오.
select ename, sal from emp
where SAL>=3000;

-- 직무가 'MANAGER'인 사람의 정보를 조회하시오.
select *from emp 
where JOB='MANAGER';

-- 급여가 2000이상 5000이하인 사원을 조회하시오.
select *from emp 
where SAL>=2000 and SAL<=5000;

-- between -oracle, mysql 지원
select * from emp where sal between 2000 and 5000;

-- 커미션이 NULL이 아닌 사원을 조회하시오.
-- null은 관계연산자가 작동하지 않는다. is, is not을 써야 함.
select *from emp 
where COMM != 'NULL'; -- 결과 안나옴

select *from emp
where comm is not null;

-- 'A'로 시작하는 이름을 가진 사원을 조회하시오
-- ~로 시작하는 와일드 카드와 like 연산자 _(한 글자)%(여러글자)
select * from emp where ename like 'A%';
select * from emp where ename like '%A'; -- A로 끝나는
-- 이름 중간에 O가 들어가는 이름
select *from emp where ename like '%O%'; -- O가 들어가는
-- 두번째 글자에 O가 들어가는 경우
select *from emp where ename like '_O%'; -- 두번째 O가 들어가는

-- 부서번호가 10,20,30에 해당하는 사원을 조회하시오.
select *from emp
where deptno =10 or deptno =20 or deptno =30;
-- 나열해서 찾아야 할 경우 -> in 연산자
select *from emp where deptno in (10,20,30); -- (오라클의 경우 500개까지 가능)
select *from emp where deptno in (10,20) or deptno in (30); 

select empno from emp;
select empno
from emp
where empno in (7521.7565, 7903, 7934);

-- 급여가 1000미만이거나 커미션이 500초과인 사원을 조회하시오.
select *from emp
where sal<1000 or comm>500;

-- 관리자가 없는 사원(mgr이 NULL)을 조회하시오.
select *from emp
where mgr is null;

-- 직무가 'CLERK'이면서 부서버노가 20인 사원을 조회하시오.
select *from emp
where job ='CLERK' and Deptno =20;

-- 입사일이 1981년 이전인 사원을 조회하시오.
select *from emp where hiredate< '1981-01-01';

select * 
from emp
-- where
order by ename; -- 이름으로 오름차순
-- order by 필드명 asc 또는 desc

select*
from emp
order by ename desc; -- 내림차순 정렬
