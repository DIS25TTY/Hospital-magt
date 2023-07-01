from tkinter import *
from tkinter import ttk
from view import *
from tkinter import messagebox
from apoin import *
# from begin_pg import *
# from begin_pg import logged


co0="#ffffff"
co1="#000000"
co2="#4456f0"

window=Tk()
window.title("")
window.geometry('600x650')
window.configure(background=co0)
window.resizable(width=FALSE,height=FALSE)

#skeleton
frame_up=Frame(window,width=650,height=50,bg=co2)
frame_up.grid(row=0,column=0,padx=0,pady=1)

frame_down=Frame(window,width=650,height=340,bg=co0)#2nd invisible block
frame_down.grid(row=1,column=0,padx=0,pady=1)

#frame tab
frame_table=Frame(window,width=550,height=300,bg=co0,relief="flat")
frame_table.grid(row=2,column=0,columnspan=2,padx=10,pady=2,sticky=NW)

def clear_fra(frame):
    for i in frame.winfo_children():
        i.destroy()

def sigin_pg(sigin,data,k):
    clear_fra(frame_down)
    clear_fra(frame_table)
    print(data)
    n=0
    if(sigin=="Admin"):
        n=3
    elif sigin=="Patient":
        n=1
    elif sigin=="Doctor" :
        n=2
    def show():
        global tree
        # data=search(data[0][5])
        if(k!=0):
            demo=view(k)
        else:
            demo=view(n)
        listh=['Name','Gender','Age','DOB','Email','Phno','Adress']
        tree=ttk.Treeview(frame_table,selectmode="extended",columns=listh,show="headings")
        vsb=ttk.Scrollbar(frame_table,orient="vertical",command=tree.yview)
        hsb=ttk.Scrollbar(frame_table,orient="horizontal",command=tree.xview)

        tree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)
        tree.grid(column=0,row=0,sticky='nsew')
        vsb.grid(column=1,row=0,sticky='ns')
        hsb.grid(column=0,row=1,sticky='ew')
        
        tree.heading(0,text='Name',anchor=NW)
        tree.heading(1,text='Gender',anchor=NW)
        tree.heading(2,text='Age',anchor=NW)
        tree.heading(3,text='DOB',anchor=NW)
        tree.heading(4,text='Email',anchor=NW)
        tree.heading(5,text='Phno',anchor=NW)
        tree.heading(6,text='Adress',anchor=NW)

        tree.column(0,width=119,anchor='nw')
        tree.column(1,width=50,anchor='nw')
        tree.column(2,width=30,anchor='nw')
        tree.column(3,width=80,anchor='nw')
        tree.column(4,width=99,anchor='nw')
        tree.column(5,width=99,anchor='nw')
        tree.column(6,width=99,anchor='nw')
        ar=["Patient","Doctor","Admin"]
        if sigin=="Admin":
            for i in demo:
                  tree.insert('','end',values=i)
            l_msg=Label(frame_down,text=ar[k-1]+" Details",height=1,font=('Ivy 11'),bg=co0,anchor=NW)
            l_msg.place(x=10,y=290)
        else:
            for i in demo:
                if(i[5]==data[0][5]):
                    tree.insert('','end',values=i)
    show()      

    def insert():
        nam=e_name.get()
        gen=e_gen.get()
        age=e_age.get()
        dob=e_birth.get()
        ema=e_ema.get()
        phno=e_tel.get()
        adr=e_adr.get()
        pas=e_pas.get()
        data=[nam,gen,age,dob,ema,phno,adr,pas]
        if(nam)=='' or gen=='' or age=='' or dob=='' or ema =='' or phno=='' or adr==''or pas=='':
            messagebox.showwarning('data' ,'Please fill in all fields')
        else:
            if k:
                add(data,k)
            else:
                add(data,n)
            messagebox.showinfo('data','Data added successfully!!')
            e_name.delete(0,'end')
            e_gen.delete(0,'end')
            e_age.delete(0,'end')
            e_birth.delete(0,'end')
            e_ema.delete(0,'end')
            e_tel.delete(0,'end')
            e_adr.delete(0,'end')
            e_pas.delete(0,'end')
            show()

    def to_update():
        try:
            tree_data=tree.focus()
            tree_dictionary=tree.item(tree_data)
            tree_list=tree_dictionary['values']

            name=str(tree_list[0])
            gen=str(tree_list[1])
            age=str(tree_list[2])
            dob=str(tree_list[3])
            ema=str(tree_list[4])
            phno=str(tree_list[5])
            adr=str(tree_list[6])
            pas=str(tree_list[7])

            e_name.insert(0,name)
            e_gen.insert(0,gen)
            e_age.insert(0,age)
            e_birth.insert(0,dob)
            e_ema.insert(0,ema)
            e_tel.insert(0,phno)
            e_pas.insert(0,pas)
            e_adr.insert(0,adr)

            def confirm():
                nnam=e_name.get()#new name
                
                nphno=e_tel.get()
                ngen=e_gen.get()
                nage=e_age.get()
                ndob=e_birth.get()
                nema=e_ema.get()
                nadr=e_adr.get()
                npas=e_pas.get()

                data=[nphno,nnam,ngen,nage,ndob,nema,nphno,nadr,npas]
                if k:
                    update(data,k)
                else:
                    update(data,n)
                # print(k)
                messagebox.showinfo('Success','data updated successfully!')
                e_name.delete(0,'end')
                e_gen.delete(0,'end')
                e_age.delete(0,'end')
                e_birth.delete(0,'end')
                e_ema.delete(0,'end')
                e_tel.delete(0,'end')
                e_adr.delete(0,'end')
                e_pas.delete(0,'end')
                for widget in frame_table.winfo_children():
                    widget.destroy()
                b_confirm.destroy()

                show()
            if(n==1):
                b_confirm=Button(frame_down,text="Confirm",width="15",bg=co2,font=('Ivy 10 bold'),fg=co0,command=confirm)
                b_confirm.place(x=465,y=290)
            else:
                b_confirm=Button(frame_down,text="Confirm",width="15",bg=co2,font=('Ivy 10 bold'),fg=co0,command=confirm)
                b_confirm.place(x=240,y=290)

        except IndexError:
            messagebox.showerror('Error','Select Your entry from the table')        

    def to_remove():
        try:
            tree_data=tree.focus()
            tree_dictionary=tree.item(tree_data)
            tree_list=tree_dictionary['values']
            tree_phno=str(tree_list[5])
            if k:
                remove(tree_phno,k)
            else:
                remove(tree_phno,n)

            messagebox.showinfo('Success','Deleted successfully!!')
            for widget in frame_table.winfo_children():
                widget.destroy()

        except IndexError:
            messagebox.showerror('Error','Select Your entry from the table') 
        show()  
    
    def to_search():
        
        phno=e_search.get()
        if k:
            data=search(phno,k)
        else:
            data=search(phno,n)
        def delete_hide():
            tree.delete(*tree.get_children())
        
        delete_hide()

        for i in data:
            tree.insert('','end',values=i)
        
        e_search.delete(0,'end')

    #frameup widgets
    # def entries(sigin):
    app_name=Label(frame_up,text=sigin+" SignIN",height=1,font=('Verdana 17 bold'),bg=co2,fg=co0)
    app_name.place(x=5,y=5)
        #framedown widgets
    l_name=Label(frame_down,text="Name *",width=20,height=1,font=('Ivy 11'),bg=co0,anchor=NW)
    l_name.place(x=10,y=20)
    e_name=Entry(frame_down,width=35,justify='left',highlightthickness=1,relief="solid")
    e_name.place(x=80,y=20)

    l_gen=Label(frame_down,text="Gender *",width=20,height=1,font=('Ivy 11'),bg=co0,anchor=NW)
    l_gen.place(x=10,y=50)
    e_gen= ttk.Combobox(frame_down,width=37)
    e_gen['values']=['','F','M']
    e_gen.place(x=80,y=50)

    l_age=Label(frame_down,text="Age *",width=20,height=1,font=('Ivy 11'),bg=co0,anchor=NW)
    l_age.place(x=10,y=80)
    e_age=Entry(frame_down,width=35,justify='left',highlightthickness=1,relief="solid")
    e_age.place(x=80,y=80)

    l_birth=Label(frame_down,text="DOB *",width=20,height=1,font=('Ivy 11'),bg=co0,anchor=NW)
    l_birth.place(x=10,y=110)
    e_birth=Entry(frame_down,width=35,justify='left',font=('Ivy',11),highlightthickness=1,relief="solid")
    e_birth.place(x=80,y=110)

    l_ema=Label(frame_down,text="Email *",width=20,height=1,font=('Ivy 11'),bg=co0,anchor=NW)
    l_ema.place(x=10,y=140)
    e_ema=Entry(frame_down,width=35,justify='left',font=('Ivy',11),highlightthickness=1,relief="solid")
    e_ema.place(x=80,y=140)

    l_tel=Label(frame_down,text="Phno *",height=1,font=('Ivy 11'),bg=co0,anchor=NW)
    l_tel.place(x=10,y=170)
    e_tel=Entry(frame_down,width=35,justify='left',font=('Ivy',11),highlightthickness=1,relief="solid")
    e_tel.place(x=80,y=170)

    l_adr=Label(frame_down,text="Address ",height=1,font=('Ivy 11'),bg=co0,anchor=NW)
    l_adr.place(x=10,y=200)
    e_adr=Entry(frame_down,width=35,justify='left',font=('Ivy',11),highlightthickness=1,relief="solid")
    e_adr.place(x=80,y=200)
    l_pas=Label(frame_down,text="Password *",height=1,font=('Ivy 11'),bg=co0,anchor=NW)
    l_pas.place(x=10,y=230)
    e_pas=Entry(frame_down,width=35,justify='left',font=('Ivy',11),highlightthickness=1,relief="solid")
    e_pas.place(x=80,y=230)

    
    if (sigin=="Admin") :
        show()
        b_search=Button(frame_down,text="Search",width="6",bg=co2,font=('Ivy 10 bold'),fg=co0,command=to_search)
        b_search.place(x=380,y=17)
        e_search=Entry(frame_down,width=16,justify='left',font=('Ivy',11),highlightthickness=1,relief="solid")
        e_search.place(x=447,y=20)
        b_view=Button(frame_down,text="View",width="12",bg=co2,font=('Ivy 10 bold'),fg=co0,command=show)
        b_view.place(x=465,y=60)
        b_add=Button(frame_down,text="Add",width="12",bg=co2,font=('Ivy 10 bold'),fg=co0,command=insert)
        b_add.place(x=465,y=100)
        b_upd=Button(frame_down,text="Update",width="12",bg=co2,font=('Ivy 10 bold'),fg=co0,command=to_update)
        b_upd.place(x=465,y=140)
        b_del=Button(frame_down,text="Delete",width="12",bg=co2,font=('Ivy 10 bold'),fg=co0,command=to_remove)
        b_del.place(x=465,y=180)
        b_exit=Button(frame_down,text="Exit",width="12",bg=co2,font=('Ivy 10 bold'),fg=co0,command=lambda:logged(sigin,data))
        b_exit.place(x=465,y=280)
     
    elif (sigin=="Patient"):
        b_exit=Button(frame_down,text="Exit",width="12",bg=co2,font=('Ivy 10 bold'),fg=co0,command=lambda:logged(sigin,data))
        b_exit.place(x=465,y=30)
        b_up=Button(frame_down,text="Update",width="12",bg=co2,font=('Ivy 10 bold'),fg=co0,command=to_update)
        b_up.place(x=465,y=60)
        l_dis=Label(frame_down,text="Disease ",height=1,font=('Ivy 11'),bg=co0,anchor=NW)
        l_dis.place(x=10,y=260)
        e_dis=Entry(frame_down,width=35,justify='left',font=('Ivy',11),highlightthickness=1,relief="solid")
        e_dis.place(x=80,y=260)
        
        l_dr=Label(frame_down,text="Doctor ",height=1,font=('Ivy 11'),bg=co0,anchor=NW)
        l_dr.place(x=10,y=290)
        e_dr= ttk.Combobox(frame_down,width=37)
        drdet=view(2)
        dat=[]
        for i in drdet:
            dat.append(i[0])
        def book():
            l_date=Label(frame_down,text="Date ",height=1,font=('Ivy 11'),bg=co0,anchor=NW)
            l_date.place(x=420,y=170)
            e_date=Entry(frame_down,width=10,justify='left',font=('Ivy',11),highlightthickness=1,relief="solid")
            e_date.place(x=465,y=170)
            l_tim=Label(frame_down,text="Time ",height=1,font=('Ivy 11'),bg=co0,anchor=NW)
            l_tim.place(x=420,y=200)
            e_time=Entry(frame_down,width=10,justify='left',font=('Ivy',11),highlightthickness=1,relief="solid")
            e_time.place(x=465,y=200)
            b_conf=Button(frame_down,text="Confirm",width="15",bg=co2,font=('Ivy 10 bold'),fg=co0,command=lambda:bk_confirm())
            b_conf.place(x=465,y=290)
            def bk_confirm():
                dis=e_dis.get()
                datebk=e_date.get()
                doc=e_dr.get()
                tim=e_time.get()
                dd=[doc,data[0][0],dis,datebk,tim]
                print(dd)
                if(dis=='' or datebk=='' or tim=='' or doc==''):
                    messagebox.showerror('Error','Fill the details')
                else:
                    add(dd,4)
                    messagebox.showinfo('Booked','Appointment Successfully Added')

        e_dr['values']=dat
        e_dr.place(x=80,y=290)
        
        b_dr=Button(frame_down,text="Book appointment",width="15",bg=co2,font=('Ivy 10 bold'),fg=co0,command=lambda:book())
        b_dr.place(x=465,y=100)
        b_del=Button(frame_down,text="Delete",width="12",bg=co2,font=('Ivy 10 bold'),fg=co0,command=to_remove)
        b_del.place(x=465,y=250)
    else:
        b_up=Button(frame_down,text="Update",width="12",bg=co2,font=('Ivy 10 bold'),fg=co0,command=to_update)
        b_up.place(x=465,y=60)
        b_del=Button(frame_down,text="Delete",width="12",bg=co2,font=('Ivy 10 bold'),fg=co0,command=to_remove)
        b_del.place(x=465,y=180)
        b_exit=Button(frame_down,text="Exit",width="12",bg=co2,font=('Ivy 10 bold'),fg=co0,command=lambda:logged(sigin,data))
        b_exit.place(x=465,y=280)
    window.mainloop()

    

