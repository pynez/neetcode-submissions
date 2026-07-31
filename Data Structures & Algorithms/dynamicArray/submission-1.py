class DynamicArray:
    array = []
    size = 0
    capacity = 0
    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.array.append(n)
        self.size += 1

    def popback(self) -> int:
        return self.array.pop(-1)

    def resize(self) -> None:
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return len(self.array)
    
    def getCapacity(self) -> int:
        return self.capacity