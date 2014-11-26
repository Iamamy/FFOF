# Write a function to find the longest common prefix string amongst an array of strings

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs)>0:
            headstr=strs[0]
            strdic={}
            for n in range(0,len(headstr)):
                str=headstr[0:n+1]
                strdic[str]=1
            
              
            for s in strs[1:]:
                for sub in strdic.keys():
                    if s.startswith(sub)==False:
                        strdic[sub]=0
            
            maxlen=0
            for s,f in strdic.items():
             
                if f==1 and len(s)>maxlen:
                    longprefix=s
                    maxlen=len(s)
        
            return longprefix
        else:
            return None


        
            
        