import numpy as np
import math

def haarMatrix(n, normalised):
    #Allow only size n of the power 2
    n = 2**np.ceil(np.log2(n)) # 2 is base---/ a ** b  =  pow(a,b) = a raised to bth power
    if n > 2:
        h = haarMatrix(n/2, normalised)
    else:
        return np.array([[1,1], [1, -1]])
    #calculate upper haar part
    h_n = np.kron(h, [1, 1])
    #calculate lower haar part
    if normalised:
        h_i = np.sqrt(n/2)*np.kron(np.eye(len(h)),[1, -1])
    else:
        h_i = np.kron(np.eye(len(h)), [1,-1])
    #combine parts
    h = np.vstack((h_n, h_i))
    return h

def printCoefficient(title, data):
    print (title, end = " ")
    for v in data:
        if (isinstance(v, np.float64)):
            print("{0:0.3f}".format(v), end= " ")
        else:
            print("{0}".format(v), end= " ")

def main():
    n = int(input("Enter a integer value for n where n will be used as 2^n: "))
    print ("Size of data will be 2^{0} = {1}".format(n, (2**n)))
    if (n <2 or n>5):
        print("Value for n is incorrect, should be 2\u2265n\u22645")
    else:
        N = 2**n
        haar = haarMatrix(N, True)
        gendata = np.random.randint(1,100, N)
        printCoefficient("Data: \t\t\t\t", gendata)
        decom = (np.matmul(haar, gendata))/(math.sqrt(N))
        printCoefficient("\nDecompressed: \t", decom)
        recomp = (np.round((np.matmul(np.transpose(haar), decom))/(math.sqrt(N)))).astype(int)
        printCoefficient("\nRecomposed: \t", recomp)
        if((gendata==recomp).all()==True):
            print("\n\nRecomposition successful!!!")

if __name__=="__main__":
        main()
