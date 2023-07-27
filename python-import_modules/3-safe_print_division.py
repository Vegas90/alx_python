def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(result))

    return result

# Test cases
#print(safe_print_division(10, 2))
#print(safe_print_division(8, 0))
#print(safe_print_division(12, 4))
