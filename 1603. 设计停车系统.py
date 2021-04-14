class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.left=[big,medium,small]


    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if self.left[carType-1] == 0:
            return False
        else:
            self.left[carType-1] -=1
            return True



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)