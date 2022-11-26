import os


def get_max_profit(list):
    max_profit = 0
    current = 0

    for i in reversed(list):
        current = max(current, i)
        profit = current - i
        max_profit = max(max_profit, profit)

    # print(max_profit)
    return max_profit

list = [10, 7, 5, 8, 11, 9]
get_max_profit(list)
