import math
import numpy as np


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


# def intersection(A, B, C, D):
#     a1 = B.y - A.y
#     b1 = A.x - B.x
#     c1 = a1*(A.x) + b1*(A.y)
#
#     a2 = D.y - C.y
#     b2 = C.x - D.x
#     c2 = a2*(C.x) + b2*(C.y)
#
#     d = a1*b2 - a2*b1
#
#     if d == 0:
#         return False
#
#     x = (b2*c1 - b1*c2)/d
#     y = (a1*c2 - a2*c1)/d
#
#     if min(A.x, B.x) <= x and x <= max(A.x, B.x) and min(C.x, D.x) <= x and x <= max(C.x, D.x):
#         return Point(x, y)
#     else:
#         return False

def intersection(A, B, C, D):
    px_num = ((A.x * B.y - A.y * B.x) * (C.x - D.x) - (A.x - B.x) * (C.x * D.y - C.y * D.x))
    px_denom = (A.x - B.x) * (C.y - D.y) - (A.y - B.y) * (C.x - D.x)
    if px_denom == 0: return False, Point(0, 0)
    else:
        px = px_num / px_denom

    py_num = ((A.x * B.y - A.y * B.x) * (C.y - D.y) - (A.y - B.y) * (C.x * D.y - C.y * D.x))
    py_denom = (A.x - B.x) * (C.y - D.y) - (A.y - B.y) * (C.x - D.x)
    if py_denom == 0: return False, Point(0, 0)
    else:
        py = py_num / py_denom

    if min(A.x, B.x) <= px and px <= max(A.x, B.x) and min(C.x, D.x) <= px and px <= max(C.x, D.x):
        return True, Point(px, py)
    else:
        return False, Point(0, 0)




def reflect(A, B, C, D):
    theta_ray = math.atan2((B.y - A.y), (B.x - A.x))
    theta_edge = math.atan2((D.y - C.y), (D.x - C.x))
    # if theta_ray <= 0:
    #     theta_out = -theta_ray - 2*(90-theta_edge)
    # elif theta_ray > 0 and theta_ray >= (np.pi/2 + theta_edge):
    #     theta_out = 2*theta_edge + 180 - theta_ray
    # else:
    #     theta_out = 2 * theta_edge - theta_ray
    #
    # return theta_out
    return 2 * theta_edge - theta_ray
