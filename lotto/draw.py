import sys
import hLotto

if (len(sys.argv) > 2):
    exit
index = int(sys.argv[1])
count = 5

hoyaLucky = hLotto.CLotto()
result = hoyaLucky.DrawNumber1(index, count)
for i in range(count):
    print(result[i])
