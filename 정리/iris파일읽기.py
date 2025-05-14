# 파일 읽기
# f = open("score.txt", "r", encoding="utf-8")
# lines = f.readlines()
# f.close

# sum = 0
# count = 0
# for line in lines:
#     line = line.strip()
#     items = line.split(",")
#     numbers = items[1:]
#     for num in numbers:
#         sum += int(num)
#         count += 1

# print("총점", sum)
# print("평균", sum / count)


# f = open("score.txt", "r")
# lines = f.readlines()
# sum =0
# for line in lines:
#     if "\n"in line:
#         line = line[: len(line) - 1]
#         #홍길동, 90,80,70 - 콤마로 자르면 list 타입 반환
#         line = line.split(",")
#     print(line)
#     sum += line


# f.close()

# print("총점",sum)
# print("평균", sum/len(lines))

# 한글처리 cp949 - 윈도우 방식, 표준 utf-8, vscode가 utf-8

f = open("iris.csv", "r", encoding="utf-8")
lines = f.readlines()


total =[0,0,0,0]
count = 0

for line in lines[1:]:
    line = line.strip()
    items = line.split(",")

    for i in range(4):
        total[i] += float(items[i])
    
    count +=1
avg = [t / count for t in total]

print("합계", total)
print("평균", avg)


#풀이
f = open("iris.csv", "r", encoding="utf-8")
lines = f.readlines()
irisList = []

for i in range(1, len(lines)):
    line = lines[i].strip()
    line = line[:len(line)-1]
    print(i,line)
    values = line.split(",")
    data = [float(values[0]), float(values[1]),float(values[2]),float(values[3])]
    irisList.append(data)

f.close

for iris in irisList:
    print(iris)

result = [0,0,0,0]
for j in range(4):
    for i in range(0, len(irisList)):
        result[j] = result[j] + irisList[i][j]

count = len(irisList)
for i in range(4):
    print(f"{result[i]/count:.2f}", end='\t'),
print()