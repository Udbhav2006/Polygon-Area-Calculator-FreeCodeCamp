class Rectangle(width, height):
  def __init__(self):
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

  def get_amount_inside(self):
    


class Square:
