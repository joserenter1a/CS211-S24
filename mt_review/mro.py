
class O():
    pass
class I(int):
    pass

class A(I, int):
    def polymorphic_add(self, x, y):
       return x.__add__(y)


A = A()
sol = (A.polymorphic_add('1', '2'))
#print(sol, type(sol))


l = [0xff] * 0xff
#print(len(l))

o = O()
#print(O.__mro__)

matrix = [[]] * 10 * 10

class fake():
    def print(self,object):
        print (f'FAKE PRINT: {object}')
        return object
f = fake()
r = "REAL OBJECT"
g = f.print(r)
x = g
print(f.print(x))

def w():
    print('1')
    return True

