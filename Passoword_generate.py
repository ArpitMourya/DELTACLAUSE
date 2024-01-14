import customtkinter
import pyperclip
password = "Suggested Password"
customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk() 
app.geometry("400x240")
app.title("Password Generator")
def copy_password():
    pyperclip.copy(password)
    print("Password copied to clipboard")
def button_function():
    global password
    password = ""
    print("button pressed")
    print(entry.get())
    for i in entry.get():
        password+=chr(ord(i)+4)
    textbox.configure(text=f"{password}")
# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="Copy",width=100, command=copy_password)
button.place(relx=0.7, rely=0.6, anchor=customtkinter.N)
button = customtkinter.CTkButton(master=app, text="Generate",width=100, command=button_function)
button.place(relx=0.3, rely=0.6, anchor=customtkinter.N)

entry = customtkinter.CTkEntry(master=app, placeholder_text="Enter Seed")
entry.grid(row=3, column=2, columnspan=1, padx=(130, 0), pady=(40, 20), sticky="nsew")
textbox = customtkinter.CTkLabel(master=app, text=password)
textbox.grid(row=1, column=2, padx=(130, 0), pady=(20, 0), sticky="nsew")
  # get entry text
app.update()
app.mainloop()