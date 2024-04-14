class Shape:
  def __init__(self,color):
    self.color = color
    
  
  def area(self):
    pass
class Rectangle(Shape):
    def __init__(self,color,width,height):
      super().__init__(color)
      self.width = width
      self.height = height
      
    def area(self):
      return self.width * self.height
def main():
    my_rectangle = Rectangle("Blue", 5, 4)
    print("Color:", my_rectangle.color)
    print("Width:", my_rectangle.width)
    print("Height:", my_rectangle.height)
    print("Area:", my_rectangle.area())

if __name__ == "__main__":
    main()    
      