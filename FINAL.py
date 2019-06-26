from decimal import *
from re  import findall
def nsd (a,b):
    a,b = abs(a), abs(b)
    while b != 0:
        a, b = b, a%b
    return a
def mx_create(arr1,arr2):
    mx = list()
    for i in range(len(arr1)):
        mx.append(list(map(lambda x,y:(x,y), arr1[i],arr2[i])))
    return mx
def isnull(mx, now):
        for i in range(now,len(mx)):
            if mx[i][now][0]!=0:
                return False, i
        return True, 0  
def el_sum(a,b):
    num = a[0]*b[1]+a[1]*b[0]
    if num == 0:
        return 0,1
    den = a[1]*b[1]
    k = nsd(num,den)
    return num//k,den//k
def el_sub(a,b):
    num = a[0]*b[1]-a[1]*b[0]
    if num==0:
        return 0, 1
    den = a[1]*b[1]
    k = nsd(num,den)
    return num//k, den//k
def el_mul(a,b):
    k = nsd(a[0],b[1])
    a0,b1=a[0]//k,b[1]//k
    k = nsd(a[1],b[0])
    a1,b0=a[1]//k,b[0]//k
    return a0*b0, a1*b1
def el_div(a,b):
    k = nsd(a[0],b[0])
    a0,b0=a[0]//k,b[0]//k
    k = nsd(a[1],b[1])
    a1,b1=a[1]//k,b[1]//k
    if b0<0:
        a0,b0=-a0,-b0
    return a0*b1, a1*b0
def freduct(mx, a, b):
    el = mx[a][b]
    mx[a][b] = nsd(el[0],el[1])
def mx_sum(mx1, mx2):
    res_mx = list()
    for i in range(len(mx1)):
        res_mx.append(list(map(lambda x,y: el_sum(x,y),mx1[i],mx2[i])))
    return res_mx
def upInput(nextInput):
    if len(nextInput)==0:
        s = input().split('\r')
        if len(s)>1:
            return s[0], s[1:]
        return s[0], []
    if len(nextInput)==1:
        if nextInput[0]!='':
            return nextInput[0], []
        return upInput([])
    elif nextInput[0]=='':
        return upInput(nextInput[1:])
    else:
        return nextInput[0], nextInput[1:]
def nullRow(mx, row):
    for i in range(len(mx)):
        if(mx[row][i][0]!=0):
            return False
    return True
def subRow(mx, a, b, r):
    for i in range(a, len(mx)):
        mx[b][i]=el_sub(mx[b][i], el_mul(mx[a][i],r))
def ex2(a):
        sum = 0,1
        for el in a:
            sum = el_sum(sum,el)
        if sum[0]<0:
            print(0)
        elif sum[0]==0:
            print(1)
        else:
            getcontext().prec=2000
            print(int((Decimal(sum[0])/Decimal(sum[1])).exp()))
def diag(mx):
    a = list()
    for i in range(len(mx)):
        a.append([(mx[i][i][0]),(mx[i][i][1])])
    return a
def determ(a):
    for i in range(len(a)):
        for j in range(i+1):
            k = nsd(a[i][0],a[j][1])
            a[i][0],a[j][1]=a[i][0]//k,a[j][1]//k
            k = nsd(a[i][1],a[j][0])
            a[i][1],a[j][0]=a[i][1]//k,a[j][0]//k
    num,den=1,1
    for el in a:
        num*=abs(el[0])
        den*=el[1]
    print(abs(num//den))
def gauss(mx):
    L = len(mx)
    koefN = 1
    koefD = 1
    for i in range(L):
        flag, row = isnull(mx,i)
        if flag:
            return
        elif row!=i:
            mx[i],mx[row]=mx[row],mx[i]
        header = mx[i][i]
        nod = nsd(header[0],header[1])
        header=header[0]//nod,header[1]//nod
        for j in range(i+1, L):
            if nullRow(mx,j):
                return
            extra = mx[j][i]
            if extra[0]==0:
                continue
            r=el_div(extra,header)
            subRow(mx, i,j,r)
        
def arrIn(arr, A, B, nextS):
    for i in range(A):
        temp, nextS = upInput(nextS)
        temp = findall(r'[^ ]+', temp)
        for j in range(B):
            temp2 = temp[j]
            arr[i][j] = int(temp2)
def CW():    
    temp, nextS = upInput([])
    S = int(temp)
    temp, nextS = upInput(nextS)
    N = int(temp)
    temp, nextS = upInput(nextS)
    M = int(temp)
    temp, nextS = upInput(nextS)
    K = int(temp)
    temp, nextS = upInput(nextS)
    L = int(temp)
    if S==1 and (N!=M or K!=L or N!=K):
        print("ERROR")
        return
    if S==2 and N!=M:
        print("ERROR")
        return
    arr1 = [[0]*N for j in range(N)]
    arrIn(arr1, N, N, nextS)
    arr2 = [[0]*N for j in range(N)]
    arrIn(arr2, N, N, nextS)
    arr3 = [[0]*L for j in range(K)]
    arrIn(arr3, K, L, nextS)
    arr4 = [[0]*L for j in range(K)]
    arrIn(arr4, K, L, nextS)
    matrix1 = mx_create(arr1,arr2)
    matrix2 = mx_create(arr3,arr4)
    if S==1:
        mx = mx_sum(matrix1,matrix2)
        gauss(mx)
        determ(diag(mx))
    elif S==2:
        ex2(diag(matrix1))

CW()