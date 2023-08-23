
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
import random

def random_generator():
   
    value1=random.randint(0,x)
    value2=random.randint(0,y)
    value3=random.randint(0,z)
    return value1, value2, value3
      
  
threshold= False
final=[]
if n == x+y+z:
    print ("Enter Valid input")
else:
    while threshold==False:
        result = random_generator()
        avg=sum(result)
        print(avg)
        if result not in final and avg!=n:
                final.append(result)
        else :
            break
             

    print(final)
        
        
        
        

