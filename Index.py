#ร้านค้าที่มีราคาเพียงแค่ 1-3 ราคา เช่นร้าน บุฟเฟ่ 
from tkinter import *
import sqlite3
from tkinter.font import Font



main = Tk()
main.title("ร้านหมูกระทะอื่มจุง")
Goodfont = Font(
 family="Tahoma",
 size=16,
 weight="normal",
 slant="roman",
 underline=0,
 overstrike=0

 )
name = Label(main,text="ร้านหมูกระทะอิ่มจุง",font=Goodfont,width=60,height=2)
name.grid(row=0,column=0,columnspan=5)
#ผู้ใหญ่
senior = Label(main,text="จำนวนผู้ใหญ่",font="Tahoma 17",padx=10,pady=10)
senior.grid(row=1,column=0,sticky=E)
valuesenior = StringVar()
amountsenior = Entry(main,width=10,font=Goodfont,textvariable=valuesenior)
amountsenior.grid(row=1,column=1)
unit1 = Label(main,text="คน",font="Tahoma 17",padx=10,pady=10)
unit1.grid(row=1,column=2,sticky=W),
#เด็ก
child = Label(main,text="จำนวนเด็ก",font="Tahoma 17",padx=10,pady=10)
child.grid(row=2,column=0,sticky=E)
valuechild = StringVar()
amountchild = Entry(main,width=10,font=Goodfont,textvariable=valuechild)
amountchild.grid(row=2,column=1)
unit2 = Label(main,text="คน",font="Tahoma 17",padx=10,pady=10)
unit2.grid(row=2,column=2,sticky=W)


#รายการ
list1 = Label(main,text="รายการ",font="Tahoma 17",bg="blue",width=30)
list1.grid(row=1,column=3,columnspan=2,sticky=NSEW)
#แพ็กเกต
pack = Label(main,text="",font="Tahoma 12",padx=10,pady=10,width=30)
pack.grid_remove()
#แพ็กเกต
notioce2 = Label(main,text="",font="Tahoma 12",padx=10,pady=10,width=30)
notioce2.grid_remove()
#จำนวนผู้ใหญ่
ase = Label(main,text="",font="Tahoma 12",padx=10,pady=10,width=30)
ase.grid_remove()
#จำนวนเด็ก
ach = Label(main,text="",font="Tahoma 12",padx=10,pady=10,width=30)
ach.grid_remove()
#ส่วนลด
rdis = Label(main,text="",font="Tahoma 12",padx=10,pady=10,width=30)
rdis.grid_remove()
#ภาษี
rvat = Label(main,text="",font="Tahoma 12",padx=10,pady=10,width=30)
rvat.grid_remove()
#รวมยอด
rtotal = Label(main,text="",font="Tahoma 12",padx=10,pady=10,width=30)
rtotal.grid_remove()

#ราคารวมที่กินทั้งหมด
total = 0
#ส่วนลดเริ่มต้น
disc = 0
#รายได้วันนี้
money = 0
#ส่วนลดทั้งหหมด
alldisc = 0
#ส่วนลดทั้งหหมด
Vat = 0

