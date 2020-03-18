#definisi fungsi
def fungsi (x):
    y = 1/(1+x)
    return y

print("fungsi yang digunakan adalah")
print("")
print("\t\t","f(x) = 1/(1+x)")
print("")


a = float(input("masukkan batas bawah integral : "))
b = float(input("masukkan batas atas integral : "))
c = int(input("masukkan n : "))
eror = []
print("")
print("----------------Hasil Integrasi-----------------")
print ("iterasi","\t","n","\t\t","Trapezoid")

for iterasi in range (0,c):
    n = 2**iterasi
    h = (b-a)/n
        
    xi = a
    y = 0
    for i in range (1,n):
        xi = xi + h
        y += fungsi(xi)
    trap = ((h)*(fungsi(a) + (2*y) + fungsi(b)))/2
    eror.append(trap)
    print (iterasi+1,"\t\t",n,"\t\t",trap)
print (eror[iterasi-1])
print(eror[iterasi])
hasil = (eror[iterasi-1]-eror[iterasi])
print(hasil)
print ("estimasi error : "+str(hasil))
