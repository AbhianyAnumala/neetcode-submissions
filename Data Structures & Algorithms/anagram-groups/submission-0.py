class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # x = []

        # def sorted_char(word:str) -> str:
        #     return "".join(sorted(word))

        # for index, value in enumerate(strs):
        #     x.append([sorted_char(value),index])
        

        # x.sort(key = lambda x: x[0])

        # print(x)

        groups = {} 

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in groups:
                groups[sorted_word] = []
            
            groups[sorted_word].append(word)


        return list(groups.values())


        