#ระบบ499
def bill499():
 global total
 global disc
 global money
 global package
 global alldisc
 global Vat
 alltotal = 0
 print(f"ส่วนลด {disc} %")
 package = 499
 getchild = int(valuechild.get()) #รับค่าจำนวนเด็ก
 allchild = getchild*0.75*package #ราคารวมเด็ก # 0.75 คือคิดราคาแค่ 75 % หรือลด 25 %
 getsenior = int(valuesenior.get()) #รับค่าจำนวนผู้ใหญ่
 allsenior = getsenior*package #ราคารวมผู้ใหญ่
 alltotal = allsenior+allchild #ราคารวมเด็กผู้ใหญ่
 alldisc = (disc/100)*(alltotal) #ราคาส่วนลด
 Afterdisc = alltotal-alldisc #ราคาที่หักส่วนลด
 Vat = ((7/100)*Afterdisc) #ราคาVat
 total = Afterdisc+Vat #ราคาสุทธิ
 print(f"แพ็คราคา 499/คน\nจำนวนผู้ใหญ่: {getsenior} คน\nจำนวนเด็ก: {getchild} คน")
 btn499.grid_remove()
 btn899.grid_remove()
 btn1299.grid_remove()
 cancel.config(text="คุณเลือกราคา 499 กดเพื่อเลือกใหม่",font="Tahoma 12")
 cancel.grid(row=3,column=0,columnspan=2,sticky=NSEW)
 clear.grid(row=3,column=2,sticky=NSEW)
 #ใช้ได้ทั้งหมด
 pack.grid(row=2,column=3,columnspan=2,sticky=EW)
 pack.config(text=f"แพ็กเกต {package} ราคา {package} บาท")
 ase.grid(row=3,column=3,columnspan=2,sticky=EW)
 ase.config(text=f"จำนวนผู้ใหญ่ * {getsenior} คน คิดเป็น {allsenior} บาท")
 ach.grid(row=4,column=3,columnspan=2,sticky=EW)
 ach.config(text=f"จำนวนเด็ก * {getchild} คน คิดเป็น {allchild} บาท")
 if disc > 0:
  rdis.config(text=f"ส่วนลด {disc} % คิดเป็น {alldisc} บาท",fg="green")
  rdis.grid(row=5,column=3,columnspan=2,sticky=EW)
 else:
  rdis.config(text=f"ไม่มีส่วนลด",fg="red")
  rdis.grid(row=5,column=3,columnspan=2,sticky=EW)
 rvat.config(text=f"VAT 7 % คิดเป็น {Vat} บาท")
 rvat.grid(row=6,column=3,columnspan=2,sticky=EW)
 rtotal.config(text=f"ราคาสุทธิ {total} บาท")
 rtotal.grid(row=7,column=3,columnspan=2,sticky=EW)
 incomeupdate()
 billplase.grid(row=8,column=3,columnspan=2,sticky=EW)

#ระบบ899
def bill899():
 global total
 global disc
 global money
 global package
 global alldisc
 global Vat
 alltotal = 0
 print(f"ส่วนลด {disc} %")
 package = 899
 getchild = int(valuechild.get()) #รับค่าจำนวนเด็ก
 allchild = getchild*0.75*package #ราคารวมเด็ก # 0.75 คือคิดราคาแค่ 75 % หรือลด 25 %
 getsenior = int(valuesenior.get()) #รับค่าจำนวนผู้ใหญ่
 allsenior = getsenior*package #ราคารวมผู้ใหญ่
 alltotal = allsenior+allchild #ราคารวมเด็กผู้ใหญ่
 alldisc = (disc/100)*(alltotal) #ราคาส่วนลด
 Afterdisc = alltotal-alldisc #ราคาที่หักส่วนลด
 Vat = ((7/100)*Afterdisc) #ราคาVat
 total = Afterdisc+Vat #ราคาสุทธิ
 print(f"แพ็คราคา 899/คน\nจำนวนผู้ใหญ่: {getsenior} คน\nจำนวนเด็ก: {getchild} คน")
 btn499.grid_remove()
 btn899.grid_remove()
 btn1299.grid_remove()
 cancel.config(text="คุณเลือกราคา 899 กดเพื่อเลือกใหม่",font="Tahoma 12")
 cancel.grid(row=3,column=0,columnspan=2,sticky=NSEW)
 clear.grid(row=3,column=2,sticky=NSEW)
 pack.grid(row=2,column=3,columnspan=2,sticky=EW)
 pack.config(text=f"แพ็กเกต {package} ราคา {package} บาท")
 ase.grid(row=3,column=3,columnspan=2,sticky=EW)
 ase.config(text=f"จำนวนผู้ใหญ่ * {getsenior} คน คิดเป็น {allsenior} บาท")
 ach.grid(row=4,column=3,columnspan=2,sticky=EW)
 ach.config(text=f"จำนวนเด็ก * {getchild} คน คิดเป็น {allchild} บาท")
 if disc > 0:
  rdis.config(text=f"ส่วนลด {disc} % คิดเป็น {alldisc} บาท",fg="green")
  rdis.grid(row=5,column=3,columnspan=2,sticky=EW)
 else:
  rdis.config(text=f"ไม่มีส่วนลด",fg="red")
  rdis.grid(row=5,column=3,columnspan=2,sticky=EW)
 rvat.config(text=f"VAT 7 % คิดเป็น {Vat} บาท")
 rvat.grid(row=6,column=3,columnspan=2,sticky=EW)
 rtotal.config(text=f"ราคาสุทธิ {total} บาท")
 rtotal.grid(row=7,column=3,columnspan=2,sticky=EW)
 incomeupdate()
 billplase.grid(row=8,column=3,columnspan=2,sticky=EW)
 
 
