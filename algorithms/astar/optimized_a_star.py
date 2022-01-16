from app_files.tree_node import TreeNode
import app_files.globals as globals


def optimized_a_star(graph, output_file, heuristic_type='trivial heuristic'):
    """
    Optimized A* algorithm. Generates a single solution.
    ```

    Parameters:
    -----------
        :param graph: Graph
            the problem graph
        :param output_file: str
            the path to the output file
        :param heuristic_type: str
            the type of heuristic

    Returns:
    --------
        :return: None
    """

    # opened_queue contains the candidate nodes for expansion
    opened_queue = [TreeNode(info=graph.initial_state,
                             parent=None,
                             g_cost=0,
                             h_cost=graph.get_h_cost(graph.initial_state))]

    # closed_queue contains the expanded nodes
    closed_queue = []

    while len(opened_queue) > 0:
        current_node = opened_queue.pop(0)
        closed_queue.append(current_node)

        # testing if the current_node is the target state of the problem
        if graph.is_target(current_node.info):
            globals.update_end_time()  # updating the end_time of process
            current_node.print_path(output_file=output_file, print_cost=True, print_length=True)  # printing the path
            globals.print_extra_information(output_file=output_file, current_node=current_node)  # printing extra info
            return

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
            found_in_opened_queue = False
            for node in opened_queue:
                if successor.info == node.info:
                    found_in_opened_queue = True
                    if successor.f_cost >= node.f_cost:
                        successors_list.remove(successor)
                    else:
                        opened_queue.remove(node)
                    break
            if not found_in_opened_queue:
                for node in closed_queue:
                    if successor.info == node.info:
                        if successor.f_cost >= node.f_cost:
                            successors_list.remove(successor)
                        else:
                            closed_queue.remove(node)
                        break

        for successor in successors_list:
            pos = 0
            found_pos = False
            for pos in range(len(opened_queue)):
                if opened_queue[pos].f_cost > successor.f_cost or (opened_queue[pos].f_cost == successor.f_cost
                                                                   and opened_queue[pos].g_cost <= successor.g_cost):
                    found_pos = True

            if found_pos:
                opened_queue.insert(pos, successor)
            else:
                opened_queue.append(successor)
