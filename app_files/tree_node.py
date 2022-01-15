class TreeNode:
    """
    TreeNode -> class for representing a node of a search tree
    ```

    Attributes
    ----------
        :arg info: int
            the information of the current node
        :arg parent: TreeNode
            the parent of the current node
        :arg g_cost: int
            the cost of the path from the root to the current node
        :arg h_cost: int
            the estimated cost of the path from the current node to the target node
        :arg f_cost: int
            the estimated total cost of the path from the root to the target node

    Methods:
    --------
        get_path(): list
            Builds the path in the searching tree starting from the calling node to the root of the tree.
        print_path(): int
            Prints the a tree path.
        in_path(): bool
             Checks whether or not a node is part of the path.
    """

    def __init__(self, info, parent, g_cost=0, h_cost=0):
        """
        Constructs all the necessary attributes for the TreeNode object.
        ```

        Parameters:
        -----------
            :param info: int
                the information of the current node
            :param parent: TreeNode
                the parent of the current node
            :param g_cost: int
                the cost of the path from the root to the current node
            :param h_cost: int
                the estimated cost of the path from the current node to the target node
        """
        self.info = info
        self.parent = parent
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = self.g_cost + self.h_cost

    def get_path(self):
        """
        Builds the path in the searching tree starting from the calling node to the root of the tree.
        ```

        Returns:
        --------
            :return: list
                the list of nodes that are part of the path
        """
        node = self
        path = [node]
        while node.parent is not None:
            path.insert(0, node.parent)
            node = node.parent
        return path

    def print_path(self, output_file, print_cost=False, print_length=False):
        """
        Prints the a tree path.
        ```

        Parameters:
        -----------
            :param output_file: str
                the path to the output file
            :param print_cost: bool
                parameter indicating whether or not the cost of the path is displayed
            :param print_length: bool
                parameter indicating whether or not the length of the path is displayed

        Returns:
        --------
            :return: int
                the length of the path
        """
        path = self.get_path()
        step_count = 1
        for node in path:
            output_file.write('STEP ' + str(step_count) + ':\n')
            output_file.write(str(node) + '\n')
            step_count += 1

        if print_cost:
            output_file.write('Cost: ' + str(self.g_cost) + '\n')

        if print_length:
            output_file.write('Path Length: ' + str(len(path)) + '\n')

        return len(path)

    def in_path(self, node_info):
        """
        Checks whether or not a node is part of the path.
        ```

        Parameters:
        -----------
            :param node_info: list
                the list of stacks representing the state of a node

        Returns:
        --------
            :return: bool
                true, if the node is part of the path, otherwise, false
        """
        path_node = self
        while path_node is not None:
            if node_info == path_node.info:
                return True
            path_node = path_node.parent
        return False

    def __eq__(self, other):
        return self.g_cost == other.g_cost

    def __lt__(self, other):
        return self.g_cost < other.g_cost

    def __repr__(self):
        output_string = ''
        output_string += str(self.info)
        return output_string

    def __str__(self):
        output_string = ''
        max_height = max([len(stack) for stack in self.info])
        for height in range(max_height, 0, -1):
            for stack in self.info:
                if len(stack) < height:
                    output_string += '      '
                else:
                    output_string += '[' + str(stack[height - 1]) + ']' + ' ' * (3 - len(str(stack[height - 1])) + 1)
            output_string += '\n'
        output_string += '=' * (6 * len(self.info) - 1)

        return output_string
