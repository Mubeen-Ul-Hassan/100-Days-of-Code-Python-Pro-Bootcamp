import tkinter as tk
import secrets
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def random_password_generator(pass_length = 12):
    password_length = pass_length
    password_generated = secrets.token_urlsafe(password_length)

    password_entry_value.set(password_generated)
    pyperclip.copy(password_generated) # Copy the generated password to clipboard



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
   website = website_entry.get()
   user_email = user_email_entry.get()
   password = password_entry.get()

   message = f"Email {user_email} \nPassword: {password} \nIs this OK?"
   response = messagebox.askyesno("Warning", message)
   if response:
        save_to_file(website, user_email, password)
   else:
       return False


def save_to_file(website, user_email, password):
    with open("credentials.txt", "a") as file:
        file.write(f"{website} | {user_email} - {password}\n")
    return True

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = tk.Canvas(height=200, width=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.config(background="white", borderwidth=0, highlightthickness=0)
canvas.grid(row=0, column=1)

# Website Label
website_label = tk.Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

# Website Entry
website_entry = tk.Entry(width=45)
website_entry.grid(row=1, column=1, columnspan=2, padx=2, pady=2)
website_entry.focus()
# Email/Username Label
user_email_label = tk.Label(text="Email/Username:", bg="white")
user_email_label.grid(row=2, column=0)

# Email/Username Entry
user_email_entry = tk.Entry(width=45)
user_email_entry.grid(row=2, column=1, columnspan=2, padx=2, pady=2)

# Password Label
password_label = tk.Label(text="Password:", bg="white")
password_label.grid(row=3, column=0, padx=2, pady=2)

# Password Entry
password_entry_value = tk.StringVar()
password_entry = tk.Entry(textvariable=password_entry_value, width=25)
password_entry.grid(row=3, column=1)

# Generate Password Button
generate_password_button = tk.Button(text="Generate Password", justify="center", bg="white", command=random_password_generator)
generate_password_button.grid(row=3, column=2)

# Add Button
add_button = tk.Button(text="Add", justify="center", bg="white", width=40, command=save_password)
add_button.grid(row=4, column=1, columnspan=3)

window.mainloop()