#ระบบ1299
def bill1299():
 global total
 global disc
 global money
 global package
 global alldisc
 global Vat
 alltotal = 0
 print(f"ส่วนลด {disc} %")
 package = 1299
 getchild = int(valuechild.get()) #รับค่าจำนวนเด็ก
 allchild = getchild*0.75*package #ราคารวมเด็ก # 0.75 คือคิดราคาแค่ 75 % หรือลด 25 %
 getsenior = int(valuesenior.get()) #รับค่าจำนวนผู้ใหญ่
 allsenior = getsenior*package #ราคารวมผู้ใหญ่
 alltotal = allsenior+allchild #ราคารวมเด็กผู้ใหญ่
 alldisc = (disc/100)*(alltotal) #ราคาส่วนลด
 Afterdisc = alltotal-alldisc #ราคาที่หักส่วนลด
 Vat = ((7/100)*Afterdisc) #ราคาVat
 total = Afterdisc+Vat #ราคาสุทธิ
 print(f"แพ็คราคา 1299/คน\nจำนวนผู้ใหญ่: {getsenior} คน\nจำนวนเด็ก: {getchild} คน")
 btn499.grid_remove()
 btn899.grid_remove()
 btn1299.grid_remove()
 cancel.config(text="คุณเลือกราคา 1299 กดเพื่อเลือกใหม่",font="Tahoma 12")
 cancel.grid(row=3,column=0,columnspan=2,sticky=NSEW)
 clear.grid(row=3,column=2,sticky=NSEW)
 pack.grid(row=2,column=3,columnspan=2,sticky=EW)
 pack.config(text=f"แพ็กเกต {package} ราคา {package} บาท")
 ase.grid(row=3,column=3,columnspan=2,sticky=EW)
 ase.config(text=f"จำนวนผู้ใหญ่ * {getsenior} คน คิดเป็น {allsenior} บาท")
 ach.grid(row=4,column=3,columnspan=2,sticky=EW)
 ach.config(text=f"จำนวนเด็ก * {getchild} คน คิดเป็น {allchild} บาท")
 if disc > 0:
  rdis.config(text=f"ส่วนลด {disc} % คิดเป็น {alldisc} บาท",fg="green")
  rdis.grid(row=5,column=3,columnspan=2,sticky=EW)
 else:
  rdis.config(text=f"ไม่มีส่วนลด",fg="red")
  rdis.grid(row=5,column=3,columnspan=2,sticky=EW)
 rvat.config(text=f"VAT 7 % คิดเป็น {Vat} บาท")
 rvat.grid(row=6,column=3,columnspan=2,sticky=EW)
 rtotal.config(text=f"ราคาสุทธิ {total} บาท")
 rtotal.grid(row=7,column=3,columnspan=2,sticky=EW)
 incomeupdate()
 billplase.grid(row=8,column=3,columnspan=2,sticky=EW)
 
 #ระบบส่วนลด
def discsystem():
 global disc
 code = valuecode.get()
 if code == "DISC50":
  disc = 50
  entercode.delete(0,END)
  notioce1.grid_remove()
  notioce1.config(text=f"คุณได้รับส่วนลด {disc}% ",fg="green")
  notioce1.grid(row=5,column=0,columnspan=3)
  return disc
  
 else:
  notioce1.config(text="โค้ดไม่ถูกต้องหรืออาจหมดอายุ",fg="red")
  notioce1.grid(row=5,column=0,columnspan=3)
  entercode.delete(0,END)



