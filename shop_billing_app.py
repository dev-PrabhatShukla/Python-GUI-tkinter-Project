from tkinter import *

import random

import math

from tkinter import messagebox

top=Tk()

top.geometry("1350x700+0+0")

top.title("Sales Shopping Mall Software")

title=Label(top,text="SHOPPING MALL",bd=10,bg="powder blue",fg="black",pady=2,font="lucida 50 bold")

title.pack(fill=X)

#==define and calculate======

#define generate bill=========

def welcome_bill():

	textarea.delete('1.0',END)	textarea.insert(END,"\t Welcome On Prabhat's Retail")

	textarea.insert(END,f"\n Bill Number : {Bill_No.get()}")

	textarea.insert(END,f"\n Customer Name : {Customer_Name.get()}")

	textarea.insert(END,f"\n Contact Number : {Customer_Phone.get()}")

	

	textarea.insert(END,f"\n =================")

	

	textarea.insert(END,f"\n Products \t\t QTY \t\t Price")

	

	textarea.insert(END,f"\n =================")

	

#defining bill area	

	

def bill_area():

	if Customer_Name.get()=="" or Customer_Phone.get()=="" :

		messagebox.showerror("Error","Customer details are must")

	else:

		welcome_bill()

		#Now set everything of each section in the bill product name quantity and price

		#Set it for mens starts

		if SShirts.get()!=0:

			textarea.insert(END,f"\n Sleeves Shirts \t\t{SShirts.get()}\t\t{float(SShirts.get())*590}")

		if Jeans.get()!=0:

			textarea.insert(END,f"\n Jeans \t\t{Jeans.get()}\t\t{float(Jeans.get())*800}")

		if MShoes.get()!=0:

			textarea.insert(END,f"\n Men Shoes\t\t{MShoes.get()}\t\t{float(MShoes.get())*800}")

		if MWatches.get()!=0:

			textarea.insert(END,f"\n Men Watches \t\t{MWatches.get()}\t\t{float(MWatches.get())*2200}")

				

		if TShirts.get()!=0:

			textarea.insert(END,f"\n Men T-shirts \t\t{TShirts.get()}\t\t{float(TShirts.get())*400}")

		if Wax.get()!=0:

			textarea.insert(END,f"\n Wax \t\t{Wax.get()}\t\t{float(Wax.get())*120}")

		if Glass.get()!=0:

			textarea.insert(END,f"\n Sun Glasses \t\t{Glass.get()}\t\t{float(Glass.get())*300}")

		#Set it for mens close

		#Set it for womens starts

		

		if SalwarSuit.get()!=0:

			textarea.insert(END,f"\n Salwar suits \t\t{SalwarSuit.get()}\t\t{float(SalwarSuit.get())*800}")

		if Saree.get()!=0:

			textarea.insert(END,f"\n Saree\t\t{Saree.get()}\t\t{float(Saree.get())*1800}")

		if Tops.get()!=0:

			textarea.insert(END,f"\n Tops \t\t{Tops.get()}\t\t{float(Tops.get())*600}")

		if WWatches.get()!=0:

			textarea.insert(END,f"\n Women Watches \t\t{WWatches.get()}\t\t{float(WWatches.get())*1700}")

			

		if Jewellery.get()!=0:

			textarea.insert(END,f"\n Jewellery \t\t{Jewellery.get()}\t\t{float(Jewellery.get())*7000}")

			

		if WShoes.get()!=0:

			textarea.insert(END,f"\n Women Shoes \t\t{WShoes.get()}\t\t{float(WShoes.get())*600}")

		if Cosmatics.get()!=0:

			textarea.insert(END,f"\n Cosmatics \t\t{Cosmatics.get()}\t\t{float(Cosmatics.get())*300}")

			

		#Set it for women closes

		

		#Set it for kids starts

		

		if Toys.get()!=0:

			textarea.insert(END,f"\n Kids Toys \t\t{Toys.get()}\t\t{float(Toys.get())*300}")

		if Games.get()!=0:

			textarea.insert(END,f"\n  Kids Games \t\t{Games.get()}\t\t{float(Games.get())*600}")

		if Frocks.get()!=0:

			textarea.insert(END,f"\n Frocks \t\t{Frocks.get()}\t\t{float(Frocks.get())*800}")

			

		if Soap.get()!=0:

			textarea.insert(END,f"\n Soaps \t\t{Soap.get()}\t\t{float(Soap.get())*40}")

		if Books.get()!=0:

			textarea.insert(END,f"\n Books \t\t{Books.get()}\t\t{float(Books.get())*60}")

			

		if HairOil.get()!=0:

			textarea.insert(END,f"\n Hair Oil \t\t{HairOil.get()}\t\t{float(HairOil.get())*120}")

		if LunchBox.get()!=0:

			textarea.insert(END,f"\n Lunch Box \t\t{LunchBox.get()}\t\t{float(LunchBox.get())*240}")

		#Set it for kids close

		

		textarea.insert(END,f"\n--------------------")

		#Adding tax in bill area starts

		

		if Mens_Tax.get()!=" Rs.0.00":

			textarea.insert(END,f" \n Tax on mens product\t\t\t{Mens_Tax.get()}")

		

		if Womens_Tax.get()!=" Rs.0.00":

			textarea.insert(END,f" \n Tax on womens product\t\t\t{Womens_Tax.get()}")

			

		if Kids_Tax.get()!=" Rs.0.00":

			textarea.insert(END,f" \n Tax on kids product\t\t\t{Kids_Tax.get()}")

		#Adding tax in bill area ends

		

		textarea.insert(END,f"\n--------------------")

		

		textarea.insert(END,f"\n--------------------")

		

		M1=float(SShirts.get())*590

		M2=float(Jeans.get())*800

		M3=float(MShoes.get())*800

		M4=float(MWatches.get())*2200

		M5=float(TShirts.get())*400

		M6=float(Wax.get())*120

		M7=float(Glass.get())*300

		

		W1=float(SalwarSuit.get())*800

		W2=float(Saree.get())*1800

		W3=float(WShoes.get())*600

		W4=float(Tops.get())*600

		W5=float(WWatches.get())*1700

		W6=float(Jewellery.get())*7000

		W7=float(Cosmatics.get())*300

		

		K1=float(Toys.get())*300

		K2=float(Games.get())*600

		K3=float(Frocks.get())*800

		K4=float(Books.get())*60

		K5=float(Soap.get())*40

		K6=float(HairOil.get())*120

		K7=float(LunchBox.get())*240

		

		Total_Billl=(M1+M2+M3+M4+M5+M6+M7)+((M1+M2+M3+M4+M5+M6+M7)*0.2)+(W1+W2+W3+W4+W5+W6+W7)+((W1+W2+W3+W4+W5+W6+W7)*0.1)+(K1+K2+K3+K4+K5+K6+K7)+((K1+K2+K3+K4+K5+K6+K7)*0.05)

		textarea.insert(END,f" \n Total Bill \t\t\t{Total_Billl}")

		

