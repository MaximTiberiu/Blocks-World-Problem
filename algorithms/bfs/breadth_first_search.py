from app_files.tree_node import TreeNode
import app_files.globals as globals


def breadth_first_search(graph, output_file, number_of_solutions=1, heuristic_type='trivial heuristic'):
    queue = [TreeNode(info=graph.initial_state, parent=None)]

    while len(queue) > 0:
        current_node = queue.pop(0)

        if graph.is_target(current_node.info):
            globals.update_end_time()
            current_node.print_path(output_file=output_file, print_cost=True, print_length=True)
            globals.print_extra_information(output_file=output_file, current_node=current_node)

            number_of_solutions -= 1
            if number_of_solutions == 0:
                return

        successors_list = graph.get_successors(current_node=current_node, heuristic_type=heuristic_type)
        if successors_list == 'Time out!':
            output_file.write('Time out! There are no solutions!')
            exit(1)
        globals.check_max_num_of_nodes(len(successors_list))
        globals.add_computed_nodes(len(successors_list))
        queue.extend(successors_list)
