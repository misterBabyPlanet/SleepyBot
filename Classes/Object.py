class Object:
    """ Object from Shop"""

    def __init__(self, name, price, picture_path):
        self.name = name,
        self.price = price,
        self.picture_path = picture_path

    def getName(self):
        return self.name

    def setName(self, new_name):
        self.name = new_name

    def getPrice(self):
        return self.price

    def setPrice(self, new_price):
        self.price = new_price

    def getPicture_path(self):
        return self.picture_path

    def setPicture_path(self, new_picture_path):
        self.picture_path = new_picture_path
