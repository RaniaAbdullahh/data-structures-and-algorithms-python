def areBracketsBalanced(expr): 
    a = [] 
  
    for i in expr: 
        if i in ["(", "{", "["]: 
  
           
            a.append(i) 
        else: 
  
     
            if not a: 
                return False
            x = a.pop() 
            if x == '(': 
                if i != ")": 
                    return False
            if x == '{': 
                if i != "}": 
                    return False
            if x == '[': 
                if i != "]": 
                    return False
  
    # Check Empty Stack 
    if a: 
        return False
    return True
  
  
# Driver Code 
if __name__ == "__main__": 
  
    # Function call 
    print(areBracketsBalanced( "{()}[]")) 
   