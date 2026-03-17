class KnapsackSolver:

    def __init__(self):
        self.best_price = 0
    
    # define a function to read items
    def read_items(self, filename):
        items = []
        with open(filename, "r") as f:
            for line in f:
                weight, price = map(int, line.strip().split())
                items.append((weight, price))
        return items
    
    # dynamic function
    def find_dynamic(self, items, capacity):
        # (TODO)
        n = len(items)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            w,p = items[i - 1]
            for c in range(1, capacity + 1):
                if w>c:
                    dp[i][w] = dp[i - 1][c]
                else:
                    dp[i][c] = max(dp[i - 1][c], p + dp[i - 1][c - w])
        selected = []
        c = capacity
        for i in range(n, 0, -1):
            if dp[i][c] != dp[i - 1][c]:
                selected.append(i - 1)
                c-= items[i - 1][0]
                self.best_price = dp[n][capacity]
        return selected[::-1]
    def find_greedy(self, items, capacity):
        sorted_items = sorted(items, key=lambda x: x[1]/x[0], reverse=True)
        curr_weight = 0
        total_value = 0
        included = []

        for _, (w, p) in enumerate(sorted_items):
            if curr_weight + w <= capacity:
                included.append(items.index((w, p)))
                curr_weight += w
                total_value += p

        self.best_price = total_value
        return included
    
    def find_enumerate(self, items, capacity):
        from itertools import chain, combinations
        best_comb = []
        self.best_price = 0

        for combo in chain.from_iterable(combinations(items, r) for r in range(1, len(items + 1))):
            total_weight = sum(w for w, _ in combo)
            total_price = sum(p for _, p in combo)

            if total_weight <= capacity and total_price > self.best_price:
                self.best_price = total_price
                best_comb = [item.index(item) for item in combo]

        return best_comb


if __name__ == "__main__":
    solver = KnapsackSolver()
    items = solver.read_items("./item.txt")
    capacity = 50

    # dynamic programming
    # (TODO)
    dp_items = solver.find_dynamic(items, capacity)
    print(f"Dynamic Solution: price {solver.best_price} items: {dp_items}")
    
    # greedy programming
    greedy_items = solver.find_greedy(items, capacity)
    print(f"Greedy Solution: price {solver.best_price} items: {greedy_items}")

    if len(items) <= 20:
        enumerate_items = solver.find_greedy(items, capacity)
        print(f"Enumeration Solution: price {solver.best_price} items: {enumerate_items}")