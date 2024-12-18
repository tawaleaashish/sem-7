import numpy as np
import binascii
pc1=np.array([57,49,41,33,25,17,9
              ,1,58,50,42,34,26,18
              ,10,2,59,51,43,35,27
              ,19,11,3,60,52,44,36
              ,63,55,47,39,31,23,15
              ,7,62,54,46,38,30,22
              ,14,6,61,53,45,37,29
              ,21,13,5,28,20,12,4])
shift=np.array([1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1])
pc2=np.array([14,17,11,24,1,5
              ,3,28,15,6,21,10
              ,23,19,12,4,26,8
              ,16,7,27,20,13,2
              ,41,52,31,37,47,55
              ,30,40,51,45,33,48
              ,44,49,39,56,34,53
              ,46,42,50,36,29,32])
initialPermutation=np.array([58,50,42,34,26,18,10,2
                             ,60,52,44,36,28,20,12,4
                             ,62,54,46,38,30,22,14,6
                             ,64,56,48,40,32,24,16,8
                             ,57,49,41,33,25,17,9,1
                             ,59,51,43,35,27,19,11,3
                             ,61,53,45,37,29,21,13,5
                             ,63,55,47,39,31,23,15,7])
Ebit=np.array([32,1,2,3,4,5
               ,4,5,6,7,8,9
               ,8,9,10,11,12,13
               ,12,13,14,15,16,17
               ,16,17,18,19,20,21
               ,20,21,22,23,24,25
               ,24,25,26,27,28,29
               ,28,29,30,31,32,1])
S=np.array([[[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
           ,[[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]
           ,[[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]
           ,[[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]
           ,[[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]
           ,[[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]
           ,[[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]
           ,[[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]])
P=np.array([16,7,20,21
            ,29,12,28,17
            ,1,15,23,26
            ,5,18,31,10
            ,2,8,24,14
            ,32,27,3,9
            ,19,13,30,6
            ,22,11,4,25])
IP_inverse=np.array([40,8,48,16,56,24,64,32
                     ,39,7,47,15,55,23,63,31
                     ,38,6,46,14,54,22,62,30
                     ,37,5,45,13,53,21,61,29
                     ,36,4,44,12,52,20,60,28
                     ,35,3,43,11,51,19,59,27
                     ,34,2,42,10,50,18,58,26
                     ,33,1,41,9,49,17,57,25])

class Solution:  

    def formattedText(self,text):
        text=text.upper()
        l=len(text)
        if l%8>0:
            for i in range(8-(l%8)):
                text+="0"
        return text,l         

    def Kplus_IP(self,plaintext,key):
        k=""
        for i in pc1:
            k+=key[i-1]
        p=""
        for i in initialPermutation:
            p+=plaintext[i-1]    
        return k,p
    
    def EbitSelection(self,right):
        er=""
        for i in Ebit:
            er+=right[i-1]
        return er 

    def keyValue(self,c,d):
        l=[]
        for i in range(16):
            c=c[shift[i]:]+c[:shift[i]]
            d=d[shift[i]:]+d[:shift[i]]
            x=c+d
            key=""
            for j in pc2:
                key+=x[j-1]
            l.append(key)    
        return l
    
    def Sbox(self,l,j):
        Srow=int(l[0]+l[-1],2)
        Scol=int(l[1:5],2)
        val=format(S[j,Srow,Scol],'b')
        while len(val)<4:
            val="0"+val
        return val

    def PermuteFunc(self,func32):
        a=""
        for i in P:
            a+=func32[i-1]
        return a    
    
    def final_IP_inverse(self,L,R):
        x=R[:]+L[:]
        c=""
        for i in IP_inverse:
            c+=x[i-1]
        c=str(hex(int(c,2))).upper()  
        return c   
       
    def encrypt(self,plaintext,key):
        key_plus,IPplain=self.Kplus_IP(plaintext,key)
        c=key_plus[:28]
        d=key_plus[28:]
        L=IPplain[:32]
        R=IPplain[32:]
        keys_list=self.keyValue(c,d)
        for i in range(16):
            X=R[:]
            ER=self.EbitSelection(R[:])
            func=""
            for j in range(48):
                if ER[j]==keys_list[i][j]:
                    func+="0"
                else:
                    func+="1"  
            func32=""    
            func_start=0     
            for j in range(8):
                func32+=self.Sbox(func[func_start:func_start+6],j)
                func_start+=6   
            func32=self.PermuteFunc(func32) 
            Y=""
            for j in range(32):
                if L[j]==func32[j]:
                    Y+="0"
                else:
                    Y+="1"         
            L=X[:]
            R=Y[:]   
        ciphertext=self.final_IP_inverse(L,R) 
        return ciphertext[2:]      

    def decrypt(self,ciphertext,key):
        key_plus,IPcipher=self.Kplus_IP(ciphertext,key)
        c=key_plus[:28]
        d=key_plus[28:]
        L=IPcipher[:32]
        R=IPcipher[32:]
        keys_list=self.keyValue(c,d)
        for i in range(16):
            X=R[:]
            ER=self.EbitSelection(R[:])
            func=""
            for j in range(48):
                if ER[j]==keys_list[15-i][j]:
                    func+="0"
                else:
                    func+="1"  
            func32=""    
            func_start=0     
            for j in range(8):
                func32+=self.Sbox(func[func_start:func_start+6],j)
                func_start+=6   
            func32=self.PermuteFunc(func32) 
            Y=""
            for j in range(32):
                if L[j]==func32[j]:
                    Y+="0"
                else:
                    Y+="1"         
            L=X[:]
            R=Y[:]   
        plaintext=self.final_IP_inverse(L,R) 
        return plaintext[2:].rjust(16,"0")      

    def E_PT(self,PT,key):
        CT=""
        m=len(PT)//64
        for i in range(m):
            CT+=self.encrypt(PT[i*64:(i*64)+64],key)
        return CT    

    def D_CT(self,CT,key):
        PT=""
        m=len(CT)//64
        for i in range(m):
            PT+=self.decrypt(CT[i*64:(i*64)+64],key)
        return PT  
      
plaintext=input("Plaintext message: ")
plaintext,l=Solution().formattedText(plaintext)
plaintext=binascii.hexlify(plaintext.encode()).decode()
key="133457799BBCDFF1"

key="".join(['{0:04b}'.format(int(d,16)) for d in key])
plaintext="".join(['{0:04b}'.format(int(d,16)) for d in plaintext.rjust(16,"0")])

ciphertext=Solution().E_PT(plaintext,key)
print("Encrypted message: "+ciphertext)

ciphertext="".join(['{0:04b}'.format(int(d,16)) for d in ciphertext])

a=Solution().D_CT(ciphertext,key)
ciphertext=binascii.unhexlify(a.encode()).decode()
print("Decrypted message: "+ciphertext[:l])