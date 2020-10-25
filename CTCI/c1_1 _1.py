class Solution:
    def spliter(self, str):
        return([item for item in str])
    def uniqueChars(self, str):
        list1 = self.spliter(str)
        unique_list = []
        for x in list1:
            if x not in unique_list:
                unique_list.append(x)
        if len(unique_list) < len(list1):
            return(False)
        else:
            return(True)
a = Solution()
out = a.uniqueChars('abcdefghijklmnopqrstuvwxyz')
print(out)
