from tkinter import*
from tkinter import ttk
from functools import partial
from tkinter import messagebox
top=Tk()

    

def calsum (num1,num2,num3,ans):
    n1=float(num1.get())
    n2=str(num2.get())
    n3=str(num3.get())
    if n2=="m" and n3=="m":
         num4=n1
    elif n2=="m" and n3=="cm":
         num4=n1*100
    elif n2=="m" and n3=="km":
         num4=n1*0.001
    elif n2=="m" and n3=="in":
         num4=n1*39.3700787
    elif n2=="m" and n3=="ft":
         num4=n1*3.2808399
    elif n2=="m" and n3=="mi":
         num4=n1*0.0006214
    elif n2=="cm" and n3=="m":
         num4=n1*0.01
    elif n2=="cm" and n3=="m":
         num4=n1*1000
    elif n2=="cm" and n3=="cm":
         num4=n1
    elif n2=="cm" and n3=="km":
         num4=n1*0.0001
    elif n2=="cm" and n3=="in":
         num4=n1*0.393700787
    elif n2=="km" and n3=="ft":
         num4=n1*0.032808399
    elif n2=="km" and n3=="mi":
         num4=n1*0.000006214
    elif n2=="km" and n3=="m":
         num4=n1*1000
    elif n2=="km" and n3=="cm":
         num4=n1*100000
    elif n2=="km" and n3=="km":
         num4=n1
    elif n2=="km" and n3=="in":
         num4=n1*39370.0787
    elif n2=="km" and n3=="ft":
         num4=n1*3280.8399
    elif n2=="km" and n3=="mi":
         num4=n1*0.6214
    elif n2=="in" and n3=="m":
         num4=n1*0.025400000025908
    elif n2=="in" and n3=="cm":
         num4=n1*2.5400000025908
    elif n2=="in" and n3=="km":
         num4=n1*0.000025400000025908
    elif n2=="in" and n3=="in":
         num4=n1
    elif n2=="in" and n3=="ft":
         num4=n1*0.08333333354500000000
    elif n2=="in" and n3=="mi":
         num4=n1*0.0000157835600160992312
    elif n2=="ft" and n3=="m":
         num4=n1*0.304799999536704
    elif n2=="ft" and n3=="cm":
         num4=n1*30.4799999536704
    elif n2=="ft" and n3=="km":
         num4=n1*0.000304799999536704
    elif n2=="ft" and n3=="in":
         num4=n1*11.999999999
    elif n2=="ft" and n3=="ft":
         num4=n1
    elif n2=="ft" and n3=="mi":
         num4=n1*0.0001894027197
    elif n2=="mi" and n3=="m":
         num4=n1*1609.26939169961
    elif n2=="mi" and n3=="cm":
         num4=n1*160.926939169961
    elif n2=="mi" and n3=="km":
         num4=n1*1.60926939169961
    elif n2=="mi" and n3=="in":
         num4=n1*63357.0626005793
    elif n2=="mi" and n3=="ft":
         num4=n1*5279.7552301255
    elif n2=="mi" and n3=="mi":
         num4=n1
    
    
    
    
    else:
           messagebox.showerror("error","Something went wrong")
    ans.config(text="%f"%num4)
num1=StringVar()
num2=StringVar()
num3=StringVar()

#frame 1 variables
V=["m","cm","km","in","ft","mi"]
V1=["m","cm","km","in","ft","mi"]
top.title("UNIT CONVERTER")


top.geometry("1350x700+0+0")
L1=Label(top,text="UNIT CONVERTER ",bd=10,bg="#0000ff",relief=SUNKEN,fg="white",font=("times new roman",50,"bold")).pack(fill=X)

F1=Frame(top,bd=7,relief=GROOVE,bg="#0000ff")
F1.place(x=0,y=100,width=337,height=300)

L1=Label(F1,text="LENGTH",bd=10,fg="white",relief=SUNKEN,bg="#0000ff",font=("times new roman",20,"bold")).pack(fill=X)
combo=ttk.Combobox(F1,values=V,width=12,textvariable=num2,font=("times new roman",15,"bold"))
combo.set("select unit")
combo.place(x=10,y=70)

