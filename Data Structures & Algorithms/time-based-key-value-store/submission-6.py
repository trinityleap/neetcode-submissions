class TimeMap:

    def __init__(self):
        self.store = {} # key -> [list of (timestamp, value) pairs], can sort on tuple

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.store.get(key):
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        data = self.store[key] # list of (timestamp, value) pairs for this key
       
        lo, hi = 0, len(data) - 1 # index of start and end of data
        best = "" # best value

        while lo <= hi:
            mid = (lo + hi) // 2 # middle index
            if data[mid][0] > timestamp:
                hi = mid - 1
            elif data[mid][0] <= timestamp:
                lo = mid + 1
                best = data[mid][1]

        return best