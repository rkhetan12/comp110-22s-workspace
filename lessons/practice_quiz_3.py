# """Plots attribute will have a mzaximim number of 100 list items. Each item will be the size of the tree in that plot.   """


# class ChristmasTreeFarm: 
#     plots: list[int]

#     def __init__(self, plots: int, initial_planting: int) -> None:
#         """Constructor of ChristmasTreeFarm."""
#         self.plots = []
#         if initial_planting > plots:
#             exit()
#         i: int = 0
#         while i < initial_planting:
#             self.plots.append(1)
#             i = i + 1
#         while i < plots:
#             self.plots.append(0)
#             i = i + 1

#     def __add__(self, rhs: ChristmasTreeFarm) -> ChristmasTreeFarm:
#         i: int = 0
#         total_plants: int = 0
#         while i < len(self.plots):
#             if self.plots[i] != 0:
#                 total_plants = total_plants + 1
#             i = i + 1
#         i = 0
#         while i < len(rhs.plots):
#             if rhs.plots[i] != 0:
#                 total_plants = total_plants + 1
#             i = i + 1

#         return ChristmasTreeFarm(len(self.plots) + len(rhs.plots), total_plants)

#     def growth(self) -> None:
#         i: int = 0
#         while i < len(self.plots):
#             if self.plots[i] != 0:
#                 self.plots[i] = self.plots[i] + 1 
#             i = i + 1

#     def plant(self, plot_index: int) -> None:
#         self.plots[plot_index] = 1

#     def harvest(self, replant: bool) -> int:
#         i: int = 0
#         total: int = 0
#         while i < len(self.plots):
#             if self.plots[i] >= 5:
#                 total = total + 1
#                 if replant:
#                     self.plots[i] = 1
#                 else:
#                     self.plots[i] = 0
#             i = i + 1
#         return total

            



# def main() -> None:
#     p1: ChristmasTreeFarm = ChristmasTreeFarm(100, 13)  # total of 100 plots and we are planting 13
#     print(p1.plots)
#     p1.plant(67)
#     p1.plant(77)
#     p1.plant(87)
#     p1.growth()
#     p1.growth()
#     p1.growth()
#     p1.growth()
#     print(p1.plots)
#     p1.harvest(True)
#     print(p1.plots)
#     print("hello ria")

# if __name__ == "__main__":
#     main()

# class Course:
#     name: str
#     level: int
#     prerequisites: list[str]

#     def is_valid_course(self, prerequisite: str) -> bool:
#         result: bool = False
#         if self.level >= 400:
#             i: int = 0
#             while i < len(self.prerequisites):
#                 if self.prerequisites[i] == prerequisite:
#                     return True
#                 i += 1
#         return result
       

# def find_courses(list_of_courses: list[Course], prerequisite: str) -> list[str]:
#     result: list[str] = []
#     for course in list_of_courses:
#         if course.level >= 400:
#             i: int = 0
#             while i < len(course.prerequisites):
#                 if course.prerequisites[i] == prerequisite:
#                     result.append(course.name)
#                 i += 1
#     return result

from types import UnionType


class Node:
    v: int
    next: Union[Node, None]

    def __init__(self, v: int, next: Union[Node, None]):
        self.v = v
        self.next = next

    def __repr__(self) -> str:
        s: str = f"{self.v} -> "
        if isinstance(self.next, Node):
            return s + self.next.__repr__()
        else:
            return s + "None"


n1 = Node(1, None)
n2 = Node(2, n1)
n3 = Node(3, n2)

print(n3)


