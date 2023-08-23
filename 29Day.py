from tkinter import *
from tkinter import messagebox
import random

def search():
     search_website=website_entry.get()
     
def generate_password():
        letters=("a", "b", "c")
        numbers=("1", "2", "3")
        symbols=("#", "$", "%")
        letters_num=random.randint(2,4)
        symbols_num=random.randint(1,4)
        numbers_num=random.randint(1,4)
    
        password_letters=[random.choice(letters) for _ in range(letters_num)]
        password_symbols=[random.choice(symbols) for _ in range(symbols_num)]
        password_numbers=[random.choice(numbers) for _ in range(numbers_num)]

        password_list=password_letters+password_symbols+password_numbers


        random.shuffle(password_list)
        x="".join(password_list)
        
        password_entry.insert(0,x)

def save():
   website=website_entry.get()
   email=email_entry.get()
   password=password_entry.get()

   if len(website)== 0 or len(email)==0 or len(password)==0:
       messagebox.showinfo(title="Oops", message="Please fill the required fields")
   else:
        is_ok=messagebox.askokcancel(title=website, message=f"Details are:\nEmail: {email}\n Password: {password}")
    
        if is_ok:
                with open("data.text", "a") as data_file:
                    data_file.write(f"{website} | {email} | {password}\n") 
                    messagebox.showinfo(message="Your Data added succesfully")
                    website_entry.delete(0,END)
                    email_entry.delete(0, END)
                    password_entry.delete(0, END)


window=Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas=Canvas(height=200, width=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label=Label(text="Website")
website_label.grid(row=1,column=0)
email_label=Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label=Label(text="password")
password_label.grid(row=3, column=0)

website_entry=Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry=Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password_button=Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button=Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button=Button(text="Search", width=6)
search_button.grid(row=1, column=2)



window.mainloop()