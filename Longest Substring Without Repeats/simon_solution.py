class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dicts = {}
        maxlength = start = 0
        for i,value in enumerate(s):
            # when duplicate was found
            if value in dicts:
                # Get the pre-duplicate index
                pre_index = dicts[value] + 1
                # 'abba' case consideration
                if pre_index > start:
                    start = pre_index
            current_len = i - start + 1
            if current_len > maxlength:
                maxlength = current_len
            # add/update the value index
            dicts[value] = i
        return maxlength
