import random
import matplotlib.pyplot as plt


class LPA(object):
    __node_type = ['r.', 'b.', 'g.',
                   'ro', 'bo', 'go',
                   'r*', 'b*', 'g*',
                   'r+', 'b+', 'g+']

    def __init__(self, g):
        self.g = g
        self.nodes_num = len(g.nodes)
        # 标签字典，用于记录图中每个点的标签
        self.label_dict = {i: -1 for i in range(self.nodes_num)}

    # 初始化标签字典，使得每个节点拥有各自的标签
    def __init_label_dict(self):
        for i in range(self.nodes_num):
            self.label_dict[i] = i

    def lpa(self):
        self.__init_label_dict()

        while True:
            flag = True
            for i in range(self.nodes_num):
                # 统计并找出邻接点中数量最多的标签
                count_d = {i: 0 for i in range(self.nodes_num)}
                tmp_label_dict = {i: 0 for i in range(self.nodes_num)}
                for key in tmp_label_dict:
                    tmp_label_dict[key] = self.label_dict[key]

                for adj in self.g.adj_list[i]:
                    count_d[self.label_dict[adj]] += 1

                max_count = -1
                new_label = []
                for label in count_d:
                    if max_count < count_d[label]:
                        max_count = count_d[label]
                        new_label.clear()
                        new_label.append(label)
                    elif max_count == count_d[label]:
                        new_label.append(label)

                # 如当前节点的标签不同于邻接点中数目最多的标签，进行一次更新
                if tmp_label_dict[i] not in new_label:
                    flag = False
                    tmp_label_dict[i] = new_label[random.randint(0, len(new_label) - 1)]

                for key in tmp_label_dict:
                    self.label_dict[key] = tmp_label_dict[key]

            # 如果不再有更新，结束算法
            if flag:
                break

    # 输出社区发现结果
    def show_communities(self):
        con = {}
        for key in self.label_dict:
            try:
                con[self.label_dict[key]].append(key)
            except:
                con[self.label_dict[key]] = [key]

        for key in con:
            print('Label:', key, end='')
            print(', Nodes:', con[key])

    # 绘制初始的网络
    def draw_raw(self, title=''):
        self.g.draw(title)

    # 绘制结果
    def draw(self, title=''):
        for edge in self.g.edges:
            x = []
            x.append(self.g.nodes[edge[0]][0])
            x.append(self.g.nodes[edge[1]][0])

            y = []
            y.append(self.g.nodes[edge[0]][1])
            y.append(self.g.nodes[edge[1]][1])
            plt.plot(x, y, 'y-')

        for i, node in enumerate(self.g.nodes):
            plt.plot(self.g.nodes[node][0], self.g.nodes[node][1],
                     self.__node_type[self.label_dict[i] % len(self.__node_type)])

        plt.title(title)
        plt.show()
