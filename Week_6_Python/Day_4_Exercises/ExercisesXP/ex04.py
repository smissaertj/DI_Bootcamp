float_list = []

for i in range(1, 6):
    float_list.append(i)
    if i == 5:
        break
    float_list.append(float_list[-1] + 0.5)

print(float_list)