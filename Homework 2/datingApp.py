
boys = input("Введите имена юношей через запятую: ").split(", ")
girls = input("Введите имена девушек через запятую: ").split(", ")


boys_sorted = sorted(boys)
girls_sorted = sorted(girls)


if len(boys_sorted) != len(girls_sorted):
    print("Внимание, кто-то может остаться без пары.")
else:
    print("Идеальные пары:")

    for i in range(len(boys_sorted)):
        print(f"{boys_sorted[i]} и {girls_sorted[i]}")
