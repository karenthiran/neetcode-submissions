class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for i in strs:
            cnt=[0]*26
            for j in i:
                cnt[ord(j)-97]=cnt[ord(j)-97]+1
            d[tuple(cnt)].append(i)
        ans=[]
        for v in d.values():
            ans.append(v)
        return ans