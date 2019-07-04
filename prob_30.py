# 30. Substring with Concatenation of All Words
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
class Solution(object):
    def findSubstring(self, s, words):
        if len(words) == 0 :
            return []
        wordlen = len(words[0])
        global_counter = {}
        for w in words:
            global_counter[w] = 1 if w not in global_counter else global_counter[w] + 1
        string_len = len(s)
        num_words = len(words)
        ans = []
        for scan_offset in range(min(wordlen, string_len-wordlen*num_words+1)): # this is offset index
            left = scan_offset
            local_counter = {}
            num_words_hit = 0
            for subscan_pointer in range(scan_offset, string_len-wordlen+1,  wordlen):
                word = s[subscan_pointer:subscan_pointer+wordlen]
                if word in global_counter:
                    local_counter[word] = 1 if word not in local_counter else local_counter[word] + 1
                    num_words_hit += 1
                    while local_counter[word] > global_counter[word]:
                        local_counter[s[left: left+wordlen]] -= 1
                        left += wordlen
                        num_words_hit -= 1
                    if num_words_hit == num_words:
                        ans.append(left)
                else:
                    left = subscan_pointer + wordlen
                    num_words_hit = 0
                    local_counter = {}
        return ans