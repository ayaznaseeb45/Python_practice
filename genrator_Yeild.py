# =========================
# Generator
# =========================

# Definition:
# A generator is a function that produces values one at a time.
# it use yeild instead of return to produce a series of values.

def numbers():
    yield 1
    yield 2
    yield 3

gen = numbers()

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3


# =========================
# yield
# =========================

# Definition:
# 'yield' returns a value and pauses the function.
# When we call next(), the function continues from where it stopped.

def test():
    yield 10
    yield 20
    yield 30

gen = test()

print(next(gen))  # 10
print(next(gen))  # 20
print(next(gen))  # 30


# =========================
# return vs yield
# =========================

# return: returns a value and exits the function.
# yield: returns a value and pauses the function.