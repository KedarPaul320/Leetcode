class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry > 0:
            val1 = int(a[i]) if i >= 0 else 0
            val2 = int(b[j]) if j >= 0 else 0
            carry, out = divmod(val1 + val2 + carry, 2)
            result.append(str(out))
            i -= 1
            j -= 1
        return "".join(result[::-1])