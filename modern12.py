import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")
root.title("Login page")


def registration():
    a=str(input("NAME:"))
    b=str(input("DOB:"))
    c=str(input("GENDER:M/F"))
    d=str(input("MOBLIE NO:"))
    f=str(input("ADDRESS:"))
    print("SUMIT\nADD\nDELETE")

    login()


def login():
    import customtkinter
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    root = customtkinter.CTk()
    root.geometry("750x500")
    root.title("Registration Form")
    
    
    
    

    
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=80, fill="both", expand=True)

    label= customtkinter.CTkLabel(master=frame, text="Registration Form")
    label.pack(pady=12, padx=10)

    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Name")
    entry1.pack(pady=12, padx=10)

    entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Date Of Birth")
    entry2.pack(pady=12, padx=10)

    entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="Gender")
    entry3.pack(pady=12, padx=10)

    entry4 = customtkinter.CTkEntry(master=frame, placeholder_text="Mobile number")
    entry4.pack(pady=12, padx=10)

    entry5 = customtkinter.CTkEntry(master=frame, placeholder_text="Address")
    entry5.pack(pady=12, padx=10)
    
    button = customtkinter.CTkButton(master=frame, text="Submit",command=registration)
    button.pack(pady=12, padx=10)
    root.mainloop()

    


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=80, fill="both", expand=True)

label= customtkinter.CTkLabel(master=frame, text="Login System")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login" , command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

                              
root.mainloop()
