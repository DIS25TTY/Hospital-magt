import sys
import csv
def add(i,n):
    if(n==1):
        with open('patient.csv','a+',newline='')as file:#using dat.csv as file in a+ mode--append mode
            writer=csv.writer(file)#for writing
            writer.writerow(i)#adds the entry as row
    elif n==2:
        with open('doctor.csv','a+',newline='')as file:#using dat.csv as file in a+ mode--append mode
            writer=csv.writer(file)#for writing
            writer.writerow(i)#adds the entry as row
    elif n==3:
        with open('admin.csv','a+',newline='')as file:#using dat.csv as file in a+ mode--append mode
            writer=csv.writer(file)#for writing
            writer.writerow(i)#adds the entry as row
    elif n==4:
        with open('apoint.csv','a+',newline='')as file:#using dat.csv as file in a+ mode--append mode
            writer=csv.writer(file)#for writing
            writer.writerow(i)#adds the entry as row
    # with open('patient.csv','a+',newline='')as file:#using dat.csv as file in a+ mode--append mode
    #     writer=csv.writer(file)#for writing
    #     writer.writerow(i)#adds the entry as row

# to check whether the data is updated or not

# add(['girl','F','13','25/7/23','123@gmail.com','456789','loose'])
# add(['girl','F','13','25/7/23','123@gmail.com','456545678','loose'])

def view(n):
    data=[]
    if(n==1):
        with open('patient.csv','r') as file:
            reader=csv.reader(file)#will be able to read every row in the file
            for(row) in reader:
                data.append(row)# loading all rows into the data var
    elif n==2:
        with open('doctor.csv','r') as file:
            reader=csv.reader(file)#will be able to read every row in the file
            for(row) in reader:
                data.append(row)
    elif n==3:
        with open('admin.csv','r') as file:
            reader=csv.reader(file)#will be able to read every row in the file
            for(row) in reader:
                data.append(row)
    elif n==4:
        with open('apoint.csv','r') as file:
            reader=csv.reader(file)#will be able to read every row in the file
            for(row) in reader:
                data.append(row)
    print(data)
    return data

# view()

def remove(i,n):
    def save(j,n):
        if(n==1):
            with open('patient.csv','w',newline='') as file:
                writer=csv.writer(file)
                writer.writerows(j)# loading all rows into the data var
        elif n==2:
            with open('doctor.csv','w',newline='') as file:
                writer=csv.writer(file)
                writer.writerows(j)
        elif n==3:
            with open('admin.csv','w',newline='') as file:
                writer=csv.writer(file)
                writer.writerows(j)
        elif n==4:
            with open('apoint.csv','w',newline='') as file:
                writer=csv.writer(file)
                writer.writerows(j)
        # with open('patient.csv','w',newline='') as file:
        #     writer=csv.writer(file)
        #     writer.writerows(j)#we r not just updating 1 row but all rows, dummy dummy stuffs



    newlist=[]
    phno=i#used as primary key
    if(n==1):
        with open('patient.csv','r') as file:
            reader=csv.reader(file)
            for row in reader:
                newlist.append(row)# for safety not to loose data so copying into new list
                for elem in row:
                    if elem ==phno:
                        newlist.remove(row)# loading all rows into the data var
    elif n==2:
        with open('doctor.csv','r') as file:
            reader=csv.reader(file)
            for row in reader:
                newlist.append(row)# for safety not to loose data so copying into new list
                for elem in row:
                    if elem ==phno:
                        newlist.remove(row)
    elif n==3:
        with open('admin.csv','r') as file:
            reader=csv.reader(file)
            for row in reader:
                newlist.append(row)# for safety not to loose data so copying into new list
                for elem in row:
                    if elem ==phno:
                        newlist.remove(row)
    elif n==4:
        with open('apoint.csv','r') as file:
            reader=csv.reader(file)
            for row in reader:
                newlist.append(row)# for safety not to loose data so copying into new list
                for elem in row:
                    if elem ==phno:
                        newlist.remove(row)

                
    # with open('patient.csv','r') as file:
    #     reader=csv.reader(file)
    #     for row in reader:
    #          newlist.append(row)# for safety not to loose data so copying into new list
    #          for elem in row:
    #              if elem ==phno:
    #                    newlist.remove(row)
    save(newlist,n)

# remove('456789')
# view()        

