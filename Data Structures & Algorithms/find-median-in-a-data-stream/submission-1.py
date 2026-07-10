import heapq

class MedianFinder:

    def __init__(self):
        self.left_heap = []
        self.right_heap = []
        self.count = 0

    def addNum(self, num: int) -> None:
        # 1. Add to left_heap (max_heap) first
        heapq.heappush(self.left_heap, -num)

        # 2. Balance: Move the largest element from left_heap to right_heap
        #    This ensures right_heap always contains elements >= left_heap's max.
        largest_in_left = -heapq.heappop(self.left_heap)
        heapq.heappush(self.right_heap, largest_in_left)

        # 3. Rebalance sizes: Ensure left_heap has more or equal elements
        #    If right_heap has more elements than left_heap, move smallest from right_heap to left_heap
        if len(self.right_heap) > len(self.left_heap):
            smallest_in_right = heapq.heappop(self.right_heap)
            heapq.heappush(self.left_heap, -smallest_in_right)
        self.count += 1

    def findMedian(self) -> float:
        if self.count % 2 == 0:
            return (-self.left_heap[0]+self.right_heap[0]) / 2
        else:
            return -self.left_heap[0]
        