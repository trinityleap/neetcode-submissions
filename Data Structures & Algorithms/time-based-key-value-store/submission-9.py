class TimeMap:

    def __init__(self):
        self.store = {} # key -> [list of (timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """
        (timestamp, value) pairs are alreaady sorted by timestamp
        -> binary search
        """

        # if key not in self.store
        data = self.store.get(key, [])

        lo, hi = 0, len(data) - 1
        best = ""

        while lo <= hi:
            mid = (lo + hi) // 2
            if data[mid][0] > timestamp:
                hi = mid - 1
            if data[mid][0] <= timestamp:
                best = data[mid][1]
                lo = mid + 1
        
        return best

