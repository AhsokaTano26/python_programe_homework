class Vector3D:
    def __init__(self,x,y,z):
        self.x,self.y,self.z = x,y,z
    
    def __str__(self):
        return str((self.x,self.y,self.z))

    def __add__(self,v):
        return Vector3D(self.x+v.x,self.y+v.y,self.z+v.z)

    def __sub__(self,v):
        return Vector3D(self.x-v.x,self.y-v.y,self.z-v.z)

    def length(self):
        return (self.x**2+self.y**2+self.z**2)**0.5
    
v1 = Vector3D(1,2,3)
v2 = Vector3D(4,5,6)
v3 = v1 + v2
v4 = v2 - v1 
print("v1 =",v1)
print("Length of v1 =", v1.length())
print(f"{v1}+{v2}={v3}")
print(f"{v2}-{v1}={v4}")