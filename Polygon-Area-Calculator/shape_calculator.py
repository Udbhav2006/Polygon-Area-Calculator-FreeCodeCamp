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
    if self.height > 50  or self.width > 50:
      return "Too big for picture."
    else: 
      pic = ''
      for i in range(0, self.height):
        pic += '*' * self.width + '\n'
      return pic

  def get_amount_inside(self, shape):
    height_left = self.height
    count = 0
    while shape.height < height_left:
      height_left -= shape.height
      count += self.width // shape.width
    return count
  
  def __str__(self):
    return f"Rectangle(width={str(self.width)}, height={str(self.height)})"

class Square(Rectangle):
  def __init__(self, side):
      self.width = int(side)
      self.height = int(side)
  
  def set_side(self, new_side):
    self.width = int(new_side)
    self.height = int(new_side)

  def set_height(self, new_height):
    self.set_side(new_height)
  
  def set_width(self, new_width):
      self.set_side(new_width)
  
  def __str__(self):
      return f"Square(side={self.width})"

