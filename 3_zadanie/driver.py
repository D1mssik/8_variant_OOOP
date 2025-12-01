class Driver:
    def __init__(self, name):
        self.name = name
        
    def get_info(self):
        return f"Водитель. Имя: {self.name}"