combo1=ttk.Combobox(F1,values=V1,width=12,textvariable=num3,font=("times new roman",15,"bold"))
combo1.set("select unit")
combo1.place(x=10,y=140)

E1=Entry(F1,font=("times new roman",15,"bold"),textvariable=num1)
E1.place(x=155,y=70,width=155)

ans=Label(F1,font=("times new roman",15,"bold"))
ans.place(x=155,y=140,width=155)

calsum = partial(calsum,num1,num2,num3,ans)

B1=Button(F1,text="convert",relief=SUNKEN,command=calsum,font=("times new roman",15,"bold"),bg="#00ff99")
B1.place(x=30,y=200)


def Tot_area(Area1,Area2,Area3,Area):
    A1=float(Area1.get())
    A2=str(Area2.get())
    A3=str(Area3.get())

    if A2 =="ac" and A3 =="ac":
        Aream=A1
    elif A2=="ac" and A3 =="ha":
        Aream=A1*0.4046944556859
    elif A2=="ac" and A3 =="km_sq":
        Aream=A1*0.004046944556859
    elif A2=="ac" and A3 =="m_sq":
        Aream=A1*4046.944556859
    elif A2=="ha" and A3 =="m_sq":
        Aream=A1*10000
    elif A2=="ha" and A3 =="km_sq":
        Aream=A1*0.01
    elif A2=="ha" and A3 =="ha":
        Aream=A1
    elif A2=="ha" and A3 =="ac":
        Aream=A1*2.471
    elif A2=="m_sq" and A3 =="ac":
        Aream=A1*0.0002471
    elif A2=="m_sq" and A3 =="ha":
        Aream=A1*0.0001
    elif A2=="m_sq" and A3 =="m_sq":
        Aream=A1
    elif A2=="m_sq" and A3 =="km_sq":
        Aream=A1*0.000001
    elif A2=="km_sq" and A3 =="ac":
        Aream=A1*247.1
    elif A2=="km_sq" and A3 =="ha":
        Aream=A1*100
    elif A2=="km_sq" and A3 =="m_sq":
        Aream=A1*1000000
    elif A2=="km_sq" and A3 =="km_sq":
        Aream=A1
    else:
        messagebox.showerror("error","Something went wrong")
    
    Area.config(text="%f"%Aream)
Area1=StringVar()
Area2=StringVar()
Area3=StringVar()

    
A1a=["ac","ha","km_sq","m_sq"]
A2a=["ac","ha","km_sq","m_sq"]

F2=Frame(top,bd=7,relief=GROOVE,bg="#0000ff")
F2.place(x=338,y=100,width=337,height=300)
L2=Label(F2,text="AREA",bd=10,fg="white",relief=SUNKEN,bg="#0000ff",font=("times new roman",20,"bold")).pack(fill=X)

comb1=ttk.Combobox(F2,values=A1a,width=12,textvariable=Area2,font=("times new roman",15,"bold"))
comb1.set("select unit")
comb1.place(x=10,y=70)

comb2=ttk.Combobox(F2,values=A2a,width=12,textvariable=Area3,font=("times new roman",15,"bold"))
comb2.set("select unit")
comb2.place(x=10,y=140)

E2=Entry(F2,font=("times new roman",15,"bold"),textvariable=Area1)
E2.place(x=155,y=70,width=155)

Area=Label(F2,font=("times new roman",15,"bold"))
Area.place(x=155,y=140,width=155)

Tot_area= partial(Tot_area,Area1,Area2,Area3,Area)

B2=Button(F2,text="convert",relief=SUNKEN,command=Tot_area,font=("times new roman",15,"bold"),bg="#00ff99")
B2.place(x=30,y=200)


