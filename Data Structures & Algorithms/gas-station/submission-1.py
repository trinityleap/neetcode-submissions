class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = 0

        for i in range(len(gas)):
            tank = tank - cost[i] + gas[i]
            if tank < 0: # if fail on i
                # dont start at any 0 to i
                start = i + 1
                tank = 0

        return start
            