def numbers():
    yield 1
    yield 2
    yield 3


result = numbers()

print(next(result))  # 1
print(next(result))  # 2
print(next(result))  # 3


# Generator Python ka special function hota hai
# jo sari values aik saath return karne ke bajaye
# aik aik karke generate karta hai.