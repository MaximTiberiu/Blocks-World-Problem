from app_files.tree_node import TreeNode
import app_files.globals as globals


def DFS(graph, output_file, current_node, number_of_solutions, heuristic_type):
    if number_of_solutions <= 0:
        return number_of_solutions

    if graph.is_target(current_node.info):
        globals.update_end_time()
        current_node.print_path(output_file=output_file, print_cost=True, print_length=True)
        globals.print_extra_information(output_file=output_file, current_node=current_node)

        number_of_solutions -= 1
        if number_of_solutions == 0:
            return number_of_solutions

    successors_list = graph.get_successors(current_node=current_node, heuristic_type=heuristic_type)
    if successors_list == 'Time out!':
        output_file.write('Time out! There are no solutions!')
        exit(1)
    globals.check_max_num_of_nodes(len(successors_list))
    globals.add_computed_nodes(len(successors_list))

    for successor in successors_list:
        if number_of_solutions != 0:
            number_of_solutions = DFS(graph=graph,
                                      output_file=output_file,
                                      current_node=successor,
                                      number_of_solutions=number_of_solutions,
                                      heuristic_type=heuristic_type)
    return number_of_solutions


def depth_first_search(graph, output_file, number_of_solutions=1, heuristic_type='trivial heuristic'):
    DFS(graph=graph,
        output_file=output_file,
        current_node=TreeNode(info=graph.initial_state, parent=None),
        number_of_solutions=number_of_solutions,
        heuristic_type=heuristic_type)
