

n, m, s = input().split(' ')

n_list = []
m_list = []
count_resume_list = []
for i in range(max(int(n), int(m))):

    n_temp, m_temp = input().split(' ')
    n_list.append(int(n_temp))
    m_list.append(int(m_temp))

for i in range(len(n_list) + 1):
    if (temp_sum := sum(n_list[:i])) > int(s):
        break
    if int(s) >= temp_sum:
        for j in range(len(m_list)):
            temp_sum += m_list[j]
            if temp_sum > int(s):
                count_resume_list.append(i + j)
                break
    if int(s) >= temp_sum:
        count_resume_list.append(i + len(m_list))

print(max(count_resume_list))



# Надо как то оптемезировать программу. Превышение лимита времени выполнения


# Memory: 3156
# StdErr: Traceback (most recent call last):
#   File "script.py", line 9, in <module>
#     n_list.append(int(n_temp)) #if n_temp.isdigit() else None
# ValueError: invalid literal for int() with base 10: '-'
#
# Статус: Ошибка во время выполнения
# Превышение лимита времени выполнения
#
# __________________________________________________
#
# Memory: 2916
# StdErr: Traceback (most recent call last):
#   File "script.py", line 1, in <module>
#     n, m, s = input().split(' ')
# EOFError: EOF when reading a line
# Status: Runtime Error (NZEC)
# Статус: Ошибка во время выполнения
# Превышение лимита времени выполнения