#def clear=======

def clear():

	op=messagebox.askyesno("Clear","Do you really want to exit? ")

	if op>0:

		SShirts.set("")

		Jeans.set("")

		MShoes.set("")

		MWatches.set("")

		TShirts.set("")

		Wax.set("")

		Glass.set("")

		#Womens

		SalwarSuit.set("")

		Saree.set("")

		Tops.set("")

		WWatches.set("")

		Jewellery.set("")

		WShoes.set("")

		Cosmatics.set("")

		#Kids

		Toys.set("")

		Games.set("")

		Frocks.set("")

		Soap.set("")

		Books.set("")

		HairOil.set("")

		LunchBox.set("")

		Total_Mens_Price.set("")

		Total_Womens_Price.set("")

		Total_Kids_Price.set("")

		Mens_Tax.set("")

		Womens_Tax.set("")

		Kids_Tax.set("")

		#Customer 

		Customer_Name.set("")

		Customer_Phone.set("")

		Bill_No.set("")	

def quitApp ():

	op=messagebox.askyesno("Exit","Do you really want to exit ? ")

	if op>0:

		top.destroy()

def total ():

	#converting variables in floating no.

	Pshirts=float(SShirts.get())

	Pjeans=float(Jeans.get())

	Pmshoes=float(MShoes.get())

	Pmwatches=float(MWatches.get())

	Ptshirts=float(TShirts.get())

	Pwax=float(Wax.get())

	Pglass=float(Glass.get())

	Psalwarsuit=float(SalwarSuit.get())

	Psaree=float(Saree.get())

	Ptops=float(Tops.get())

	Pwwatches=float(WWatches.get())

	Pjewellery=float(Jewellery.get())

	Pwshoes=float(WShoes.get())

	Pcosmatics=float(Cosmatics.get())

	Ptoys=float(Toys.get())

	Pgames=float(Games.get())

	Pfrocks=float(Frocks.get())

	Pbooks=float(Books.get())

	Psoap=float(Soap.get())

	Phairoil=float(HairOil.get())

	Plunchbox=float(LunchBox.get())

	

	#Apply cost in it

	NPshirts=Pshirts*590

	NPjeans=Pjeans*800

	NPmshoes=Pmshoes*800

	NPmwatches=Pmwatches*2200

	NPtshirts=Ptshirts*400

	NPwax=Pwax*120

	NPglass=Pglass*300

	NPsalwarsuit=Psalwarsuit*800

	NPsaree=Psaree*1800

	NPtops=Ptops*600

	NPwwatches=Pwwatches*1700

	NPjewellery=Pjewellery*7000

	NPwshoes=Pwshoes*600

	NPcosmatics=Pcosmatics*300

	NPtoys=Ptoys*300

	NPgames=Pgames*600

	NPfrocks=Pfrocks*800

	NPbooks=Pbooks*60

	NPsoap=Psoap*40

	NPhairoil=Phairoil*120

	NPlunchbox=Plunchbox*240

	#Now main calculation

	#Calculating price for each section is start now

	Tmc=(NPshirts+NPjeans+NPmshoes+NPmwatches+NPtshirts+NPwax+NPglass)

	

	Totalmc="Rs.",str('%.2f' %(Tmc) )

	

	Twc=(NPsalwarsuit+NPsaree+NPtops+NPwwatches+NPjewellery+NPwshoes+NPcosmatics)

			

	Totalwc="Rs.",str('%.2f' %(Twc) )

	

	Tkc=(NPtoys+NPgames+NPfrocks+NPbooks+NPsoap+NPhairoil+NPlunchbox)

	

	Totalkc="Rs.",str('%.2f' % (Tkc))

	

	#Calculating price for each section ends

	

	#Now calculating tax foreach setions

	Tmt=((NPshirts+NPjeans+NPmshoes+NPmwatches+NPtshirts+NPwax+NPglass)*0.2)

	

	Totalmt="Rs.",str('%.2f' %(Tmt) )

	

	Twt=((NPsalwarsuit+NPsaree+NPtops+NPwwatches+NPjewellery+NPwshoes+NPcosmatics)*0.1)

	

	Totalwt="Rs.",str('%.2f' % (Twt))

	

	Tkt=((NPtoys+NPgames+NPfrocks+NPbooks+NPsoap+NPhairoil+NPlunchbox)*0.05)

	

	Totalkt="Rs.",str('%.2f' %(Tkt) )

	

	#calculation tax is ends here

	

	 #setting the price in box start		

	Total_Mens_Price.set(Totalmc)

			

	Total_Womens_Price.set(Totalwc)

	

	Total_Kids_Price.set(Totalkc)

	

	#setting the price ends

	

	#setting tax starts

	

	Mens_Tax.set(Totalmt)

	Womens_Tax.set(Totalwt)

	Kids_Tax.set(Totalkt)

        

        # setting tax ends

	

					

