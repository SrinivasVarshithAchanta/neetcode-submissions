class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        new_s=list(s)
        new_t=list(t)
        new_s.sort()
        new_t.sort()
        for i in range(0,len(s)):
            if new_s[i]==new_t[i]:
                j=1
            else:
                return False

        if j==1:
            return True

# mistake i tried to sort the list at the declaration of new_s and new_t
# but its not possible we need to do it seperatelt in next lines


        