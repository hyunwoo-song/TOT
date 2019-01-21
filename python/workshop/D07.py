class Circle():
    pi = 3.14
    x = 0
    y = 0
    r = 0

    def area(self):
        return self.pi * self.r * self.r

    def circumference(self):
        return 2 * self.pi * self.r

    def center(self):
        return (self.x, self.y)

    def move(self, x, y):
        self.x = x
        self.y = y


aaa = Circle()
print(aaa.x, aaa.y, aaa.r)
aaa.x = 2
aaa.y = 4
aaa.r = 3
print(aaa.x, aaa.y, aaa.r)

bbb = Circle()
bbb.x =1
bbb.y = 5
bbb.r =4
print(bbb.x, bbb.y, bbb.r)

print(aaa.area())
print(aaa.circumference())
print(bbb.center())