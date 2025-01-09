import tkinter as tki
from tkinter import *
from tkinter import messagebox
import csv
import pandas as pd
import os

#Reading the CSVs
df=pd.read_csv("logreg.csv")
bcsv=pd.read_csv("BirthCertificate.csv")
ccsv=pd.read_csv("VehicalOwnership.csv")
pcsv=pd.read_csv("PropertyOwnership.csv")

#EXIT BUTTON
def ex():
    mc=messagebox.askquestion("Exit","Are you sure you want to exit?")
    if mc == "yes":
        os._exit(0)

#LOGIN BUTTON
def log():
    tk.withdraw()
    lw=Toplevel()
    lw.title("Login Window")
    lw.geometry("370x250")

    def log_run():

        login = False

        while login == False:
            data=[]
            with open("logreg.csv") as csvfile:
                reader=csv.reader(csvfile)
                for row in reader:
                    data.append(row)
                    
            username=e1.get()
            password=e2.get()
 
            col0 = [x[0] for x in data]
            col1 = [x[1] for x in data]

            if username in col0:
                for k in range(0,len(col0)):
                    if col0[k] == username and col1[k] == password:
                        login = True
                        lw.destroy()


                        #MAIN WINDOW
                        def mw():
                            mw=Toplevel()
                            mw.title("MAIN WINDOW")
                            mw.geometry("500x500")

                            #BIRTH CERTIFICATE
                            def bc():
                                a=[]
                                for i in bcsv["Name"]:
                                    a.append(i)
                                    if username in a:
                                        mw.withdraw()

                                        #BC WINDOW
                                    
                                        bc=Toplevel()
                                        bc.title("Birth Certificate Manager")
                                        bc.geometry("370x250")
                                        hb1=Label(bc,text="To Show all Details : ",font=("Arial Bold",17))

                                        def all_info():
                                            bdf=bcsv.set_index(["Name"])
                                            iw=Toplevel()
                                            iw.title("Information")

                                            text=Text(iw)
                                            text.insert(INSERT,bdf.loc[username])
                                            text.pack()

                                                                                        
                                        
                                        bb1=Button(bc,text="Click Here",padx=17,pady=5,command=all_info)
                                        sb1=Label(bc,text="                    ")
                                        hb2=Label(bc,text="To select details --  ",font=("Arial Bold",17))
                                        #Options--
                                        options=["Choose Here",
                                                 "Name",
                                                 "Sex","Date Of Birth",
                                                 "Place Of Birth",
                                                 "Name of Father",
                                                 "Name of Mother",
                                                 "Reg.No.",
                                                 "Date of Reg.",
                                                 "Date"
                                                 ]
                                        
                                        clkd=StringVar(bc)
                                        clkd.set(options[0])
                                        
                                        dd1=OptionMenu(bc,clkd,*options)

                                        #def select
                                        def slct():
                                            bdf=bcsv.set_index(["Name"])
                                            if clkd.get()=="Name":
                                                nm="Name : "
                                                ch=username
                                            elif clkd.get()=="Sex":
                                                nm="Sex : "
                                                ch=bdf.loc[username,"Sex"]
                                            elif clkd.get()=="Date Of Birth":
                                                nm="DOB : "
                                                ch=bdf.loc[username,"Date Of Birth"]
                                            elif clkd.get()=="Place Of Birth":
                                                nm="Place Of Birth : "
                                                ch=bdf.loc[username,"Place Of Birth"]
                                            elif clkd.get()=="Name of Father":
                                                nm="Father's Name : "
                                                ch=bdf.loc[username,"Name of Father"]
                                            elif clkd.get()=="Name of Mother":
                                                nm="Mother's Name : "
                                                ch=bdf.loc[username,"Name of Mother"]
                                            elif clkd.get()=="Reg.No.":
                                                nm="Reg. No. : "
                                                ch=bdf.loc[username,"Registration No."]
                                            elif clkd.get()=="Date of Reg.":
                                                nm="Reg. Date : "
                                                ch=bdf.loc[username,"Date of Registration"]
                                            elif clkd.get()=="Date":
                                                nm="Date"
                                                ch=bdf.loc[username,"Date"]

                                            iw=Toplevel()
                                            iw.title("Selected Information")

                                            text=Text(iw)
                                            text.insert(INSERT,nm)
                                            text.insert(END,ch)
                                            text.pack()
                                            

                                        bb2=Button(bc,text="Select",padx=15,pady=5,command=slct)

                                        def mr():
                                            mw.deiconify()
                                            bc.destroy()
                                        
                                        bb3=Button(bc,text="Go Back",padx=15,pady=5,command=mr)

                                        hb1.grid(row=0,column=0,columnspan=3)
                                        bb1.grid(row=0,column=4)
                                        sb1.grid(row=1,column=0)
                                        hb2.grid(row=2,column=0,columnspan=3,sticky="W")
                                        dd1.grid(row=2,column=4)
                                        bb2.grid(row=3,column=1)
                                        bb3.grid(row=5,column=0,sticky="W")


                                        break
                                    else:
                                        mc=messagebox.askquestion("Add","A file doesint exist. Do you want to create a new one?")
                                        if mc == "yes":
                                            mw.withdraw()
                                            inpbc=Toplevel()
                                            inpbc.title("Add Birth Certificate")
                                            inpbc.geometry("400x350")

                                            h1=Label(inpbc,text="Sex : ",font=("Arial Bold",))
                                            h2=Label(inpbc,text="Date Of Birth : ",font=("Arial Bold",))
                                            h3=Label(inpbc,text="Place Of Birth : ",font=("Arial Bold",))
                                            h4=Label(inpbc,text="Name of Father : ",font=("Arial Bold",))
                                            h5=Label(inpbc,text="Name of Mother : ",font=("Arial Bold",))
                                            h6=Label(inpbc,text="Reg. No. : ",font=("Arial Bold",))
                                            h7=Label(inpbc,text="Date of Reg.",font=("Arial Bold",))
                                            h8=Label(inpbc,text="Date",font=("Arial Bold",))

                                            e1=Entry(inpbc,width=35,borderwidth=5)
                                            e2=Entry(inpbc,width=35,borderwidth=5)
                                            e3=Entry(inpbc,width=35,borderwidth=5)
                                            e4=Entry(inpbc,width=35,borderwidth=5)
                                            e5=Entry(inpbc,width=35,borderwidth=5)
                                            e6=Entry(inpbc,width=35,borderwidth=5)
                                            e7=Entry(inpbc,width=35,borderwidth=5)
                                            e8=Entry(inpbc,width=35,borderwidth=5)


                                            def enter():
                                                bcsv=pd.read_csv("BirthCertificate.csv")
                                                df={"Name":username,"Sex":e1.get(),
                                                    "Date Of Birth":e2.get(),
                                                    "Place Of Birth":e3.get(),
                                                    "Name of Father":e4.get(),
                                                    "Name of Mother":e5.get(),
                                                    "Registration No.":e6.get(),
                                                    "Date of Registration":e7.get(),
                                                    "Date":e8.get(),
                                                    }
                                                bcsv=bcsv.append(df,ignore_index=True)
                                                bcsv.to_csv("BirthCertificate.csv",index=False)

                                                mc=messagebox.showinfo("Done","Your data had been added")
                                                inpbc.destroy()
                                                mw.deiconify()
                                                
                                            b1=Button(inpbc,text="Enter",command=enter)

                                            def back():
                                                inpbc.destroy()
                                                mw.deiconify()
                                            b2=Button(inpbc,text="Go Back",command=back)
                                            
                                            #grid
                                            
                                            h1.grid(row=0,column=0,sticky="W")
                                            e1.grid(row=0,column=1,sticky="W")
                                            h2.grid(row=1,column=0,sticky="W")
                                            e2.grid(row=1,column=1,sticky="W")
                                            h3.grid(row=2,column=0,sticky="W")
                                            e3.grid(row=2,column=1,sticky="W")
                                            h4.grid(row=3,column=0,sticky="W")
                                            e4.grid(row=3,column=1,sticky="W")
                                            h5.grid(row=4,column=0,sticky="W")
                                            e5.grid(row=4,column=1,sticky="W")
                                            h6.grid(row=5,column=0,sticky="W")
                                            e6.grid(row=5,column=1,sticky="W")
                                            h7.grid(row=6,column=0,sticky="W")
                                            e7.grid(row=6,column=1,sticky="W")
                                            h8.grid(row=7,column=0,sticky="W")
                                            e8.grid(row=7,column=1,sticky="W")
                                            b1.grid(row=8,sticky="W")
                                            b2.grid(row=9,sticky="W")

                                            
                                            break

                                            

                       
                            #PROPERTY OWNERSHIP
                            def po():
                                a=[]
                                for i in pcsv["Name Of Owner"]:
                                    a.append(i)
                                    if username in a:
                                        mw.withdraw()

                                        #PROPERTY OWNERSHIP WINDOW

                                        po=Toplevel()
                                        po.title("Property Ownership Manager")
                                        po.geometry("370x250")
                                        
                                        hb1=Label(po,text="To Show all Details : ",font=("Arial Bold",17))

                                        
                                        def all_info():
                                            pdf=pcsv.set_index(["Name Of Owner"])
                                            iw=Toplevel()
                                            iw.title("Information")

                                            text=Text(iw)
                                            text.insert(INSERT,pdf.loc[username])
                                            text.pack()
                                        
                                        bb1=Button(po,text="Click Here",padx=17,pady=5,command=all_info)
                                        sb1=Label(po,text="                    ")
                                        hb2=Label(po,text="To select details --  ",font=("Arial Bold",17))
                                        #Options--
                                        options=["Name Of Owner",
                                                 "Name Of Previous Owner",
                                                 "State","District",
                                                 "Address",
                                                 "Postal Code",
                                                 "Landmark",
                                                 "Date Of Regestration"
                                                 ]
                                        
                                        clkd=StringVar(po)
                                        clkd.set(options[0])
                                        
                                        dd1=OptionMenu(po,clkd,*options)

                                        #def select
                                        def slct():
                                            pdf=pcsv.set_index(["Name Of Owner"])
                                            if clkd.get()=="Name Of Owner":
                                                nm="Name Of Owner : "
                                                ch=username
                                            elif clkd.get()=="Name Of Previous Owner":
                                                nm="Name Of Previous Owner : "
                                                ch=pdf.loc[username,"Name Of Previous Owner"]
                                            elif clkd.get()=="State":
                                                nm="State : "
                                                ch=pdf.loc[username,"State"]
                                            elif clkd.get()=="District":
                                                nm="District : "
                                                ch=pdf.loc[username,"District"]
                                            elif clkd.get()=="Address":
                                                nm="Address : "
                                                ch=pdf.loc[username,"Address"]
                                            elif clkd.get()=="Postal Code":
                                                nm="Postal Code : "
                                                ch=pdf.loc[username,"Postal Code"]
                                            elif clkd.get()=="Landmark":
                                                nm="Landmark : "
                                                ch=pdf.loc[username,"Landmark"]
                                            elif clkd.get()=="Date Of Regestration":
                                                nm="Date Of Regestration : "
                                                ch=pdf.loc[username,"Date Of Regestration"]

                                            iw=Toplevel()
                                            iw.title("Selected Information")

                                            text=Text(iw)
                                            text.insert(INSERT,nm)
                                            text.insert(END,ch)
                                            text.pack()

                                        bb2=Button(po,text="Select",padx=15,pady=5,command=slct)

                                        def mr():
                                            mw.deiconify()
                                            po.destroy()
                                        
                                        bb3=Button(po,text="Go Back",padx=15,pady=5,command=mr)

                                        hb1.grid(row=0,column=0,columnspan=3)
                                        bb1.grid(row=0,column=4)
                                        sb1.grid(row=1,column=0)
                                        hb2.grid(row=2,column=0,columnspan=3,sticky="W")
                                        dd1.grid(row=2,column=4)
                                        bb2.grid(row=3,column=1)
                                        bb3.grid(row=5,column=0,sticky="W")


                                        break
                                    else:
                                        mc=messagebox.askquestion("Add","A file doesint exist. Do you want to create a new one?")
                                        if mc == "yes":
                                            mw.withdraw()
                                            inppo=Toplevel()
                                            inppo.title("Add Property Ownership")
                                            inppo.geometry("400x350")

                                            h1=Label(inppo,text="Name Of Previous Owner : ",font=("Arial Bold",))
                                            h2=Label(inppo,text="State : ",font=("Arial Bold",))
                                            h3=Label(inppo,text="District : ",font=("Arial Bold",))
                                            h4=Label(inppo,text="Address : ",font=("Arial Bold",))
                                            h5=Label(inppo,text="Postal Code : ",font=("Arial Bold",))
                                            h6=Label(inppo,text="Landmark : ",font=("Arial Bold",))
                                            h7=Label(inppo,text="Date Of Registration : ",font=("Arial Bold",))

                                            e1=Entry(inppo,width=35,borderwidth=5)
                                            e2=Entry(inppo,width=35,borderwidth=5)
                                            e3=Entry(inppo,width=35,borderwidth=5)
                                            e4=Entry(inppo,width=35,borderwidth=5)
                                            e5=Entry(inppo,width=35,borderwidth=5)
                                            e6=Entry(inppo,width=35,borderwidth=5)
                                            e7=Entry(inppo,width=35,borderwidth=5)
                                            
                                            def enter():
                                                pcsv=pd.read_csv("PropertyOwnership.csv")
                                                df={"Name Of Owner":username,
                                                    "Name Of Previous Owner":e1.get(),
                                                    "State":e2.get(),
                                                    "District":e3.get(),
                                                    "Address":e4.get(),
                                                    "Postal Code":e5.get(),
                                                    "Landmark":e6.get(),
                                                    "Date Of Registration":e7.get(),
                                                    }
                                                pcsv=pcsv.append(df,ignore_index=True)
                                                pcsv.to_csv("PropertyOwnership.csv",index=False)

                                                mc=messagebox.showinfo("Done","Your data had been added")
                                                inppo.destroy()
                                                mw.deiconify()
                                                
                                            b1=Button(inppo,text="Enter",command=enter)

                                            def back():
                                                inppo.destroy()
                                                mw.deiconify()
                                            b2=Button(inppo,text="Go Back",command=back)
                                            
                                            #grid
                                            
                                            h1.grid(row=0,column=0,sticky="W")
                                            e1.grid(row=0,column=1,sticky="W")
                                            h2.grid(row=1,column=0,sticky="W")
                                            e2.grid(row=1,column=1,sticky="W")
                                            h3.grid(row=2,column=0,sticky="W")
                                            e3.grid(row=2,column=1,sticky="W")
                                            h4.grid(row=3,column=0,sticky="W")
                                            e4.grid(row=3,column=1,sticky="W")
                                            h5.grid(row=4,column=0,sticky="W")
                                            e5.grid(row=4,column=1,sticky="W")
                                            h6.grid(row=5,column=0,sticky="W")
                                            e6.grid(row=5,column=1,sticky="W")
                                            h7.grid(row=6,column=0,sticky="W")
                                            e7.grid(row=6,column=1,sticky="W")
                                            b1.grid(row=7,sticky="W")
                                            b2.grid(row=8,sticky="W")
                                            break
                                        
                            #VEHICLE OWNERSHIP
                            def vo():
                                a=[]
                                for i in ccsv["Owners Name"]:
                                    a.append(i)
                                    if username in a:
                                        mw.withdraw()

                                        #VEHICAL OWNERSHIP WINDOW

                                        vo=Toplevel()
                                        vo.title("Vehical Ownership Manager")
                                        vo.geometry("370x250")
                                        
                                        hb1=Label(vo,text="To Show all Details : ",font=("Arial Bold",17))

                                        
                                        def all_info():
                                            cdf=ccsv.set_index(["Owners Name"])
                                            iw=Toplevel()
                                            iw.title("Information")

                                            text=Text(iw)
                                            text.insert(INSERT,cdf.loc[username])
                                            text.pack()
                                        
                                        bb1=Button(vo,text="Click Here",padx=17,pady=5,command=all_info)
                                        sb1=Label(vo,text="                    ")
                                        hb2=Label(vo,text="To select details --  ",font=("Arial Bold",17))
                                        #Options--
                                        options=["Choose Here",
                                                 "Owner's Name",
                                                 "Company Name",
                                                 "Dealership Name",
                                                 "Dealership Number",
                                                 "Car Model",
                                                 "Fuel Type",
                                                 "Stock Colour",
                                                 "Licence Plate",
                                                 "Reg. Date",
                                                 "Safety Measures"
                                                 ]
                                        
                                        clkd=StringVar(vo)
                                        clkd.set(options[0])
                                        
                                        dd1=OptionMenu(vo,clkd,*options)

                                        #def select
                                        def slct():
                                            cdf=ccsv.set_index(["Owners Name"])
                                            if clkd.get()=="Owners Name":
                                                nm="Owners Name : "
                                                ch=username
                                            elif clkd.get()=="Company Name":
                                                nm="Company Name : "
                                                ch=cdf.loc[username,"Company Name"]
                                            elif clkd.get()=="Dealership Name":
                                                nm="Dealership Name : "
                                                ch=cdf.loc[username,"Dealership Name"]
                                            elif clkd.get()=="Dealership Number":
                                                nm="Dealership Number: "
                                                ch=cdf.loc[username,"Dealership Number"]
                                            elif clkd.get()=="Car Model":
                                                nm="Car Model : "
                                                ch=cdf.loc[username,"Car Model"]
                                            elif clkd.get()=="Fuel Type":
                                                nm="Fuel Type : "
                                                ch=cdf.loc[username,"Fuel Type"]
                                            elif clkd.get()=="Stock Colour":
                                                nm="Stock Colour : "
                                                ch=cdf.loc[username,"Stock Colour"]
                                            elif clkd.get()=="Licence Plate":
                                                nm="Licence Plate : "
                                                ch=cdf.loc[username,"Licence Plate"]
                                            elif clkd.get()=="Reg. Date":
                                                nm="Reg. Date : "
                                                ch=cdf.loc[username,"Reg. Date"]
                                            elif clkd.get()=="Safety Measures":
                                                nm="Safety Measures : "
                                                ch=cdf.loc[username,"Safety Measures"]

                                            iw=Toplevel()
                                            iw.title("Selected Information")

                                            text=Text(iw)
                                            text.insert(INSERT,nm)
                                            text.insert(END,ch)
                                            text.pack()

                                        bb2=Button(vo,text="Select",padx=15,pady=5,command=slct)

                                        def mr():
                                            mw.deiconify()
                                            vo.destroy()
                                        
                                        bb3=Button(vo,text="Go Back",padx=15,pady=5,command=mr)

                                        hb1.grid(row=0,column=0,columnspan=3)
                                        bb1.grid(row=0,column=4)
                                        sb1.grid(row=1,column=0)
                                        hb2.grid(row=2,column=0,columnspan=3,sticky="W")
                                        dd1.grid(row=2,column=4)
                                        bb2.grid(row=3,column=1)
                                        bb3.grid(row=5,column=0,sticky="W")


                                        break
                                    else:
                                        mc=messagebox.askquestion("Add","A file doesint exist. Do you want to create a new one?")
                                        if mc == "yes":
                                            mw.withdraw()
                                            inpvo=Toplevel()
                                            inpvo.title("Add Vehical Ownership")
                                            inpvo.geometry("400x350")

                                            h1=Label(inpvo,text="Company Name : ",font=("Arial Bold",))
                                            h2=Label(inpvo,text="Dealership Name : ",font=("Arial Bold",))
                                            h3=Label(inpvo,text="Dealership Number : ",font=("Arial Bold",))
                                            h4=Label(inpvo,text="Car Model : ",font=("Arial Bold",))
                                            h5=Label(inpvo,text="Fuel Type : ",font=("Arial Bold",))
                                            h6=Label(inpvo,text="Stock Colour : ",font=("Arial Bold",))
                                            h7=Label(inpvo,text="Licence Plate : ",font=("Arial Bold",))
                                            h8=Label(inpvo,text="Reg. Date : ",font=("Arial Bold",))
                                            h9=Label(inpvo,text="Safety Measures  : ",font=("Arial Bold",))

                                            e1=Entry(inpvo,width=35,borderwidth=5)
                                            e2=Entry(inpvo,width=35,borderwidth=5)
                                            e3=Entry(inpvo,width=35,borderwidth=5)
                                            e4=Entry(inpvo,width=35,borderwidth=5)
                                            e5=Entry(inpvo,width=35,borderwidth=5)
                                            e6=Entry(inpvo,width=35,borderwidth=5)
                                            e7=Entry(inpvo,width=35,borderwidth=5)
                                            e8=Entry(inpvo,width=35,borderwidth=5)
                                            e9=Entry(inpvo,width=35,borderwidth=5)


                                            def enter():
                                                ccsv=pd.read_csv("VehicalOwnership.csv")
                                                df={"Name":username,
                                                    "Company Name":e1.get(),
                                                    "Dealership Name":e2.get(),
                                                    "Dealership Number":e3.get(),
                                                    "Car Model":e4.get(),
                                                    "Fuel Type":e5.get(),
                                                    "Stock Colour":e6.get(),
                                                    "Licence Plate":e7.get(),
                                                    "Reg. Date":e8.get(),
                                                    "Safety Measures":e9.get()
                                                    }
                                                ccsv=ccsv.append(df,ignore_index=True)
                                                ccsv.to_csv("VehicalOwnership.csv",index=False)

                                                mc=messagebox.showinfo("Done","Your data had been added")
                                                inpvo.destroy()
                                                mw.deiconify()
                                                
                                            b1=Button(inpvo,text="Enter",command=enter)

                                            def back():
                                                inpvo.destroy()
                                                mw.deiconify()
                                            b2=Button(inpvo,text="Go Back",command=back)
                                            
                                            #grid
                                            
                                            h1.grid(row=0,column=0,sticky="W")
                                            e1.grid(row=0,column=1,sticky="W")
                                            h2.grid(row=1,column=0,sticky="W")
                                            e2.grid(row=1,column=1,sticky="W")
                                            h3.grid(row=2,column=0,sticky="W")
                                            e3.grid(row=2,column=1,sticky="W")
                                            h4.grid(row=3,column=0,sticky="W")
                                            e4.grid(row=3,column=1,sticky="W")
                                            h5.grid(row=4,column=0,sticky="W")
                                            e5.grid(row=4,column=1,sticky="W")
                                            h6.grid(row=5,column=0,sticky="W")
                                            e6.grid(row=5,column=1,sticky="W")
                                            h7.grid(row=6,column=0,sticky="W")
                                            e7.grid(row=6,column=1,sticky="W")
                                            h8.grid(row=7,column=0,sticky="W")
                                            e8.grid(row=7,column=1,sticky="W")
                                            b1.grid(row=8,sticky="W")
                                            b2.grid(row=9,sticky="W")
                                            break
                            

                            h1=tki.Label(mw,text="Welcome . Please Choose an Option",font=("Arial Bold",20))
                            h2=tki.Label(mw,text="                                 ",font=("Arial Bold",20))
                            h3=tki.Label(mw,text="Search : ",font=("Arial Bold",15))
                            h4=tki.Label(mw,text="                                 ",font=("Arial Bold",20))
                            h5=tki.Label(mw,text="Update Files : ",font=("Arial Bold",15))
                            h6=tki.Label(mw,text="                                 ",font=("Arial Bold",20))


                            h1.grid(row=0,column=0,columnspan=3)
                            h2.grid(row=1,column=0,columnspan=3)
                            h3.grid(row=2,column=0,sticky="W")
                            h4.grid(row=4,column=0,columnspan=3)
                            h5.grid(row=5,column=0,sticky="W")
                            h6.grid(row=7,column=0,columnspan=3)


                            b1=Button(mw,text="1.Birth Certificate ",padx=26,pady=10,command=bc)
                            b2=Button(mw,text="2.Property Ownership",padx=26,pady=10,command=po)
                            b3=Button(mw,text="3.Vehicle Ownership ",padx=26,pady=10,command=vo)

                            def ubc():
                                a=[]
                                for i in bcsv["Name"]:
                                    a.append(i)
                                    if username in a:
                                        mw.withdraw()

                                        #Update birth certificate

                                        ubc=Toplevel()
                                        ubc.title("Update Brith Certificate")
                                        ubc.geometry("370x300")

                                        t1=Label(ubc,text="Which detail do you want to update : ",font=("Arial Bold",15))
                                        #Options--
                                        options=["Choose Here",
                                                 "Sex","Date Of Birth",
                                                 "Place Of Birth",
                                                 "Name of Father",
                                                 "Name of Mother",
                                                 "Reg.No.",
                                                 "Date of Reg.",
                                                 "Date"
                                                 ]
                                        
                                        clkd=StringVar(ubc)
                                        clkd.set(options[0])
                                        
                                        om=OptionMenu(ubc,clkd,*options)
                                        
                                        t2=Label(ubc,text="Enter new detail here : ",font=("Arial Bold",15))
                                        e1=Entry(ubc,width=25,borderwidth=5)
                                        s1=Label(ubc,text="                        ",font=("Arial Bold",15))

                                        def select():
                                            bdf=bcsv.set_index(["Name"])
                                            
                                            if clkd.get()=="Sex":
                                                a=e1.get()
                                                bdf.loc[username,"Sex"] = a
                                                                                                
                                            elif clkd.get()=="Date Of Birth":
                                                a=e1.get()
                                                bdf.loc[username,"Date Of Birth"] = a

                                            elif clkd.get()=="Place Of Birth":
                                                a=e1.get()
                                                bdf.loc[username,"Place Of Birth"] = a
                                                
                                            elif clkd.get()=="Name of Father":
                                                a=e1.get()
                                                bdf.loc[username,"Name of Father"] = a
                                                
                                            elif clkd.get()=="Name of Mother":
                                                a=e1.get()
                                                bdf.loc[username,"Name of Mother"] = a
                                                
                                            elif clkd.get()=="Reg.No.":
                                                a=e1.get()
                                                bdf.loc[username,"Reg.No."] = a
                                                
                                            elif clkd.get()=="Date of Reg.":
                                                a=e1.get()
                                                bdf.loc[username,"Date of Reg."] = a
                                                
                                            elif clkd.get()=="Date":
                                                a=e1.get()
                                                bdf.loc[username,"Date"] = a

                                            mb=messagebox.askquestion("Confirm","Are you sure you want to make changes")
                                            if mb == "yes":
                                                bdf.to_csv("BirthCertificate.csv")
                                                ubc.destroy()
                                                mw.deiconify()        
                                            
                                        b1=Button(ubc,text="Change Detail",padx=20,pady=5,command=select)
                                        s2=Label(ubc,text="                        ",font=("Arial Bold",10))
                                        def bac():
                                            ubc.destroy()
                                            mw.deiconify()
                                        b2=Button(ubc,text="Go Back",padx=20,pady=5,command=bac)

                                        def addfile():
                                            ubc.withdraw()
                                            af=Toplevel()
                                            af.title("Add File")
                                            af.geometry("500x500")

                                            h1=Label(af,text="Sex : ",font=("Arial Bold",))
                                            h2=Label(af,text="Date Of Birth : ",font=("Arial Bold",))
                                            h3=Label(af,text="Place Of Birth : ",font=("Arial Bold",))
                                            h4=Label(af,text="Name of Father : ",font=("Arial Bold",))
                                            h5=Label(af,text="Name of Mother : ",font=("Arial Bold",))
                                            h6=Label(af,text="Reg. No. : ",font=("Arial Bold",))
                                            h7=Label(af,text="Date of Reg.",font=("Arial Bold",))
                                            h8=Label(af,text="Date",font=("Arial Bold",))

                                            e1=Entry(af,width=35,borderwidth=5)
                                            e2=Entry(af,width=35,borderwidth=5)
                                            e3=Entry(af,width=35,borderwidth=5)
                                            e4=Entry(af,width=35,borderwidth=5)
                                            e5=Entry(af,width=35,borderwidth=5)
                                            e6=Entry(af,width=35,borderwidth=5)
                                            e7=Entry(af,width=35,borderwidth=5)
                                            e8=Entry(af,width=35,borderwidth=5)


                                            def enter():
                                                bcsv=pd.read_csv("BirthCertificate.csv")
                                                df={"Name":username,"Sex":e1.get(),
                                                    "Date Of Birth":e2.get(),
                                                    "Place Of Birth":e3.get(),
                                                    "Name of Father":e4.get(),
                                                    "Name of Mother":e5.get(),
                                                    "Registration No.":e6.get(),
                                                    "Date of Registration":e7.get(),
                                                    "Date":e8.get(),
                                                    }
                                                bcsv=bcsv.append(df,ignore_index=True)
                                                bcsv.to_csv("BirthCertificate.csv",index=False)
                                                
                                            b1=Button(af,text="Enter",command=enter)

                                            def back():
                                                af.destroy()
                                                ubc.deiconify()
                                            b2=Button(af,text="Go Back",command=back)
                                            
                                            #grid
                                            
                                            h1.grid(row=0,column=0,sticky="W")
                                            e1.grid(row=0,column=1,sticky="W")
                                            h2.grid(row=1,column=0,sticky="W")
                                            e2.grid(row=1,column=1,sticky="W")
                                            h3.grid(row=2,column=0,sticky="W")
                                            e3.grid(row=2,column=1,sticky="W")
                                            h4.grid(row=3,column=0,sticky="W")
                                            e4.grid(row=3,column=1,sticky="W")
                                            h5.grid(row=4,column=0,sticky="W")
                                            e5.grid(row=4,column=1,sticky="W")
                                            h6.grid(row=5,column=0,sticky="W")
                                            e6.grid(row=5,column=1,sticky="W")
                                            h7.grid(row=6,column=0,sticky="W")
                                            e7.grid(row=6,column=1,sticky="W")
                                            h8.grid(row=7,column=0,sticky="W")
                                            e8.grid(row=7,column=1,sticky="W")
                                            b1.grid(row=8,sticky="W")
                                            b2.grid(row=9,sticky="W")
                                    
                                            
                                        ab=Button(ubc,text="Add",padx=20,pady=5,command=addfile)
                                    

                                        t1.grid(row=0,column=0,columnspan=7,sticky="W")
                                        om.grid(row=1,column=0,sticky="W")
                                        t2.grid(row=2,column=0,columnspan=7,sticky="W")
                                        e1.grid(row=3,column=0,sticky="W")
                                        s1.grid(row=4,column=0,columnspan=7,sticky="W")
                                        b1.grid(row=5,column=0,sticky="W")
                                        s2.grid(row=6,column=0,columnspan=7,sticky="W")
                                        b2.grid(row=7,column=0,sticky="W")
                                        ab.grid(row=8,sticky="W")

                                        break
                          
                            b4=Button(mw,text="1.Birth Certificate ",padx=26,pady=10,command=ubc)
                            
                            def upo():
                                a=[]
                                for i in pcsv["Name Of Owner"]:
                                    a.append(i)
                                    if username in a:
                                        mw.withdraw()

                                        #Update property ownership

                                        upo=Toplevel()
                                        upo.title("Update Property Ownership")
                                        upo.geometry("370x300")

                                        t1=Label(upo,text="Which detail do you want to update : ",font=("Arial Bold",15))
                                        #Options--
                                        options=["Choose Here",
                                                 "Name Of Owner",
                                                 "Name Of Previous Owner",
                                                 "State","District",
                                                 "Address",
                                                 "Postal Code",
                                                 "Landmark",
                                                 "Date Of Regestration"
                                                 ]
                                        
                                        clkd=StringVar(upo)
                                        clkd.set(options[0])
                                        
                                        om=OptionMenu(upo,clkd,*options)
                                        
                                        t2=Label(upo,text="Enter new detail here : ",font=("Arial Bold",15))
                                        e1=Entry(upo,width=25,borderwidth=5)
                                        s1=Label(upo,text="                        ",font=("Arial Bold",15))

                                        def select():
                                            pdf=pcsv.set_index(["Name Of Owner"])
                                            
                                            if clkd.get()=="Name Of Previous Owner":
                                                a=e1.get()
                                                pdf.loc[username,"Name Of Previous Owner"] = a
                                                                                                
                                            elif clkd.get()=="State":
                                                a=e1.get()
                                                pdf.loc[username,"State"] = a

                                            elif clkd.get()=="District":
                                                a=e1.get()
                                                pdf.loc[username,"District"] = a
                                                
                                            elif clkd.get()=="Address":
                                                a=e1.get()
                                                pdf.loc[username,"Address"] = a
                                                
                                            elif clkd.get()=="Postal Code":
                                                a=e1.get()
                                                pdf.loc[username,"Postal Code"] = a
                                                
                                            elif clkd.get()=="Landmark":
                                                a=e1.get()
                                                pdf.loc[username,"Landmark"] = a

                                            elif clkd.get()=="Date Of Regestration":
                                                a=e1.get()
                                                pdf.loc[username,"Date Of Regestration"] = a

                                            mb=messagebox.askquestion("Confirm","Are you sure you want to make changes")
                                            if mb == "yes":
                                                pdf.to_csv("PropertyOwnership.csv")
                                                upo.destroy()
                                                mw.deiconify()        
                                            
                                        b1=Button(upo,text="Change Detail",padx=20,pady=5,command=select)
                                        s2=Label(upo,text="                        ",font=("Arial Bold",10))
                                        
                                        def bac():
                                            upo.destroy()
                                            mw.deiconify()
                                        b2=Button(upo,text="Go Back",padx=20,pady=5,command=bac)
                                        
                                        def addfile():
                                            upo.withdraw()
                                            af=Toplevel()
                                            af.title("Add File")
                                            af.geometry("500x500")

                                            h1=Label(af,text="Sex : ",font=("Arial Bold",))
                                            h2=Label(af,text="Date Of Birth : ",font=("Arial Bold",))
                                            h3=Label(af,text="Place Of Birth : ",font=("Arial Bold",))
                                            h4=Label(af,text="Name of Father : ",font=("Arial Bold",))
                                            h5=Label(af,text="Name of Mother : ",font=("Arial Bold",))
                                            h6=Label(af,text="Reg. No. : ",font=("Arial Bold",))
                                            h7=Label(af,text="Date of Reg.",font=("Arial Bold",))
                                            h8=Label(af,text="Date",font=("Arial Bold",))

                                            e1=Entry(af,width=35,borderwidth=5)
                                            e2=Entry(af,width=35,borderwidth=5)
                                            e3=Entry(af,width=35,borderwidth=5)
                                            e4=Entry(af,width=35,borderwidth=5)
                                            e5=Entry(af,width=35,borderwidth=5)
                                            e6=Entry(af,width=35,borderwidth=5)
                                            e7=Entry(af,width=35,borderwidth=5)
                                            e8=Entry(af,width=35,borderwidth=5)


                                            def enter():
                                                pcsv=pd.read_csv("PropertyOwnership.csv")
                                                df={"Name":username,"Sex":e1.get(),
                                                    "Date Of Birth":e2.get(),
                                                    "Place Of Birth":e3.get(),
                                                    "Name of Father":e4.get(),
                                                    "Name of Mother":e5.get(),
                                                    "Registration No.":e6.get(),
                                                    "Date of Registration":e7.get(),
                                                    "Date":e8.get(),
                                                    }
                                                bcsv=bcsv.append(df,ignore_index=True)
                                                bcsv.to_csv("PropertyOwnership.csv",index=False)
                                                
                                            b1=Button(af,text="Enter",command=enter)

                                            def back():
                                                af.destroy()
                                                upo.deiconify()
                                            b2=Button(af,text="Go Back",command=back)
                                            
                                            #grid
                                            
                                            h1.grid(row=0,column=0,sticky="W")
                                            e1.grid(row=0,column=1,sticky="W")
                                            h2.grid(row=1,column=0,sticky="W")
                                            e2.grid(row=1,column=1,sticky="W")
                                            h3.grid(row=2,column=0,sticky="W")
                                            e3.grid(row=2,column=1,sticky="W")
                                            h4.grid(row=3,column=0,sticky="W")
                                            e4.grid(row=3,column=1,sticky="W")
                                            h5.grid(row=4,column=0,sticky="W")
                                            e5.grid(row=4,column=1,sticky="W")
                                            h6.grid(row=5,column=0,sticky="W")
                                            e6.grid(row=5,column=1,sticky="W")
                                            h7.grid(row=6,column=0,sticky="W")
                                            e7.grid(row=6,column=1,sticky="W")
                                            h8.grid(row=7,column=0,sticky="W")
                                            e8.grid(row=7,column=1,sticky="W")
                                            b1.grid(row=8,sticky="W")
                                            b2.grid(row=9,sticky="W")
                                    
                                            
                                        ab=Button(ubc,text="Add",padx=20,pady=5,command=addfile)
                                    

                                        t1.grid(row=0,column=0,columnspan=7,sticky="W")
                                        om.grid(row=1,column=0,sticky="W")
                                        t2.grid(row=2,column=0,columnspan=7,sticky="W")
                                        e1.grid(row=3,column=0,sticky="W")
                                        s1.grid(row=4,column=0,columnspan=7,sticky="W")
                                        b1.grid(row=5,column=0,sticky="W")
                                        s2.grid(row=6,column=0,columnspan=7,sticky="W")
                                        b2.grid(row=7,column=0,sticky="W")
                                        ab.grid(row=8,sticky="W")

                                        break

                            b5=Button(mw,text="2.Property Ownership",padx=26,pady=10,command=upo)
                            
                            def uvo():
                                a=[]
                                for i in ccsv["Owners Name"]:
                                    a.append(i)
                                    if username in a:
                                        mw.withdraw()

                                        #Update vehical ownership

                                        uvo=Toplevel()
                                        uvo.title("Update Vehical Ownership")
                                        uvo.geometry("370x300")

                                        t1=Label(uvo,text="Which detail do you want to update : ",font=("Arial Bold",15))
                                        #Options--
                                        options=["Choose Here",
                                                 "Owners Name",
                                                 "Company",
                                                 "Dealership Name",
                                                 "Dealership Number",
                                                 "Car Model",
                                                 "Fuel Type",
                                                 "Stock Colour",
                                                 "Licence Plate",
                                                 "Reg. Date"
                                                 "Safety Measures"
                                                 ]
                                        
                                        clkd=StringVar(uvo)
                                        clkd.set(options[0])
                                        
                                        om=OptionMenu(uvo,clkd,*options)
                                        
                                        t2=Label(uvo,text="Enter new detail here : ",font=("Arial Bold",15))
                                        e1=Entry(uvo,width=25,borderwidth=5)
                                        s1=Label(uvo,text="                        ",font=("Arial Bold",15))

                                        def select():
                                            cdf=ccsv.set_index(["Owners Name"])
                                            
                                            if clkd.get()=="Company":
                                                a=e1.get()
                                                cdf.loc[username,"Company"] = a
                                                                                                
                                            elif clkd.get()=="Dealership Name":
                                                a=e1.get()
                                                cdf.loc[username,"Dealership Name"] = a

                                            elif clkd.get()=="Dealership Number":
                                                a=e1.get()
                                                cdf.loc[username,"Dealership Number"] = a
                                                
                                            elif clkd.get()=="Car Model":
                                                a=e1.get()
                                                cdf.loc[username,"Car Model"] = a
                                                
                                            elif clkd.get()=="Fuel Type":
                                                a=e1.get()
                                                cdf.loc[username,"Fuel Type"] = a
                                                
                                            elif clkd.get()=="Stock Colour":
                                                a=e1.get()
                                                cdf.loc[username,"Stock Colour"] = a

                                            elif clkd.get()=="Licence Place":
                                                a=e1.get()
                                                cdf.loc[username,"Licence Place"] = a

                                            elif clkd.get()=="Reg. Date":
                                                a=e1.get()
                                                cdf.loc[username,"Reg. Date"] = a

                                            elif clkd.get()=="Safety Measures":
                                                a=e1.get()
                                                cdf.loc[username,"Safety Measures"] = a

                                            mb=messagebox.askquestion("Confirm","Are you sure you want to make changes")
                                            if mb == "yes":
                                                cdf.to_csv("VehicalOwnership.csv")
                                                uvo.destroy()
                                                mw.deiconify()        
                                            
                                        b1=Button(uvo,text="Change Detail",padx=20,pady=5,command=select)
                                        s2=Label(uvo,text="                        ",font=("Arial Bold",10))
                                        
                                        def bac():
                                            uvo.destroy()
                                            mw.deiconify()
                                            
                                        b2=Button(uvo,text="Go Back",padx=20,pady=5,command=bac)
                                        
                                        def addfile():
                                            uvo.withdraw()
                                            af=Toplevel()
                                            af.title("Add File")
                                            af.geometry("500x500")

                                            h1=Label(af,text="Company : ",font=("Arial Bold",))
                                            h2=Label(af,text="Dealership Name : ",font=("Arial Bold",))
                                            h3=Label(af,text="Dealership Number : ",font=("Arial Bold",))
                                            h4=Label(af,text="Car Model : ",font=("Arial Bold",))
                                            h5=Label(af,text="Fuel Type : ",font=("Arial Bold",))
                                            h6=Label(af,text="Stock Colour : ",font=("Arial Bold",))
                                            h7=Label(af,text="Licence Plate : ",font=("Arial Bold",))
                                            h8=Label(af,text="Reg. Date : ",font=("Arial Bold",))
                                            h9=Label(af,text="Safety Measures : ",font=("Arial Bold",))

                                            e1=Entry(af,width=35,borderwidth=5)
                                            e2=Entry(af,width=35,borderwidth=5)
                                            e3=Entry(af,width=35,borderwidth=5)
                                            e4=Entry(af,width=35,borderwidth=5)
                                            e5=Entry(af,width=35,borderwidth=5)
                                            e6=Entry(af,width=35,borderwidth=5)
                                            e7=Entry(af,width=35,borderwidth=5)
                                            e8=Entry(af,width=35,borderwidth=5)
                                            e9=Entry(af,width=35,borderwidth=5)



                                            def enter():
                                                ccsv=pd.read_csv("VehicalOwnership.csv")
                                                df={"Owners Name":username,
                                                    "Company":e1.get(),
                                                    "Dealership Name":e2.get(),
                                                    "Dealership Number":e3.get(),
                                                    "Car Model":e4.get(),
                                                    "Fuel Type":e5.get(),
                                                    "Stock Colour":e6.get(),
                                                    "Licence Plate":e7.get(),
                                                    "Reg. Date":e8.get(),
                                                    "Safety Measures":e9.get()
                                                    }
                                                ccsv=ccsv.append(df,ignore_index=True)
                                                ccsv.to_csv("VehicalOwnership.csv",index=False)
                                                
                                            b1=Button(af,text="Enter",command=enter)

                                            def back():
                                                af.destroy()
                                                uvo.deiconify()
                                            b2=Button(af,text="Go Back",command=back)
                                            
                                            #grid
                                            
                                            h1.grid(row=0,column=0,sticky="W")
                                            e1.grid(row=0,column=1,sticky="W")
                                            h2.grid(row=1,column=0,sticky="W")
                                            e2.grid(row=1,column=1,sticky="W")
                                            h3.grid(row=2,column=0,sticky="W")
                                            e3.grid(row=2,column=1,sticky="W")
                                            h4.grid(row=3,column=0,sticky="W")
                                            e4.grid(row=3,column=1,sticky="W")
                                            h5.grid(row=4,column=0,sticky="W")
                                            e5.grid(row=4,column=1,sticky="W")
                                            h6.grid(row=5,column=0,sticky="W")
                                            e6.grid(row=5,column=1,sticky="W")
                                            h7.grid(row=6,column=0,sticky="W")
                                            e7.grid(row=6,column=1,sticky="W")
                                            h8.grid(row=7,column=0,sticky="W")
                                            e8.grid(row=7,column=1,sticky="W")
                                            h9.grid(row=8,column=0,sticky="W")
                                            e9.grid(row=8,column=1,sticky="W")
                                            b1.grid(row=9,sticky="W")
                                            b2.grid(row=10,sticky="W")
                                    
                                            
                                        ab=Button(uvo,text="Add",padx=20,pady=5,command=addfile)
                                        b3                                    

                                        t1.grid(row=0,column=0,columnspan=7,sticky="W")
                                        om.grid(row=1,column=0,sticky="W")
                                        t2.grid(row=2,column=0,columnspan=7,sticky="W")
                                        e1.grid(row=3,column=0,sticky="W")
                                        s1.grid(row=4,column=0,columnspan=7,sticky="W")
                                        b1.grid(row=5,column=0,sticky="W")
                                        s2.grid(row=6,column=0,columnspan=7,sticky="W")
                                        b2.grid(row=7,column=0,sticky="W")
                                        ab.grid(row=8,sticky="W")

                                        break
                            b6=Button(mw,text="3.Vehicle Ownership ",padx=26,pady=10,command=uvo)

                            def extmw():
                                mw.destroy()
                                tk.deiconify()
                            b7=Button(mw,text="Log Out",padx=30,pady=10,command=extmw)

                            b1.grid(row=3,column=0)
                            b2.grid(row=3,column=1)
                            b3.grid(row=3,column=2)
                            b4.grid(row=6,column=0)
                            b5.grid(row=6,column=1)
                            b6.grid(row=6,column=2)
                            b7.grid(row=8,column=0,sticky="W")
                        mw()
            else:
                messagebox.showerror("Incorrect","Username Or Password is Incorrect")
                break
                

    e1=Entry(lw,width=35,borderwidth=5)
    t1=Label(lw,text="Enter Username:",font=("Arial Bold",15))
    e2=Entry(lw,width=35,borderwidth=5,show="*")
    t2=Label(lw,text="Enter Password:",font=("Arial Bold",15))

    bl1=Button(lw,text="Enter",padx=40,pady=10,command=log_run)

    def go_back():
        tk.deiconify()
        lw.destroy()
    bl2=Button(lw,text="Go back",padx=40,pady=10,command=go_back)

    t1.grid(row=0,column=0,sticky=W)
    e1.grid(row=1,column=0)
    t2.grid(row=2,column=0,sticky=W)
    e2.grid(row=3,column=0)
    bl1.grid(row=4,column=0)
    bl2.grid(row=5,column=0)








    

