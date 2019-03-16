import sys
if __name__ == '__main__':

    i=1
    while i<10:

        b=1
        while b<=i:

            print(b,"*",i,"=",b*i,"\t",end='')
            b+=1
        i += 1
        print()
    print("结束while循环")

    m9=[1,2,3,4,5,6,7,8,9]
    for i1 in m9:
        for ii in m9:
            if ii<=i1:
                print(i1, "*", ii, "=", i1 * ii, "\t", end='')
            else :
                print(end="")
        print()
    print("结束for循环")