def Tot_volume(Volume1,Volume2,Volume3,Volume):
    V1=float(Volume1.get())
    V2=str(Volume2.get())
    V3=str(Volume3.get())

    if V2 =="al" and V3 =="l":
        Volumem=A1
    elif V2=="l" and V3 =="m_cube":
        Volumem=V1*0.001
    elif V2=="l" and V3 =="ml":
        Volumem=V1*1000
    elif V2=="l" and V3 =="mm_cube":
        Volumem=V1*1000000
    elif V2=="m_cube" and V3 =="l":
        Volumem=V1*1000
    elif V2=="m_cube" and V3 =="m_cube":
        Volumem=V1
    elif V2=="m_cube" and V3 =="ml":
        Volumem=V1*1000000
    elif V2=="m_cube" and V3 =="mm_cube":
        Volumem=V1*1000000000
    elif V2=="ml" and V3 =="mm_cube":
        Volumem=V1*1000
    elif V2=="ml" and V3 =="l":
        Volumem=V1*0.001
    elif V2=="ml" and V3 =="m_cube":
        Volumem=V1*0.000001
    elif V2=="ml" and V3 =="ml":
        Volumem=V1
    elif V2=="mm_cube" and V3 =="m_cube":
        Volumem=00
    elif V2=="mm_cube" and V3 =="l":
        Volumem=V1*0.000001
    elif V2=="mm_cube" and V3 =="ml":
        Volumem=V1*0.001
    elif V2=="mm_cube" and V3 =="mm_cube":
        Volumem=V1
    
    
    else:
        messagebox.showerror("error","Something went wrong")
    
    Volume.config(text="%f"%Volumem)
Volume1=StringVar()
Volume2=StringVar()
Volume3=StringVar()

    
V1a=["l","m_cube","ml","mm_cube"]
V2a=["l","m_cube","ml","mm_cube"]


F3=Frame(top,bd=7,relief=GROOVE,bg="#0000ff")
F3.place(x=675,y=100,width=337,height=300)
L3=Label(F3,text="VOLUME",bd=10,fg="white",relief=SUNKEN,bg="#0000ff",font=("times new roman",20,"bold")).pack(fill=X)

com1=ttk.Combobox(F3,values=V1a,width=12,textvariable=Volume2,font=("times new roman",15,"bold"))
com1.set("select unit")
com1.place(x=10,y=70)

com2=ttk.Combobox(F3,values=V2a,width=12,textvariable=Volume3,font=("times new roman",15,"bold"))
com2.set("select unit")
com2.place(x=10,y=140)

E3=Entry(F3,font=("times new roman",15,"bold"),textvariable=Volume1)
E3.place(x=155,y=70,width=155)

Volume=Label(F3,font=("times new roman",15,"bold"))
Volume.place(x=155,y=140,width=155)

Tot_volume= partial(Tot_volume,Volume1,Volume2,Volume3,Volume)

B3=Button(F3,text="convert",relief=SUNKEN,command=Tot_volume,font=("times new roman",15,"bold"),bg="#00ff99")
B3.place(x=30,y=200)


def Tot_speed(Speed1,Speed2,Speed3,Speed):
    S1=float(Speed1.get())
    S2=str(Speed2.get())
    S3=str(Speed3.get())

    if S2 =="mile/hr" and S3 =="mile/hr":
        Speedm=S1
    elif S2=="mile/hr" and S3 =="m/s":
        Speedm=S1*0.44704005836555
    elif S2=="mile/hr" and S3 =="km/hr":
        Speedm=S1*1.60934421011598
    elif S2=="mile/hr" and S3 =="in/s":
        Speedm=S1*17.60000241401631437845
    elif S2=="m/s" and S3 =="mile/hr":
        Speedm=S1*2.2369936
    elif S2=="m/s" and S3 =="m/s":
        Speedm=S1
    elif S2=="m/s" and S3 =="km/hr":
        Speedm=S1*0.001
    elif S2=="m/s" and S3 =="in/s":
        Speedm=S1*39.370079
    elif S2=="km/hr" and S3 =="in/s":
        Speedm=S1*10.93613305555555
    elif S2=="km/hr" and S3 =="km/hr":
        Speedm=S1
    elif S2=="km/hr" and S3 =="m/s":
        Speedm=S1*0.277777777778
    elif S2=="km/hr" and S3 =="mile/hr":
        Speedm=S1*0.62137111111111111111608208
    elif S2=="in/s" and S3 =="mile/hr":
        Speedm=S1*0.0568181740250000
    elif S2=="in/s" and S3 =="m/s":
        Speedm=S1*0.0253999998
    elif S2=="in/s" and S3 =="km/hr":
        Speedm=S1*0.0914399999939
    elif S2=="in/s" and S3 =="in/s":
        Speedm=S1
 
    else:
        messagebox.showerror("error","Something went wrong")
    
    Speed.config(text="%f"%Speedm)
