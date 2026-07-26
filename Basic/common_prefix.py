class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
            
        prefix = strs[0]
        n = len(strs)
        for i in range(1, n):
            current = strs[i]

            j = 0

            while j < len(prefix) and j < len(current) and prefix[j] == current[j]:
                j = j + 1           
            prefix = prefix[:j]

            if not prefix:
                break
        
        if len(prefix) == 0:
            return ""
        
        return prefix
    

# list_1 = ["flower", "flow", "flight"]
# prefix = ""
# first_string = list_1[0]
# loop_break = False
# for i in range(len(first_string)):
#     for j in range(1, len(list_1)):
#         if i >= len(list_1[j]) or list_1[j][i] != first_string[i]:
#             loop_break = True
            
#     if loop_break:
#         break
#     prefix = prefix + first_string[i]
    
# print(prefix)

