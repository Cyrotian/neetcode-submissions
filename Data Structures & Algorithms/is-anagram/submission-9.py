class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_dict = {}
        
        for val in s:
            if val in count_dict:
                count_dict[val] = count_dict[val] + 1
            else: 
                count_dict[val] = 1
          

        for val in t:
            if val in count_dict:
                count_dict[val] = count_dict[val] - 1
                if count_dict[val] < 0:
                    return False
            else:
                return False
        return True