#======Variables====

#======Mens====

SShirts=IntVar()

Jeans=IntVar()

MShoes=IntVar()

MWatches=IntVar()

TShirts=IntVar()

Wax=IntVar()

Glass=IntVar()

#======Womens===

SalwarSuit=IntVar()

Saree=IntVar()

Tops=IntVar()

WWatches=IntVar()

Jewellery=IntVar()

WShoes=IntVar()

Cosmatics=IntVar()

		

#========Kids======

Toys=IntVar()

Games=IntVar()

Frocks=IntVar()

Soap=IntVar()

Books=IntVar()

HairOil=IntVar()

LunchBox=IntVar()

Total_Mens_Price=StringVar()

Total_Womens_Price=StringVar()

Total_Kids_Price=StringVar()

Mens_Tax=StringVar()

Womens_Tax=StringVar()

		

Kids_Tax=StringVar()

#===Customer Info===

Customer_Name=StringVar()

Customer_Phone=StringVar()

Bill_No=StringVar()

#now generating a bill no.here

x=random.randint(1000,9999)

Bill_No.set(str(x))

Search_Bill=StringVar

		

#Customer details frame

		

F1=LabelFrame(top,text="Customer Details",font="lucida 20 bold",fg="red",bg="powder blue",bd=20,relief=SUNKEN)

