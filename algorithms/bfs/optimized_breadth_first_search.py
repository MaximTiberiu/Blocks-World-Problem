from app_files.tree_node import TreeNode
import app_files.globals as globals


def optimized_breadth_first_search(graph, output_file, number_of_solutions=1, heuristic_type='trivial heuristic'):
    """
    Optimized BFS algorithm. Generates more solutions, if required.
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

    # the queue is initialized with the root node (initial state of the problem)
    queue = [TreeNode(info=graph.initial_state, parent=None)]

    while len(queue) > 0:
        # the first node is popped out from the queue
        current_node = queue.pop(0)

        # generating the successors of the current_node
        successors_list = graph.get_successors(current_node=current_node, heuristic_type=heuristic_type)
        if successors_list == 'Time out!':
            # if the previously returned result is 'Time out!', the timeout condition has been activated
            output_file.write('Time out! There are no solutions!')
            exit(1)

        # updating extra info
        globals.check_max_num_of_nodes(len(successors_list))
        globals.add_computed_nodes(len(successors_list))

        for successor in successors_list:
            # testing if the successor is the target state of the problem
            if graph.is_target(successor.info):
                globals.update_end_time()  # updating the end_time of process
                successor.print_path(output_file=output_file, print_cost=True, print_length=True)  # printing the path
                globals.print_extra_information(output_file=output_file, current_node=current_node)  # printing extra info

                number_of_solutions -= 1
                if number_of_solutions == 0:
                    return

        queue.extend(successors_list)