#REGISTER BUTTON
def reg():
    tk.withdraw()
    rw=Toplevel()
    rw.title("Register Window")
    rw.geometry("500x500")

    def reg_run():
            username=e1.get()
            password=e2.get()
            conpass=e3.get()
            phnumber=e4.get()
            email=e5.get()
            dob=e6.get()
            
            if password == conpass:
                df=pd.read_csv("logreg.csv")
                
                df2={"Username":username,
                     "Password":password,
                     "Phone Number":phnumber,
                     "Email ID":email,
                     "DOB":dob
                     }
                
                df=df.append(df2,ignore_index=True)
                df.to_csv("logreg.csv",index=False)

                messagebox.showinfo("REGISTERED","You have been Successfully Registered")

                rw.destroy()
                log()
                
            else:
                messagebox.showerror("ERROR","Password and Confirmation not Identical")



    e1=Entry(rw,width=35,borderwidth=5)
    t1=Label(rw,text="Enter Username:",font=("Arial Bold",15))
    e2=Entry(rw,width=35,borderwidth=5,show="*")
    t2=Label(rw,text="Enter Password:",font=("Arial Bold",15))
    e3=Entry(rw,width=35,borderwidth=5,show="*")
    t3=Label(rw,text="Confirm Password:",font=("Arial Bold",15))
    e4=Entry(rw,width=35,borderwidth=5)
    t4=Label(rw,text="Phone Number:",font=("Arial Bold",15))
    e5=Entry(rw,width=35,borderwidth=5)
    t5=Label(rw,text="Email ID:",font=("Arial Bold",15))
    e6=Entry(rw,width=35,borderwidth=5)
    t6=Label(rw,text="Date Of Birth:",font=("Arial Bold",15))

    br1 = Button(rw, text="Enter", padx=40, pady=10,command=reg_run)

    def rwback():
        tk.deiconify()
        rw.destroy()
        
    br2 = Button(rw, text="Go back", padx=40, pady=10, command=rwback)

    t1.grid(row=0, column=0,sticky=W)
    e1.grid(row=1, column=0)
    t2.grid(row=2, column=0,sticky=W)
    e2.grid(row=3, column=0)
    t3.grid(row=4,column=0,sticky=W)
    e3.grid(row=5,column=0)
    t4.grid(row=6,column=0,sticky=W)
    e4.grid(row=7,column=0)
    t5.grid(row=8,column=0,sticky=W)
    e5.grid(row=9,column=0)
    
    br1.grid(row=10, column=0)
    br2.grid(row=11, column=0)


