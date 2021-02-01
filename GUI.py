from tkinter import *


facebook = Tk()
facebook.geometry('2000x600')
facebook.config(bg="yellow")
facebook.title("FACEBOOK PAGE")
font="calibiri"
starting_line=Label(facebook,text="\nBengal Collage Of Engineering and Technology\n ",bg="blue",fg="white",font=font,width="44",height="3")
starting_line.grid(row=0,column=7)

headline=Label(facebook,text = " \nSignin ",bg="yellow",fg="black",font=font)
headline.grid(row=1,column=3)
username= Label(facebook,text = "\n \a Username :- ",bg="yellow",fg="black",font=font)
username.grid(row=2,column=2)
username=Entry(facebook)
username.grid(row=2,column=5)


password=Label(facebook,text= "\n \b Password  :-",bg="yellow",fg="black",font=font)
password.grid(row=3,column=2)
password=Entry(facebook)
password.grid(row=3,column=5)

login=Button(facebook,text="Login ",bg="yellow",fg="black",font=font)
login.grid(row=4,column=5)

create=Label(facebook,text = " \nSignup ",bg="yellow",fg="black",font=font)
create.grid(row=1,column=10)

first_name=Label(facebook,text = "\n\t \v First Name :- ",bg="yellow",fg="black",font=font)
first_name.grid(row=2,column=9)
first_name=Entry(facebook)
first_name.grid(row=2,column=11)

second_name=Label(facebook,text = "\n\t \b Second Name :- ",bg="yellow",fg="black",font=font)
second_name.grid(row=3,column=9)
second_name=Entry(facebook)
second_name.grid(row=3,column=11)

email=Label(facebook,text = "\n\t \f Email I'd :-",bg="yellow",fg="black",font=font)
email.grid(row=4,column=9)
email=Entry(facebook)
email.grid(row=4, column=11)

gender=Label(facebook,text="\n\t \a Gender :-",bg="yellow",fg="black",font=font)
gender.grid(row=5,column=9)
male=Checkbutton(facebook,text="Male",fg="black",bg="yellow",font=font)
male.grid(row=5,column=11)
female=Checkbutton(facebook,text="female",fg="black",bg="yellow",font=font)
female.grid(row=5,column=12)

age=Label(facebook,text="\n\t \b Age :-",fg="black",bg="yellow",font=font)
age.grid(row=6,column=9)
age=Entry(facebook)
age.grid(row=6,column=11)
age=Entry(facebook)
age.grid(row=6,column=12)
age=Entry(facebook)
age.grid(row=6,column=13)

phone=Label(facebook,text="\n\t \f Phone No. :-",fg="black",bg="yellow",font=font)
phone.grid(row=7,column=9)
phone=Entry(facebook)
phone.grid(row=7,column=11)

signup=Button(facebook,text="Signup",bg="yellow",fg="black",font=font)
signup.grid(row=8,column=11)




facebook.mainloop()

