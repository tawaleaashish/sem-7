import random
P=random.randint(10,2^32)
G=random.randint(10,2^32)
print("Public numbers for Alice and Bob is P:",P," G:",G)
class Solution:
    def Alice_secret_key(self):
        a=17
        x=(G**a)%P
        return x   
    
    def Bob_secret_key(self):
        b=31
        y=(G**b)%P
        return y  
      
    def Alice(self):
        a=17
        print("Private key for Alice is a:",a)
        x=(G**a)%P
        print("Computed public key for Alice is x:",x)
        y=self.Bob_secret_key()
        print("Public key received from Bob b:",y)
        key_a=(y**a)%P
        print("Alice's shared secret key ka:",key_a)

    def Bob(self):
        b=31
        print("Private key for Bob is b:",b)
        y=(G**b)%P
        print("Computed public key for Bob is y:",y)
        x=self.Alice_secret_key()
        print("Public key received from Alice a:",x)
        key_b=(x**b)%P
        print("Bob's shared secret key kb:",key_b)


print("\nAlice's Case:")
Solution().Alice()
print("\nBob's Case:")
Solution().Bob()