Speed1=StringVar()
Speed2=StringVar()
Speed3=StringVar()

    
S1a=["mile/hr","m/s","km/hr","in/s"]
S2a=["mile/hr","m/s","km/hr","in/s"]


F4=Frame(top,bd=7,relief=GROOVE,bg="#0000ff")
F4.place(x=1011,y=100,width=337,height=300)
L4=Label(F4,text="SPEED",bd=10,fg="white",relief=SUNKEN,bg="#0000ff",font=("times new roman",20,"bold")).pack(fill=X)

co1=ttk.Combobox(F4,values=S1a,width=12,textvariable=Speed2,font=("times new roman",15,"bold"))
co1.set("select unit")
co1.place(x=10,y=70)

co2=ttk.Combobox(F4,values=S2a,width=12,textvariable=Speed3,font=("times new roman",15,"bold"))
co2.set("select unit")
co2.place(x=10,y=140)

E4=Entry(F4,font=("times new roman",15,"bold"),textvariable=Speed1)
E4.place(x=155,y=70,width=155)

Speed=Label(F4,font=("times new roman",15,"bold"))
Speed.place(x=155,y=140,width=155)

Tot_speed= partial(Tot_speed,Speed1,Speed2,Speed3,Speed)

B4=Button(F4,text="convert",relief=SUNKEN,command=Tot_speed,font=("times new roman",15,"bold"),bg="#00ff99")
B4.place(x=30,y=200)

def Tot_weight(Weight1,Weight2,Weight3,Weight):
    W1=float(Weight1.get())
    W2=str(Weight2.get())
    W3=str(Weight3.get())

    if W2 =="kg" and W3 =="kg":
        Weightm=W1
    elif W2=="kg" and W3 =="mg":
        Weightm=W1*1000000
    elif W2=="kg" and W3 =="g":
        Weightm=W1*1000
    elif W2=="kg" and W3 =="q":
        Weightm=W1*0.01
    elif W2=="mg" and W3 =="kg":
        Weightm=W1*0.000001
    elif W2=="mg" and W3 =="mg":
        Weightm=W1
    elif W2=="mg" and W3 =="g":
        Weightm=W1*0.001
    elif W2=="mg" and W3 =="q":
        Weightm=0.00
    elif W2=="g" and W3 =="kg":
        Weightm=W1*0.001
    elif W2=="g" and W3 =="mg":
        Weightm=W1*1000
    elif W2=="g" and W3 =="g":
        Weightm=W1
    elif W2=="g" and W3 =="q":
        Weightm=W1*0.00001
    elif W2=="q" and W3 =="kg":
        Weightm=W1*100
    elif W2=="q" and W3 =="mg":
        Weightm=W1*100000000
    elif W2=="q" and W3 =="g":
        Weightm=W1*100000
    elif W2=="q" and W3 =="q":
        Weightm=W1

    else:
        messagebox.showerror("error","Something went wrong")
    
    Weight.config(text="%f"%Weightm)
Weight1=StringVar()
Weight2=StringVar()
Weight3=StringVar()

    
W1a=["kg","mg","g","q"]
W2a=["kg","mg","g","q"]



F5=Frame(top,bd=7,relief=GROOVE,bg="#0000ff")
F5.place(x=0,y=402,width=337,height=295)
L5=Label(F5,text="WEIGHT",bd=10,fg="white",relief=SUNKEN,bg="#0000ff",font=("times new roman",20,"bold")).pack(fill=X)


c1=ttk.Combobox(F5,values=W1a,width=12,textvariable=Weight2,font=("times new roman",15,"bold"))
c1.set("select unit")
c1.place(x=10,y=70)

