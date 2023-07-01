from tkinter import *
from tkinter import ttk
from view import *
from tkinter import messagebox



def appoint(sigin,data):
    co0="#ffffff"
    co1="#000000"
    co2="#4456f0"

    if(sigin=="Admin"):
        k=3
    elif sigin=="Patient":
        k=1
    elif sigin=="Doctor" :
        k=2

    window=Tk()
    window.title("")
    window.geometry('600x350')
    window.configure(background=co0)
    window.resizable(width=FALSE,height=FALSE)

    #skeleton
    frame_up=Frame(window,width=650,height=50,bg=co2)
    frame_up.grid(row=0,column=0,padx=0,pady=1)

    #frame tab
    frame_table=Frame(window,width=550,height=300,bg=co0,relief="flat")
    frame_table.grid(row=2,column=0,columnspan=2,padx=10,pady=2,sticky=NW)
    frame_down=Frame(window,width=650,height=50,bg=co0)#2nd invisible block
    frame_down.grid(row=1,column=0,padx=0,pady=1)
    def show():
        global tree
        demo=view(4)
        app_name=Label(frame_up,text=sigin+"Appointments                  DG Hosp",height=1,font=('Verdana 17 bold'),bg=co2,fg=co0)
        app_name.place(x=5,y=5)   
        listh=['dr','pat','dis','Date','Time']
        tree=ttk.Treeview(frame_table,selectmode="extended",columns=listh,show="headings")
        vsb=ttk.Scrollbar(frame_table,orient="vertical",command=tree.yview)
        hsb=ttk.Scrollbar(frame_table,orient="horizontal",command=tree.xview)

        tree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)
        tree.grid(column=0,row=0,sticky='nsew')
        vsb.grid(column=1,row=0,sticky='ns')
        hsb.grid(column=0,row=1,sticky='ew')
        
        tree.heading(0,text='Dr',anchor=NW)
        tree.heading(1,text='Patient',anchor=NW)
        tree.heading(2,text='Disease',anchor=NW)
        tree.heading(3,text='Date',anchor=NW)
        tree.heading(4,text='Time',anchor=NW)

        tree.column(0,width=120,anchor='nw')
        tree.column(1,width=120,anchor='nw')
        tree.column(2,width=120,anchor='nw')
        tree.column(3,width=100,anchor='nw')
        tree.column(4,width=100,anchor='nw')
        def to_remove():
            try:
                tree_data=tree.focus()
                tree_dictionary=tree.item(tree_data)
                tree_list=tree_dictionary['values']
                tree_phno=str(tree_list[5])

                remove(tree_phno,4)

                messagebox.showinfo('Success','Deleted successfully!!')
                for widget in frame_table.winfo_children():
                    widget.destroy()

            except IndexError:
                messagebox.showerror('Error','Select Your entry from the table') 
            show()
        b_log=Button(frame_down,text="Delete",width="15",bg=co2,font=('Ivy 10 bold'),fg=co0,command=to_remove)
        b_log.place(x=220,y=15)

            
        if k==3:
            for i in demo:
                tree.insert('','end',values=i)
        else:
            dd=search(data[0][0],4)
            print(data[0][5])
            tree.insert('','end',values=dd[0])
            
    show()
    window.mainloop()
