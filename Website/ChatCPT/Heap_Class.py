import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import networkx as nx
import math
import imageio
import os





class MinHeap:
    def __init__(self, arr=None):
        self.heap = []
        if type(arr) is list:
            self.heap = arr.copy()
            number = math.ceil(len(self.heap)/2)
            for i in range(number)[::-1]:
                print(i, self.heap)
                self.create_pic(i+1, self.heap)
                self._siftdown(i)
                if i == 0:
                    self.create_pic(i, self.heap)
                print(i, self.heap, "Second")
            print(0, self.heap, "final")
            self.create_gif()

    def visualize_heap(self, arr):
        plt.clf()
        G = nx.DiGraph()
        for i, val in enumerate(arr):
            G.add_node(i, val=val)
            if i > 0:
                parent = (i-1)//2
                G.add_edge(parent, i)
        pos = {}
        level_height = 5 # adjust as needed
        for i, val in enumerate(arr):
            level = int(math.log2(i+1))
            children = [j for j in G.successors(i)]
            if i > 0:
                parent = (i-1)//2
                left_child = 2 * parent + 1
                right_child = 2 * parent + 2
                parent_x, parent_y = pos[parent]
                offset = (5/ -level,5/level)
                if i == left_child:
                    pos[i] = (parent_x + offset[0], -level*level_height)
                else:
                    pos[i] = (parent_x + offset[1], -level*level_height)
            else:
                pos[i] = (0, -level*level_height)
        nx.draw_networkx(G, pos, arrows=False, with_labels=False)
        labels = nx.get_node_attributes(G, 'val')
        nx.draw_networkx_labels(G, pos, labels)
        return G, pos

    def create_pic(self, i, updated_heap):
        G, pos = self.visualize_heap(updated_heap)
        plt.savefig(f"anim_{i}.png")

    def create_gif(self):
        with imageio.get_writer("anim.gif", mode="I",duration = 5) as writer:
            for j in range(math.ceil(len(self.heap)/2)+1)[::-1]:
                image = imageio.imread(f"anim_{j}.png")
                writer.append_data(image)
                os.remove(f"anim_{j}.png")

    def _siftup(self, i):
        parent = (i-1)//2
        while i != 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i-1)//2

    def _siftdown(self, i):
        left = 2*i + 1
        right = 2*i + 2
        while (left < len(self.heap) and self.heap[i] > self.heap[left]) or (right < len(self.heap) and self.heap[i] > self.heap[right]):
            smallest = left if (right >= len(self.heap) or self.heap[left] < self.heap[right]) else right
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest
            left = 2*i + 1
            right = 2*i + 2

    def insert(self, element):
        self.heap.append(element)
        self._siftup(len(self.heap)-1)

    def get_min(self):
        return self.heap[0] if len(self.heap) > 0 else None

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        minval = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self._siftdown(0)
        return minval

    def update_by_index(self, i, new):
        old = self.heap[i]
        self.heap[i] = new
        if new < old:
            self._siftup(i)
        else:
            self._siftdown(i)

    def update(self, old, new):
        if old in self.heap:
            self.update_by_index(self.heap.index(old), new)

class MaxHeap:
    def __init__(self, arr=None):
        self.heap = []
        if type(arr) is list:
            self.heap = arr.copy()
            for i in range(len(self.heap))[::-1]:
                self._siftdown(i)

    def _siftup(self, i):
        parent = (i-1)//2
        while i != 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i-1)//2

    def _siftdown(self, i):
        left = 2*i + 1
        right = 2*i + 2
        while (left < len(self.heap) and self.heap[i] < self.heap[left]) or (right < len(self.heap) and self.heap[i] < self.heap[right]):
            biggest = left if (right >= len(self.heap) or self.heap[left] > self.heap[right]) else right
            self.heap[i], self.heap[biggest] = self.heap[biggest], self.heap[i]
            i = biggest
            left = 2*i + 1
            right = 2*i + 2

    def insert(self, element):
        self.heap.append(element)
        self._siftup(len(self.heap)-1)

    def get_max(self):
        return self.heap[0] if len(self.heap) > 0 else None

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        maxval = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self._siftdown(0)
        return maxval

    def update_by_index(self, i, new):
        old = self.heap[i]
        self.heap[i] = new
        if new > old:
            self._siftup(i)
        else:
            self._siftdown(i)

    def update(self, old, new):
        if old in self.heap:
            self.update_by_index(self.heap.index(old), new)


def heapsort(arr):
    heap = MinHeap(arr)
    return [heap.extract_min() for i in range(len(heap.heap))]
