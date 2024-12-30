def collect(f,a,b,n):
    h=(b-a)/n
    area=0
    area=(f(a)+f(b))/2.0
    for i in range(1,n):
        area+=f(a+i*h)
    return area*h



