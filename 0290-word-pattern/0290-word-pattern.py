class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern)!= len(words):
            return False
        map_p_w = {}
        map_w_p = {}
        for p, w in zip(pattern, words):
            if p not in map_p_w and w not in map_w_p:
                map_p_w[p] = w
                map_w_p[w] = p
            elif map_p_w.get(p)!= w or map_w_p.get(w)!= p:
                return False
        return True