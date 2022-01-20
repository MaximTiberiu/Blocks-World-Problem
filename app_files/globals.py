from datetime import datetime, timedelta

max_number_of_nodes = 0
number_of_computed_nodes = 0
timeout = datetime.now()
start_time = datetime.now()
end_time = datetime.now()


def check_max_num_of_nodes(num):
    """
    Updates the maximum number of nodes.
    ```

    Parameters:
    -----------
        :param num: int
            the number of nodes

    Returns:
    --------
        :return: None
    """
    global max_number_of_nodes
    max_number_of_nodes = max(max_number_of_nodes, num)


def add_computed_nodes(num):
    """
    Updates the total number of nodes.
    ```

    Parameters:
    -----------
        :param num: int
            the number of nodes to be added to the total number
    Returns:
    --------
        :return: None
    """
    global number_of_computed_nodes
    number_of_computed_nodes += num


def update_start_time():
    """
    Updates the start time.
    ```

    Returns:
    --------
        :return: None
    """
    global start_time
    start_time = datetime.now()


def update_end_time():
    """
    Updates the end time.
    ```

    Returns:
    --------
        :return: None
    """
    global end_time
    end_time = datetime.now()


def initialize_timeout(timeout_value):
    """
    Initializes the timeout time.
    ```

    Parameters:
    -----------
        :param timeout_value: int
            the timeout value

    Returns:
    --------
        :return: None
    """
    global timeout
    timeout = datetime.now() + timedelta(seconds=timeout_value)


def print_extra_information(output_file, current_node):
    """
    Prints the global information.
    ```

    Parameters:
    -----------
        :param output_file: str
            the path to the output file
        :param current_node: TreeNode
            the current node of the tree

    Returns:
    --------
        :return: None
    """
    global max_number_of_nodes, number_of_computed_nodes
    output_file.write('Time: ' + str(end_time - start_time) + '\n')
    output_file.write('Total number of computed nodes: ' + str(number_of_computed_nodes) + '\n')
    output_file.write('Max number of nodes: ' + str(max_number_of_nodes) + '\n')
    mark = '#' * (6 * len(current_node.info) - 1)
    output_file.write('\n' + mark + '\n\n')
