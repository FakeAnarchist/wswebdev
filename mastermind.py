import random 

def generateSecret():
    possible_list = [1,2,3,4,5,6,7,8]
    secret = []
    for i in range(4):
        secret.append(str(possible_list.pop(random.randint(0,len(possible_list)-1))))

    t=tuple(secret)
    print(t)
    return t

def getInput():					
    allowed = ''.join([str(i) for i in range(1,9)])	
    while True:																					
        try:
            s = tuple(input('Select the colors by their number: '))								
            if len(set(s)) == 4 and len(s) == len(set(s)) and set(s).issubset(allowed):	
                return s
        except ValueError:
            pass

def match(t, k):
	return	{ 
		"placed":[ t[x]==k[x] for x in range(0,len(k)) ].count(True),"right":len(set(k).intersection(set(t)))						
	}



if __name__ == "__main__":
    t=getInput()
    k=generateSecret()    
    match(t,k)

