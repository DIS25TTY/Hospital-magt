from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from main import *
from apoin import *

def starting():
    clear_fra(frame_down)
    app_name=Label(frame_up,text="DG HOSPITAL",height=1,font=('Verdana 17 bold'),bg=co2,fg=co0)
    app_name.place(x=5,y=5)   
    b_ad=Button(frame_down,text="Admin",width="20",bg=co2,font=('Ivy 20 bold'),fg=co0,command=lambda:login("Admin"))
    b_ad.place(x=130,y=100)
    b_pa=Button(frame_down,text="Patient",width="20",bg=co2,font=('Ivy 20 bold'),fg=co0,command=lambda:login('Patient'))
    b_pa.place(x=130,y=180)
    b_dr=Button(frame_down,text="Doctor",width="20",bg=co2,font=('Ivy 20 bold'),fg=co0,command=lambda:login('Doctor'))
    b_dr.place(x=130,y=260)
def clear_fra(frame):
    for i in frame.winfo_children():
        i.destroy()

def logged(sigin,data):
    clear_fra(frame_down)
    
    app_name=Label(frame_up,text="Logged IN              "+sigin+"--"+data[0][0]+"  DGH",height=1,font=('Verdana 17 bold'),bg=co2,fg=co0)
    app_name.place(x=5,y=5)    
    
    if(sigin=="Admin"):
        b_adm=Button(frame_down,text="Admin Details",width="20",bg=co2,font=('Ivy 20 bold'),fg=co0,command=lambda: sigin_pg("Admin",data,3))
        b_adm.place(x=130,y=80)
        b_pa=Button(frame_down,text="Patient Details",width="20",bg=co2,font=('Ivy 20 bold'),fg=co0,command=lambda:sigin_pg("Admin",data,1))
        b_pa.place(x=130,y=160)
        b_dr=Button(frame_down,text="Doctor Details",width="20",bg=co2,font=('Ivy 20 bold'),fg=co0,command=lambda:sigin_pg("Admin",data,2))
        b_dr.place(x=130,y=240)
        b_ap=Button(frame_table,text="Appointments Details",width="20",bg=co2,font=('Ivy 20 bold'),fg=co0,command=lambda:appoint("Admin",data))
        b_ap.place(x=120,y=5)
    
    elif sigin=="Doctor":
        b_my=Button(frame_down,text="My Details",width="20",bg=co2,font=('Ivy 20 bold'),fg=co0,command=lambda: sigin_pg("Doctor",data,0))
        b_my.place(x=130,y=100)
        b_ap=Button(frame_down,text="Appointment Details",width="20",bg=co2,font=('Ivy 20 bold'),fg=co0,command=lambda:appoint("Doctor",data))
        b_ap.place(x=130,y=180)
    else:  
        b_pa=Button(frame_down,text="My Details",width="20",bg=co2,font=('Ivy 20 bold'),fg=co0,command=lambda: sigin_pg("Patient",data,0))
        b_pa.place(x=130,y=100)
        b_ap=Button(frame_down,text="Appointment Details",width="20",bg=co2,font=('Ivy 20 bold'),fg=co0,command=lambda:appoint("Patient",data))
        b_ap.place(x=130,y=180)


    window.mainloop()

def login(sigin):
    clear_fra(frame_down)
    clear_fra(frame_up)
    if(sigin=="Admin"):
        n=3
    elif sigin=="Patient":
        n=1
    elif sigin=="Doctor" :
        n=2
    app_name=Label(frame_up,text=sigin+" Login                       DG Hospital",height=1,font=('Verdana 17 bold'),bg=co2,fg=co0)
    app_name.place(x=5,y=5)
    l_phno=Label(frame_down,text="Phno *",width=25,height=2,font=('Ivy 13'),bg=co0,anchor=NW)
    l_phno.place(x=100,y=150)
    e_phno=Entry(frame_down,width=35,justify='left',highlightthickness=1,relief="solid")
    e_phno.place(x=190,y=150)
    l_pas=Label(frame_down,text="Password *",width=25,height=2,font=('Ivy 13'),bg=co0,anchor=NW)        
    l_pas.place(x=100,y=190)
    e_pas=Entry(frame_down,width=35,justify='left',highlightthickness=1,relief="solid")
    e_pas.place(x=190,y=190)
    def check():
        phno=e_phno.get()
        pas=e_pas.get()
        data=search(phno,n)
        print(data)
        if data:
            if data[0][7]==pas and data[0][5]==phno:
                logged(sigin,data)
            else:
                messagebox.showerror('Error','Wrong details!!') 
    b_back=Button(frame_down,text="Back",width="15",bg=co2,font=('Ivy 10 bold'),fg=co0,command=starting)
    b_back.place(x=200,y=220)
    b_log=Button(frame_down,text="Login",width="15",bg=co2,font=('Ivy 10 bold'),fg=co0,command=check)
    b_log.place(x=200,y=260)
    if(sigin=="Patient"):
        b_sup=Button(frame_down,text="Sign up",width="15",bg=co2,font=('Ivy 10 bold'),fg=co0,command=lambda: newsig_pg(sigin))
        b_sup.place(x=200,y=300) 
    window.mainloop()

starting()



window.mainloop()