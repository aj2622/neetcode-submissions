from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        alphabet = set()
        for word in words:
            for char in word:
                alphabet.add(char)
        lis = list(alphabet)
        indeg = {char:0 for char in alphabet}
        

        g = defaultdict(set)

        def connection(s1, s2):
            if s1 == s2 or not s1 or not s2:
                return
            elif s1[0] == s2[0]:
                connection(s1[1:], s2[1:])
            else:
                if s2[0] not in g[s1[0]]:
                    g[s1[0]].add(s2[0])
                    indeg[s2[0]] += 1

        ans = ""
        
        for word1, word2 in zip(words, words[1:]):
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""            
            connection(word1, word2)
        
        dq = deque([char for char in indeg if indeg[char] == 0]) 

        while dq:
            current = dq.popleft()
            ans += current
            for nxt in g[current]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    dq.append(nxt)
    
        return ans if len(ans) == len(alphabet) else ""