import numpy as np
import sympy as sp
import string
alp=string.ascii_uppercase
alp+=" _?:,.!0123456789"
class Solution:
    def key_matrix(self,encrp_key):
        l=[]
        for i in encrp_key:
            l.append(alp.index(i))
        l=np.array(l).reshape(3,3)
        return l    
    
    def formatted_text(self,plaintext):
        plaintext="".join([ch.upper() for ch in plaintext])
        extra=len(plaintext)
        while len(plaintext)%3!=0:
            plaintext+="X"       
        return plaintext,extra

    def Encrypt_Pairs(self,pairs,matrix):
        l=[]
        for i in pairs:
            l.append(alp.index(i))
        l=np.array(l).reshape(3,1)    
        
        r=np.dot(matrix,l)%43
        r=r.reshape(1,3)
        text=""
        for i in r[0]:
            text+=alp[i]
        return text    
    
    def Decrypt_Pairs(self,pairs,dmatrix):
        l=[]
        for i in pairs:
            l.append(alp.index(i))
        l=np.array(l).reshape(3,1)

        r=np.dot(dmatrix,l)%43
        r=r.reshape(1,3)
        text=""
        for i in r[0]:
            text+=alp[i]
        return text    

    def mod_inverse_matrix(self, matrix, modulus):
        dmatrix=np.array(sp.Matrix(matrix).inv_mod(modulus))
        return dmatrix
    
    def Encrypt(self,plaintext,encrp_key):
        plaintext=plaintext.upper()
        matrix=Solution().key_matrix(encrp_key)
        formatted_plaintext,extra=Solution().formatted_text(plaintext)
        ciphertext=""
        for i in range(0, len(formatted_plaintext), 3):
            ciphertext+=Solution().Encrypt_Pairs(formatted_plaintext[i:i + 3],matrix)
        return ciphertext,extra,matrix        
        
    def Decrypt(self,ciphertext,extra,matrix):
        dmatrix=Solution().mod_inverse_matrix(matrix,43)   
        print("Decryption key matrix: \n",dmatrix) 
        plaintext=""
        for i in range(0, len(ciphertext), 3):
            plaintext+=Solution().Decrypt_Pairs(ciphertext[i:i + 3],dmatrix)
        return plaintext[:extra]    

plaintext="Hi I am Ash,I am 21."
print("Plaintext: ",plaintext)
key="GYBNQKURP"
ciphertext,extra,matrix=Solution().Encrypt(plaintext,key)
print("Encryption key matrix: \n",matrix)
print("Encrypted message: ",ciphertext)

a=Solution().Decrypt(ciphertext,extra,matrix)
print("Decrypted message: ",a)