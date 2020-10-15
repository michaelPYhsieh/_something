https://leetcode.com/problems/pascals-triangle-ii/
```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        e = 1
        re = [e]
        for i in range(rowIndex):
            e = int(e*(rowIndex-i)/(i+1))
            re.append(e)
        return re
```
