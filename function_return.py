def get_product1(n, m):
    product = n * m


def get_product2(n, m):
    product = n * m
    return product


result = get_product1(5, 8)
print('calling function1, result=', result)

result = get_product2(5, 8)
print('calling function2, result=', result)
