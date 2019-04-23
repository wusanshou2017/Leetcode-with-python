class Solution:
    def generatePatheses(self, n):
        res = []
        self.generate(n, n, "", res)
        return res

    def generate(self, left, right, str, res):
        if left == 0 and right == 0:
            res.append(str)
            return
        if left > 0:
            self.generate(left - 1, right, str + "(", res)
        if right > left:
            self.generate(left, right - 1, str + ")", res)


solution = Solution()
test = solution.generatePatheses(3)
print(test)