F1.place(x=0,y=110)

		

#Frame 1 starts

		

#Customer name

		

cnamelbl=Label(F1,text="Customer Name",font="lucida 15 bold",bg="powder blue",fg="black")

cnamelbl.grid(row=0,column=0,padx=20,pady=5)

		

cnametxt=Entry(F1,font="lucida 10 bold",bd=8,width=15,textvariable=Customer_Name)

cnametxt.grid(row=0,column=1,padx=10,pady=5)

#Customer phone no

cphonelbl=Label(F1,text="Contact number",font="lucida 15 bold",bg="powder blue",fg="black")

cphonelbl.grid(row=0,column=2,padx=20,pady=5)

cphonetxt=Entry(F1,font="lucida 10 bold",bd=8,width=15,textvariable=Customer_Phone)

cphonetxt.grid(row=0,column=3,padx=10,pady=5)

		

#Bill number

		

cbilllbl=Label(F1,text="Bill No.",font="lucida 12 bold",bg="powder blue",fg="black")

cbilllbl.grid(row=0,column=4,padx=20,pady=5)

		

cbilltxt=Entry(F1,font="lucida 10 bold",bd=8,width=15,textvariable=Bill_No)

cbilltxt.grid(row=0,column=5,padx=10,pady=5)

		

#Search button

		

searchbtn=Button(F1,text="Search",font="lucida 12",bd=10,width=15)

searchbtn.grid(row=0,column=6,padx=10,pady=10)

#Frame1 closes

		

#Frame 2 starts

		

F2=LabelFrame(top,text="Mens",font="lucida 15 bold",fg="red",bg="powder blue",bd=10,relief=SUNKEN)

F2.place(x=5,y=230,height=380,width=350)

		

#Mens frame starts now

#Shirt

shirtlbl=Label(F2,text="Sleeves Shirts",font="lucida 12 bold",bg="powder blue",fg="black")

shirtlbl.grid(row=0,column=0,padx=2,pady=2)

shirttxt=Entry(F2,font="lucida 10 bold",bd=5,width=15,textvariable=SShirts)

shirttxt.grid(row=0,column=1,padx=2,pady=2)

#jeans

jeanslbl=Label(F2,text="Jeans",font="lucida 12 bold",bg="powder blue",fg="black")

jeanslbl.grid(row=1,column=0,padx=2,pady=2)

jeanstxt=Entry(F2,font="lucida 10 bold",bd=5,width=15,textvariable=Jeans)

jeanstxt.grid(row=1,column=1,padx=2,pady=2)

		

#Shoes

		

shoeslbl=Label(F2,text="Shoes",font="lucida 12 bold",bg="powder blue",fg="black")

shoeslbl.grid(row=2,column=0,padx=2,pady=2)

		

shoestxt=Entry(F2,font="lucida 10 bold",bd=5,width=15,textvariable=MShoes)

shoestxt.grid(row=2,column=1,padx=2,pady=2)

		

#Watches

		

watcheslbl=Label(F2,text="Watches",font="lucida 12 bold",bg="powder blue",fg="black")

watcheslbl.grid(row=3,column=0,padx=2,pady=2)

