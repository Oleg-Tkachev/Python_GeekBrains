import math

n, m, s = map(int, input().split())
sum_resume, count = 0, 0
qn = []
qm = []


for i in range(max(n, m)):
    a, b = input().split()
    qn.append(int(a.replace('-', '0')))
    qm.append(int(b.replace('-', '0')))
qn.append(0)            # Добавляем ноль в конце списка если он меньше
qm.append(0)            # Добавляем ноль в конце списка если он меньше

while sum_resume < s and qn[0] != 0 and qm[0] != 0:
    if sum(qn[:2]) < sum(qm[:2]):
        if sum_resume + qn[0] <= s:
            sum_resume += qn.pop(0)     # удаляем из списка 0-й элемент сдвигаем их выше
            count += 1
            continue
        elif sum_resume + qm[0] <= s:
            sum_resume += qm.pop(0)
            count += 1
            continue
        else:
            break
    if sum(qn[:2]) > sum(qm[:2]):
        if sum_resume + qm[0] <= s:
            sum_resume += qm.pop(0)
            count += 1
            continue
        elif sum_resume + qn[0] <= s:
            sum_resume += qn.pop(0)
            count += 1
            continue
        else:
            break
    if sum(qn[:2]) == sum(qm[:2]):
        if sum_resume + qn[0] <= s:
            if qn[0] > qm[0]:
                sum_resume += qn.pop(0)
                count += 1
            elif sum_resume + qm[0] <= s:
                sum_resume += qm.pop(0)
                count += 1
        elif sum_resume + qm[0] <= s:
            if qm[0] > qn[0]:
                sum_resume += qm.pop(0)
                count += 1
            elif sum_resume + qn[0] <= s:
                sum_resume += qn.pop(0)
                count += 1
        else:
            break


if sum_resume < s:
    while True:
        if qn[0] != 0 and sum_resume + qn[0] <= s:
            sum_resume += qn.pop(0)
            count += 1
        elif qm[0] != 0 and sum_resume + qm[0] <= s:
            sum_resume += qm.pop(0)
            count += 1
        else:
            break

print(count)