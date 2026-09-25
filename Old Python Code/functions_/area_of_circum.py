def circle_properties(radius):
    pi = 3.14
    area = pi * radius ** 2
    circumference = 2 * pi * radius
    return area, circumference

# Example usage:
a, c = circle_properties(5)
print("Area:", a)
print("Circumference:", c)