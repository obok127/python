#time.time() : 협정 세계 표준시를 사용하여 현재 시간을 실수 형태로 리턴하는 함수
#time.localtime : time.time()이 리턴한 실숫값을 사용해서 연/월/시/분/초 형태로 튜플 형태로 변환
#time.asctime : time.localtime의 값을 보기 쉽게 리턴하는 함수
#time.ctime : time.asctime(time.localtime(time.time()))
import time
print(time.ctime()) 


#time.strftime : 시간 관련 여러 포맷 코드 제공
import time
time.strftime('%x', time.localtime(time.time()))
# %a : Tue, %A: Tuesday
# %b : Jan, %B : January
# %c : Tue May 13 19:03:46 2025
# %y : 25, %Y : 2025 -> 이외에도 다양함.

#예제 :  현재 시간이 오전인지 오후인지 판단해서 "지금은 오전입니다." 또는 "지금은 오후입니다." 라고 출력
import time
a=time.strftime('%p', time.localtime(time.time()))
if a == "PM" :
    print("지금은 오후입니다.")
else:
    print("지금은 오전입니다.")

#gpt clean_code ver.
import time

current_period = time.strftime('%p', time.localtime())
#time.localtime(time.time()) → time.localtime()으로 축약 가능😲

message = "지금은 오후입니다." if current_period == "PM" else "지금은 오전입니다."
print(message)



#math.gcd : 최대공약수 계산 함수(python 3.5부터)
#math.lcm : 최소공배수 계산 함수(python 3.9부터)
import math
math.gcd(60, 100, 80)



#예제 : 기계 A와 B의 점검 주기를 입력받고 두 기계가 다시 동시에 점검을 받을 시점을 출력

import math

a = int(input())
b = int(input())

lcm = math.lcm(a, b)  
day = lcm // 24  
hour = lcm % 24 

if day<=0:
    print(f"두 기계가 다시 동시에 점검을 받는 시각은 {hour}시 입니다.")

else: 
    print(f"두 기계가 다시 동시에 점검을 받는 시각은 {day}일 후 {hour}시 입니다.")