def newsig_pg(sigin):

    clear_fra(frame_down)
    clear_fra(frame_table)
    if(sigin=="Admin"):
        n=3
    elif sigin=="Patient":
        n=1
    elif sigin=="Doctor" :
        n=2
    
    def show():
        global tree
        listh=['Name','Gender','Age','DOB','Email','Phno','Adress']
        tree=ttk.Treeview(frame_table,selectmode="extended",columns=listh,show="headings")
        vsb=ttk.Scrollbar(frame_table,orient="vertical",command=tree.yview)
        hsb=ttk.Scrollbar(frame_table,orient="horizontal",command=tree.xview)

        tree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)
        tree.grid(column=0,row=0,sticky='nsew')
        vsb.grid(column=1,row=0,sticky='ns')
        hsb.grid(column=0,row=1,sticky='ew')
        
        tree.heading(0,text='Name',anchor=NW)
        tree.heading(1,text='Gender',anchor=NW)
        tree.heading(2,text='Age',anchor=NW)
        tree.heading(3,text='DOB',anchor=NW)
        tree.heading(4,text='Email',anchor=NW)
        tree.heading(5,text='Phno',anchor=NW)
        tree.heading(6,text='Adress',anchor=NW)

        tree.column(0,width=119,anchor='nw')
        tree.column(1,width=50,anchor='nw')
        tree.column(2,width=30,anchor='nw')
        tree.column(3,width=80,anchor='nw')
        tree.column(4,width=99,anchor='nw')
        tree.column(5,width=99,anchor='nw')
        tree.column(6,width=99,anchor='nw')   
        
        phno=e_tel.get()
        print(phno)
        data=search(phno,n)

        for i in data:
            tree.insert('','end',values=i)
        

    def insert():
        nam=e_name.get()
        gen=e_gen.get()
        age=e_age.get()
        dob=e_birth.get()
        ema=e_ema.get()
        phno=e_tel.get()
        adr=e_adr.get()
        pas=e_pas.get()
        data=[nam,gen,age,dob,ema,phno,adr,pas]
        if(nam)=='' or gen=='' or age=='' or dob=='' or ema =='' or phno=='' or adr==''or pas=='':
            messagebox.showwarning('data' ,'Please fill in all fields')
        else:
            add(data,n)
            messagebox.showinfo('data','Data added successfully!!')
            show()

    def to_update():
        try:
            tree_data=tree.focus()
            tree_dictionary=tree.item(tree_data)
            tree_list=tree_dictionary['values']

            name=str(tree_list[0])
            gen=str(tree_list[1])
            age=str(tree_list[2])
            dob=str(tree_list[3])
            ema=str(tree_list[4])
            phno=str(tree_list[5])
            adr=str(tree_list[6])
            pas=str(tree_list[7])

            e_name.insert(0,name)
            e_gen.insert(0,gen)
            e_age.insert(0,age)
            e_birth.insert(0,dob)
            e_ema.insert(0,ema)
            e_tel.insert(0,phno)
            e_pas.insert(0,pas)
            e_adr.insert(0,adr)

            def confirm():
                nnam=e_name.get()#new name
                
                nphno=e_tel.get()
                ngen=e_gen.get()
                nage=e_age.get()
                ndob=e_birth.get()
                nema=e_ema.get()
                nadr=e_adr.get()
                npas=e_pas.get()

                data=[nphno,nnam,ngen,nage,ndob,nema,nphno,nadr,npas]
                update(data,n)
                messagebox.showinfo('Success','data updated successfully!')
                e_name.delete(0,'end')
                e_gen.delete(0,'end')
                e_age.delete(0,'end')
                e_birth.delete(0,'end')
                e_ema.delete(0,'end')
                e_tel.delete(0,'end')
                e_adr.delete(0,'end')
                e_pas.delete(0,'end')
                for widget in frame_table.winfo_children():
                    widget.destroy()
                b_confirm.destroy()
                show()
            b_confirm=Button(frame_down,text="Confirm",width="15",bg=co2,font=('Ivy 10 bold'),fg=co0,command=confirm)
            b_confirm.place(x=200,y=290)
        except IndexError:
            messagebox.showerror('Error','Select Your entry from the table')        

    def to_remove():
        try:
            tree_data=tree.focus()
            tree_dictionary=tree.item(tree_data)
            tree_list=tree_dictionary['values']
            tree_phno=str(tree_list[5])

            remove(tree_phno,n)

            messagebox.showinfo('Success','Deleted successfully!!')
            for widget in frame_table.winfo_children():
                widget.destroy()

        except IndexError:
            messagebox.showerror('Error','Select Your entry from the table') 
        show()  
    
        
        #frameup widgets
        # def entries(sigin):
    app_name=Label(frame_up,text=sigin+" SignUP",height=1,font=('Verdana 17 bold'),bg=co2,fg=co0)
    app_name.place(x=5,y=5)
            #framedown widgets
    l_name=Label(frame_down,text="Name *",width=20,height=1,font=('Ivy 11'),bg=co0,anchor=NW)
    l_name.place(x=10,y=20)
    e_name=Entry(frame_down,width=35,justify='left',highlightthickness=1,relief="solid")
    e_name.place(x=80,y=20)

    l_gen=Label(frame_down,text="Gender *",width=20,height=1,font=('Ivy 11'),bg=co0,anchor=NW)
    l_gen.place(x=10,y=50)
    e_gen= ttk.Combobox(frame_down,width=37)
    e_gen['values']=['','F','M']
    e_gen.place(x=80,y=50)
    l_age=Label(frame_down,text="Age *",width=20,height=1,font=('Ivy 11'),bg=co0,anchor=NW)
    l_age.place(x=10,y=80)
    e_age=Entry(frame_down,width=35,justify='left',highlightthickness=1,relief="solid")
    e_age.place(x=80,y=80)

    l_birth=Label(frame_down,text="DOB *",width=20,height=1,font=('Ivy 11'),bg=co0,anchor=NW)
    l_birth.place(x=10,y=110)
    e_birth=Entry(frame_down,width=35,justify='left',font=('Ivy',11),highlightthickness=1,relief="solid")
    e_birth.place(x=80,y=110)
    l_ema=Label(frame_down,text="Email *",width=20,height=1,font=('Ivy 11'),bg=co0,anchor=NW)
    l_ema.place(x=10,y=140)
    e_ema=Entry(frame_down,width=35,justify='left',font=('Ivy',11),highlightthickness=1,relief="solid")
    e_ema.place(x=80,y=140)

    l_tel=Label(frame_down,text="Phno *",height=1,font=('Ivy 11'),bg=co0,anchor=NW)
    l_tel.place(x=10,y=170)
    e_tel=Entry(frame_down,width=35,justify='left',font=('Ivy',11),highlightthickness=1,relief="solid")
    e_tel.place(x=80,y=170)
    l_adr=Label(frame_down,text="Address ",height=1,font=('Ivy 11'),bg=co0,anchor=NW)
    l_adr.place(x=10,y=200)
    e_adr=Entry(frame_down,width=35,justify='left',font=('Ivy',11),highlightthickness=1,relief="solid")
    e_adr.place(x=80,y=200)
    l_pas=Label(frame_down,text="Password *",height=1,font=('Ivy 11'),bg=co0,anchor=NW)
    l_pas.place(x=10,y=230)
    e_pas=Entry(frame_down,width=35,justify='left',font=('Ivy',11),highlightthickness=1,relief="solid")
    e_pas.place(x=80,y=230)
    
    
       
    b_view=Button(frame_down,text="View",width="12",bg=co2,font=('Ivy 10 bold'),fg=co0,command=show)
    b_view.place(x=465,y=60)
    b_add=Button(frame_down,text="Add",width="12",bg=co2,font=('Ivy 10 bold'),fg=co0,command=insert)
    b_add.place(x=465,y=100)
    b_upd=Button(frame_down,text="Update",width="12",bg=co2,font=('Ivy 10 bold'),fg=co0,command=to_update)
    b_upd.place(x=465,y=140)
    b_exit=Button(frame_down,text="Update",width="12",bg=co2,font=('Ivy 10 bold'),fg=co0,command=starting)
    b_exit.place(x=465,y=240)
    
    l_dis=Label(frame_down,text="Disease ",height=1,font=('Ivy 11'),bg=co0,anchor=NW)
    l_dis.place(x=10,y=260)
    e_dis=Entry(frame_down,width=35,justify='left',font=('Ivy',11),highlightthickness=1,relief="solid")
    e_dis.place(x=80,y=260)
    l_dr=Label(frame_down,text="Doctor ",height=1,font=('Ivy 11'),bg=co0,anchor=NW)
    l_dr.place(x=10,y=290)
    e_dr= ttk.Combobox(frame_down,width=37)
    e_dr['values']=['','Dr Fatima','Dr Mahesh','Dr Anjali']
    e_dr.place(x=80,y=290)
    dis=e_dis.get()
    b_del=Button(frame_down,text="Delete",width="12",bg=co2,font=('Ivy 10 bold'),fg=co0,command=to_remove)
    b_del.place(x=465,y=180)






def starting():
    clear_fra(frame_down)
    clear_fra(frame_table)
    clear_fra(frame_up)
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
    clear_fra(frame_table)
    
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
    b_exit=Button(frame_table,text="Exit",width="20",bg=co2,font=('Ivy 20 bold'),fg=co0,command=starting)
    b_exit.place(x=120,y=80)


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
    b_back.place(x=220,y=220)
    b_log=Button(frame_down,text="Login",width="15",bg=co2,font=('Ivy 10 bold'),fg=co0,command=check)
    b_log.place(x=220,y=260)
    if(sigin=="Patient"):
        b_sup=Button(frame_down,text="Sign up",width="15",bg=co2,font=('Ivy 10 bold'),fg=co0,command=lambda: newsig_pg(sigin))
        b_sup.place(x=220,y=300) 
    window.mainloop()

starting()
window.mainloop()
