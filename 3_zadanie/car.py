class Car:
    def __init__(self, model, driver):
        self.model = model
        self.driver = driver
        
    def get_info(self):
        return f"Автомобиль. Модель: {self.model}. Водитель: {self.driver}"