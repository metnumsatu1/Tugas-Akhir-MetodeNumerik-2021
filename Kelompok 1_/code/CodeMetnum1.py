#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Modul II

print(" =========================================================\n",
"Modul 2 : Akar - Akar Persamaan\n",
"Nama Kelompok: 1 \n",
"Kelas: Oseanografi B \n",
"=========================================================\n")

#Metode Setengah Interval
def Setengah_Interval (X1,X2):
    X1 = float(input("Masukkan nilai pertama : "))
    X2 = float(input("Masukkan nilai kedua : "))
    error = 1
    iterasi = 0
    while(error > 0.0001):
        iterasi +=1
        FXi = (float(-0.6887*(X1**3)))+(float(7.1759*(X1**2)))-(7.2665*X1)-92.306
        FXii = (float(-0.6887*(X2**3)))+(float(7.1759*(X2**2)))-(7.2665*X2)-92.306
        Xt = (X1 + X2)/2
        FXt = (float(-0.6887*(Xt**3)))+(float(7.1759*(Xt**2)))-(7.2665*Xt)-92.306
        if FXi * FXt > 0:
            X1 = Xt
        elif FXi * FXt < 0:
            X2 = Xt
        else:
            print("Akar Penyelesaian:", Xt)
        if FXt < 0:
            error = FXt * (-1)
        else:
            error = FXt
        if iterasi > 100:
            print ("Angka tak hingga")
            break
        print(iterasi,"|",FXi,"|",FXii,"|",Xt,"|",FXt,"|",error)
    print("Jumlah iterasi = ", iterasi)
    print("Akar Persamaan = ", Xt)
    print("Toleransi Error = ", error)


#Metode Interpolasi Linier
def Interpolasi_Linier (X1):
    X1 = float(input("Masukkan nilai pertama : "))
    X2 = X1 + 1
    print("Nilai kedua : ", X2)
    error = 1
    iterasi = 0
    while(error > 0.0001):
        iterasi +=1
        FX1 = (float(-0.6887*(X1**3)))+(float(7.1759*(X1**2)))-(7.2665*X1)-92.306
        FX2 = (float(-0.6887*(X2**3)))+(float(7.1759*(X2**2)))-(7.2665*X2)-92.306
        Xt = (X1 + X2)/2
        FXt = (float(-0.6887*(Xt**3)))+(float(7.1759*(Xt**2)))-(7.2665*Xt)-92.306
        if FX1 * FXt > 0:
            X2 = Xt
            FX2 = FXt
        else:
            X1 = Xt
            FX1 = FXt
        if FXt < 0:
            error = FXt * (-1)
        else:
            error = FXt
        if iterasi > 500:
            print ("Angka tak hingga")
            break
        print(iterasi,"|",FX1,"|",FX2,"|",Xt,"|",FXt,"|",error)
    print("Jumlah iterasi = ", iterasi)
    print("Akar Persamaan = ", Xt)
    print("Toleransi Error = ", error)


# Metode Newton-Rapson
def Newton_Rhapson (X1):
    X1 = float(input("Masukkan nilai pertama : "))
    iterasi = 0
    akar = 1
    while(akar > 0.0001):
        iterasi +=1
        Fxn = (float(-0.6887*(X1**3)))+(float(7.1759*(X1**2)))-(7.2665*X1)-92.306
        Fxxn = (float(3*-0.6887*X1)**2)+(float(2*7.1759*X1))-7.2665
        xnp1 = X1 - (Fxn/Fxxn)
        fxnp1 = (xnp1**3)+(xnp1**2)-(3*xnp1)-3
        Ea = ((xnp1-X1)/xnp1)*100
        if Ea < 0.0001:
            X1 = xnp1
            akar = Ea*(-1)
        else:
            akar = xnp1
        if iterasi > 100:
            break
        print(iterasi,"|",X1,"|",xnp1,"|",akar,"|",Ea)
    print("Jumlah iterasi = ", iterasi)
    print("Akar Persamaan = ", xnp1)
    print("Toleransi Error = ", error)


