from app_files.tree_node import TreeNode
from copy import deepcopy
from datetime import datetime

from app_files.utils import check_relatively_prime_numbers
from app_files.utils import count_divisors
from app_files.utils import get_min_cost, get_max_cost

import app_files.globals as globals


class Graph:
    # TODO docstring
    def __init__(self, input_file):
        # TODO docstring

        def get_stacks(string):
            # TODO docstring
            strings_stacks = string.strip().split('\n')
            stacks_list = [list(map(int, strings_stack.strip().split(';'))) if strings_stack != '~' else []
                           for strings_stack in strings_stacks]
            return stacks_list

        file = open(input_file, 'r')
        file_content = file.read()
        input_file_content = file_content.split('-----')
        self.initial_state = get_stacks(input_file_content[0])
        self.target_heights = list(map(int, input_file_content[1].split()))

        # print('Initial state: ', self.initial_state)
        # print('Target heights: ', self.target_heights)

    def is_target(self, node_info):
        if len(node_info) != len(self.target_heights):
            return 0

        for i in range(len(node_info)):
            if len(node_info[i]) != self.target_heights[i]:
                return 0
        return 1

    def get_successors(self, current_node, heuristic_type):
        if datetime.now() > globals.timeout:
            return 'Time out!'

        successors_list = []
        current_node_stack = current_node.info
        num_of_stacks = len(current_node_stack)

        for id_copy in range(num_of_stacks):
            temp_copy = deepcopy(current_node_stack)
            if len(temp_copy[id_copy]) == 0:
                continue
            block = temp_copy[id_copy].pop()

            for id_paste in range(num_of_stacks):
                if id_copy == id_paste:
                    continue

                paste_level = len(temp_copy[id_paste])
                if paste_level != 0:
                    paste_block = temp_copy[id_paste][-1]
                    if not check_relatively_prime_numbers(block, paste_block):
                        continue

                try:
                    previous_paste_block = temp_copy[id_paste - 1][paste_level]
                except IndexError:
                    previous_paste_block = -1
                try:
                    next_paste_block = temp_copy[id_paste + 1][paste_level]
                except IndexError:
                    next_paste_block = -1

                if block == previous_paste_block or block == next_paste_block:
                    continue

                new_stacks_list = deepcopy(temp_copy)
                new_stacks_list[id_paste].append(block)
                block_move_cost = count_divisors(block)

                if not current_node.in_path(new_stacks_list):
                    new_node = TreeNode(info=new_stacks_list,
                                        parent=current_node,
                                        g_cost=current_node.g_cost + block_move_cost,
                                        h_cost=self.get_h_cost(new_stacks_list, heuristic_type))
                    successors_list.append(new_node)
        return successors_list

    def get_h_cost(self, node, heuristic_type='trivial heuristic'):
        if heuristic_type == 'trivial heuristic':
            if self.is_target(node) == 0:
                return get_min_cost(node)
            return 0
        elif heuristic_type == 'first admissible heuristic':
            heuristics = []
            for i in range(len(node)):
                h_cost = get_min_cost(node)
                diff = self.target_heights[i] - len(node[i])
                if diff > 0:
                    h_cost += diff
                heuristics.append(h_cost)
            return min(heuristics)
        elif heuristic_type == 'second admissible heuristic':
            heuristics = []
            for i in range(len(node)):
                h_cost = get_min_cost(node)
                diff = self.target_heights[i] - len(node[i])
                if diff > 0:
                    for j in range(diff, len(node[i])):
                        h_cost += count_divisors(node[i][j])
                heuristics.append(h_cost)
            return min(heuristics)
        elif heuristic_type == 'inadmissible heuristic':
            heuristics = []
            for i in range(len(node)):
                h_cost = (self.target_heights[i] - len(node[i])) * get_max_cost(node)
                heuristics.append(abs(h_cost))
            return max(heuristics)

    def __repr__(self):
        output_string = ''
        for key, value in self.__dict__.items():
            output_string += '{} = {}\n'.format(key, value)
        return output_string
