def gcd(a,b):
    a,b=abs(a), abs(b)
    if a<b:
        t=a
        a=b
        b=t
    if a%b==0:
        return b
    else:
        return gcd(a%b, b)

class Fraction:
    def __init__(self,a,b):
        if a==0:
            self.a=0
            self.b=1
            return
        if a*b<0:
            a=-abs(a)
            b=abs(b)
        d=gcd(a,b)
        a=int(a/d)
        b=int(b/d)
        self.a=a
        self.b=b
    def __repr__(self):
        return str(self.a)+'/'+str(self.b)
    def __str__(self):
        return str(self.a)+'/'+str(self.b)
    def __add__(self,other):
        return Fraction(self.a*other.b+self.b*other.a, self.b*other.b)
    def __sub__(self, other):
        return Fraction(self.a*other.b-self.b*other.a, self.b*other.b)
    def __neg__(self):
        return Fraction(0,1)-self
    def __mul__(self, other):
        return Fraction(self.a*other.a,self.b*other.b)
    def __truediv__(self, other):
        return self*Fraction(other.b,other.a)
    def __pow__(self, other):
        return (self.a/self.b)**other
    def __eq__(self,other):
        if self.a==other.a and self.b==other.b:
            return True
        return False
    def __gt__(self, other):
        if (self-other).a>0:
            return True
        return False
  
def Euc(a,b):
    x=0
    if a<b:
        t=a
        a=b
        b=t
        x=1
    if a%b==0:
        M=1
        N=-a//b+1
        if x==1:
            t=M
            M=N
            N=t
        return [M,N]
    else:
        r=a%b
        q=(a-a%b)//b
        m=Euc(r,b)[0]
        n=Euc(r,b)[1]
        M=m
        N=n-q*m
        if x==1:
            t=M
            M=N
            N=t
        return [M,N]

def inv(a,p):
    x=Euc(a,p)[0]
    x=x%p
    return x

def prime(N):
    N=N-2
    A=2
    P=[]
    P.append(A)
    A=3
    P.append(A)
    while A<=N:
        A=A+2
        t=2+N**0.5
        t=int(t)
        for p in P:
            if p>t:
                break
            if A%p==0:
                break
        if A%p==0:
            continue
        P.append(A)
    return P


def RIntegral(f, lower, higher):
    step=0.001
    a=lower
    result=0
    while a<higher:
        result+=step*(f(a)+f(a+step))/2
        a+=step
    return result

