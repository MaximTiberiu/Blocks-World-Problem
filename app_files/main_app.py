import sys
from sys import argv

from os.path import exists
from os import mkdir, listdir

from app_files.graph import Graph

from algorithms.bfs import breadth_first_search, optimized_breadth_first_search
from algorithms.dfs import depth_first_search, iterative_depth_first_search
from algorithms.ucs import uniform_cost_search, optimized_uniform_cost_search
from algorithms.astar import a_star, optimized_a_star
from algorithms.greedy import greedy

from app_files.utils import check_valid_file

import app_files.globals as globals

# TODO ↓


def list_algorithms():
    print('Algorithms:')
    print('1. Breadth First Search')
    print('2. Depth First Search')
    print('3. Iterative Depth First Search')
    print('4. Uniform Cost Search')
    print('5. A*')
    print('6. Greedy')

    option = 0
    read_validation = False
    while not read_validation:
        option = int(input('Please select your option: '))
        if option in [1, 2, 3, 4, 5, 6]:
            read_validation = True
        else:
            print('Invalid option! Please select your option again!')
    return option


def list_heuristics():
    heuristic_dictionary = {1: 'trivial heuristic', 2: 'first admissible heuristic',
                            3: 'second admissible heuristic', 4: 'inadmissible heuristic'}

    print('Heuristics:')
    print('1. Trivial heuristic')
    print('2. First admissible heuristic')
    print('3. Second admissible heuristic')
    print('4. Inadmissible heuristic')

    option = 0
    read_validation = False
    while not read_validation:
        option = int(input('Please select your option: '))
        if option in [1, 2, 3, 4]:
            read_validation = True
        else:
            print('Invalid option! Please select your option again!')
    return heuristic_dictionary[option]


class MainApp:
    def __init__(self):
        try:
            self.input_folder = argv[1]
            self.output_folder = argv[2]
            self.number_of_searched_solution = int(argv[3])
            sys.setrecursionlimit(6000)

        except IndexError:
            print('Initialization error: invalid number of arguments!')
            exit(1)

        if not exists(self.input_folder):
            print('Initialization error: invalid input_folder!')
            exit(1)

        if not exists(self.output_folder):
            mkdir(self.output_folder)
            print('Folder ' + self.output_folder + ' does not exist! It was created automatically by the system.')

    def start_app(self):
        algorithm_option = list_algorithms()
        heuristic_option = list_heuristics()

        files = listdir(self.input_folder)
        for file in files:
            input_file_name = self.input_folder + '/' + file
            graph = Graph(input_file_name)

            globals.update_start_time()

            output_file_name = 'out_' + file
            output_file = open(self.output_folder + '/' + output_file_name, 'w')

            if not check_valid_file(graph.initial_state, graph.target_heights):
                output_file.write('Invalid input file! There are no solutions!')
                output_file.close()
                continue

            if algorithm_option == 1:
                if self.number_of_searched_solution == 1:
                    optimized_breadth_first_search.optimized_breadth_first_search(graph=graph,
                                                                                  output_file=output_file,
                                                                                  heuristic_type=heuristic_option)
                else:
                    breadth_first_search.breadth_first_search(graph=graph,
                                                              output_file=output_file,
                                                              number_of_solutions=self.number_of_searched_solution,
                                                              heuristic_type=heuristic_option)
            elif algorithm_option == 2:
                depth_first_search.depth_first_search(graph=graph,
                                                      output_file=output_file,
                                                      number_of_solutions=self.number_of_searched_solution,
                                                      heuristic_type=heuristic_option)
            elif algorithm_option == 3:
                iterative_depth_first_search.iterative_depth_first_search(graph=graph,
                                                                          output_file=output_file,
                                                                          number_of_solutions=
                                                                          self.number_of_searched_solution,
                                                                          heuristic_type=heuristic_option)
            elif algorithm_option == 4:
                if self.number_of_searched_solution == 1:
                    optimized_uniform_cost_search.optimized_uniform_cost_search(graph=graph,
                                                                                output_file=output_file,
                                                                                heuristic_type=heuristic_option)
                else:
                    uniform_cost_search.uniform_cost_search(graph=graph,
                                                            output_file=output_file,
                                                            number_of_solutions=self.number_of_searched_solution,
                                                            heuristic_type=heuristic_option)
            elif algorithm_option == 5:
                if self.number_of_searched_solution == 1:
                    optimized_a_star.optimized_a_star(graph=graph,
                                                      output_file=output_file,
                                                      heuristic_type=heuristic_option)
                else:
                    a_star.a_star(graph=graph,
                                  output_file=output_file,
                                  number_of_solutions=self.number_of_searched_solution,
                                  heuristic_type=heuristic_option)
            else:
                greedy.greedy(graph=graph,
                              output_file=output_file,
                              heuristic_type=heuristic_option)

            output_file.close()
