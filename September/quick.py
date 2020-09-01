from typing import List


class Solution:
    def print_solution(self):
        if self.best_solution is None:
            return ""
        return '{}{}:{}{}'.format(
            self.best_solution[0],
            self.best_solution[1],
            self.best_solution[2],
            self.best_solution[3]
        )

    def update_solution(self):
        if self.best_solution is not None:
            for (v, bv) in zip(self.solution, self.best_solution):
                if bv > v:
                    return
        self.best_solution = self.solution.copy()

    def largest(self, i: int, A: List[int], limits: List[int]):

        for val in A:
            if val <= limits[i]:
                self.solution[i] = val
                A_cp = A.copy()
                A_cp.remove(val)
                if i == 0:
                    limits[1] = 3 if self.solution[i] == 2 else 9
                self.largest(i+1, A_cp, limits)
                if i == 3:
                    self.update_solution()

    def largestTimeFromDigits(self, A: List[int]) -> str:
        self.best_solution = None
        self.solution = [-1, -1, -1, -1]
        A.sort(reverse=True)
        self.largest(0, A, [2, 3, 5, 9])
        return self.print_solution()


if __name__ == "__main__":
    sol = Solution()
    sol.largestTimeFromDigits([5, 5, 5, 5])
    print(sol.print_solution())
