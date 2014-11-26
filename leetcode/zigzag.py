class Solution:
    # @return a string
    def convert(self, s, nRows):
        len_s=len(s)
        l=list(s)
        ll=[]
        if len_s==0 or len_s<nRows or nRows==1:
            return s
             
        for r in range(0,nRows):
                if r==0 or r==(nRows-1):
                    gap=2*(nRows-1)
                    k=r      
                    while k<len_s:
                        ll.append(s[k])
                        k=k+gap
                    
                   
                else:
                    gap1=2*(nRows-1)
                    gap2=2*(nRows-1-r)
                    k=r
                    ll.append(s[k])
                    while k<len_s and gap2>0 and (k+gap2)<len_s:
                        ll.append(s[k+gap2])
                        if (k+gap1)<len_s:
                            ll.append(s[k+gap1])
                        k=k+gap1
                       
        return ''.join(ll)
        