c2=ttk.Combobox(F5,values=W2a,width=12,textvariable=Weight3,font=("times new roman",15,"bold"))
c2.set("select unit")
c2.place(x=10,y=140)

E5=Entry(F5,font=("times new roman",15,"bold"),textvariable=Weight1)
E5.place(x=155,y=70,width=155)

Weight=Label(F5,font=("times new roman",15,"bold"))
Weight.place(x=155,y=140,width=155)

Tot_weight= partial(Tot_weight,Weight1,Weight2,Weight3,Weight)

B5=Button(F5,text="convert",relief=SUNKEN,command=Tot_weight,font=("times new roman",15,"bold"),bg="#00ff99")
B5.place(x=30,y=200)



def Tot_temp(Temp1,Temp2,Temp3,Temp):
    T1=float(Temp1.get())
    T2=str(Temp2.get())
    T3=str(Temp3.get())

    if T2 =="k" and T3 =="k":
        Tempm=T1
    elif T2=="k" and T3 =="f":
        Tempm=9/5(T1-273.15)+32
    elif T2=="k" and T3 =="c":
        Tempm=T1*(-272.15)
    elif T2=="f" and T3 =="k":
        Tempm=T1*255.92777777777
    elif T2=="f" and T3 =="f":
        Tempm=T1
    elif T2=="f" and T3 =="c":
        Tempm=T1*(-17.22222222222222)
    elif T2=="c" and T3 =="k":
        Tempm=T1*(274.15)
    elif T2=="c" and T3 =="f":
        Tempm=T1*33.8
    elif T2=="c" and T3 =="c":
        Tempm=T1
    


    else:
        messagebox.showerror("error","Something went wrong")
    
    Temp.config(text="%f"%Tempm)
Temp1=StringVar()
Temp2=StringVar()
Temp3=StringVar()

    
T1a=["k","f","c"]
T2a=["k","f","c"]


F6=Frame(top,bd=7,relief=GROOVE,bg="#0000ff")
F6.place(x=338,y=402,width=337,height=295)
L6=Label(F6,text="TEMPERATURE",bd=10,fg="white",relief=SUNKEN,bg="#0000ff",font=("times new roman",20,"bold")).pack(fill=X)

mo1=ttk.Combobox(F6,values=T1a,width=12,textvariable=Temp2,font=("times new roman",15,"bold"))
mo1.set("select unit")
mo1.place(x=10,y=70)

mo2=ttk.Combobox(F6,values=T2a,width=12,textvariable=Temp3,font=("times new roman",15,"bold"))
mo2.set("select unit")
mo2.place(x=10,y=140)

E6=Entry(F6,font=("times new roman",15,"bold"),textvariable=Temp1)
E6.place(x=155,y=70,width=155)

Temp=Label(F6,font=("times new roman",15,"bold"))
Temp.place(x=155,y=140,width=155)

Tot_temp= partial(Tot_temp,Temp1,Temp2,Temp3,Temp)

B6=Button(F6,text="convert",relief=SUNKEN,command=Tot_temp,font=("times new roman",15,"bold"),bg="#00ff99")
B6.place(x=30,y=200)


def Tot_power(Power1,Power2,Power3,Power):
    P1=float(Power1.get())
    P2=str(Power2.get())
    P3=str(Power3.get())

    if P2 =="w" and P3 =="w":
        Powerm=P1
    elif P2=="w" and P3 =="hp":
        Powerm=P1*0.0013410221
    elif P2=="w" and P3 =="kw":
        Powerm=P1*0.001
    elif P2=="hp" and P3 =="w":
        Powerm=P1*745.699865796395153
    elif P2=="hp" and P3 =="hp":
        Powerm=P1
    elif P2=="hp" and P3 =="kw":
        Powerm=P1*0.7456998657963
    elif P2=="kw" and P3 =="w":
        Powerm=P1*1000
    elif P2=="kw" and P3 =="hp":
        Powerm=P1*1.3410221
    elif P2=="kw" and P3 =="kw":
        Powerm=P1

    


    else:
        messagebox.showerror("error","Something went wrong")
    
    Power.config(text="%f"%Powerm)
