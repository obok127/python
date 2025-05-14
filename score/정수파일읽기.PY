f = open("정수.txt", "r")
lines = f.readlines()
sum =0
for line in lines:
    if "\n"in line: #데이터 파일 만들 때 커서를 맨 뒤에 두면 안 써도 됨
        line = line[: len(line) - 1]
    print(line)
    sum += int(line)
f.close()

print("평균", sum/len(lines))

