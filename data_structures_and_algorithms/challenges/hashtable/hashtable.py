class Hashmap:
    def __init__(self,size):
        self.size=size 
        self.map=[None]*size

    def hash(self,key):
        ascii_tot=0
        for char in key:
            ascii_tot += ord(char) 
        hashed_key= (ascii_tot*17)%self.size      
        return hashed_key


    def add(self,key,value):
        idx=self.hash(key)
        if self.map[idx] == None :
            self.map[idx]=[[key,value],]
        else:
            self.map[idx].append([key,value])

    def contains(self,key):
        idx=self.hash(key)
        x= dict(self.map[idx])
        y=x.keys()
      
        if key in y :
            return True
        else:
            return False       

    def get(self,key):
        idx=self.hash(key)
        x= dict(self.map[idx])
        # if key in x.items():
        #     return x.values()
        for key, value in x.items():
            if key == key:
                return value


    
if __name__ == "__main__":
    hashtab=Hashmap(1024)
    hashtab.add('name','Ran')
    hashtab.add('age','24')
    hashtab.add('gen','Fem')
    print(hashtab.hash('gen'))
    print(hashtab.contains('gen'))
    print(hashtab.get('gen'))
    #print(hashtab.get('gen','fem'))
    #print(hashtab.map[hashtab.get_hash('gen')])
    #print(hashtab.map[1::2])