watchestxt=Entry(F2,font="lucida 10 bold",bd=5,width=15,textvariable=MWatches)

watchestxt.grid(row=3,column=1,padx=2,pady=2)

		

#tshirts

tshirtslbl=Label(F2,text="T-Shirts",font="lucida 12 bold",bg="powder blue",fg="black")

tshirtslbl.grid(row=4,column=0,padx=2,pady=2)

		

tshirtstxt=Entry(F2,font="lucida 10 bold",bd=5,width=15,textvariable=TShirts)

tshirtstxt.grid(row=4,column=1,padx=2,pady=2)

		

#Hairwax

waxlbl=Label(F2,text="Hair wax",font="lucida 12 bold",bg="powder blue",fg="black")

waxlbl.grid(row=5,column=0,padx=2,pady=2)

		

waxtxt=Entry(F2,font="lucida 10 bold",bd=5,width=15,textvariable=Wax)

waxtxt.grid(row=5,column=1,padx=2,pady=2)

		

#Sunglasses

glasslbl=Label(F2,text="Sun glasses",font="lucida 12 bold",bg="powder blue",fg="black")

glasslbl.grid(row=6,column=0,padx=2,pady=2)

		

glasstxt=Entry(F2,font="lucida 10 bold",bd=5,width=15,textvariable=Glass)

glasstxt.grid(row=6,column=1,padx=2,pady=2)

		

#Mens Frames Ends Now

		

#Frame 2 close

		

#Frame 3 starts now

		

F3=LabelFrame(top,text="Womens",font="lucida 15 bold",fg="red",bg="powder blue",bd=10,relief=SUNKEN)

F3.place(x=355,y=230,height=380,width=350)

		

#Womens Frame Start

#Salwarsuit

salwarsuitlbl=Label(F3,text="Salwarsuit",font="lucida 12 bold",bg="powder blue",fg="black")

salwarsuitlbl.grid(row=0,column=0,padx=10,pady=2)

		

salwarsuittxt=Entry(F3,font="lucida 10 bold",bd=5,width=15,textvariable=SalwarSuit)

salwarsuittxt.grid(row=0,column=1,padx=5,pady=2)

		

#Saree

sareelbl=Label(F3,text="Saree",font="lucida 12 bold",bg="powder blue",fg="black")

sareelbl.grid(row=1,column=0,padx=10,pady=2)

		

sareetxt=Entry(F3,font="lucida 10 bold",bd=5,width=15,textvariable=Saree)

sareetxt.grid(row=1,column=1,padx=5,pady=2)

		

#tops

		

toplbl=Label(F3,text="Tops",font="lucida 12 bold",bg="powder blue",fg="black")

toplbl.grid(row=2,column=0,padx=10,pady=2)

		

toptxt=Entry(F3,font="lucida 10 bold",bd=5,width=15,textvariable=Tops)

toptxt.grid(row=2,column=1,padx=5,pady=2)

		

#watches

		

wwatcheslbl=Label(F3,text="Watches",font="lucida 12 bold",bg="powder blue",fg="black")

wwatcheslbl.grid(row=3,column=0,padx=10,pady=2)

		

wwatchestxt=Entry(F3,font="lucida 10 bold",bd=5,width=15,textvariable=WWatches)

wwatchestxt.grid(row=3,column=1,padx=5,pady=2)

		

#Jewellery

		

jewellerylbl=Label(F3,text="Jewellery",font="lucida 12 bold",bg="powder blue",fg="black")

jewellerylbl.grid(row=4,column=0,padx=10,pady=2)

		

jewellerytxt=Entry(F3,font="lucida 10 bold",bd=5,width=15,textvariable=Jewellery)

		

jewellerytxt.grid(row=4,column=1,padx=5,pady=2)

		

#shoes

		

shoeslbl=Label(F3,text="Shoes",font="lucida 12 bold",bg="powder blue",fg="black")

shoeslbl.grid(row=5,column=0,padx=10,pady=2)

		

shoestxt=Entry(F3,font="lucida 10 bold",bd=5,width=15,textvariable=WShoes)

shoestxt.grid(row=5,column=1,padx=5,pady=2)

		

