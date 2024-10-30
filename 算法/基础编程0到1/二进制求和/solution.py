class Solution:
    def addBinary(self, a: str, b: str) -> str:
        na, nb = 0, 0
        for n in range(len(a)):
            na += (int(a[len(a)-n-1]) * 2 ** n)
        for n in range(len(b)):
            nb += (int(b[len(b)-n-1]) * 2 ** n)
        return bin(na+nb)[2:]