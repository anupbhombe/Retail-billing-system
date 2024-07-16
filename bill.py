from tkinter import *

root=Tk()
root.title('Retail Billing System')
root.geometry('1340x700') #1270x685
root.iconbitmap('icon.ico')

#first label
headingLabel=Label(root,text='Retail Billing System',font=('times new roman',30,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
headingLabel.pack(fill=X,pady=10)


customer_details_frame=LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='gray20',fg='white')
nameLabel.grid(row=0,column=0,padx=20,pady=2) #(same like a pack only diff is )help to add a labels with a respect of rows and columns
nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7)
nameEntry.grid(row=0,column=1,padx=8)


phoneLabel=Label(customer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),bg='gray20',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)
phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7)
phoneEntry.grid(row=0,column=3,padx=8)

BillNumberLabel=Label(customer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),bg='gray20',fg='white')
BillNumberLabel.grid(row=0,column=4,padx=20,pady=2)
BillNumberEntry=Entry(customer_details_frame,font=('arial',15),bd=7)
BillNumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=10) #bd border
searchButton.grid(row=0,column=6,padx=20,pady=8)

#third Frame

#__________first label frame
productsFrame=Frame(root)
productsFrame.pack(fill=X,pady=10)

Cosmetis_Label=LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
Cosmetis_Label.grid(row=0,column=0)

BathSoapLabel=Label(Cosmetis_Label,text='Bath Soap',font=('times new roman',15,'bold'),bg='gray20',fg='white')
BathSoapLabel.grid(row=0,column=0,padx=5,pady=13)
BathSoapEntry=Entry(Cosmetis_Label,font=('arial',10),bd=7)
BathSoapEntry.grid(row=0,column=1,padx=20)


FaceCreamLabel=Label(Cosmetis_Label,text='Face Cream',font=('times new roman',15,'bold'),bg='gray20',fg='white')
FaceCreamLabel.grid(row=2,column=0,padx=5,pady=13)
FaceCreamEntry=Entry(Cosmetis_Label,font=('arial',10),bd=7)
FaceCreamEntry.grid(row=2,column=1,padx=20)


FaceWashLabel=Label(Cosmetis_Label,text='Face Wash',font=('times new roman',15,'bold'),bg='gray20',fg='white')
FaceWashLabel.grid(row=3,column=0,padx=5,pady=13)
FaceWashEntry=Entry(Cosmetis_Label,font=('arial',10),bd=7)
FaceWashEntry.grid(row=3,column=1,padx=20)


HairSprayLabel=Label(Cosmetis_Label,text='Hair Spreay',font=('times new roman',15,'bold'),bg='gray20',fg='white')
HairSprayLabel.grid(row=4,column=0,padx=5,pady=13)
HairSprayEntry=Entry(Cosmetis_Label,font=('arial',10),bd=7)
HairSprayEntry.grid(row=4,column=1,padx=20)


HairGelLabel=Label(Cosmetis_Label,text='Hair Gel',font=('times new roman',15,'bold'),bg='gray20',fg='white')
HairGelLabel.grid(row=5,column=0,padx=5,pady=13)
HairGelEntry=Entry(Cosmetis_Label,font=('arial',10),bd=7)
HairGelEntry.grid(row=5,column=1,padx=20)


BodyLotionLabel=Label(Cosmetis_Label,text='Body Lotion',font=('times new roman',15,'bold'),bg='gray20',fg='white')
BodyLotionLabel.grid(row=6,column=0,padx=5,pady=13)
BodyLotionEntry=Entry(Cosmetis_Label,font=('arial',10),bd=7)
BodyLotionEntry.grid(row=6,column=1,padx=20)



#__________________second Label frame

Grocery_Label=LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
Grocery_Label.grid(row=0,column=1,padx=10)

RiceLabel=Label(Grocery_Label,text='Rice',font=('times new roman',15,'bold'),bg='gray20',fg='white')
RiceLabel.grid(row=0,column=0,padx=5,pady=13)
RiceEntry=Entry(Grocery_Label,font=('arial',10),bd=7)
RiceEntry.grid(row=0,column=1,padx=20)