#Metode Secant
def Secant (X1):
    X1 = float(input("Masukkan nilai pertama : "))
    X2 = X1 - 1
    print("Nilai kedua : ", X2)
    error = 1
    iterasi = 0
    while(error > 0.0001):
        iterasi +=1
        FX1 = (float(-0.6887*(X1**3)))+(float(7.1759*(X1**2)))-(7.2665*X1)-92.306
        FXmin = (float(-0.6887*(X2**3)))+(float(7.1759*(X2**2)))-(7.2665*X2)-92.306
        X3 = X1 - ((FX1)*(X1-(X2)))/((FX1)-(FXmin))
        FXplus = (float(-0.6887*(X3**3)))+(float(7.1759*(X3**2)))-(7.2665*X3)-92.306
        if FXplus < 0:
            error = FXplus * (-1)
        else:
            error = FXplus
        if error > 0.0001:
            X2 = X1
            X1 = X3
        else:
        print("Selesai")
        if iterasi > 500:
            print ("Angka tak hingga")
            break
        print(iterasi,"|",FX1,"|",FXmin,"|",X3,"|",FXplus,"|",error)
    print("Jumlah iterasi = ", iterasi)
    print("Akar Persamaan = ", X3)
    print("Toleransi Error = ", error)


#Metode Iterasi
def Iterasi (X1):
    X1 = float(input("Masukkan nilai pertama : "))
    error = 1
    iterasi = 0
    while(error > 0.0001):
        iterasi +=1
        FXn = (float(-0.6887*(X1**3)))+(float(7.1759*(X1**2)))-(7.2665*X1)-92.306
        X2 = (((-0.6887*X1)**2)+(3*7.1759*X1)+7.2665)**(0.333334)
        Ea = (((X2-X1)/(X2))*100)
        if Ea < error:
            X1 = X2
            if Ea > 0:
                error = Ea
            else:
                error = Ea*(-1)
        else:
            error = Ea
        if iterasi > 100:
            print ("Angka tak hingga")
            break
        print(iterasi,"|",FXn,"|",X2,"|",Ea,"|",error)
    print("Jumlah iterasi = ", iterasi)
    print("Akar Persamaan = ", X2)
    print("Toleransi Error = ", error)



# In[ ]:


#Modul III

print(" =========================================================\n",
"Modul 2 :Sistem Persamaan Linier dan Matriks\n",
"Nama Kelompok: 1 \n",
"Kelas: Oseanografi B \n",
"=========================================================\n")

#Gauss
import numpy as np
print('''Metode Gauss''')
A = np.array ([[5,9,2,8],
               [3,7,6,6],
               [3,6,8,7],
               [2,5,8,4,]], dtype='float')
b = np.array ([4.152, 9.152, 18.819, 10.819])
Ab = np.hstack([A, b.reshape(-1,1)])
print("matriks persamaan: \n",
      Ab,"\n")
n = len(b)
for i in range(n):
  a = Ab[i]
  for j in range(i+1, n):
    b = Ab[j]
    m = a[i] / b[i]
    Ab[j] = a - m * b
for i in range (n-1, -1, -1):
  Ab[i] = Ab[i] / Ab[i, i]
  a = Ab[i]
  for j in range(i - 1, -1, -1):
    b = Ab[j]
    m = a[i] / b[i]
    Ab[j] = a - m * b
x = Ab[:, 4]
print("matriks hasil: \n",
      Ab,"\n")
print("hasil akhir: \n", x)


#GAUSSJORDAN
import numpy as np
import sys
print('''


Metode Gauss_Jordan''')
A = np.array([[5,9,2,8,4.152],
              [3,7,6,6,9.152],
              [3,6,8,7,18.819],
              [2,5,8,4,10.819]],dtype='float')
n= 4

def GaussJordan (a,n):
    print('===============Mulai Iterasi===============')
    for i in range(n):
        if a[i][i]==0:
            sys.exit('Dibagi dengan angka nol (proses tidak dapat dilanjutkan)')
        for j in range(n):
            if i !=j:
                ratio= a[j][i]/a[i][i]
                
                for k in range (n+1):
                    a[j, k]=a[j][k]-ratio*a[i][k]
                print(a)
                print("==============")
    ax = np.zeros((n,n+1))
    for i in range(n):
        for j in range(n+1):
            ax[i, j]=a[i][j]/a[i][i]
    print("======= Akhir Iterasi =======")
    return ax

