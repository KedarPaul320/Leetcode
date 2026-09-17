class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0 :
            return False
        
        st = []
        for ch in list(s):
            if ch=="(" or ch=="[" or ch=="{":
                st.append(ch)
            else :
                if not st :
                    return False
                top = st.pop()
                if ch == ")" and top!="(":
                    return False
                elif ch == "]" and top!="[":
                    return False
                elif ch=="}" and top!="{":
                    return False 
                
        return not st 

        