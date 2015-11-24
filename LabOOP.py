

class Expr:
    pass

class Plus(Expr):
    def __init__(self,l,r):
        self.l=l
        self.r=r

    def __str__(self):
        return "(" + str(self.l)+"+"+str(self.r)+")"

    def eval(self,eval):
        return self.l.eval(env) + self.reval(env)

class Mult(Expr) :
    def __init__(self,l,r):
        self.l=l
        self.r=r

    def __str__(self):
        return "("+str(self.l)+"*"+str(self.r)+")" 
    
    def eval(self,env):
        return self.l.eval(env) * self.r.eval(env) 
    
class Const(Expr) :
    def __init__(self,v):
        self.v = v

    def eval(self,env) :
        return self.v

    def __str__(self):
        return str(self.v)

class Var(Expr) :
    def __init__(self,n) :
        self.n = n

    def __str__(self) :
        return self.n

    def eval(self,env) :
        return env[self.n]


e1 = Plus(Mult(Const(2),Plus(Var("x"),Const(4))),Const(7))
e2 = Plus(Plus(Const(1),Const(2)),Const(3))
e3 = Plus(Const(1),Plus(Const(2),Const(3))) 

class Or(l,r):
    pass

def __init__(self,l,r):
        self.l=l
        self.r=r
    
def equiv(l,r):
        if l != r:
            return "Or(And("+l+","+r+"),And(Not("+l+"),Not("+r+")))"

def __str__(self,l,r):
        return "("+str(self.l)+"*"+str(self.r)+")"


    
