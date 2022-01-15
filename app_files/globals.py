from datetime import datetime, timedelta
from sys import argv

max_number_of_nodes = 0
number_of_computed_nodes = 0
timeout = datetime.now() + timedelta(seconds=int(argv[4]))
start_time = datetime.now()
end_time = datetime.now()


def check_max_num_of_nodes(num):
    global max_number_of_nodes
    max_number_of_nodes = max(max_number_of_nodes, num)


def add_computed_nodes(num):
    global number_of_computed_nodes
    number_of_computed_nodes += num


def update_start_time():
    global start_time
    start_time = datetime.now()


def update_end_time():
    global end_time
    end_time = datetime.now()


def print_extra_information(output_file, current_node):
    global max_number_of_nodes, number_of_computed_nodes
    output_file.write('Time: ' + str(end_time - start_time) + '\n')
    output_file.write('Total number of computed nodes: ' + str(number_of_computed_nodes) + '\n')
    output_file.write('Max number of nodes: ' + str(max_number_of_nodes) + '\n')
    mark = '#' * (6 * len(current_node.info) - 1)
    output_file.write('\n' + mark + '\n\n')
