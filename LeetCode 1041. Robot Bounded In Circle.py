class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        #      x y a  bi
        mat = [0,0,0, 1]
        
        for i in instructions:
            if i =='G':
                mat[0] += mat[2]
                mat[1] += mat[3]
                
            elif i == 'L':
                mat[2], mat[3] = -mat[3], mat[2]
                # (a+bi) *i
                # = -b +ai
                
            elif i == 'R':
                mat[2], mat[3] = mat[3], -mat[2]
                # (a+bi) *i^3
                # = b -ai
        
        return mat[:2] == [0, 0] or mat[2:] != [0,1]
