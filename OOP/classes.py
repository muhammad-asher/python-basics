# Pascal Naming convention
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("Move")

    def draw(self):
        print("draw")


pointobj = Point(10,20)
pointobj.x = 11
pointobj.y = 22
pointobj.move()
print(pointobj.x,pointobj.y)

pointobj2 = Point(30,40)
pointobj2.draw()

point = Point(50, 60)
print(point.x)
