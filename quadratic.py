import math

def solve_quadratic (a,b,c):
    if  (pow(b,2)-4*a*c) > 0 :  
        print (     ( (-b + math.sqrt(pow(b,2)-4*a*c))/2) ,  ((-b - math.sqrt(pow(b,2)-4*a*c))/2)    )
    elif (pow(b,2)-4*a*c) == 0 :
        return -b/(2*a)
    else:
        return None
        