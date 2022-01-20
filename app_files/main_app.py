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


def list_algorithms():
    """
    Lists the algorithms that can be used in this app and reads the option of the user.
    ```

    Returns:
    --------
        :return: int
            the user's choice of which algorithm he wants to use
    """
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
    """
        Lists the heuristics that can be used in this app and reads the option of the user.
        ```

        Returns:
        --------
            :return: int
                the user's choice of which heuristic he wants to use
    """
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
    """
    MainApp -> class for representing the main application data
    ```

    Attributes
    ----------
        :arg input_folder: str
            the path to the input folder
        :arg output_folder: str
            the path to the output folder
        :arg number_of_searched_solutions: int
            the number of searched solutions, if applicable
        :arg timeout: int
            the timeout value

    Methods:
    --------
        start_app(): None
            Main function used to start the application.
    """
    def __init__(self):
        """
        Constructs all the necessary attributes for the TreeNode object.
        ```

        """
        try:
            self.input_folder = argv[1]
            self.output_folder = argv[2]
            self.number_of_searched_solution = int(argv[3])
            self.timeout = int(argv[4])
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
        """
        Main function used to start the application.
        ```

        """
        algorithm_option = list_algorithms()
        heuristic_option = list_heuristics()

        files = listdir(self.input_folder)
        for file in files:
            input_file_name = self.input_folder + '/' + file
            graph = Graph(input_file_name)

            globals.update_start_time()
            globals.initialize_timeout(self.timeout)

            output_file_name = 'out_' + file
            output_file = open(self.output_folder + '/' + output_file_name, 'w')

            if not check_valid_file(graph.initial_state, graph.target_heights):
                output_file.write('There are no solutions!')
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
