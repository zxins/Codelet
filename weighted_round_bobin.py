# 负载均衡-加权轮询算法

import itertools

class WeightedRoundRobin:
    def __init__(self, nodes):
        self.nodes = nodes
        self.weights = [node["weight"] for node in nodes]
        self.max_weight = max(self.weights)
        self.gcd_weight = self.gcd_of_list(self.weights)
        self.current_weight = self.max_weight
        self.index = -1

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def gcd_of_list(self, numbers):
        return functools.reduce(self.gcd, numbers)

    def next_node(self):
        while True:
            self.index = (self.index + 1) % len(self.nodes)
            if self.index == 0:
                self.current_weight = self.current_weight - self.gcd_weight
                if self.current_weight <= 0:
                    self.current_weight = self.max_weight
                    if self.current_weight == 0:
                        return None
            if self.weights[self.index] >= self.current_weight:
                return self.nodes[self.index]

# 示例
nodes = [
    {"name": "Node1", "weight": 1},
    {"name": "Node2", "weight": 2},
    {"name": "Node3", "weight": 3},
]

wrr = WeightedRoundRobin(nodes)

for _ in range(9):
    node = wrr.next_node()
    print(node["name"])
