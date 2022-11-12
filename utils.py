import numpy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# class Line:
#     def __init__(self, p1, p2):
#         self.p1 = p1
#         self.p2 = p2
#         self.r = numpy.sqrt((p1.x - p2.x)^2 + (p1.y - p2.y)^2)
#         self.theta = numpy.arctan((p1.y - p2.y)/(p1.x - p2.x))

def intersection(A, B, C, D):
    a1 = B.y - A.y
    b1 = A.x - B.x
    c1 = a1*(A.x) + b1*(A.y)
 
    a2 = D.y - C.y
    b2 = C.x - D.x
    c2 = a2*(C.x) + b2*(C.y)

    d = a1*b2 - a2*b1

    if d == 0:
        return False

    x = (b2*c1 - b1*c2)/d
    y = (a1*c2 - a2*c1)/d

    if min(A.x, B.x) <= x and x <= max(A.x, B.x) and min(C.x, D.x) <= x and x <= max(C.x, D.x):
        return Point(x, y)
    else:
        return False

def reflect(A, B, C, D):
    theta1 = B / A