#from data_structures_and_algorithms.challenges.hashtable.hashtable import Hashmap

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


def left_join(ht_one, ht_two):

    
    listtt = []
    for element in ht_one:
        if element:

            i = 0
            curr_elem = element[i]


            while curr_elem:

                key = curr_elem[0]

                if ht_two.contains(key):
                    listtt.append([key, curr_elem[1], ht_two.get(key)])


                else:
                    listtt.append([key, curr_elem[1], None])
                try:    
                    if element[i+1]:
                        i+=1
                        curr_elem = element[i]
                    else:
                        curr_elem = None
                except:
                    break

    return listtt


if __name__ == "__main__":
    one = Hashmap()
    one.add('fond','enamored')        
    one.add('wrath', 'anger')          
    one.add('diligent', 'employed')    
    one.add('outfit', 'garb')           
    one.add('guide', 'usher')
    two = Hashmap()
    two.add('fond', 'averse')
    two.add('wrath', 'delight')
    two.add('diligent', 'idle')
    two.add('guide', 'follow')
    two.add('flow', 'jam')
    print(left_join(one,two))    

    