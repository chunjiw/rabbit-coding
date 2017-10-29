# LaiData python coding final exam
# question 4


class GraphNode:
    def __init__(self, val):
        self.value = val
        self.neighbors = None


def get_components_count(graph):
    """ input is a set of GraphNode
    """
    labels = 0
    while graph:
        tolabel = {graph.pop()}
        while tolabel:
            node = tolabel.pop()
            if node in graph:
                graph.remove(node)    # label the node as visited
            for nei in node.neighbors:
                if nei in graph:
                    tolabel.add(nei)
        labels += 1
    return labels


if __name__ == "__main__":
    node1 = GraphNode(1)
    node2 = GraphNode(1)
    node3 = GraphNode(1)
    node4 = GraphNode(1)
    node5 = GraphNode(1)
    node1.neighbors = [node2, node3]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node1]
    node4.neighbors = [node5]
    node5.neighbors = [node4]
    print(get_components_count({node1, node2, node3, node4, node5}))