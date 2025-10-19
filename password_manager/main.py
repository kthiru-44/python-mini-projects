# ---------------------------- PASSWORD GENERATOR ------------------------------- #


from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json

def search():


    try:

        with open("password.json", "r") as pp:

            data = json.load(pp)
            website = entry_1.get()

            try :

                messagebox.showinfo(title=website,message=f"Email : {data[website]["email"]} \nPassword : {data[website]["password"]}")
                entry_1.delete(0,END)

            except KeyError:

                messagebox.showinfo(title="Error",message="No Such Website in Database")
                entry_1.delete(0, END)


    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found")


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    entry_3.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():

    web = entry_1.get()
    email = entry_2.get()
    pas = entry_3.get()

    pas_dict = {web :{"email" : email,
                  "password" : pas}
            }

    if pas == "" or web == "" :

        messagebox.showinfo(title="Error",message="Dont leave any field empty")
        entry_3.delete(0, END)
        entry_1.delete(0, END)

    else :

        try:
            with open("password.json","r") as pp :

                data = json.load(pp)

        except FileNotFoundError:

            with open("password.json", "w") as pp:

                json.dump(pas_dict, pp, indent=4)


        else:

            data.update(pas_dict)

            with open("password.json" , "w") as p :

                json.dump(data,p,indent=4)

        finally:

            entry_3.delete(0,END)
            entry_1.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Password Generator")
window.config(padx=20,pady=20)

img = PhotoImage(file= "logo.png")

canvas = Canvas(height=200,width=200)
canvas.create_image(100,100,image=img)
canvas.grid(column=1,row=0,pady=20,padx=20)

label_1 = Label(text="Website :" ,fg="black")
label_1.grid(column=0,row=1)

entry_1 = Entry(width=39)
entry_1.grid(column=1,row=1,pady=5,padx=5)
entry_1.focus()

button_1 = Button(text="          Search          ",fg="white",bg="green",command=search)
button_1.grid(column=2,row=1)

label_2 = Label(text="Email/Username :",fg="black")
label_2.grid(column=0,row=2)

entry_2 = Entry(width=58)
entry_2.insert(0,"thirukumaran3057@gmail.com")
entry_2.grid(column=1,row=2,columnspan=2,pady=5,padx=5)

button_2 = Button(text="Generate Password",fg="white",bg="green",command=generate_password)
button_2.grid(column=2,row=3)

label_3 = Label(text="Password :",fg="black")
label_3.grid(column=0,row=3)

entry_3= Entry(width=39)
entry_3.grid(column=1,row=3,pady=5,padx=5)

button_3 = Button(text="Add",fg="white",bg="red",width=33,command=add)
button_3.grid(column=1,row=4,pady=5,padx=5)



window.mainloop()