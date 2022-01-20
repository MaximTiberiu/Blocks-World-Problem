from app_files.tree_node import TreeNode
import app_files.globals as globals


def DFI(graph, output_file, current_node, depth, number_of_solutions, heuristic_type):
    """
    Iterative DFS algorithm.
    ```

    Parameters:
    -----------
        :param graph: Graph
            the problem graph
        :param output_file: str
            the path tot the output file
        :param current_node: TreeNode
            the current_node of the search tree
        :param depth: int
            the maximum depth of the tree
        :param number_of_solutions: int
            the number of solutions to be found
        :param heuristic_type: str
            the type of heuristic

    Returns:
    --------
        :return: int
            the number of searched solutions
    """
    if depth == 1 and graph.is_target(current_node.info):
        globals.update_end_time()
        current_node.print_path(output_file=output_file, print_cost=True, print_length=True)
        globals.print_extra_information(output_file=output_file, current_node=current_node)

        number_of_solutions -= 1
        if number_of_solutions == 0:
            return number_of_solutions

    if depth > 1:
        successors_list = graph.get_successors(current_node=current_node, heuristic_type=heuristic_type)
        if successors_list == 'Time out!':
            output_file.write('Time out! There are no solutions!')
            exit(1)
        globals.check_max_num_of_nodes(len(successors_list))
        globals.add_computed_nodes(len(successors_list))

        for successor in successors_list:
            if number_of_solutions != 0:
                number_of_solutions = DFI(graph=graph,
                                          output_file=output_file,
                                          current_node=successor,
                                          depth=depth - 1,
                                          number_of_solutions=number_of_solutions,
                                          heuristic_type=heuristic_type)
    return number_of_solutions


def iterative_depth_first_search(graph, output_file, number_of_solutions=1, heuristic_type='trivial heuristic'):
    """
    Container for DFI algorithm.
    ```

    Parameters:
    -----------
        :param graph: Graph
            the problem graph
        :param output_file: str
            the path tot the output file
        :param number_of_solutions: int
            the number of solutions to be found
        :param heuristic_type: str
            the type of heuristic

    Returns:
    --------
        :return: None
    """
    for i in range(1, 11):
        if number_of_solutions == 0:
            return
        number_of_solutions = DFI(graph=graph,
                                  output_file=output_file,
                                  current_node=TreeNode(info=graph.initial_state, parent=None),
                                  depth=i,
                                  number_of_solutions=number_of_solutions,
                                  heuristic_type=heuristic_type)