#Cosmatics

cosmaticlbl=Label(F3,text="Cosmatics",font="lucida 12 bold",bg="powder blue",fg="black")

cosmaticlbl.grid(row=6,column=0,padx=10,pady=2)

		

cosmatictxt=Entry(F3,font="lucida 10 bold",bd=5,width=15,textvariable=Cosmatics)

cosmatictxt.grid(row=6,column=1,padx=5,pady=2)

#Womens Frame Ends

#Frame 3 Ends

		

#Frame 4 starts

F4=LabelFrame(top,text="Kids",font="lucida 15 bold",fg="red",bg="powder blue",bd=10,relief=SUNKEN)

F4.place(x=700,y=230,height=385,width=400)

		

#Kids Frame Starts

#Toys

toyslbl=Label(F4,text="Toys",font="lucida 12 bold",bg="powder blue",fg="black")

toyslbl.grid(row=0,column=0,padx=10,pady=2)

		

toystxt=Entry(F4,font="lucida 10 bold",bd=5,width=15,textvariable=Toys)

toystxt.grid(row=0,column=1,padx=5,pady=2)

		

#Games

		

gamelbl=Label(F4,text="Games",font="lucida 12 bold",bg="powder blue",fg="black")

gamelbl.grid(row=1,column=0,padx=10,pady=2)

gametxt=Entry(F4,font="lucida 10 bold",bd=5,width=15,textvariable=Games)

gametxt.grid(row=1,column=1,padx=5,pady=2)

		

#Frocks

frocklbl=Label(F4,text="Frocks",font="lucida 12 bold",bg="powder blue",fg="black")

frocklbl.grid(row=2,column=0,padx=10,pady=2)

		

frocktxt=Entry(F4,font="lucida 10 bold",bd=5,width=15,textvariable=Frocks)

frocktxt.grid(row=2,column=1,padx=5,pady=2)

#Babysoap

		

soaplbl=Label(F4,text="Baby soap",font="lucida 12 bold",bg="powder blue",fg="black")

soaplbl.grid(row=3,column=0,padx=10,pady=2)

		

soaptxt=Entry(F4,font="lucida 10 bold",bd=5,width=15,textvariable=Soap)

soaptxt.grid(row=3,column=1,padx=5,pady=2)

		

#books

bookslbl=Label(F4,text="Babies Books",font="lucida 12 bold",bg="powder blue",fg="black")

bookslbl.grid(row=4,column=0,padx=10,pady=2)

		

bookstxt=Entry(F4,font="lucida 10 bold",bd=5,width=15,textvariable=Books)

bookstxt.grid(row=4,column=1,padx=5,pady=2)

		

#Hairoil

		

oillbl=Label(F4,text="Hair oil",font="lucida 12 bold",bg="powder blue",fg="black")

oillbl.grid(row=5,column=0,padx=10,pady=2)

		

oiltxt=Entry(F4,font="lucida 10 bold",bd=5,width=15,textvariable=HairOil)

oiltxt.grid(row=5,column=1,padx=5,pady=2)

		

#Lunch Box

boxlbl=Label(F4,text="Lunch Box",font="lucida 12 bold",bg="powder blue",fg="black")

boxlbl.grid(row=6,column=0,padx=10,pady=2)

		

boxtxt=Entry(F4,font="lucida 10 bold",bd=5,width=15,textvariable=LunchBox)

boxtxt.grid(row=6,column=1,padx=5,pady=2)

		

#Kids Frame Ends

		

#Frame 2 Ends

		

#Bill frame starts

		

F5=LabelFrame(top,bg="white",bd=15,relief=SUNKEN)

F5.place(x=1100,y=237,height=398,width=440)

		

#Bill Description Starts

Blbl=Label(F5,text="BILL",font="lucida 18 bold",bg="sky blue",fg="black",bd=18,height=1,width=22)

Blbl.pack(fill=X)

		

#Scrollbar starts

Scroll=Scrollbar(F5)

textarea=Text(F5,yscrollcommand=Scroll.set)

Scroll.pack(side=RIGHT,fill=Y)

Scroll.config(command=textarea.yview)