print("Matriks Persamaan")
print(A)

A = GaussJordan(A,n)
print(f""" Hasil Pengolahan Metode Gauss Jordan :
{A}""")


#GaussSeidel
import numpy as np 
from scipy.linalg import solve 
print('''


Metode Gauss_Seidel''')
def GaussSeidel (A, b, x, n):
    L = np.tril(A)
    U = A -L
    for i in range(n):
        x=np.dot(np.linalg.inv(L), b - np.dot(U,x))
        print (f'Iterasi Ke-{str(i+1).zfill(3)}'),
        print (x)
    return x

#Masukan
A= np.array ([
              [5, 9, 2, 8],
              [3, 7, 6, 6],
              [3, 6, 8, 7],
              [2, 5, 8, 4]])
b=[4.152, 9.152, 18.819, 10.819]
x=np.zeros_like(b)
n=25

H= GaussSeidel(A, b, x, n)
K= solve(A,b)

print(f'Hasil pengerjaan menggunakan Gauss Seidel didapatkan nilai tiap variabel {H}')
print(f'Variabel matriks menggunakan SciPy {K}')


#Jacobi
import numpy as np
from scipy.linalg import solve
print('''


Metode Jacobi''')
def jacobi(A,b,x,n):
  D = np.diag(A)
  R = A-np.diagflat(D)
  for i in range(n):
    x = (b-np.dot(R,x))/D
    print (f'Iterasi Ke-{str(i+1).zfill(3)}'),
    print (x)
  return x

A= np.array ([
              [5, 9, 2, 8],
              [3, 7, 6, 6],
              [3, 6, 8, 7],
              [2, 5, 8, 4]])
b=[4.152, 9.152, 18.819, 10.819]
x = [1.0,1.0,1.0,1.0]
n = 25
J = jacobi(A,b,x,n)
O = solve(A,b)
print(f'Hasil pengerjaan menggunakan Jacobi didapatkan nilai tiap variabel {J}')
print(f'Variabel matriks menggunakan SciPy {O}')


# In[ ]:


#Modul IV

print(" =========================================================\n",
"Modul 4 :Integrasi Numerik\n",
"Nama Kelompok: 1 \n",
"Kelas: Oseanografi B \n",
"=========================================================\n")


#trapesium banyak pias

import numpy as np
import matplotlib.pyplot as plt

def trapesium(f,a,b,N):
    x = np.linspace(a,b,N+1)
    y = f(x)
    y_right = y[1:] 
    y_left = y[:-1] 
    dx = (b - a)/N
    T = (dx/2) * np.sum(y_right + y_left)
    return T

f = lambda x : x**3+x**2+2
a = 4
b = 4
N = 2

x = np.linspace(a,b,N+1)
y = f(x)

X = np.linspace(a,b+1,N)
Y = f(X)
plt.plot(X,Y)

for i in range(N):
    xs = [x[i],x[i],x[i+1],x[i+1]]
    ys = [0,f(x[i]),f(x[i+1]),0]
    plt.fill(xs,ys,'b',edgecolor='b',alpha=0.2)

plt.title('Trapesium banyak pias, N = {}'.format(N))
plt.savefig('image\trapesium banyak pias.png')

L = trapesium(f,a,b,N)
print("Luas Trapesium Banyak pias, N = 2 :" , L)



#simpson 1/3

def f(x):
    return 4*x**3 + 4*x**2 + 2

def simpson1per3(x0,xn,n):
    h = (xn - x0) / n
    
    integral = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        
        if i%2 == 0:
            integral = integral + 2 * f(k)
        else:
            integral = integral + 4 * f(k)
    
    integral = integral * h/3
    
    return integral
    
x1 = float(input("batas bawah (x1): "))
x2 = float(input("batas atas (x2): "))

hasil = simpson1per3(x1, x2, 2)
print("nilai integral metode Simpson 1/3:",hasil )