Power1=StringVar()
Power2=StringVar()
Power3=StringVar()

    
P1a=["w","hp","kw"]
P2a=["w","hp","kw"]



F7=Frame(top,bd=7,relief=GROOVE,bg="#0000ff")
F7.place(x=675,y=402,width=337,height=295)
L7=Label(F7,text="POWER",bd=10,fg="white",relief=SUNKEN,bg="#0000ff",font=("times new roman",20,"bold")).pack(fill=X)


m1=ttk.Combobox(F7,values=P1a,width=12,textvariable=Power2,font=("times new roman",15,"bold"))
m1.set("select unit")
m1.place(x=10,y=70)

m2=ttk.Combobox(F7,values=P2a,width=12,textvariable=Power3,font=("times new roman",15,"bold"))
m2.set("select unit")
m2.place(x=10,y=140)

E7=Entry(F7,font=("times new roman",15,"bold"),textvariable=Power1)
E7.place(x=155,y=70,width=155)

Power=Label(F7,font=("times new roman",15,"bold"))
Power.place(x=155,y=140,width=155)

Tot_power= partial(Tot_power,Power1,Power2,Power3,Power)

B7=Button(F7,text="convert",relief=SUNKEN,command=Tot_power,font=("times new roman",15,"bold"),bg="#00ff99")
B7.place(x=30,y=200)


def Tot_pressure(Pressure1,Pressure2,Pressure3,Pressure):
    Z1=float(Pressure1.get())
    Z2=str(Pressure2.get())
    Z3=str(Pressure3.get())

    if Z2 =="bar" and Z3 =="bar":
        Presssurem=Z1
    elif Z2=="bar" and Z3 =="atm":
        Pressurem=Z1*0.986923
    elif Z2=="bar" and Z3 =="hpa":
        Pressurem=Z1*1000
    elif Z2=="atm" and Z3 =="bar":
        Pressurem=Z1*1.0132502738
    elif Z2=="atm" and Z3 =="atm":
        Pressurem=Z1
    elif Z2=="atm" and Z3 =="hpa":
        Pressurem=Z1*1013.2502738308
    elif Z2=="hpa" and Z3 =="bar":
        Pressurem=Z1*0.001
    elif Z2=="hpa" and Z3 =="atm":
        Pressurem=Z1*0.000986923
    elif Z2=="hpa" and Z3 =="hpa":
        Pressurem=Z1

    


    else:
        messagebox.showerror("error","Something went wrong")
    
    Pressure.config(text="%f"%Pressurem)
Pressure1=StringVar()
Pressure2=StringVar()
Pressure3=StringVar()

    
Z1a=["bar","atm","hpa"]
Z2a=["bar","atm","hpa"]


F8=Frame(top,bd=7,relief=GROOVE,bg="#0000ff")
F8.place(x=1011,y=402,width=337,height=295)
L8=Label(F8,text="PRESSURE",bd=10,fg="white",relief=SUNKEN,bg="#0000ff",font=("times new roman",20,"bold")).pack(fill=X)

n1=ttk.Combobox(F8,values=Z1a,width=12,textvariable=Pressure2,font=("times new roman",15,"bold"))
n1.set("select unit")
n1.place(x=10,y=70)

n2=ttk.Combobox(F8,values=Z2a,width=12,textvariable=Pressure3,font=("times new roman",15,"bold"))
n2.set("select unit")
n2.place(x=10,y=140)

E8=Entry(F8,font=("times new roman",15,"bold"),textvariable=Pressure1)
E8.place(x=155,y=70,width=155)

Pressure=Label(F8,font=("times new roman",15,"bold"))
Pressure.place(x=155,y=140,width=155)

Tot_pressure= partial(Tot_pressure,Pressure1,Pressure2,Pressure3,Pressure)

B8=Button(F8,text="convert",relief=SUNKEN,command=Tot_pressure,font=("times new roman",15,"bold"),bg="#00ff99")
B8.place(x=30,y=200)



         
top.mainloop()
 
