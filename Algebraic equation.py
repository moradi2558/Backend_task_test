import math

def solve_quadratic(a, b, c):
    
    delta = b**2 - 4*a*c
    
    
    if delta > 0:
        root1 = (-b + math.sqrt(delta)) / (2*a)
        root2 = (-b - math.sqrt(delta)) / (2*a)
        return root1, root2
    elif delta == 0:
        root = -b / (2*a)
        return root,
    else:
        return None


a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))


roots = solve_quadratic(a, b, c)

if roots is None:
    print("This equation has no real roots.")

elif len(roots) == 1:
    print(f"This equation has a double root: {roots[0]}")

else:
    print(f"This equation has two roots: {roots[0]} و {roots[1]}")