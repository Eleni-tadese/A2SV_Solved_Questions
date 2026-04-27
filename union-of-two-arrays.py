t = int (input())
for _ in range(t):
    s = input()
    
    p1 =0
    p2 =1
    check=[]
    while p2<len(s):
        
        if s[p1] == s[p2]:
            check.append(s[p1])
            p1+=1
            p2+=1
    
          
        else:
        
            p2 += 1
        
    print(check)
            
           
            
        
           
    
        