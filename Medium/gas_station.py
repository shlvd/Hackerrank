def canCompleteCircuit(self, gas, cost):
        start, tank, total = 0, 0, 0
        for idx in range(len(cost)):
            tank += gas[idx] - cost[idx]
            if tank < 0:
                start = idx + 1
                total += tank
                tank = 0

        if total + tank < 0:
            return -1
        else:
            return start