textarea.pack()

		

#Scroolbar ends

		

#Bill Description Ends

		

#Frame 5 Ends

		

#Frame 6 starts

		

F6=LabelFrame(top,text="Billing Menu",font="lucida 15 bold",fg="red",bg="powder blue",bd=12,relief=SUNKEN)

		

F6.place(x=5,y=600,height=250,width=1540)

		

#Billing Menu starts

#Total mens price starts

TMPlbl=Label(F6,text="Total Mens Price",font="lucida 14 bold",bg="powder blue",fg="black")

TMPlbl.grid(row=0,column=0,padx=10,pady=2)

		

TMPtxt=Entry(F6,font="lucida 12 bold",bd=7,width=15,textvariable=Total_Mens_Price)

TMPtxt.grid(row=0,column=1,padx=5,pady=2)

		

#Total women price

TWPlbl=Label(F6,text="Total Womens Price",font="lucida 14 bold",bg="powder blue",fg="black")

		

TWPlbl.grid(row=1,column=0,padx=10,pady=2)

		

TWPtxt=Entry(F6,font="lucida 12 bold",bd=7,width=15,textvariable=Total_Womens_Price)

TWPtxt.grid(row=1,column=1,padx=5,pady=2)

		

#Total kids price

TKPlbl=Label(F6,text="Total Kids Price",font="lucida 14 bold",bg="powder blue",fg="black")

TKPlbl.grid(row=2,column=0,padx=10,pady=2)

		

TKPtxt=Entry(F6,font="lucida 12 bold",bd=7,width=15,textvariable=Total_Kids_Price)

TKPtxt.grid(row=2,column=1,padx=5,pady=2)

		

#Tax in second column

		

#Men

		

MTlbl=Label(F6,text="Men's Tax",font="lucida 14 bold",bg="powder blue",fg="black")

		

MTlbl.grid(row=0,column=2,padx=10,pady=2)

		

MTtxt=Entry(F6,font="lucida 12 bold",bd=7,width=15,textvariable=Mens_Tax)

MTtxt.grid(row=0,column=3,padx=5,pady=2)

		

#Women

		

WTlbl=Label(F6,text="Women's Tax",font="lucida 14 bold",bg="powder blue",fg="black")

WTlbl.grid(row=1,column=2,padx=10,pady=2)

		

WTtxt=Entry(F6,font="lucida 12 bold",bd=7,width=15,textvariable=Womens_Tax)

		

WTtxt.grid(row=1,column=3,padx=5,pady=2)

		

#Kids

		

KTlbl=Label(F6,text="Kid'sTax",font="lucida 14 bold",bg="powder blue",fg="black")

KTlbl.grid(row=2,column=2,padx=10,pady=2)

		

KTtxt=Entry(F6,font="lucida 12 bold",bd=7,width=15,textvariable=Kids_Tax)

KTtxt.grid(row=2,column=3,padx=5,pady=2)

		

#Total menu price close

#Frame 6 ends

		

#Billing Menu closes

#Frame 6 closes

#Frame 7 starts

		

F7=LabelFrame(F6,bg="powder blue",bd=8,relief=SUNKEN)

F7.place(x=1100,width=440)

		

#Executions button starts

		

#Total

		

Tbtn=Button(F7,text="Total",font="lucida 15",bd=10,width=10,bg="gold",command=total)

		

Tbtn.grid(row=0,column=0,padx=15,pady=15)

		

#Clear

		

Cbtn=Button(F7,text="Clear",font="lucida 15",bd=10,width=10,bg="gold",command=clear)

Cbtn.grid(row=0,column=1,padx=15,pady=15)

		

#Generate bill

Gbtn=Button(F7,text="Generate Bill",font="lucida 15",bd=10,width=10,bg="gold",command=bill_area)

		

Gbtn.grid(row=1,column=0,padx=15,pady=15)

welcome_bill()

#Exit

Ebtn=Button(F7,text="Exit",font="lucida 15",bd=10,width=10,bg="red",command=quitApp)

Ebtn.grid(row=1,column=1,padx=15,pady=15)

		

top.mainloop()
