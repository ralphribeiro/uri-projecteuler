"""
    Integer right triangles

    If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.
    {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p ≤ 1000, is the number of solutions maximised?

 """

def is_right_angled(a, b, c):
    return a**2 + b**2 == c**2


def get_triangle(perimeter):
    triangles = set()
    for a in range(1, perimeter + 1):
        for b in range(a, perimeter + 1):
            c = perimeter - a - b
            if a + b + c == perimeter and is_right_angled(a, b, c):
                triangles.add(tuple(sorted([a, b, c])))
    return triangles


def main():
    max_perimiter = 0
    max_count = 0
    for perimeter in range(1, 1001):
        triangles = get_triangle(perimeter)
        count = len(triangles)
        if count > max_count:
            max_count = count
            max_perimiter = perimeter
    return max_perimiter


if __name__ == '__main__':
    print(main())