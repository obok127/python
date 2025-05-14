#파일 읽기
f = open("score.txt", "r", encoding = "utf-8")
lines = f.readlines()
f.close

sum =0
count =0
for line in lines:
    line = line.strip()
    items = line.split(",")
    numbers = items[1:]
    for num in numbers:
        print(num)
        sum += int(num)
        count += 1

print("총점",sum)
print("평균",sum/count)


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