OilLabel=Label(Grocery_Label,text='Oil',font=('times new roman',15,'bold'),bg='gray20',fg='white')
OilLabel.grid(row=1,column=0,padx=5,pady=13)
OilEntry=Entry(Grocery_Label,font=('arial',10),bd=7)
OilEntry.grid(row=1,column=1,padx=20)

DaalLabel=Label(Grocery_Label,text='DaalLabel',font=('times new roman',15,'bold'),bg='gray20',fg='white')
DaalLabel.grid(row=2,column=0,padx=5,pady=13)
DaalEntry=Entry(Grocery_Label,font=('arial',10),bd=7)
DaalEntry.grid(row=2,column=1,padx=20)


WheatLabel=Label(Grocery_Label,text='Wheat',font=('times new roman',15,'bold'),bg='gray20',fg='white')
WheatLabel.grid(row=3,column=0,padx=5,pady=13)
WheatEntry=Entry(Grocery_Label,font=('arial',10),bd=7)
WheatEntry.grid(row=3,column=1,padx=20)


SugarLabel=Label(Grocery_Label,text='Sugar',font=('times new roman',15,'bold'),bg='gray20',fg='white')
SugarLabel.grid(row=4,column=0,padx=5,pady=13)
SugarEntry=Entry(Grocery_Label,font=('arial',10),bd=7)
SugarEntry.grid(row=4,column=1,padx=20)


TeaLabel=Label(Grocery_Label,text='Oil',font=('times new roman',15,'bold'),bg='gray20',fg='white')
TeaLabel.grid(row=5,column=0,padx=5,pady=13)
TeaEntry=Entry(Grocery_Label,font=('arial',10),bd=7)
TeaEntry.grid(row=5,column=1,padx=20)




#___________________third frame label

colddrinks_Label=LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
colddrinks_Label.grid(row=0,column=2,padx=10)

MaazaLabel=Label(colddrinks_Label,text='Maaza',font=('times new roman',15,'bold'),bg='gray20',fg='white')
MaazaLabel.grid(row=0,column=0,padx=5,pady=13)
MaazaEntry=Entry(colddrinks_Label,font=('arial',10),bd=7)
MaazaEntry.grid(row=0,column=1,padx=20)

PepsiLabel=Label(colddrinks_Label,text='Pepsi',font=('times new roman',15,'bold'),bg='gray20',fg='white')
PepsiLabel.grid(row=1,column=0,padx=5,pady=13)
PepsiEntry=Entry(colddrinks_Label,font=('arial',10),bd=7)
PepsiEntry.grid(row=1,column=1,padx=20)


SpriteLabel=Label(colddrinks_Label,text='Sprite',font=('times new roman',15,'bold'),bg='gray20',fg='white')
SpriteLabel.grid(row=2,column=0,padx=5,pady=13)
SpriteEntry=Entry(colddrinks_Label,font=('arial',10),bd=7)
SpriteEntry.grid(row=2,column=1,padx=20)

DewLabel=Label(colddrinks_Label,text='Rice',font=('times new roman',15,'bold'),bg='gray20',fg='white')
DewLabel.grid(row=3,column=0,padx=5,pady=13)
DewEntry=Entry(colddrinks_Label,font=('arial',10),bd=7)
DewEntry.grid(row=3,column=1,padx=20)


SugarLabel=Label(Grocery_Label,text='Sugar',font=('times new roman',15,'bold'),bg='gray20',fg='white')
SugarLabel.grid(row=4,column=0,padx=5,pady=13)
SugarEntry=Entry(Grocery_Label,font=('arial',10),bd=7)
SugarEntry.grid(row=4,column=1,padx=20)


TeaLabel=Label(Grocery_Label,text='Oil',font=('times new roman',15,'bold'),bg='gray20',fg='white')
TeaLabel.grid(row=5,column=0,padx=5,pady=13)
TeaEntry=Entry(Grocery_Label,font=('arial',10),bd=7)
TeaEntry.grid(row=5,column=1,padx=20)





root.mainloop()