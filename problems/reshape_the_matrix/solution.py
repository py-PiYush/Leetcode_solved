class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        if m*n!=r*c:
            return mat
        grid,row=[],[]
        for i in mat:
            print(i)
            for j in i:
                print(j)
                if len(row)<c:
                    row.append(j)
                    print(row)
                else:
                    grid.append(row)
                    row=[j]
        grid.append(row)
        return grid
                