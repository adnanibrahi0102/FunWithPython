import time


def cache(func):
    cached_value ={}
    print("Cache" ,cached_value)
    def wrapper(*args, **kwargs):
        if args in cached_value:
            return cached_value[args]
        result = func(*args, **kwargs)
        cached_value[args] = result
        return result
    return wrapper



@cache
def calculate(a,b):
    time.sleep(4)
    return a + b

print(calculate(1,6))
print(calculate(1,6))
print(calculate(30,56))
print(calculate(10,56))
print(calculate(30,46))
print(calculate(30,46))
