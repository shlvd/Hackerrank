def setZeroes(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = [i for i, row in enumerate(matrix) if 0 in row]
        cols = [i for i, col in enumerate(zip(*matrix)) if 0 in col]

        emptyRow = [0] * len(matrix[0])
        for i in range(len(matrix)):
            if i in rows:
                matrix[i] = emptyRow
            else:
                for j in cols:
                    matrix[i][j] = 0
