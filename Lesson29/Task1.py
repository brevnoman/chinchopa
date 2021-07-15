from typing import List


class BinHeap:

    def __init__(self) -> None:
        self.heap_list: List[int] = []

    def swap(self, i) -> None:
        self.heap_list[i // 2], self.heap_list[i] = self.heap_list[i], self.heap_list[i // 2]

    def __len__(self):
        return len(self.heap_list)

    def build_heap(self, items: List[int]) -> None:
        for root in items:
            self.heap_list.append(root)
            self.validate(len(self)-1)

    def validate(self, index):
        root_index = (index) // 2
        if root_index >= 0:
            if self.heap_list[index] > self.heap_list[root_index]:
                self.swap(index)
                self.validate(root_index)

    def insert(self, k) -> None:
        self.heap_list.append(k)
        self.validate(len(self)-1)

    def print_heap(self):
        ml = max(len(str(x)) for x in self.heap_list)
        ars = [('{:0'+str(ml)+'}').format(x) for x in self.heap_list]
        dp = len(bin(len(self.heap_list))) - 1
        print('*' * 2**(dp-2) * (ml + 1))
        for i in range(1, dp + 1):
            str_space = ' ' * max(0, 2**(dp-i-2) * (ml + 1) - 1 - ml // 2)
            sep_space = ' ' * max(0, 2**(dp-i-1) * (ml + 1) - ml)
            print(str_space + sep_space.join(ars[2**(i-1) - 1: 2**i - 1]))
        print('*' * 2**(dp-2) * (ml + 1))

    def delete_max(self):
        new_list = self.heap_list[1:]
        self.heap_list = []
        self.build_heap(new_list)

    def delete_min(self):
        check_list= self.heap_list[len(self)//2:]
        found_min = check_list[0]
        for i in check_list:
            if i < found_min:
                found_min = i
        counter = 0
        for j in self.heap_list:
            if j == found_min:
                self.heap_list.pop(counter)
                break
            else:
                counter += 1
        new_list = self.heap_list
        self.heap_list = []
        self.build_heap(new_list)

# heap = PriorityQueue()
# heap.build_heap([7, 1, 0, 2, 3, 8, 5,6,4,9,10,11,12,13,14])
# print(heap.heap_list)
# heap.print_heap()
# heap.insert(15)
# heap.print_heap()
# heap.delete_max()
# heap.print_heap()
# print(heap.heap_list)
