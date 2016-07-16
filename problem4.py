def is_palindrome(value):
    return value == value[::-1]

def main():
    result = max(x * y for x in xrange(999, 99, -1) 
                 for y in xrange(999, 99, -1) 
                 if is_palindrome(str(x*y)))
    print result

if __name__ == '__main__':
    main()