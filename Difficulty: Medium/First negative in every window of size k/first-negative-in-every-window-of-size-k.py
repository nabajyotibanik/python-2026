from collections import deque

class Solution:
    def firstNegInt(self, arr, k):

        q = deque()
        ans = []

        for i in range(len(arr)):

            
            if arr[i] < 0:
                q.append(i)

            # Window starts after k-1
            if i >= k - 1:

                # Remove out of window indices
                while q and q[0] < i - k + 1:
                    q.popleft()

                # First negative element
                if q:
                    ans.append(arr[q[0]])
                else:
                    ans.append(0)

        return ans
          
          