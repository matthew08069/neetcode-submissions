class MyHashMap:
    def __init__(self):
        self.keyList = [[]]

    def put(self, key: int, value: int) -> None:
        # Key = index of array, Value = value at array[key] in a list
        if key >= len(self.keyList):
            self.keyList.extend([[] for _ in range(key)])
        self.keyList[key].append(value)

    def get(self, key: int) -> int:
        if key >= len(self.keyList) or self.keyList[key] == []:
            return -1
        return self.keyList[key][-1]

    def remove(self, key: int) -> None:
        if key < len(self.keyList) and self.keyList[key] != []:
            self.keyList[key] = []


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