#เลือกใหม่
def cancelselect():
 btn499.grid(row=3,column=0)
 btn899.grid(row=3,column=1)
 btn1299.grid(row=3,column=2)
 cancel.grid_remove()
 clear.grid_remove()
 pack.grid_remove()
 ase.grid_remove()
 ach.grid_remove()
 rdis.grid_remove()
 rvat.grid_remove()
 rtotal.grid_remove()
 billplase.grid_remove()


#ล้างค่า
def clearall():
 global disc
 btn499.grid(row=3,column=0)
 btn899.grid(row=3,column=1)
 btn1299.grid(row=3,column=2)
 cancel.grid_remove()
 clear.grid_remove()
 amountchild.delete(0,END)
 amountsenior.delete(0,END)
 entercode.delete(0,END)
 pack.grid_remove()
 ase.grid_remove()
 ach.grid_remove()
 rdis.grid_remove()
 rvat.grid_remove()
 rtotal.grid_remove()
 disc = 0
 notioce1.grid_remove()
 billplase.grid_remove()
 
#รับเงินมา
getmoney = 0
#เงินทอน
change = 0
#แพ็กเกต
package = 0

def cashing():
 global total
 global getmoney
 global change
 cash = Tk()
 cash.title("ระชำระเงิน")
 cash.geometry("820x200+50+400")
 pack.grid_remove()
 ase.grid_remove()
 ach.grid_remove()
 rdis.grid_remove()
 rvat.grid_remove()
 rtotal.grid_remove()
 notioce2.config(text="กำลังอยู่ในขั้นตอนการชำระเงิน",font="Tahoma 12",fg="red")
 notioce2.grid(row=2,column=3,columnspan=2,sticky=EW)
 billplase.grid_remove()
 reset.grid(row=3,column=0,columnspan=3,sticky=NSEW)
 billplase.grid_remove()
 head = Label(cash,text=f"ยอดที่ต้องชำระคือ {total} บาท",font="Tahoma 17",width=65,bg="blue")
 head.grid(row=0,column=0,columnspan=3)
 textgetmoney = Label(cash,text="รับเงิน",font="Tahoma 17")
 textgetmoney.grid(row=1,column=0,sticky=E)
 getmoneyvalue = StringVar()
 getmoney = Entry(cash,textvariable=getmoneyvalue,font="Tahoma 17")
 getmoney.grid(row=1,column=1,sticky=E)
 textbath = Label(cash,text="บาท",font="Tahoma 17")
 textbath.grid(row=1,column=2,sticky=W)
 textchange = Label(cash,text="เงินทอน",font="Tahoma 17")
 textchange.grid(row=2,column=0,sticky=E)
 textchangeint = Label(cash,text=f"",font="Tahoma 17")
 textchangeint.grid(row=2,column=1,sticky=E)
 textbath = Label(cash,text="บาท",font="Tahoma 17")
 textbath.grid(row=2,column=2,sticky=W)
 def kitcash():
   moneys = int(getmoney.get())
   change = moneys-total
   if change  >= 0:
    textchangeint.config(text=change)
    notioce3.grid_remove()
    prinser()
   else:
    notioce3.grid(row=4,column=0,columnspan=4)
 Btn1 = Button(cash,text="จ่ายเงิน",font="Tahoma 17",width=40,command=kitcash)
 Btn1.grid(row=3,column=0,columnspan=3)
 notioce3 = Label(cash,text="ยอดเงินรับไม่ถูกต้อง กรุณากรอกใหม่",font="Tahoma 17",fg="red")
 notioce3.grid_remove()
 #แสงดปุ่มprinser
 def prinser():
  Btn1.config(text="พิมพ์ใบเสร็จ",bg="green",command=printing)
 
 
  
  
 def printing():
  global money
  global total
  global package
  global alldisc
  global disc
  global Vat
  global txt
  pt = Tk()
  getsenior = int(valuesenior.get())
  getchild = int(valuechild.get())
  pt.title("ใบเสร็จสำหรับลูกค้า")
  pt.geometry("300x530+890+70")
  txt = Label(pt,text="ใบเสร็จ",font="Tahoma 16").pack()
  txt = Label(pt,text="ร้านหมูกระทะอิ่มจุง",font="Tahoma 12").pack()
  txt = Label(pt,text="เบอร์โทร: 123-456-7890",font="Tahoma 12").pack()
  txt = Label(pt,text=".....................................................",font="Tahoma 12").pack()
  txt = Label(pt,text=f"ผู้ใหญ่*{getsenior} ราคา {package*getsenior} บาท",font="Tahoma 12").pack()
  txt = Label(pt,text=f"เด็ก*{getchild} ราคา {package*getchild*0.75} บาท",font="Tahoma 12").pack()
  txt = Label(pt,text=f"ส่วนลด {disc} % ราคา {alldisc} บาท",font="Tahoma 12").pack()
  txt = Label(pt,text=f"ภาษี 7 % ราคา {int(Vat)} บาท",font="Tahoma 12").pack()
  txt = Label(pt,text=f"ราคาสุทธิ {total} บาท",font="Tahoma 12").pack()
  txt = Label(pt,text=".....................................................",font="Tahoma 12").pack()
  txt = Label(pt,text="ขอบคุณที่ใช้บริการ",font="Tahoma 12").pack()
  def finish():
   global money
   pt.destroy()
   cash.destroy()
   btn499.grid(row=3,column=0)
   btn899.grid(row=3,column=1)
   btn1299.grid(row=3,column=2)
   cancel.grid_remove()
   clear.grid_remove()
   reset.grid_remove()
   amountchild.delete(0,END)
   amountsenior.delete(0,END)
   entercode.delete(0,END)
   notioce2.grid_remove()
   money += total
   incomeupdate()
  def cashedfc():
   Btn1.config(text="เสร็จสิ้น",bg="yellow",command=finish)
  cashedfc()


