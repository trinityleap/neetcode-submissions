class TimeMap:

    def __init__(self):
        self.store = {} # key -> [list of tuples (timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        stores a key associated with a value, timestamp pair
        doesnt return anything
        """
        if key not in self.store:
            self.store[key] = []
        
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """
        retrieve and return the value that key was set to be paired with, 
        at a timestamp at or before given timestamp param
        """
        data = self.store.get(key, []) # list of tuples that key is mapped to

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
