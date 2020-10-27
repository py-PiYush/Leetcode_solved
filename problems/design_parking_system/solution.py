class ParkingSystem:
    b=0
    m=0
    s=0

    def __init__(self, big: int, medium: int, small: int):
        self.big=big
        self.medium=medium
        self.small=small
        

    def addCar(self, carType: int) -> bool:
        
        if carType==1:
            self.b+=1
            if self.b>self.big:
                return False
        if carType==2:
            self.m+=1
            if self.m>self.medium:
                return False
        if carType==3:
            self.s+=1
            if self.s>self.small:
                return False
        return True
            
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)