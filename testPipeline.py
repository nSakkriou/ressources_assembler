def a(val):
    return val + 2

def b(val):
    return val + 3

def pipeline(data, f1, f2):
    data = f1(data)
    data = f2(data)

    return data

if __name__ == "__main__":
    d = 5
    print(pipeline(d, a, b))