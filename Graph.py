import matplotlib.pyplot as plt


class Graph(object):
    '''
    初始化图需要的参数类型以及形式：
    nodes: dict
        {0: [x0,y0], 1: [x1,y1], ...]
    edges: list
        [[index1, index2], [index3, index4], ...]
    '''

    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        # 构建邻接表
        self.adj_list = [[] for _ in range(len(nodes))]
        for edge in edges:
            self.adj_list[edge[0]].append(edge[1])
            self.adj_list[edge[1]].append(edge[0])

    # 画出图
    def draw(self, title=''):
        for edge in self.edges:
            x = []
            x.append(self.nodes[edge[0]][0])
            x.append(self.nodes[edge[1]][0])

            y = []
            y.append(self.nodes[edge[0]][1])
            y.append(self.nodes[edge[1]][1])
            plt.plot(x, y, 'y-')

        for node in self.nodes:
            plt.plot(self.nodes[node][0], self.nodes[node][1], 'r.')

        plt.title(title)
        plt.show()
