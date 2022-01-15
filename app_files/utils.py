from math import sqrt
from math import inf


def greatest_common_divisor(num1, num2):
    if num1 == 0:
        return num2
    return greatest_common_divisor(num2 % num1, num1)


def check_relatively_prime_numbers(num1, num2):
    if greatest_common_divisor(num1, num2) == 1:
        return True
    return False


def count_divisors(num):
    count = 0
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            if num / i == i:
                count += 1
            else:
                count += 2
    return count


def get_min_cost(node_info):
    min_cost = inf
    for stack in node_info:
        for block in stack:
            block_cost = count_divisors(block)
            min_cost = min(block_cost, min_cost)
    return min_cost


def get_max_cost(node_info):
    max_cost = -inf
    for stack in node_info:
        for block in stack:
            block_cost = count_divisors(block)
            max_cost = max(block_cost, max_cost)
    return max_cost


def check_valid_file(initial_state, target_heights):
    total_nodes = sum(target_heights)

    block_count = 0
    for stack in initial_state:
        block_count += len(stack)

    if total_nodes != block_count:
        return False
    return True

