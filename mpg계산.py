# ##mpg.csv파일 가져와서 실린더 개수 8 6 4 2 종류별 카운트 하기
# from collections import Counter
# f = open("mpg.csv", "r", encoding="utf-8")
# lines = f.readlines()
# result=set()

# for i in range(1, len(lines)):
#     line = lines[i].strip()
#     line = line[:len(line)-1]
#     values = line.split(",")
#     result.add(values[1])

# result=sorted(result)
# print(result)

# count_data = Counter(lines)
# print(count_data)

# # result2 = [0,0,0,0]
# # for j in range(4):
# #     for i in range(0, len(lines)):
# #         if 
# #         result[j] = result[j] + lines[i][j]

from collections import Counter

f = open("mpg.csv", "r", encoding="utf-8")
lines = f.readlines()
f.close()

# We'll collect the column values (e.g., cylinders in values[1])
column_values = []

for i in range(1, len(lines)):
    line = lines[i].strip()
    if line:  # skip empty lines
        values = line.split(",")
        column_values.append(values[1])  # assuming values[1] is the column you want

# Count occurrences of each unique value
count_data = Counter(column_values)

# Optional: sort by key
for key in sorted(count_data.keys()):
    print(f"{key}: {count_data[key]} 개")
    
    

# f.close



#풀이
f= open("mpg.csv","r")
lines = f.readlines()
f.close()

lines = lines[1:] #1번방부터 끝까지 복사
#print(lines[:4])
cylinder_count={}
for line in lines:
    line = line[:len(line)-1] #마지막에 있는 \n지우기
    values = line.split(",")
    if values[1] in cylinder_count.keys():
        cylinder_count[values[1]]+=1
    else:
        cylinder_count[values[1]]=1

print(cylinder_count)
