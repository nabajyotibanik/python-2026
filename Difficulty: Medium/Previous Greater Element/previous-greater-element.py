class Solution:
	def preGreaterEle(self, arr):
		# code here\
		res = []
        stack = []

        for i in range(len(arr)):

            while stack and stack[-1] <= arr[i]:
                stack.pop()

            if stack:
                res.append(stack[-1])
            else:
                res.append(-1)

            stack.append(arr[i])

        return res