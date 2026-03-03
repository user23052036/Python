class Address:
    def __init__(self,city,pincode,state):
        self.city = city
        self.pincode = pincode
        self.state = state

    def change_address(self,new_city,new_pin,new_state):
        self.city = new_city
        self.pincode = new_pin
        self.state = new_state

    def __repr__(self):
        return f"city: {self.city} pin: {self.pincode} state: {self.state}"