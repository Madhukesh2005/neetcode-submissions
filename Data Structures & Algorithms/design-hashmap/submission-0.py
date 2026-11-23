class MyHashMap:

    def __init__(self):
        self.size = 1009
        self.buckets = [[] for _ in range(self.size)]

    def _index(self, key: int) -> int:
        return key % self.size
        
    def put(self, key: int, value: int) -> None:
        index = self._index(key)
        bucket = self.buckets[index]  # Fixed spelling

        for i, pair in enumerate(bucket):
            if key == pair[0]:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        
    def get(self, key: int) -> int:
        index = self._index(key)
        bucket = self.buckets[index]  # Fixed spelling

        for k, v in bucket:           # Cleaner loop without range(len())
            if key == k:
                return v
        return -1                     # Return -1 if key is not found

    def remove(self, key: int) -> None:
        index = self._index(key)
        bucket = self.buckets[index]  # Fixed spelling

        for i, pair in enumerate(bucket):
            if key == pair[0]:
                bucket.pop(i)         # pop(i) is faster than remove(pair) since you already have index i
                return                # Stop looping once removed



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)