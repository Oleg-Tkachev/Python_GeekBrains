
n, m, s = map(int, input().split())
sum_resume, count = 0, 0
array_n = []
array_m = []


for i in range(max(n, m)):
    a, b = input().split()
    array_n.append(int(a.replace('-', '0')))
    array_m.append(int(b.replace('-', '0')))
array_m.append(0)
array_n.append(0)

while sum_resume < s and array_n[0] != 0 and array_m[0] != 0:
    if sum(array_n[:2]) < sum(array_m[:2]):
        if sum_resume + array_n[0] <= s:
            sum_resume += array_n.pop(0)
            count += 1
            continue
        elif sum_resume + array_m[0] <= s:
            sum_resume += array_m.pop(0)
            count += 1
            continue
        else:
            break
    if sum(array_n[:2]) > sum(array_m[:2]):
        if sum_resume + array_m[0] <= s:
            sum_resume += array_m.pop(0)
            count += 1
            continue
        elif sum_resume + array_n[0] <= s:
            sum_resume += array_n.pop(0)
            count += 1
            continue
        else:
            break
    if sum(array_n[:2]) == sum(array_m[:2]):
        if sum_resume + array_n[0] <= s:
            if array_n[0] > array_m[0]:
                sum_resume += array_n.pop(0)
                count += 1
            elif sum_resume + array_m[0] <= s:
                sum_resume += array_m.pop(0)
                count += 1
        elif sum_resume + array_m[0] <= s:
            if array_m[0] > array_n[0]:
                sum_resume += array_m.pop(0)
                count += 1
            elif sum_resume + array_n[0] <= s:
                sum_resume += array_n.pop(0)
                count += 1
        else:
            break

if sum_resume < s:
    while True:
        if array_n[0] != 0 and sum_resume + array_n[0] <= s:
            sum_resume += array_n.pop(0)
            count += 1
        elif array_m[0] != 0 and sum_resume + array_m[0] <= s:
            sum_resume += array_m.pop(0)
            count += 1
        else:
            break

print(count)