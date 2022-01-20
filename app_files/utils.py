from math import sqrt
from math import inf


def greatest_common_divisor(num1, num2):
    """
    Finds the greatest common divisor of two numbers.
    ```

    Parameters:
    -----------
        :param num1: int
            the first number
        :param num2: int
            the second number

    Returns:
    --------
        :return: int
            the greatest common divisor for num1 and num2
    """
    if num1 == 0:
        return num2
    return greatest_common_divisor(num2 % num1, num1)


def check_relatively_prime_numbers(num1, num2):
    """
    Checks if two numbers are relatively prime.
    ```

    Parameters:
    -----------
        :param num1: int
            the first number
        :param num2: int
            the second number

    Returns:
    --------
        :return: bool
            returns true if the numbers are relatively prime, otherwise, returns false
    """
    if greatest_common_divisor(num1, num2) == 1:
        return True
    return False


def count_divisors(num):
    """
    Counts the divisors of a number.
    ```

    Parameters:
    -----------
        :param num: int
            the number for which the number of divisors will be found

    Returns:
    --------
        :return: int
            the number of divisors for num
    """
    count = 0
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            if num / i == i:
                count += 1
            else:
                count += 2
    return count


def get_min_cost(node_info):
    """
    Gets the minimum cost to move a block.
    ```

    Parameters:
    -----------
        :param node_info: list
            list of stacks representing the current state of a node
    Returns:
    --------
        :return: int
            the minimum cost to move a block
    """
    min_cost = inf
    for stack in node_info:
        for block in stack:
            block_cost = count_divisors(block)
            min_cost = min(block_cost, min_cost)
    return min_cost


def get_max_cost(node_info):
    """
        Gets the maximum cost to move a block.
        ```

        Parameters:
        -----------
            :param node_info: list
                the list of stacks representing the current state of a node
        Returns:
        --------
            :return: int
                the maximum cost to move a block
    """
    max_cost = -inf
    for stack in node_info:
        for block in stack:
            block_cost = count_divisors(block)
            max_cost = max(block_cost, max_cost)
    return max_cost


def check_valid_file(initial_state, target_heights):
    """
    Checks if a file is valid or not.
    ```

    Parameters:
    -----------
        :param initial_state: list
            the list of stacks representing the initial state of the node
        :param target_heights: list
            the list of target heights

    Returns:
    --------
        :return: bool
            returns true if the file is valid, otherwise, returns false
    """
    if len(initial_state) != len(target_heights):
        return False

    total_nodes = sum(target_heights)
    block_count = 0

    for stack in initial_state:
        block_count += len(stack)

    if total_nodes != block_count:
        return False

    max_block_position = get_max_block_position(initial_state)
    max_block = initial_state[max_block_position[0]][max_block_position[1]]

    if check_max_block_divides(initial_state, max_block):
        if len(initial_state[max_block_position[0]]) != (max_block_position[1] + 1) and (1 not in target_heights):
            return False
    return True


def get_max_block_position(initial_state):
    """
    Gets the position of the block with the maximum value.
    ```

    Parameters:
    -----------
        :param initial_state: list
             the list of stacks representing the initial state of the node

    Returns:
    --------
        :return: list
            the list that contains the position of the block in the node with the maximum value
    """
    max_block = -inf
    pos = [-1, -1]

    for i in range(len(initial_state)):
        for j in range(len(initial_state[i])):
            if initial_state[i][j] > max_block:
                max_block = initial_state[i][j]
                pos = [i, j]
    return pos


def check_max_block_divides(initial_state, max_block):
    """
    Checks if the maximum value from the node's blocks is relatively prime to the other values.
    ```

    Parameters:
    -----------
        :param initial_state: list
            the list of stacks representing the initial state of the node
        :param max_block: int
            the maximum value

    Returns:
    --------
        :return: bool
            returns true, if the condition is satisfied, otherwise, returns false
    """
    for stack in initial_state:
        for block in stack:
            if check_relatively_prime_numbers(block, max_block):
                return False
    return True
