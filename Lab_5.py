from typing import Union

import networkx as nx


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """

    i, prices = nx.dijkstra_predecessor_and_distance(graph, 0)
    return list(prices.values())[-1]

def build_graph(list_):
    """Функция, которая формирует граф по стоимости ступеней"""

    graph = nx.DiGraph()
    queue = list(list_)[::-1]
    graph.add_weighted_edges_from([(0, 1, queue.pop())])
    n = 1
    while queue:
        weight = queue.pop()
        graph.add_weighted_edges_from([(n, n + 1, weight), (n - 1, n + 1, weight)])
        n += 1
    return graph

if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    graph_ = build_graph(stairway)
    print(stairway_path(graph_))  # 72


