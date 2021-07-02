from typing import List


class PriorityQueue:
    """
    я посмотрел на код предлагаемой бинарной кучи
    и понял что ничего не понял, поэтому нашерстил
    в интернете что такое бинарная куча и как её реализовать,
    в итоге по своему пониманию сделал её
    и уже исходя из неё сделал задание(для изменения типа кучи нужно сменить только один знак)
    """
    def __init__(self) -> None:
        self.heap_list: List[int] = []

    def __swap(self, child_index, parent_index) -> None:
        self.heap_list[child_index], self.heap_list[parent_index] = self.heap_list[parent_index], self.heap_list[child_index]

    def __len__(self):
        return len(self.heap_list)

    def build_queue(self, items: List[int]) -> None:
        for root in items:
            self.heap_list.append(root)
            self.validate(len(self)-1)

    def validate(self, index):
        root_index = (index-1) // 2
        if root_index >= 0:
            if self.heap_list[index] > self.heap_list[root_index]:      #в этой строке достаточно сменить ">" на "<" чтобы получить минимальную кучу
                self.__swap(index, root_index)
                self.validate(root_index)

    def enqueue(self, k) -> None:
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
        self.build_queue(new_list)

    def dequeue(self, k):
        found = k
        counter = 0
        for j in self.heap_list:
            if j == found:
                self.heap_list.pop(counter)
                break
            else:
                counter += 1
        new_list = self.heap_list
        self.heap_list = []
        self.build_queue(new_list)

# queue = PriorityQueue()
# queue.build_queue([7, 1, 0, 2, 3, 8, 5,6,4,9,11,12,10,14])
# queue.print_heap()
# queue.enqueue(13)
# queue.print_heap()
# queue.dequeue(13)
# queue.print_heap()