import numpy as np
import matplotlib.pyplot as plt
import math


CL = float(input("koefisien lift: "))
v = float(input("kecepatan bola: "))
distance = float(input("Input the distance(metre): "))
angle = float(input("Input the angle(Degres 0-360): "))
wind_factor = float(input("Wind Factor(Horizontal): "))
f_spin = float(input("frekuensi putaran: "))

g = 9.81 

#asumsi kerapatan udara 1,2kg/m3

D = 0.22 #Diameter atau luas permukaan
A = 0.25 # luas permukaan 1/4 pi D2
rho = 1.22  #konstanta rho / kerapatan udara
massa = 0.43

Cd = wind_factor
#F = m.a.a F/m m disini FL atau efek magnus karena hasilnya satuan Newton 

#asumsi gaya lift/koefisien LIFT CL


#nanti ini buat kalkulasi gaya gesek
alpha = angle*3.14/180 #sudut

x = 0.      #jarak awal
y = distance #Tinggi dari tanah
vx = v * np.cos(alpha)
vy = v * np.sin(alpha)
vx_init = vx
t = 0.

X = [x]
Y = [y]
dt = 0.01


# Jarak tembak maksimum Xm(V0 sin2 teta)/g
# Ketinggian maksimum Ym = (v02 sin 2teta)/2g 

t = 0

#jika t = 0 maka x dan y = juga sama dengan NOL



def drag(v, alpha):
    F =0.5*rho*(v**2)*A*Cd # F = gaya gesek yang dihasilkan
    return (F*np.cos(alpha), F*np.sin(alpha))
def magnus():
    FL = CL*rho*D*f_spin*v # Magnus
    return FL
def movement():
    if(x == 0 | y == 0):
        return x,y
    else:
        Xm = (vx*np.sin(alpha))
        Ym = (vy*np.cos(alpha))

    return Xm, Ym
    
#def movement(v, alpha):
   

# #def vektor(v, alpha):
#     fresultan = fresultan * g / a * w

while ((y>0) | (vy>0)):
    Fx, Fy = drag(v, alpha)
    # acceleration:
    ax = -Fx/massa
    ay = -Fy/massa - g

    x = x + vx*dt + 0.5*ax*dt**2
    y = y + vy*dt + 0.5*ay*dt**2

    vx = vx + ax*dt
    vy = vy + ay*dt

    v = np.sqrt(vx*vx+vy*vy)
    alpha = math.atan2(vy,vx)

    X.append(x)
    Y.append(y)
    t = t + dt

    ft = Y[-2]/(Y[-2]-Y[-1]) # fractional time to last point
    X[-1] = X[-2] + (X[-1]-X[-2])*ft
    Y[-1] = 0.
    t = t - (1-ft)*dt

    print('Total flight time: %.2f sec'%t)
    print('Total distance   : %.2f m'%X[-1])

    print("the magnus : ", magnus)
    print("Jarak tendang Max: ", movement)
    print("Ketinggian Max: ", drag)

    plt.figure()
    plt.plot(X,Y)

    plt.title('knuckleshoot')
    plt.xlabel('Distance')
    plt.ylabel('Height')
    plt.show()




        






