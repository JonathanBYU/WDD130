import math

class Circle:
    circumference = 0.0
    area = 0.0
    diameter = 0.0
    radius = 0.0

    def __init__(self,radius):
        self.radius = radius
        
    def get_radius(self):
        return self.radius
    
    def get_area(self):
        area = math.pi * self.radius * self.radius
        return area
    
    def set_radius(self,radius):
        self.radius = radius

def main():
    # x = 10
    # y = 1233.12
    # name = "Bob"
    # name.lower()

    my_circle = Circle(10)
    print(f'The radius is: {my_circle.get_radius()}')
    # print(x)

    my_circle.set_radius(23)
    print(f'The radius is: {my_circle.get_radius()}')


if __name__ == '__main__':
    main()