class Force:
    def __init__(self,x,y):
        self.fx,self.fy = x, y

    def show(self):
        return "(%f,%f)"%(self.fx,self.fy)
    __repr__ = show

    def __lt__(self,force2):
        return self.fx*self.fx + self.fy*self.fy < force2.fx*force2.fx \
               + force2.fy*force2.fy

fList = [Force(1,2), Force(0,2),Force(3,4),Force(2,1)]

ff = fList.copy()
ff.sort()
print(ff)

ft = sorted(fList,key =lambda x : x.fx * x.fx + x.fy * x.fy )
print(ft)