from random import randint
from MH import prime, gcd, inv
from copy import deepcopy
import sys

def No_2(N):
    i=0
    while N%2==0:
        i+=1
        N/=2
    return i, int(N)

def pow_mod(a,x,p):
    t=a
    for i in range(x-1):
        a*=t
        a%=p
    return a

def Rabin(p, a):
    n=p-1
    t, m=No_2(n)
    result=pow(a, m, p)
    if result==1 or result==p-1:    return True
    i=0
    while i<t-1:
        result=pow_mod(result, 2, p)
        if result==1:   return False
        if result==p-1:  return True
        i+=1
    return False

def Rabin_fast(p, a):
    n=p-1
    t, m=No_2(n)
    result=pow(a, m, p)
    if result==1 or result==p-1:    return True
    i=0
    while i<t-1:
        result=pow_mod(result, 2, p)
        if result==1:   return False
        if result==p-1:  return True
        i+=1
    return False


def n_random(r, n):  #from 2 to r-1
    result=[]
    i=0
    while i<n:
        a=randint(2, r-1)
        if  not a in result:
            result.append(a)
            i+=1
    return result

def prime_test(p, n=5):
    rands=n_random(p, n)
    for i in rands:
        if not Rabin(p, i): return False
    return True     

def prime_test_fast(p):#n=5
    rands=[2, 3,7, 11, 43]
    for i in rands:
        if not Rabin_fast(p, i): return False
    return True     



def correctness_test():
    prime_list=prime(20000)
    t=1001
    while t<20000:
        if prime_test_fast(t):
            if t not in prime_list:
                print(t,"   Composite Accepted!")
        else:
            if t in prime_list:
                print(t, "  PRIME REJECTED!!")
        t+=2
    print("Finished")
    input()

def generate_prime(a=10, b=16):
    x=randint(10**a, 10**b)
    if x%2==0:
        x+=1
    while not prime_test_fast(x):
        x+=2
    return x


def generate_key():
    p=generate_prime()
    q=generate_prime()
    m=(p-1)*(q-1)
    a=randint(10**6, 10**7)
    while not gcd(a, m)==1:
        a=randint(10**6, 10**7)
    b=inv(a, m)
    return p*q, a, b


def correctness_test_RSA():
    N, alpha, beta=generate_key()
    A=7
    B=pow(A, alpha, N)
    A=pow(B, beta, N)
    print(A)

def encrypt(A, alpha, N):
    return pow(A, alpha, N)

#Below are file system
def get_num(filename):
    f=open(filename,'r')
    content=f.read()
    f.close()
    temp=[]
    result=[]
    i=0
    while True:
        if i+8>=len(content):
            #temp.append(content[i:len(content)])
            for i1 in range(len(content)-i):
                temp.append(content[i+i1])
            j=0
            while j<8-(len(content)-i):
                j+=1
                temp.append(chr(0))
            result.append(temp)
            return result
        result.append(content[i: i+8])
        i+=8
        
        
def encode(char_list):
    result=[]
    for element in char_list:
        i=0
        temp=0
        for t in element:
            temp+=ord(t)*(128**i)
            i+=1
        result.append(temp)
    return result

def decode(num_list):
    result=[]
    temp=[0,0,0,0,0,0,0,0]
    for a in num_list:
        for i in range(8):
            temp[i]=chr(a%128)
            a//=128
        result.append(deepcopy(temp))
    return result

def op_k(filename):
    f=open(filename, 'w')
    n, a, b=generate_key()
    f.write(str(n)+'\t'+str(a)+'\t'+str(b))
    f.close()

def op_e(key,filename):
    f=open(key,'r')
    keys=f.read()
    passwords=keys.split()
    N=int(passwords[0])
    a=int(passwords[1])
    f.close()
    #encrypt:
    result=encode(get_num(filename))
    fw=open(filename[:-4]+"_encrypted.txt",'w')
    for i in result:
        fw.write(str(encrypt(i, a, N)))
        fw.write("\t")
    fw.close()

def op_d(key,filename):
    f=open(key,'r')
    keys=f.read()
    passwords=keys.split()
    N=int(passwords[0])
    a=int(passwords[2])
    f.close()
    #decrypt:
    f=open(filename,'r')
    result=f.read().split()
    fw=open(filename[:-4]+"_decrypted.txt",'w')
    temp_result=[]
    for i in result:
        temp_result.append(encrypt(int(i), a, N))
    final_result=decode(temp_result)
    for row in final_result:
        for ch in row:
            fw.write(ch)
    fw.close()


def main():
    if sys.argv[1]=='-k':
        op_k(sys.argv[2])
    if sys.argv[1]=='-e':
        op_e(sys.argv[2],sys.argv[3])
    if sys.argv[1]=='-d':
        op_d(sys.argv[2],sys.argv[3])
main()