def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def main():
    sum = 0
    for value in fibonacci():
        if value > 4000000:
            break
        elif value % 2 == 0:
            sum += value
        
    print sum

if __name__ == '__main__':
    main()