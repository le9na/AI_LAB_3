class TRA:
    def __init__(self, size, loc):
        self.N = size
        self.currPos = loc
        self.setup_graph()
        print("----------Traverse-------------")
        print()

    def setup_graph(self):
        self.G = [[False] * self.N for _ in range(self.N)]
        edges = [
            (0, 1), (0, 8), (0, 4),
            (1, 2), (1, 3),
            (2, 6),
            (3, 4), (3, 5),
            (6, 7),
            (8, 9),
            (9, 10),
            (10, 11)
        ]
        for u, v in edges:
            self.G[u][v] = self.G[v][u] = True

    def traverse(self):
        print(f"The current city is: {self.ret_city(self.currPos)}\n")
        connected = [i for i in range(self.N) if self.G[self.currPos][i]]
        for i, city in enumerate(connected):
            print(f"[{i}] {self.ret_city(city)}\t")
        print()
        print("Choose moving method:\n1. FIFO\n2. LIFO\n-1. Stop")

        num = int(input())
        if num == -1:
            print("Stopping program")
            return
        elif num == 1:
            self.fifo_traverse()
        elif num == 2:
            self.lifo_traverse()

    def fifo_traverse(self):
        from collections import deque
        q = deque()
        add_to_q = "From the front of the queue: "
        for i in range(self.N):
            if self.G[self.currPos][i]:
                q.append(i)
                add_to_q += self.ret_city(i) + "\t"
        add_to_q += "]\n"
        print(add_to_q)
        print(f"{self.ret_city(q[0])} is destination\n")
        self.currPos = q[0]
        self.traverse()

    def lifo_traverse(self):
        stack = []
        add_to_stack = "["
        for i in range(self.N):
            if self.G[self.currPos][i]:
                stack.append(i)
                add_to_stack += self.ret_city(i) + "\t"
        add_to_stack += "top=>]"
        print(add_to_stack)
        self.currPos = stack[-1]
        self.traverse()

    @staticmethod
    def ret_city(i):
        cities = ["Buraydah", "Unayzah", "AlZulfi", "Al-Badai",
            "Riyadh-Alkhabra", "AlRass", "UmSedrah", "Shakra",
            "Al-Bukayriyah", "Sheehyah", "Dhalfa", "Mulida"]
        return cities[i]


def main():
    print("\nChoose a city number to start: \n")
    for i in range(12):
        print(f"{TRA.ret_city(i)} city[{i}]")
    print("\nInput: ")

    choosen_city = int(input())
    tra_graph = TRA(12, choosen_city)
    tra_graph.traverse()


if __name__ == "__main__":
    main()
