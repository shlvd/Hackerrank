def numOfMinutes(n, headID, manager, informTime):
        adj = [[] for _ in range(n)]
        for i, manager_i in enumerate(manager):
            if manager_i != -1:
                adj[manager_i].append(i)

        return _dfs(headID, adj, informTime, 0)

    def _dfs(current, adj, informTime, currentTime):
        timeCost = currentTime
        for child in adj[current]:
            timeCost = max(
                _dfs(child, adj, informTime, currentTime + informTime[current]),
                timeCost
            )
        return timeCost