#ADMIN LOGIN
def adm():
    tk.withdraw()
    ad=Toplevel()
    ad.title("Admin Login")
    ad.geometry("370x250")

    def admrun():
        if e1.get() == "Admin" :
            if e2.get() == "admin@123" :
                ad.destroy()

                #ADMIN WINDOW
                
                adm_pg=Toplevel()
                adm_pg.title("Admin Page")
                h1=Label(adm_pg,text="Welcome to the Admin Page",font=("Arial Bold",25))
                h2=Label(adm_pg,text="Select : ",font=("Arial Bold",15))
                sb1=Label(adm_pg,text="         ")
                
                
                def view():
                    adm_pg.withdraw()
                    vw=Toplevel()
                    vw.title("View Files")
                    vw.geometry("400x250")

                    h1=Label(vw,text="Select : ",font=("Arial Bold",25))
                    sb1=Label(vw,text="         ")

                    
                    def bc_adm():
                        vw.withdraw()
                        badm=Toplevel()
                        badm.title("Birth Certificate Files")
                        badm.geometry("370x250")

                        bh1=Label(badm,text="Choose User : ",font=("Arial Bold",15))

                        #Options--
                        a=[]
                        for i in bcsv["Name"]:
                            a.append(i)
                        options=a
                        
                        clkd=StringVar(badm)
                        clkd.set(options[0])
                        
                        dd1=OptionMenu(badm,clkd,*options)

                        def sl():
                            
                            name=clkd.get()
                            
                            bdf=bcsv.set_index(["Name"])
                            sl=Toplevel()
                            sl.title("Values")

                            text=Text(sl)
                            text.insert(INSERT,bdf.loc[name])
                            text.pack()

                        bb1=Button(badm,text="Select",padx=15,pady=5,command=sl)
                        def bck():
                            vw.deiconify()
                            badm.destroy()                           
                        bb2=Button(badm,text="Go Back",padx=15,pady=5,command=bck)

                        bh1.grid(row=0,sticky="W")
                        dd1.grid(row=1,column=0)
                        bb1.grid(row=1,column=1)
                        bb2.grid(row=2,column=0,sticky="W")

                    b1=Button(vw,text="Birth Certificate",padx=15,pady=5,command=bc_adm)

                    
                    def po_adm():
                        vw.withdraw()
                        padm=Toplevel()
                        padm.title("Birth Certificate Files")
                        padm.geometry("370x250")

                        ph1=Label(padm,text="Choose User : ",font=("Arial Bold",15))

                        #Options--
                        a=[]
                        for i in pcsv["Name Of Owner"]:
                            a.append(i)
                        options=a
                        
                        clkd=StringVar(padm)
                        clkd.set(options[0])
                        
                        dd1=OptionMenu(padm,clkd,*options)

                        def sl():
                            
                            name=clkd.get()
                            
                            pdf=pcsv.set_index(["Name Of Owner"])
                            sl=Toplevel()
                            sl.title("Values")

                            text=Text(sl)
                            text.insert(INSERT,pdf.loc[name])
                            text.pack()

                        pb1=Button(padm,text="Select",padx=15,pady=5,command=sl)
                        def bck():
                            vw.deiconify()
                            padm.destroy()                           
                        pb2=Button(padm,text="Go Back",padx=15,pady=5,command=bck)

                        ph1.grid(row=0,sticky="W")
                        dd1.grid(row=1,column=0)
                        pb1.grid(row=1,column=1)
                        pb2.grid(row=2,column=0,sticky="W")
                        
                    b2=Button(vw,text="Property Ownership",padx=15,pady=5,command=po_adm)
                    
                    def vp_adm():
                        vw.withdraw()
                        cadm=Toplevel()
                        cadm.title("Birth Certificate Files")
                        cadm.geometry("370x250")

                        ch1=Label(cadm,text="Choose User : ",font=("Arial Bold",15))

                        #Options--
                        a=[]
                        for i in ccsv["Owners Name"]:
                            a.append(i)
                        options=a
                        
                        clkd=StringVar(cadm)
                        clkd.set(options[0])
                        
                        dd1=OptionMenu(cadm,clkd,*options)

                        def sl():
                            
                            name=clkd.get()
                            
                            cdf=ccsv.set_index(["Owners Name"])
                            sl=Toplevel()
                            sl.title("Values")

                            text=Text(sl)
                            text.insert(INSERT,cdf.loc[name])
                            text.pack()

                        cb1=Button(cadm,text="Select",padx=15,pady=5,command=sl)
                        def bck():
                            vw.deiconify()
                            cadm.destroy()                           
                        cb2=Button(cadm,text="Go Back",padx=15,pady=5,command=bck)

                        ch1.grid(row=0,sticky="W")
                        dd1.grid(row=1,column=0)
                        cb1.grid(row=1,column=1)
                        cb2.grid(row=2,column=0,sticky="W")
                                                
                    b3=Button(vw,text="Vehical Ownership",padx=15,pady=5,command=vp_adm)

                                       
                    def bac():
                        vw.destroy()
                        adm_pg.deiconify()
                    b4=Button(vw,text="GO Back",padx=15,pady=5,comman=bac)

                    h1.grid(row=0,column=0,columnspan=2,sticky="W")
                    b1.grid(row=1,column=0)
                    b2.grid(row=1,column=1)
                    b3.grid(row=1,column=2)
                    sb1.grid(row=2,columnspan=2)
                    b4.grid(row=3,column=0,sticky="W")

                
                def add():
                    adm_pg.withdraw()
                    aw=Toplevel()
                    aw.title("Add Files")
                    aw.geometry("400x250")

                    h1=Label(aw,text="Select : ")
                    

                    def add_bc():
                        aw.withdraw()
                        adbc=Toplevel()
                        adbc.title("Add BirthCertificate")
                        #adbc.geometry()

                        h1=Label(adbc,text="Choose Name : ")

                        u1=Entry(adbc,width=35,borderwidth=5)

                        def select():
                            username=u1.get()
                            inpbc=Toplevel()
                            inpbc.title("Add Birth Certificate")
                            inpbc.geometry("400x350")

                            h1=Label(inpbc,text="Sex : ",font=("Arial Bold",))
                            h2=Label(inpbc,text="Date Of Birth : ",font=("Arial Bold",))
                            h3=Label(inpbc,text="Place Of Birth : ",font=("Arial Bold",))
                            h4=Label(inpbc,text="Name of Father : ",font=("Arial Bold",))
                            h5=Label(inpbc,text="Name of Mother : ",font=("Arial Bold",))
                            h6=Label(inpbc,text="Reg. No. : ",font=("Arial Bold",))
                            h7=Label(inpbc,text="Date of Reg. : ",font=("Arial Bold",))
                            h8=Label(inpbc,text="Date : ",font=("Arial Bold",))

                            e1=Entry(inpbc,width=35,borderwidth=5)
                            e2=Entry(inpbc,width=35,borderwidth=5)
                            e3=Entry(inpbc,width=35,borderwidth=5)
                            e4=Entry(inpbc,width=35,borderwidth=5)
                            e5=Entry(inpbc,width=35,borderwidth=5)
                            e6=Entry(inpbc,width=35,borderwidth=5)
                            e7=Entry(inpbc,width=35,borderwidth=5)
                            e8=Entry(inpbc,width=35,borderwidth=5)


                            def enter():
                                bcsv=pd.read_csv("BirthCertificate.csv")
                                df={"Name":username,"Sex":e1.get(),
                                    "Date Of Birth":e2.get(),
                                    "Place Of Birth":e3.get(),
                                    "Name of Father":e4.get(),
                                    "Name of Mother":e5.get(),
                                    "Registration No.":e6.get(),
                                    "Date of Registration":e7.get(),
                                    "Date":e8.get(),
                                    }
                                bcsv=bcsv.append(df,ignore_index=True)
                                bcsv.to_csv("BirthCertificate.csv",index=False)

                                mc=messagebox.showinfo("Done","Your data had been added")
                                inpbc.destroy()
                                adm_pg.deiconify()
                                
                            b1=Button(inpbc,text="Enter",command=enter)

                            def back():
                                inpbc.destroy()
                                adm_pg.deiconify()
                            b2=Button(inpbc,text="Go Back",command=back)
                            
                            #grid
                            
                            h1.grid(row=0,column=0,sticky="W")
                            e1.grid(row=0,column=1,sticky="W")
                            h2.grid(row=1,column=0,sticky="W")
                            e2.grid(row=1,column=1,sticky="W")
                            h3.grid(row=2,column=0,sticky="W")
                            e3.grid(row=2,column=1,sticky="W")
                            h4.grid(row=3,column=0,sticky="W")
                            e4.grid(row=3,column=1,sticky="W")
                            h5.grid(row=4,column=0,sticky="W")
                            e5.grid(row=4,column=1,sticky="W")
                            h6.grid(row=5,column=0,sticky="W")
                            e6.grid(row=5,column=1,sticky="W")
                            h7.grid(row=6,column=0,sticky="W")
                            e7.grid(row=6,column=1,sticky="W")
                            h8.grid(row=7,column=0,sticky="W")
                            e8.grid(row=7,column=1,sticky="W")
                            b1.grid(row=8,sticky="W")
                            b2.grid(row=9,sticky="W")
            
                        b1=Button(adbc,text="Select",padx=15,pady=5,command=select)

                        def back():
                            adbc.destroy()
                            aw.deiconify()
                        b2=Button(adbc,text="Go Back",padx=15,pady=5,command=back)

                        h1.grid(row=0,sticky="W")
                        u1.grid(row=1,column=0,sticky="W")
                        b1.grid(row=1,column=1)
                        b2.grid(row=2,sticky="W")
                        
                    b1=Button(aw,text="Birth Certificate",padx=15,pady=5,command=add_bc)
                    

                    def add_po():
                        aw.withdraw()
                        adpo=Toplevel()
                        adpo.title("Add Property ownership")
                        #adpo.geometry()

                        h1=Label(adpo,text="Choose Name : ")

                        u1=Entry(adpo,width=35,borderwidth=5)

                        def select():
                            username=u1.get()
                            adpo.withdraw()
                            inppo=Toplevel()
                            inppo.title("Add Property Ownership")
                            inppo.geometry("400x350")

                            h1=Label(inppo,text="Name Of Previous Owner : ",font=("Arial Bold",))
                            h2=Label(inppo,text="State : ",font=("Arial Bold",))
                            h3=Label(inppo,text="District : ",font=("Arial Bold",))
                            h4=Label(inppo,text="Address : ",font=("Arial Bold",))
                            h5=Label(inppo,text="Postal Code : ",font=("Arial Bold",))
                            h6=Label(inppo,text="Landmark : ",font=("Arial Bold",))
                            h7=Label(inppo,text="Date Of Registration : ",font=("Arial Bold",))

                            e1=Entry(inppo,width=35,borderwidth=5)
                            e2=Entry(inppo,width=35,borderwidth=5)
                            e3=Entry(inppo,width=35,borderwidth=5)
                            e4=Entry(inppo,width=35,borderwidth=5)
                            e5=Entry(inppo,width=35,borderwidth=5)
                            e6=Entry(inppo,width=35,borderwidth=5)
                            e7=Entry(inppo,width=35,borderwidth=5)
                            
                            def enter():
                                pcsv=pd.read_csv("PropertyOwnership.csv")
                                df={"Name Of Owner":username,
                                    "Name Of Previous Owner":e1.get(),
                                    "State":e2.get(),
                                    "District":e3.get(),
                                    "Address":e4.get(),
                                    "Postal Code":e5.get(),
                                    "Landmark":e6.get(),
                                    "Date Of Registration":e7.get(),
                                    }
                                pcsv=pcsv.append(df,ignore_index=True)
                                pcsv.to_csv("PropertyOwnership.csv",index=False)

                                mc=messagebox.showinfo("Done","Your data had been added")
                                inppo.destroy()
                                adm_pg.deiconify()
                                
                            b1=Button(inppo,text="Enter",command=enter)

                            def back():
                                inppo.destroy()
                                adm_pg.deiconify()
                            b2=Button(inppo,text="Go Back",command=back)
                            
                            #grid
                            
                            h1.grid(row=0,column=0,sticky="W")
                            e1.grid(row=0,column=1,sticky="W")
                            h2.grid(row=1,column=0,sticky="W")
                            e2.grid(row=1,column=1,sticky="W")
                            h3.grid(row=2,column=0,sticky="W")
                            e3.grid(row=2,column=1,sticky="W")
                            h4.grid(row=3,column=0,sticky="W")
                            e4.grid(row=3,column=1,sticky="W")
                            h5.grid(row=4,column=0,sticky="W")
                            e5.grid(row=4,column=1,sticky="W")
                            h6.grid(row=5,column=0,sticky="W")
                            e6.grid(row=5,column=1,sticky="W")
                            h7.grid(row=6,column=0,sticky="W")
                            e7.grid(row=6,column=1,sticky="W")
                            b1.grid(row=7,sticky="W")
                            b2.grid(row=8,sticky="W")

                        b1=Button(adpo,text="Select",padx=15,pady=5,command=select)

                        def back():
                            adpo.destroy()
                            aw.deiconify()
                        b2=Button(adpo,text="Go Back",padx=15,pady=5,command=back)

                        h1.grid(row=0,sticky="W")
                        u1.grid(row=1,column=0,sticky="W")
                        b1.grid(row=1,column=1)
                        b2.grid(row=2,sticky="W")
                        
                    b2=Button(aw,text="Property Ownership",padx=15,pady=5,command=add_po)
                    

                    def add_vo():
                        aw.withdraw()
                        advo=Toplevel()
                        advo.title("Add Property ownership")
                        #advo.geometry()

                        h1=Label(advo,text="Choose Name : ")

                        u1=Entry(advo,width=35,borderwidth=5)

                        def select():
                            username=u1.get()
                            advo.withdraw()
                            inpvo=Toplevel()
                            inpvo.title("Add Vehical Ownership")
                            inpvo.geometry("400x350")

                            h1=Label(inpvo,text="Company Name : ",font=("Arial Bold",))
                            h2=Label(inpvo,text="Dealership Name : ",font=("Arial Bold",))
                            h3=Label(inpvo,text="Dealership Number : ",font=("Arial Bold",))
                            h4=Label(inpvo,text="Car Model : ",font=("Arial Bold",))
                            h5=Label(inpvo,text="Fuel Type : ",font=("Arial Bold",))
                            h6=Label(inpvo,text="Stock Colour : ",font=("Arial Bold",))
                            h7=Label(inpvo,text="Licence Plate : ",font=("Arial Bold",))
                            h8=Label(inpvo,text="Reg. Date : ",font=("Arial Bold",))
                            h9=Label(inpvo,text="Safety Measures  : ",font=("Arial Bold",))

                            e1=Entry(inpvo,width=35,borderwidth=5)
                            e2=Entry(inpvo,width=35,borderwidth=5)
                            e3=Entry(inpvo,width=35,borderwidth=5)
                            e4=Entry(inpvo,width=35,borderwidth=5)
                            e5=Entry(inpvo,width=35,borderwidth=5)
                            e6=Entry(inpvo,width=35,borderwidth=5)
                            e7=Entry(inpvo,width=35,borderwidth=5)
                            e8=Entry(inpvo,width=35,borderwidth=5)
                            e9=Entry(inpvo,width=35,borderwidth=5)


                            def enter():
                                ccsv=pd.read_csv("VehicalOwnership.csv")
                                df={"Name":username,
                                    "Company Name":e1.get(),
                                    "Dealership Name":e2.get(),
                                    "Dealership Number":e3.get(),
                                    "Car Model":e4.get(),
                                    "Fuel Type":e5.get(),
                                    "Stock Colour":e6.get(),
                                    "Licence Plate":e7.get(),
                                    "Reg. Date":e8.get(),
                                    "Safety Measures":e9.get()
                                    }
                                ccsv=ccsv.append(df,ignore_index=True)
                                ccsv.to_csv("VehicalOwnership.csv",index=False)

                                mc=messagebox.showinfo("Done","Your data had been added")
                                inpvo.destroy()
                                adm_pg.deiconify()
                                
                            b1=Button(inpvo,text="Enter",command=enter)

                            def back():
                                inpvo.destroy()
                                adm_pg.deiconify()
                            b2=Button(inpvo,text="Go Back",command=back)
                            
                            #grid
                            
                            h1.grid(row=0,column=0,sticky="W")
                            e1.grid(row=0,column=1,sticky="W")
                            h2.grid(row=1,column=0,sticky="W")
                            e2.grid(row=1,column=1,sticky="W")
                            h3.grid(row=2,column=0,sticky="W")
                            e3.grid(row=2,column=1,sticky="W")
                            h4.grid(row=3,column=0,sticky="W")
                            e4.grid(row=3,column=1,sticky="W")
                            h5.grid(row=4,column=0,sticky="W")
                            e5.grid(row=4,column=1,sticky="W")
                            h6.grid(row=5,column=0,sticky="W")
                            e6.grid(row=5,column=1,sticky="W")
                            h7.grid(row=6,column=0,sticky="W")
                            e7.grid(row=6,column=1,sticky="W")
                            h8.grid(row=7,column=0,sticky="W")
                            e8.grid(row=7,column=1,sticky="W")
                            b1.grid(row=8,sticky="W")
                            b2.grid(row=9,sticky="W")
                            
                        b1=Button(advo,text="Select",padx=15,pady=5,command=select)

                        def back():
                            advo.destroy()
                            aw.deiconify()
                        b2=Button(advo,text="Go Back",padx=15,pady=5,command=back)

                        h1.grid(row=0,sticky="W")
                        u1.grid(row=1,column=0,sticky="W")
                        b1.grid(row=1,column=1)
                        b2.grid(row=2,sticky="W")
                        
                    b3=Button(aw,text="Vechial Ownership",padx=15,pady=5,command=add_vo)
                    

                    def back():
                        aw.destroy()
                        adm_pg.deiconify()

                    b4=Button(aw,text="Go Back",padx=15,pady=5,command=back)

                    h1.grid(row=0,columnspan=5,sticky="W")
                    b1.grid(row=1,column=0)
                    b2.grid(row=1,column=1)
                    b3.grid(row=1,column=2)
                    b4.grid(row=2,sticky="W")

                
                def delete():
                    adm_pg.withdraw()
                    dw=Toplevel()
                    dw.title("Delete Files")
                    dw.geometry("435x150")

                    h1=Label(dw,text="Choose File to Delete : ")
                    
                    def del_bc():
                        dw.withdraw()
                        delbc=Toplevel()
                        delbc.title("Delete Birth Certificate")
                        delbc.geometry("220x150")

                        h1=Label(delbc,text="Select Name : ")
                        #Options--
                        a=[]
                        for i in bcsv["Name"]:
                            a.append(i)
                        options=a
                        
                        clkd=StringVar(delbc)
                        clkd.set(options[0])
                        
                        om=OptionMenu(delbc,clkd,*options)

                        def sel():
                            bdf=bcsv.set_index(["Name"])
                            mb=messagebox.askquestion("Delete","Are you sure you want to Delete this file")
                            if mb == "yes":
                                name=clkd.get()
                                bdf.drop([name],inplace=True)
                                bdf.to_csv("BirthCertificate.csv")
                                delbc.destroy()
                                dw.deiconify()
                        b1=Button(delbc,text="Select",padx=15,pady=5,command=sel)
                        def bak():
                            delbc.destroy()
                            dw.deiconify()
                        b2=Button(delbc,text="Go Back",padx=15,pady=5,command=bak)

                        h1.grid(row=0,columnspan=5,sticky="W")
                        om.grid(row=1,column=0)
                        b1.grid(row=1,column=1)
                        b2.grid(row=3)
                        
                    b1=Button(dw,text="Birth Certificate : ",padx=15,pady=5,command=del_bc)
                    
                    def del_po():
                        dw.withdraw()
                        delpo=Toplevel()
                        delpo.title("Delete Birth Certificate")
                        delpo.geometry("220x150")

                        h1=Label(delpo,text="Select Name : ")
                        #Options--
                        a=[]
                        for i in pcsv["Name Of Owner"]:
                            a.append(i)
                        options=a
                        
                        clkd=StringVar(delpo)
                        clkd.set(options[0])
                        
                        om=OptionMenu(delpo,clkd,*options)

                        def sel():
                            pdf=pcsv.set_index(["Name Of Owner"])
                            mb=messagebox.askquestion("Delete","Are you sure you want to Delete this file")
                            if mb == "yes":
                                name=clkd.get()
                                pdf.drop([name],inplace=True)
                                pdf.to_csv("PropertyOwnership.csv")
                                delpo.destroy()
                                dw.deiconify()
                        b1=Button(delpo,text="Select",padx=15,pady=5,command=sel)
                        def bak():
                            delpo.destroy()
                            dw.deiconify()
                        b2=Button(delpo,text="Go Back",padx=15,pady=5,command=bak)

                        h1.grid(row=0,columnspan=5,sticky="W")
                        om.grid(row=1,column=0)
                        b1.grid(row=1,column=1)
                        b2.grid(row=3)
                        
                    b2=Button(dw,text="Property Ownership : ",padx=15,pady=5,command=del_po)
                    
                    def del_vo():
                        dw.withdraw()
                        delvo=Toplevel()
                        delvo.title("Delete Birth Certificate")
                        delvo.geometry("220x150")

                        h1=Label(delvo,text="Select Name : ")
                        #Options--
                        a=[]
                        for i in ccsv["Owners Name"]:
                            a.append(i)
                        options=a
                        
                        clkd=StringVar(delvo)
                        clkd.set(options[0])
                        
                        om=OptionMenu(delvo,clkd,*options)

                        def sel():
                            cdf=ccsv.set_index(["Owners Name"])
                            mb=messagebox.askquestion("Delete","Are you sure you want to Delete this file")
                            if mb == "yes":
                                name=clkd.get()
                                cdf.drop([name],inplace=True)
                                cdf.to_csv("VehicalOwnership.csv")
                                delvo.destroy()
                                dw.deiconify()
                        b1=Button(delvo,text="Select",padx=15,pady=5,command=sel)
                        def bak():
                            delvo.destroy()
                            dw.deiconify()
                        b2=Button(delvo,text="Go Back",padx=15,pady=5,command=bak)

                        h1.grid(row=0,columnspan=5,sticky="W")
                        om.grid(row=1,column=0)
                        b1.grid(row=1,column=1)
                        b2.grid(row=3)
                        
                    b3=Button(dw,text="Vechical Ownership : ",padx=15,pady=5,command=del_vo)
                    
                    def back():
                        dw.destroy()
                        adm_pg.deiconify()
                    b4=Button(dw,text="Go Back",padx=10,pady=5,command=back)

                    h1.grid(row=0,columnspan=5,sticky="W")
                    b1.grid(row=1,column=0)
                    b2.grid(row=1,column=1)
                    b3.grid(row=1,column=2)
                    b4.grid(row=2,sticky="W")
               
                b1=Button(adm_pg,text="View",padx=15,pady=5,command=view)
                b2=Button(adm_pg,text="Add",padx=25,pady=5,command=add)
                b3=Button(adm_pg,text="Delete",padx=25,pady=5,command=delete)

                def gb():
                    
                    adm_pg.destroy()
                    tk.deiconify()
                                  
                b4=Button(adm_pg,text="Log Out",padx=25,pady=5,command=gb)
                
                h1.grid(row=0,columnspan=7)
                h2.grid(row=1,column=0,sticky="W")
                b1.grid(row=1,column=1)
                b2.grid(row=1,column=2)
                b3.grid(row=1,column=3)
                sb1.grid(row=2,columnspan=7)
                b4.grid(row=3,sticky="W")

            else:
                messagebox.showerror("Incorrect","Username Or Password is Incorrect")



    e1=Entry(ad,width=35,borderwidth=5)
    t1=Label(ad,text="Enter Username:",font=("Arial Bold",15))
    e2=Entry(ad,width=35,borderwidth=5,show="*")
    t2=Label(ad,text="Enter Password:",font=("Arial Bold",15))

    br1 = Button(ad, text="Enter", padx=40, pady=10,command=admrun)

    def adback():
        tk.deiconify()
        ad.destroy()
        
    br2 = Button(ad, text="Go back", padx=40, pady=10, command=adback)

    t1.grid(row=0, column=0,sticky=W)
    e1.grid(row=1, column=0)
    t2.grid(row=2, column=0,sticky=W)
    e2.grid(row=3, column=0)
    br1.grid(row=4, column=0)
    br2.grid(row=5, column=0)


#FIRST WINDOW
tk=Tk()
tk.title("TITLE PAGE")
tk.geometry("370x250")

h1=tki.Label(tk,text="Welcome to our Home Page",font=("Arial Bold",20))
h1.grid(row=0,column=0,columnspan=5)
h2=tki.Label(tk,text="                        ",font=("Arial Bold",15))
h2.grid(row=6,column=0,columnspan=5)


b1=Button(tk,text=" Login   ",padx=40,pady=10,command=log)
b2=Button(tk,text="Register",padx=40,pady=10,command=reg)
b3=Button(tk,text=" ADMIN",padx=40,pady=10,command=adm)
b4=Button(tk,text=" EXIT   ",padx=40,pady=10,command=ex )

b1.grid(row=3,column=2,columnspan=1)
b2.grid(row=4,column=2,columnspan=1)
b3.grid(row=5,column=2,columnspan=1)
b4.grid(row=7,column=2,columnspan=1)

tk.mainloop()


