people = [19, 32, 10, 14]
grades = [[4, 4, 4, 4, 4, 4], [5, 3, 2, 5, 4, 4, 5], [3, 4], [1, 1, 1, 3, 2, 2, 4, 5, 1]]
p = []
for i in grades:
    sr = sum(i) / len(i)
    p.append(sr)
for h, k in enumerate(p, 1):
    print(f'В классе {h} оценочки: {round(k, 1)}')