# In[ ]:


#Modul V

#=== Modul 5 Persamaan Diferensial Biasa ===#
#=== Import Library ===#
from IPython import get_ipython
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib','inline')


#=== Modul 5 Persamaan Diferensial Biasa ===#
#=== Import Library ===#
from IPython import get_ipython
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib','inline')


Kelompok = print("Kelompok : 1")
print("===== Modul 5 Persamaan Differensial Biasa =====")

#Metode Euler

def Euler (a, b, c, h, x0, xn, y0):
  h = h
  x0 = x0
  xn = xn
  x = np.arange(x0, xn + h, h)
  y0 = y0
  a = a
  b = b
  c = c
  G = (a*x*3)+(b*x*2)+c*x
  f = lambda x, y: (a*x*3)+(b*x*2)+c*x # Persamaan Differensial Biasa
  y = np.zeros(len(x))
  y[0] = y0
  for i in range(0, len(x) - 1):
    y[i + 1] = y[i] + h*f(x[i], y[i])
  Galat = G-y
  print (Galat)
  Judul = ("Grafik Pendekatan Persamaan Differensial Biasa (Metode Euler)")
  plt.figure(figsize = (12, 12))
  plt.plot(x, y, 'b--', label='Hasil Pendekatan') 
  plt.plot(x, G, '-g', label='Hasil Analitik')
  plt.title(Judul) # Judul plot
  plt.xlabel('x') # Label sumbu x
  plt.ylabel('F(x)') # Label sumbu y
  plt.grid() # Menampilkan grid
  plt.legend(loc='lower right')
  plt.savefig('image\euler.png')

#Metode Heun
def Heun (a, b, c, h, x0, xn, y0):
    a = a
    b = b
    c = c
    h = h
    x0 = x0
    xn = xn
    x = np.arange(x0, xn + h, h)
    y0 = y0
    G = (a*x*3)+(b*x*2)+c*x
    f = lambda x, y: (a*x*3)+(b*x*2)+c*x 
    y = np.zeros(len(x))
    y[0] = y0
    for i in range(0, len(x) - 1):
      k1 = f(x[i], y[i])
      k2 = f((x[i]+h), (y[i]+(h*k1)))
      y[i+1] = y[i]+(0.5*h*(k1+k2))
    Galat = G-y
    print (Galat)
    Judul = ("Grafik Pendekatan Persamaan Differensial Biasa (Metode Heun)")
    plt.figure(figsize = (12, 12))
    plt.plot(x, y, 'b--', label='Hasil Pendekatan') 
    plt.plot(x, G, '-g', label='Hasil Analitik')
    plt.title(Judul) # Judul plot
    plt.xlabel('x') # Label sumbu x
    plt.ylabel('F(x)') # Label sumbu y
    plt.grid() # Menampilkan grid
    plt.legend(loc='lower right')
    plt.savefig('image\heun.png')

##### Output #####
print("Kode Persamaan Differensial Biasa: \n",
      "1. Euler \n",
      "2. Heun \n")
setting = int(input("Masukkan Kode Persamaan Differensial Biasa :"))
if (setting == 1):
  a = float(input("Masukkan nilai a: "))
  b = float(input("Masukkan nilai b: "))
  c = float(input("Masukkan nilai c: "))
  h = float(input("Masukkan nilai h: ")) 
  x0 = float(input("Masukkan nilai x awal: "))
  xn = float(input("Masukkan nilai x akhir: "))
  y0 = float(input("Masukkan nilai y awal: "))
  X = Euler (a, b, c, h, x0, xn, y0)
  print(X)
else :
  a = float(input("Masukkan nilai a: "))
  b = float(input("Masukkan nilai b: "))
  c = float(input("Masukkan nilai c: "))
  h = float(input("Masukkan nilai h: ")) 
  x0 = float(input("Masukkan nilai x awal: "))
  xn = float(input("Masukkan nilai x akhir: "))
  y0 = float(input("Masukkan nilai y awal: "))
  X = Heun (a, b, c, h, x0, xn, y0)
  print(X)