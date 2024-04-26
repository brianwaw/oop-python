class Restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        restaurant = {"restaurantName":self.restaurant_name, "cuisineType" : self.cuisine_type}
        print(restaurant)


class Flavors:
    def __init__(self, flavors):
        self.flavors = flavors

    def printFlavors(self):
        for flavor in self.flavors:
            print(flavor)


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cusine_type, flavors):
        super().__init__(restaurant_name, cusine_type)
        self.flavor_object = Flavors(flavors)

myicestand = IceCreamStand('brianstand','fresh', ['strawberry','vanilla'])

myicestand.flavor_object.printFlavors()