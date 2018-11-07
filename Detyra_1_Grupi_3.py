class DetyraEPare:
    
    def __init__(self,_array):
        self.array = array
        self.vleraMaksimale = self.shumaMaksimaleDC(0,len(self.array)-1)
        print("Shuma maksimale qe eshte gjendur ne ",self.array," eshte : ",self.vleraMaksimale)
        
    def shumaMaksimaleDC(self,_from,_to):
        if _from == _to:
            return self.array[1]
        #Pika e mesit
        _middle = (_from+_to)//2
        #Tash duhet me kqyr per qdo ane
        #Per anen e majt, anen e djatht dhe ne fund me kqyr kombinimin
        #Pasi ti gjajm vlerat max per kto pozita, atehere duhet me mor vleren maksimale
        return max(self.shumaMaksimaleDC(_from,_middle),self.shumaMaksimaleDC(_middle+1,_to),self.shumaMaksimaleNdermjet(_from,_middle,_to))

    def shumaMaksimaleNdermjet(self,_from,_middle,_to):
        tempCount = 0
        shumaMajtas = -100000000
        #Me gjet shumen maksimale majtas
        for i in range(_middle,_from-1,-1):
            tempCount = tempCount + self.array[i]
            if(tempCount > shumaMajtas):
                shumaMajtas = tempCount
                
        #Me gjet shumen maksimale ne anen e djatht
        tempCount = 0
        shumaDjathtas = -100000000
        for i in range(_middle+1,_to+1):
            tempCount = tempCount + self.array[i]
            if tempCount > shumaDjathtas:
                shumaDjathtas = tempCount
        return shumaMajtas+shumaDjathtas
array =[-3,2,1,1,-5]
obj = DetyraEPare(array)

    