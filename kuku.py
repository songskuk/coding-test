num = input("원하는 구구단 단수를 입력해주세요")
print(num + "단을 출력하겠습니다.")
for count in range(1,10) :
    result = int(num) * int(count)
    print (num + "x" + str(count) + "=" + str(result))
