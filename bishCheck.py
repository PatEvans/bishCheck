def squareCheck(x1,y1,x2,y2):
    if(x1 > 8 or x2 >8 or y1>8 or y2 >8): return 0;
    if(x1 < 1 or x2 < 1 or y1< 1 or y2 < 1): return 0;
    #checks that x2,y2 is reachable from x1,y1
    if(((x1+y1) %2 ==0 and (x2+y2) %2 ==0) or ((x1+y1) %2 ==1 and (x2+y2) %2 ==1)):
        #this means target is reachable
        return 1;
    else:
        return 0;

def bishCheck(x1,y1,x2,y2):
    if (squareCheck(x1,y1,x2,y2)==0):
        print("Unreachable");
    elif(abs(y2-y1)==abs(x2-x1)==0):
         print("0 moves");
    elif(abs(y2-y1)==abs(x2-x1)):
        print("1 move");
    else:
        print("2 moves");
        

bishCheck(2,2,3,3);

            
    
        
