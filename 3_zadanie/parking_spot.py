class ParkingSpot:
    def __init__(self, number):
        self.number = number
        self.is_empty = True
        self.car = None
        
    def is_empty_spot(self):
        return self.is_empty
    
    def get_info(self):
        if self.is_empty is True:
            return f"Место №{self.number} свободно."
        else:
            return f"Место №{self.number} занято."
    
    