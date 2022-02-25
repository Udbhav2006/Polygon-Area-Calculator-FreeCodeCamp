class Rectangle():
  def __init__(self, width, height):
    self.width = int(width)
    self.height = int(height)

  def set_width(self, new_width):
    self.width = int(new_width)

  def set_height(self, new_height):
    self.height = int(new_height)

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    pic = ''
    for i in self.height:
      pic += '*' * self.width + '\n'
    return pic

  def get_amount_inside(self, shape):
    height_left = self.height
    count = 0
    for i in shape.height:
      if i < height_left:
        height_left -= i
        count += self.width // shape.width
    return count
  
  def __str__(self):
    return f"Rectangle(width = {str(self.width)}, height = {str(self.height)})"

class Square:
  pass