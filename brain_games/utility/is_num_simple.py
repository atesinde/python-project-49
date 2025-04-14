def is_num_simple(number):
    for i in range(2, number // 2):
        if number % i == 0:
            return False
    return True