def update(i,n):
    def up_new(j):#modifying the format
        if n==1:
            with open('patient.csv','w',newline='') as file:
                writer =csv.writer(file)
                writer.writerows(j)
        elif n==2:
            with open('doctor.csv','w',newline='') as file:
                writer =csv.writer(file)
                writer.writerows(j)
        elif n==3:
            with open('admin.csv','w',newline='') as file:
                writer =csv.writer(file)
                writer.writerows(j)
        elif n==4:
            with open('apoint.csv','w',newline='') as file:
                writer =csv.writer(file)
                writer.writerows(j)
    newlist=[]
    phno=i[0]
    if(n==1):
        with open('patient.csv','r') as file:
            reader =csv.reader(file)
            for row in reader:
                newlist.append(row)
                for elem in row:
                    if(elem) ==phno:
                        nam=i[1]
                        gen=i[2]
                        age=i[3]
                        dob=i[4]
                        email=i[5]
                        ph=i[6]
                        adr=i[7]
                        pas=i[8]

                        data=[nam,gen,age,dob,email,ph,adr,pas]
                        index=newlist.index(row)
                        newlist[index]=data# loading all rows into the data var
    elif n==2:
        with open('doctor.csv','r') as file:
            reader =csv.reader(file)
            for row in reader:
                newlist.append(row)
                for elem in row:
                    if(elem) ==phno:
                        nam=i[1]
                        gen=i[2]
                        age=i[3]
                        dob=i[4]
                        email=i[5]
                        ph=i[6]
                        adr=i[7]
                        pas=i[8]

                        data=[nam,gen,age,dob,email,ph,adr,pas]
                        index=newlist.index(row)
                        newlist[index]=data
    elif n==3:
        with open('admin.csv','r') as file:
            reader =csv.reader(file)
            for row in reader:
                newlist.append(row)
                for elem in row:
                    if(elem) ==phno:
                        nam=i[1]
                        gen=i[2]
                        age=i[3]
                        dob=i[4]
                        email=i[5]
                        ph=i[6]
                        adr=i[7]
                        pas=i[8]

                        data=[nam,gen,age,dob,email,ph,adr,pas]
                        index=newlist.index(row)
                        newlist[index]=data
    elif n==4:
        with open('apoint.csv','r') as file:
            reader =csv.reader(file)
            for row in reader:
                newlist.append(row)
                for elem in row:
                    if(elem) ==phno:
                        nam=i[1]
                        gen=i[2]
                        age=i[3]
                        dob=i[4]
                        email=i[5]
                        ph=i[6]
                        adr=i[7]
                        pas=i[8]

                        data=[nam,gen,age,dob,email,ph,adr,pas]
                        index=newlist.index(row)
                        newlist[index]=data

    # with open('patient.csv','r')as file:
    #         reader =csv.reader(file)
    #         for row in reader:
    #             newlist.append(row)
    #             for elem in row:
    #                 if(elem) ==phno:
    #                     nam=i[1]
    #                     gen=i[2]
    #                     age=i[3]
    #                     dob=i[4]
    #                     email=i[5]
    #                     ph=i[6]
    #                     adr=i[7]
    #                     pas=i[8]

    #                     data=[nam,gen,age,dob,email,ph,adr,pas]
    #                     index=newlist.index(row)
    #                     newlist[index]=data
    up_new(newlist)

# sam=['123','girlcod','F','13','12/1/23','girl@gmail.com','123','konnapana']
# update(sam)

def search(i,n):
    data=[]
    phno=i
    if(n==1):
        with open('patient.csv','r')as file:#using dat.csv as file in a+ mode--append mode
            reader =csv.reader(file)
            
            for row in reader:
                for elem in row:
                    if elem==phno:
                        data.append(row)
    elif n==2:
        with open('doctor.csv','r')as file:#using dat.csv as file in a+ mode--append mode
            reader =csv.reader(file)
            
            for row in reader:
                for elem in row:
                    if elem==phno:
                        data.append(row)
    elif n==3:
        with open('admin.csv','r')as file:#using dat.csv as file in a+ mode--append mode
            reader =csv.reader(file)
            
            for row in reader:
                for elem in row:
                    if elem==phno:
                        data.append(row)
    elif n==4:
        with open('apoint.csv','r')as file:#using dat.csv as file in a+ mode--append mode
            reader =csv.reader(file)
            for row in reader:
                for elem in row:
                    if elem==phno:
                        data.append(row)
    # with open('patient.csv','r') as file:
    #         reader =csv.reader(file)
            
    #         for row in reader:
    #             for elem in row:
    #                 if elem==phno:
    #                     data.append(row)
    return data
