def caulenh_giatri(i, j, k):
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else:
        if j > k:
            j = i
        else:
            i = k
    return i, j, k

giatri = [
    (3, 5, 7),
    (3, 7, 5),
    (5, 3, 7),
    (5, 7, 3),
    (7, 3, 5),
    (7, 5, 3)
]

labels = [
"(a) i = 3, j = 5, and k = 7 -> ",
"(b) i = 3, j = 7, and k = 5 -> ",
"(c) i = 5, j = 3, and k = 7 -> ",
"(d) i = 5, j = 7, and k = 3 -> ",
"(e) i = 7, j = 3, and k = 5 -> ",
"(f) i = 7, j = 5, and k = 3 -> "]

for label, (i, j, k) in zip(labels, giatri):
    i, j, k = caulenh_giatri(i, j, k)
    print(f"{label} i = {i}, j = {j}, k = {k}")
