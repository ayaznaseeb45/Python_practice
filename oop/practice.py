class Demo:
    def __init__(self):
        print("Object created")

    def __del__(self):
        print("Object destroyed")


x = Demo()
del x

print(x)   # ❌ yahan error
