n = int(input())

# f(1) 값을 배열에 저장 (0은 index 맞추기용)
res = [0, 0]

for i in range(2, n + 1):
    re = [res[i - 1]]           # case 3
    if i % 3 == 0:              # case 1
        re.append(res[i // 3])
    if i % 2 == 0:              # case 2
        re.append(res[i // 2])

    res.append(min(re) + 1)

print(res[n])