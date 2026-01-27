
def kwargs_func(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
        print(end='')

kwargs_func(name= "Ayaz", gender= "Male")