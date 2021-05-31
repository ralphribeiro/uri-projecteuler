def organiza_upas(n, uvs):
    to_remove = []
    for uv in uvs:
        if min(uv) not in to_remove:
            to_remove.append(min(uv))

    return [u for u in range(1, n+1) if u not in to_remove]


N1 = 10
M1 = 4
UVS1 = [(10, 9), (8, 7), (8, 6), (1, 2)]

r1 = organiza_upas(N1, UVS1)

assert len(r1) == 6
assert r1 == [2, 3, 4, 5, 8, 10]


N2 = 13
M2 = 19
UVS2 = [
    (12, 1), (12, 2), (12, 3), (12, 4), (10, 5), (13, 6),
    (3, 7), (1, 8), (1, 9), (11, 10), (7, 11), (12, 13),
    (1, 5), (9, 13), (6, 2), (8, 11), (8, 7), (11, 3), (7, 12)
]

r2 = organiza_upas(N2, UVS2)
print(r2)

assert len(r2) == 5
assert r2 == [2, 4, 5, 11, 13]
