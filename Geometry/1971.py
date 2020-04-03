from math import sqrt, acos

def dist(v1, v2):
    return sqrt((v1[0]-v2[0])**2 + (v1[1]-v2[1])**2)

def dot(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1]

def cross(v1, v2, v3):
    return (v2[0]-v1[0])*(v3[1]-v1[1]) - (v2[1]-v1[1])*(v3[0]-v1[0])

def norm(v1):
    return sqrt(v1[0]*v1[0] + v1[1]*v1[1])

def angle(v1, v2):
    return acos(dot(v1,v2)/(norm(v1)*norm(v2)))

def sort_points_by_y(vect):
    return sorted(vect, key = lambda x: (x[1], x[0]))

def sort_points_by_angle(vect):
    l = len(vect)
    angles = list(map(angle, [(1,0) for _ in range(l)], vect))

    for k in range(l-1):
        for w in range(k+1,l):
            if angles[k] > angles[w]:
                vect[k], vect[w] = vect[w], vect[k]
                angles[k], angles[w] = angles[w], angles[k]

    return vect, angles

def remove_collinear(p0, vect, angles):
    l = len(vect)

    to_remove_vect = []
    to_remove_angle = []
    for k in range(l-1):
        for w in range(k+1,l):
            if angles[k] == angles[w]:
                if dist(p0,vect[k]) < dist(p0,vect[w]):
                    to_remove_vect.append(vect[k])
                    to_remove_angle.append(angles[k])
                else:
                    to_remove_vect.append(vect[w])
                    to_remove_angle.append(angles[w])

    for v,a in zip(to_remove_vect, to_remove_angle):
        vect.remove(v)
        angles.remove(a)

    return vect, angles, to_remove_vect, to_remove_angle

def graham_scan(p0, vect):
    if len(vect) < 2:
        return "Convex hull is empty"

    stack = [p0, vect[0], vect[1]]
    stack_size = 3

    if len(vect) == 2:
        return stack

    l = len(vect)
    for k in range(2, l):
        while(True):
            print(stack)
            d = cross(stack[stack_size - 2], stack[stack_size - 1], vect[k])
            print(d)
            if d < 0: # left turn
                break
            else: # non left turn
                stack.pop()
                stack_size -= 1
        stack.append(vect[k])
        stack_size += 1

    return stack

p1 = (1,1)
p2 = (5,3)
p3 = (7,6)
p4 = (3,5)
a1 = (4,4)
a2 = (6,4)

# Pipeline
#    1 - sort_points_by_y
#    2 - sort_points_by_angle
#    3 - remove_collinear
