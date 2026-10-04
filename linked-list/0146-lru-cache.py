"""
146. LRU Cache  (Medium)
https://leetcode.com/problems/lru-cache/

Pattern:    hashmap + doubly linked list, clue: "O(1) get/put" + "evict least recently used"
Key idea:
  - dict: key -> node, for O(1) lookup
  - list order: tail = most recent, head = least recent
  - get/put move the node to the tail; when full, evict head.next
  - node stores its key, so eviction knows which dict entry to delete
  - doubly linked: unlink a node in O(1) (a Python list would be O(n))
Complexity: O(1) time for get and put, O(capacity) space
Mistake I made:
  - evicted from the tail, the same end I add recent items to
  - forgot to link the sentinels in __init__
  - self.prev instead of self.end.prev
  - del node.value instead of del self.dict[node.key]
"""


class Node:
    def __init__(self, key: int=0, value: int=0):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = abs(capacity)
        self.dict = {} # key: node
        self.start = Node()
        self.end = Node()
        self.start.next = self.end
        self.end.prev = self.start

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
    
    def move_to_end(self, node):
        self.end.prev.next = node
        node.prev = self.end.prev
        node.next = self.end
        self.end.prev = node

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        
        node = self.dict[key]
        self.remove_node(node)
        self.move_to_end(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.value = value
            self.remove_node(node)
            self.move_to_end(node)
            return
        
        if len(self.dict) == self.capacity:
            node = self.start.next
            self.remove_node(node)
            del self.dict[node.key]
        
        new_node = Node(key, value)
        self.move_to_end(new_node)
        self.dict[key] = new_node

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)