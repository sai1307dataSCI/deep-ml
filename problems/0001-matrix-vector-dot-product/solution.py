def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float]:
    if not a or len(a[0]) != len(b):
        return -1
    res = []
    for i in range(len(a)):
        product = 0
        for j in range(len(b)):
            product += a[i][j] * b[j]
        res.append(product)
    return res