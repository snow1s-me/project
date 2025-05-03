import math


def solve_quadratic(a, b, c):
    D = b**2 - 4*a*c
    print(f"Дискримінант: D = {D}")

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(f"Рівняння має два корені: x1 = {x1}, x2 = {x2}")