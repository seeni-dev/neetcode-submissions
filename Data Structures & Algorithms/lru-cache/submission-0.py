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
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.data:
            res = self.data[key]
            self.register(res)
            return res.value
        else:
            return -1

    def evict(self) -> None:
        if self.head:
            del self.data[self.head.key]
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.nexst
        return

    def register(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            if self.tail != node:
                if self.head == node:
                    self.head = self.head.nexst
                # Remove the node fist
                if node.previous:
                    node.previous.nexst = node.nexst
                if node.nexst:
                    node.nexst.previous = node.previous

                self.tail.nexst = node
                node.previous = self.tail
                node.nexst = None
                self.tail = node
            
                

    def put(self, key: int, value: int) -> None:
        if key in self.data:
           res = self.data[key]
           res.value = value
        else:
            if len(self.data) == self.capacity:
                self.evict()
            self.data[key] = LRUCacheNode(key, value)
        self.register(self.data[key])
        return 

