def sum_func(final_value_, multiple_):
    """
        You will pass the initial value and the multiple that
        you want to divide to generate the sum.
        param1 = final_value that will finish the loop.
        param2 = multiple that will change the sum.
    """
    sum_result = 0
    for i in range(1, int(final_value_) + 1, 1):
        if int(i) % int(multiple_) == 0:
            print(i)
            sum_result = sum_result + i
    return sum_result