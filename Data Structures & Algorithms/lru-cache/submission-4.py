from dataclasses import dataclass
@dataclass
class LRUCacheNode:
    key: int
    value: int
    nexst: LRUCacheNode = None
    previous: LRUCacheNode = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}
        self.head = LRUCacheNode(None, None)
        self.tail = LRUCacheNode(None, None)
        self.head.nexst = self.tail 
        self.tail.previous = self.head

    def remove(self, node):
        prev, nexst = node.previous, node.nexst
        prev.nexst = nexst
        nexst.previous = prev
    
    def insert(self, node):
        node.previous = self.tail.previous
        node.nexst = self.tail
        self.tail.previous.nexst = node
        self.tail.previous = node

    def get(self, key: int) -> int:
        if key in self.data:
            res = self.data[key]
            self.remove(res)
            self.insert(res)
            return res.value
        else:
            return -1

    def evict(self) -> None:
        to_remove = self.head.nexst
        del self.data[to_remove.key]
        self.remove(to_remove)

    def put(self, key: int, value: int) -> None:
        if key in self.data:
           res = self.data[key]
           self.remove(res)
           res.value = value
        else:
            if len(self.data) == self.capacity:
                self.evict()
            self.data[key] = LRUCacheNode(key, value)
        self.insert(self.data[key])
        return 

