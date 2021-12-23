from PIL import ImageDraw, Image


class Rectangle ():
    def __init__(self, width, height, fill='gray',outline=None ):  # size: tuple (x,y)
        if width == 0 or height == 0:
            print('its line or dot oskol')
            return
        self.__width, self.__height = width, height
        self.fill = fill
        self.outline= outline

    def __size_validation(self):
        if self.__width == 0 or self.height == 0:
            return False

    def __is_drawable(self, rect_location, image):
        # rect_location: [(x1, y1), (x2,y2)]
        image_x, image_y = image.size
        if rect_location[0][0] < 0 or rect_location[0][1] < 0 or rect_location[1][0] > image_x or rect_location[1][1] > image_y:
            return False
        return True

    # we must init image before
    def draw(self, center, image):  # center point: tuple(x,y)
        cx, cy = center
        rect_xy = [(cx-self.__width/2, cy-self.__height/2),
                   (cx+self.__width/2, cy+self.__height/2)]
        if not self.__is_drawable(rect_xy, image):
            print(f'undrawable {rect_xy} rect  in {image.size} page')
            return False
        paper = ImageDraw.Draw(image)
        paper.rectangle(rect_xy, fill=self.fill, outline=self.outline)
        return True

    def size(self):
        return (self.__width, self.__height)
    def swap_height_width(self):
        self.__width, self.__height = self.__height, self.__width
        


""" whiteboard = Image.new('RGB', (200, 200), color='white')
rect1 = Rectangle(40, 50)
rect1.draw((100, 100), whiteboard)
print(rect1.size())
whiteboard.show() 
 """