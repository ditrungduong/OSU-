def my_generator():
    value = 1
    while True:
        if value == 1:
            yield "2"
        elif value == 2:
            yield "12"
        else:
            x = "12"
            for i in range(3, value+1):
                x += "$"
                l = len(x)
                count = 1
                temp = ""
                for y in range(1, l):
                    if x[y] != x[y-1]:
                        temp += str(count)
                        temp += x[y-1]
                        count = 1
                    else:
                        count += 1
                    x = temp
                yield x
            value += 1
print(my_generator())

