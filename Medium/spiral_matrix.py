def spiralOrder(matrix):
        ret = []
        while len(matrix) > 0:
            ret.extend(matrix[0])
            matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return ret