def reseting():
 print("reset")

#คิดเงิน
billplase = Button(main,text="ชำระเงิน",font="Tahoma 16",padx=10,pady=10,bg="pink",width=30,command=cashing)
billplase.grid_remove()


#แพ็กเกตที่กิน
#499-.
btn499 = Button(main,text="499",font="Tahoma 18",width=10,command=bill499)
btn499.grid(row=3,column=0)
#899-.
btn899 = Button(main,text="899",font="Tahoma 18",width=10,command=bill899)
btn899.grid(row=3,column=1)
#1299-.
btn1299 = Button(main,text="1299",font="Tahoma 18",width=10,command=bill1299)
btn1299.grid(row=3,column=2)
#ยกเลิกการเลือก เคสนี้ยกเลือกแค่ราคา ค่าที่กรอกมาใช้ค่าเดิม
cancel = Button(main,text="",font=Goodfont,fg="red",width=30,command=cancelselect)
cancel.grid_remove()
#cancel.grid(row=3,column=0,columnspan=2,sticky=NSEW)

#ล้างค่า เคสนี้ยกเลิกทั้งราคา และตัวเลขที่ต้องกรอก
clear = Button(main,text="ล้าง",font=Goodfont,fg="red",width=10,command=clearall)
clear.grid_remove()
#clear.grid(row=3,column=2,sticky=NSEW)

#รีเซ็ต
reset = Button(main,text="กำลังอยู่ในขั้นตอนการชำระเงิน ไม่สามารถยกเลิกได้",font="Tahoma 11",fg="red",width=10,command=reseting)
reset.grid_remove()
#clear.grid(row=3,column=2,sticky=NSEW)

#ส่วนลด code 
namecode = Label(main,text="โค้ดส่วนลด",font="Tahoma 17",padx=10,pady=10)
namecode.grid(row=4,column=0,sticky=E)
valuecode =StringVar()
entercode = Entry(main,width=10,font=Goodfont,textvariable=valuecode)
entercode.grid(row=4,column=1)
sentcode = Button(main,text="ส่ง",font="Tahoma 17",width=10,command=discsystem)
sentcode.grid(row=4,column=2,sticky=W)

#notice
notioce1 = Label(main,text="",font="tahoma 14")

#ช่องทางการชำระเงิน


#imcome
def incomeupdate():
 global money
 income.config(text=f"รายได้วันนี้: {money} บาท")
income = Label(main,text="รายได้วันนี้: 0 บาท")
income.grid(row=8)




main.geometry("+50+70")
main.mainloop()