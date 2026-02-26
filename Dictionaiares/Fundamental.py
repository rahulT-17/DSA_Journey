# Building a tiny hash tables :

# step 1 : creating a storage for the hash table :

class SimpleHashTable :
    def __init__(self,size) :
        self.size = size
        self.table = [None] * size

# step 2 : creating a hash function to convert the key into an index :
    def hash_function(self,key) :
        return hash(key) % self.size
    
# step 3 : creating a method to insert key-value pairs into the hash table :  

# """ this have a huge problem of hash collision but we will solve it later ."""

    def insert(self,key,value) :                   
        index = self.hash_function(key)
        self.table[index] = value                 


"""HASH COLLISION : when two different keys produce the same hash value and thus the same index in the hash table,
                    this causes a collision and we need to handle it to avoid data loss ."""

# 2 ways to handle hash collision :
# Chaining : we can store multiple key-value pairs at the same index using a linked list or a list .

# Open Addressing : we can find the next available index in the hash table to store the key-value pair .

"Seeing how Chaining works :"


