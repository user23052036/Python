class CUSTOMER:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address
    
    def intro(self):
        print('I am',self.name,'and gender is ',self.gender)
    
    def edit_profile(self,new_name,new_gender,new_city,new_pin,new_state):
        self.name = new_name
        self.gender = new_gender
        self.address.change_address(new_city,new_pin,new_state)

    def __repr__(self):
        return f"name: {self.name}\n gender: {self.gender}\n address: {self.address}"