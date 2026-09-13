class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # # A seen dict with {char: frequentcy}
        # freq_list = []

        # for word in words:
        #     char_count = {}
        #     for char in word:
        #         char_count[char] = char_count.get(char, 0) + 1
        #     freq_list.append(char_count)
                
        
        # res = []
        # word_set = set()
        # for char in words[0]:
        #     word_set.add(char)
        

        # for char in word_set:
        #     min_count = float("inf")
        #     for freq_dict in freq_list:
        #         count = freq_dict.get(char, 0)
        #         min_count = min(min_count, count)
        #     res.extend([char] * min_count)
        # return res

        cnt = Counter(words[0])

        for w in words:
            cur_cnt = Counter(w)
            for c in cnt:
                cnt[c] = min(cnt[c], cur_cnt[c])

        res = []
        for c in cnt:
            # for i in range(cnt[c]):
            #     res.append(c)
            res.extend([c] * cnt[c])
        return res