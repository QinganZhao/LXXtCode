### Algorithm 1
### construct heap from scratch
### Use min-heap
### TLE

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        h = heap()
        self.nums.append(val)
        for i in range(len(self.nums)):
            if len(h.list) == self.k:
                if self.nums[i] > h.list[0]:
                    h.pop()
                    h.add(self.nums[i])
            else:
                h.add(self.nums[i])
        return h.list[0]

        
class heap:
    
    def __init__(self):
        self.list = []
        self.size = 0
    
    def add(self, val):
        self.size += 1
        self.list.append(val)
        self.swapup(self.size-1)
        
    def construct(self, List):
        self.list = List
        self.size = len(List)
        end = len(List) - 1
        endParent = (end - 1) // 2
        while endParent >= 0:
            self.swapdown(endParent)
            endParent -= 1
    
    def swapup(self, node):
        while node > 0 and node < self.size:
            if self.list[node] < self.list[(node-1)//2]:
                self.list[node], self.list[(node-1)//2] = self.list[:][(node-1)//2], self.list[:][node]
            node = (node - 1) // 2
    
    ### if max-heap, change ">" to "<" in if statement
    ### and change "minChild" to "maxChild"
    def swapdown(self, node):
        while 2 * node + 1 < self.size and node >= 0:
            minChild = self.minChild(node)
            if self.list[node] > self.list[minChild]:
                self.list[node], self.list[minChild] = self.list[:][minChild], self.list[:][node]
            node = minChild
            
    def maxChild(self, node):
        if 2 * node + 2 >= self.size:
            return 2 * node + 1
        if self.list[2 * node + 2] > self.list[2 * node + 1]:
            return 2 * node + 2
        return 2 * node + 1
    
    def minChild(self, node):
        if 2 * node + 2 >= self.size:
            return 2 * node + 1
        if self.list[2 * node + 2] < self.list[2 * node + 1]:
            return 2 * node + 2
        return 2 * node + 1
    
    def pop(self):
        res = self.list[0]
        self.list[0] = self.list[-1]
        self.list.pop()
        self.size -= 1
        self.swapdown(0)
        

### Algorithm 1 (pro)
### Use Python heapq 
### TLE

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        h = []
        heapq.heapify(h)
        self.nums.append(val)
        for i in range(len(self.nums)):
            if len(h) == self.k:
                Min = heapq.heappop(h)
                if self.nums[i] > Min:
                    heapq.heappush(h, self.nums[i])
                else:
                    heapq.heappush(h, Min)
            else:
                heapq.heappush(h, self.nums[i])
        return heapq.heappop(h)


### Algorithm 2
### construct heap from scratch
### Use min-heap
### SUCCEED!!!!!! Fucking algorithm king Franklin!!!
### 8060 ms though...

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        h = heap()
        h.construct(self.nums)
        while h.size > self.k:
            h.pop()
        self.heap = h

    def add(self, val: int) -> int:
        if self.heap.size < self.k:
            self.heap.add(val)
        elif val > self.heap.list[0]:
            self.heap.pop()
            self.heap.add(val)
        return self.heap.list[0]
    
    
### Algorithm 2 (pro)
### Use Python heapq 
class KthLargest(object):

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val):
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)
        return self.nums[0]


### Python heapq cheating 
### TLE (no cheating...)

class KthLargest(object):

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

    def add(self, val):
        self.nums.append(val)
        return heapq.nlargest(self.k, self.nums)[-1]
    
    
### Sorting cheating 
### TLE (no cheating...)

class KthLargest(object):

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

    def add(self, val):
        self.nums.append(val)
        return sorted(self.nums, reverse=True)[self.k-1]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
