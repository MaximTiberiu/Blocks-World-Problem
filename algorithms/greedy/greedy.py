from app_files.tree_node import TreeNode
import app_files.globals as globals


def greedy(graph, output_file, heuristic_type='trivial heuristic'):
    queue = [TreeNode(info=graph.initial_state,
                      parent=None,
                      g_cost=0,
                      h_cost=graph.get_h_cost(graph.initial_state))]
    while len(queue) > 0:
        current_node = queue.pop(0)
        if graph.is_target(current_node.info):
            globals.update_end_time()
            current_node.print_path(output_file=output_file, print_cost=True, print_length=True)
            globals.print_extra_information(output_file=output_file, current_node=current_node)
            return

        successors_list = graph.get_successors(current_node=current_node, heuristic_type=heuristic_type)
        if successors_list == 'Time out!':
            output_file.write('Time out! There are no solutions!')
            exit(1)
        globals.check_max_num_of_nodes(len(successors_list))
        globals.add_computed_nodes(len(successors_list))

        for successor in successors_list:
            pos = 0
            found_pos = False
            for pos in range(len(queue)):
                if queue[pos].h_cost > successor.h_cost:
                    found_pos = True
                    break

            if found_pos:
                queue.insert(pos, successor)
            else:
                queue.append(successor)
