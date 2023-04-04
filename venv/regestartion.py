from tkinter import *
from tkinter import messagebox
from validation import *
from datetime import datetime
import ast
import re
import json
import os
import locale
import tkinter as tk
#

root = Tk()
root.title("FundsEra")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False,False)
##############################################################
users_file = "users.json"
def login(user, code):
    email = user.get()
    password = code.get()

    # Check if email and password match with any user in the database
    users = load_json_data(users_file)
    userr = None  # Initialize user variable before the loop
    for userr in users:
        if userr["email"] == email and userr["password"] == password:

            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
            # screen = Toplevel(root)
            # screen.title("APP")
            # screen.geometry("925x500+300+200")
            # screen.config(bg="white")
            #
            # Label(screen, text='FUNDSRAISING!', bg='#fff', font=('Calibri(Body)', 50, 'bold')).pack(expand=True)
            #
            # screen.mainloop()

            crud = Tk()
            crud.title("FundsEra")
            crud.geometry("925x500+300+200")
            crud.configure(bg="#fff")
            crud.resizable(False, False)

            ###############################################

            #image = PhotoImage(file=r'C:\Users\Speed\PycharmProjects\CRUDoperations\venv\My project-2.png')
            image = PhotoImage(file='My project-2.png')
            # Label(crud, image=image, bg='white').place(x=480, y=5)
            # Label.pack()

            ###############################################
            class FundRaiseCampaign:

                def clear_entries(self):
                    self.title_entry.delete(0, END)
                    self.details_entry.delete(0, END)
                    self.target_entry.delete(0, END)
                    self.start_time_entry.delete(0, END)
                    self.end_time_entry.delete(0, END)

                def __init__(self, master):
                    self.master = master
                    master.title("FundsEra Campaign")

                    # create the output text widget
                    # create the output text widget
                    self.output_text = tk.Text(self.master, height=10, width=95, wrap='word')
                    self.output_text.place(x=25, y=220)
                    # self.output_text.grid(row=9, column=3)
                    # output_text = Text(crud, width=50, height=20)
                    # output_text.grid(row=0, column=0, padx=10, pady=10)

                    # self.campaigns_listbox = tk.Listbox(self.master)
                    # self.campaigns_listbox.pack()

                    # create labels
                    self.title_label = Label(master, text="Title:", fg='black', bg='white',
                                             font=('Microsoft YaHei UI Light', 18, 'bold'))
                    self.details_label = Label(master, text="Details:", fg='black', bg='white',
                                               font=('Microsoft YaHei UI Light', 18, 'bold'))
                    self.target_label = Label(master, text="Total Target:", fg='black', bg='white',
                                              font=('Microsoft YaHei UI Light', 18, 'bold'))
                    self.start_time_label = Label(master, text="Start Time:", fg='black', bg='white',
                                                  font=('Microsoft YaHei UI Light', 18, 'bold'))
                    self.end_time_label = Label(master, text="End Time:", fg='black', bg='white',
                                                font=('Microsoft YaHei UI Light', 18, 'bold'))

                    # create entry boxes
                    self.title_entry = Entry(master, width=35, font=('Microsoft YaHei UI Light', 11))
                    self.details_entry = Entry(master, width=35, font=('Microsoft YaHei UI Light', 11))
                    self.target_entry = Entry(master, width=35, font=('Microsoft YaHei UI Light', 11))
                    self.start_time_entry = Entry(master, width=35, font=('Microsoft YaHei UI Light', 11))
                    self.end_time_entry = Entry(master, width=35, font=('Microsoft YaHei UI Light', 11))

                    # create buttons

                    self.create_button = Button(master, width=11, pady=7, text="Create", bg='#57f864', fg='white',
                                                border=0, font=('Helvetica', 12, 'bold'),
                                                command=self.create_campaign).place(x=740, y=400)
                    # self.create_button.place(x=25, y=204)
                    self.view_button = Button(master, width=11, pady=7, text="View All", bg='#57f864', fg='white',
                                              border=0, font=('Helvetica', 12, 'bold'),
                                              command=self.view_campaigns).place(x=260, y=400)
                    self.edit_button = Button(master, width=11, pady=7, text="Update", bg='#57f864', fg='white',
                                              border=0, font=('Helvetica', 12, 'bold'),
                                              command=lambda: self.update_campaign(self.title_entry.get())).place(x=380,
                                                                                                                  y=400)
                    self.delete_button = Button(master, width=11, pady=7, text="Delete", bg='#57f864', fg='white',
                                                border=0, font=('Helvetica', 12, 'bold'),
                                                command=lambda: self.delete_campaign(self.title_entry.get())).place(
                        x=500, y=400)
                    self.search_button = Button(master, width=11, pady=7, text="Search", bg='#57f864', fg='white',
                                                border=0, font=('Helvetica', 12, 'bold'),
                                                command=lambda: self.search_campaign(self.title_entry.get())).place(
                        x=620, y=400)

                    # grid layout
                    self.title_label.grid(row=0, column=0)
                    self.details_label.grid(row=1, column=0)
                    self.target_label.grid(row=2, column=0)
                    self.start_time_label.grid(row=3, column=0)
                    self.end_time_label.grid(row=4, column=0)
                    self.title_entry.grid(row=0, column=1)
                    self.details_entry.grid(row=1, column=1)
                    self.target_entry.grid(row=2, column=1)
                    self.start_time_entry.grid(row=3, column=1)
                    self.end_time_entry.grid(row=4, column=1)
                    # self.create_button.grid(row=5, column=0)
                    # self.view_button.grid(row=5, column=1)
                    # self.edit_button.grid(row=5, column=2)
                    # self.delete_button.grid(row=5, column=3)
                    # self.search_button.grid(row=5, column=4)

                    # create a button to update the output text widget
                    self.update_button = Button(master, width=11, pady=7, text="Clear", bg='#57f864', fg='white',
                                                border=0, font=('Helvetica', 12, 'bold'),
                                                command=self.update_output_text).place(x=25, y=400)

                # self.update_button.grid(row=5, column=5)
                # self.create_button.grid_forget()

                def update_output_text(self):
                    # clear the output text widget
                    self.output_text.delete("1.0", END)

                    # add new text to the output text widget
                    self.output_text.insert(END, "")

                def create_campaign(self):
                    title = self.title_entry.get()
                    details = self.details_entry.get()
                    target = self.target_entry.get()
                    start_time = self.start_time_entry.get()
                    end_time = self.end_time_entry.get()
                    if not title or not details or not target or not start_time or not end_time:
                        messagebox.showerror("Error", "All fields are required.")
                        return
                    try:
                        target = int(target)
                    except ValueError:
                        messagebox.showerror("Error", "Total Target must be an integer.")
                        return
                    try:
                        locale.setlocale(locale.LC_TIME, "en_US")
                        start_time = datetime.strptime(start_time, "%d/%m/%y")
                        end_time = datetime.strptime(end_time, "%d/%m/%y")
                    except ValueError:
                        messagebox.showerror("Error", "Invalid date format. Use the following format: DD/MM/YY ")
                        return
                    if start_time > end_time:
                        messagebox.showerror("Error", "Start time must be before end time.")
                        return

                    campaign = {
                        "title": title,
                        "details": details,
                        "target": target,
                        "start_time": start_time.strftime("%d/%m/%Y"),
                        "end_time": end_time.strftime("%d/%m/%Y")
                    }

                    with open("campaigns.json", "a") as file:
                        json.dump(campaign, file)
                        file.write("\n")
                    self.clear_entries()

                    messagebox.showinfo('Campaign', 'Campaign created')

                def view_campaigns(self):
                    try:
                        with open("campaigns.json", "r") as file:
                            campaigns = file.readlines()
                    except FileNotFoundError:
                        self.output_text.insert('end', "No campaigns found.")
                        return

                    if campaigns:
                        for campaign in campaigns:
                            self.output_text.insert('end', campaign)
                    else:
                        self.output_text.insert('end', "No campaigns found.")

                def delete_campaign(self, title):
                    try:
                        with open("campaigns.json", "r") as file:
                            campaigns = file.readlines()
                    except FileNotFoundError:
                        messagebox.showerror("Error", "No campaigns found.")
                        return

                    with open("campaigns.json", "w") as file:
                        for campaign in campaigns:
                            campaign_dict = json.loads(campaign)
                            if campaign_dict['title'] != title:
                                json.dump(campaign_dict, file)
                                file.write("\n")
                    self.clear_entries()
                    messagebox.showinfo('Campagin', 'Deleted Succesfully')

                def search_campaign(self, title):
                    try:
                        with open("campaigns.json", "r") as file:
                            campaigns = file.readlines()
                    except FileNotFoundError:
                        messagebox.showerror("Error", "No campaigns found.")
                        # self.output_text.insert('end', "No campaigns found.")
                        return

                    if campaigns:
                        for campaign in campaigns:
                            campaign_data = json.loads(campaign)
                            if campaign_data['title'] == title:
                                self.output_text.insert('end', campaign)
                                break
                        else:
                            messagebox.showerror("Error", "This campaign is not found.")
                            # self.output_text.insert('end', "This campaign is not found.")
                    else:
                        messagebox.showerror("Error", "No campaigns found.")
                        # self.output_text.insert('end', "No campaigns found.")

                def update_campaign(self, title):
                    try:
                        with open("campaigns.json", "r") as file:
                            campaigns = file.readlines()
                    except FileNotFoundError:
                        messagebox.showerror("Error", "No campaigns found.")
                        return

                    updated_campaign = {}
                    for campaign in campaigns:
                        campaign_dict = json.loads(campaign)
                        if campaign_dict['title'] == title:
                            updated_title = self.title_entry.get()
                            updated_details = self.details_entry.get()
                            updated_target = self.target_entry.get()
                            updated_start_time = self.start_time_entry.get()
                            updated_end_time = self.end_time_entry.get()

                            if updated_title:
                                campaign_dict['title'] = updated_title
                            if updated_details:
                                campaign_dict['details'] = updated_details
                            if updated_target:
                                try:
                                    updated_target = int(updated_target)
                                    campaign_dict['target'] = updated_target
                                except ValueError:
                                    messagebox.showerror("Error", "Total Target must be an integer.")
                                    return
                            if updated_start_time:
                                try:
                                    locale.setlocale(locale.LC_TIME, "en_US")
                                    updated_start_time = datetime.strptime(updated_start_time, "%d/%m/%y")
                                    campaign_dict['start_time'] = updated_start_time.strftime("%d/%m/%Y")
                                except ValueError:
                                    messagebox.showerror("Error",
                                                         "Invalid date format. Use the following format: DD/MM/YY ")
                                    return
                            if updated_end_time:
                                try:
                                    locale.setlocale(locale.LC_TIME, "en_US")
                                    updated_end_time = datetime.strptime(updated_end_time, "%d/%m/%y")
                                    campaign_dict['end_time'] = updated_end_time.strftime("%d/%m/%Y")
                                except ValueError:
                                    messagebox.showerror("Error",
                                                         "Invalid date format. Use the following format: DD/MM/YY ")
                                    return

                            updated_campaign = campaign_dict
                            break
                    else:
                        messagebox.showerror("Error", "This campaign is not found.")
                        return

                    with open("campaigns.json", "w") as file:
                        for campaign in campaigns:
                            campaign_dict = json.loads(campaign)
                            if campaign_dict['title'] != title:
                                json.dump(campaign_dict, file)
                                file.write("\n")
                        json.dump(updated_campaign, file)
                        file.write("\n")

                    self.clear_entries()
                    messagebox.showinfo('Campaign', 'Campaign updated successfully.')

            #########################################
            app = FundRaiseCampaign(crud)
            crud.mainloop()
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
            user = userr
            break  # Exit the loop once the user is found

    if user is None:
        messagebox.showerror('Invalid',"Incorrect email or password! Please try again.")
        #messagebox.destroy()
        # print(f"{r}Incorrect email or password! Please try again.{r1}")
        return None
    else:
        return user
#****************************************************************************

def signup_command():
    window=Toplevel(root)
    #window = Tk()
    window.title("FundsEra ©BassantAhmed")
    window.geometry("925x500+300+200")
    window.configure(bg="#fff")
    window.resizable(False, False)

    #######################

    # Define a list to store registered users
    # users = []

    # class User:
    #     def __init__(self, fname, lname, email, password, phone):
    #         self.fname = fname
    #         self.lname = lname
    #         self.email = email
    #         self.password = password
    #         self.phone = phone

    # Function to validate email
    def validate_email(email):
        email_pattern = r"[^@]+@[^@]+\.[^@]+"
        return re.match(email_pattern, email)

    # validated against Egyptian phone numbers
    def validate_mobile(phone):
        mobile_pattern = r"(01)[0125][0-9]{8}"
        return re.match(mobile_pattern, phone)

    ##########fn()#########################
    users = []
    users_file = "users.json"

    def signup():
        Firstname = fname.get()
        Lastname = lname.get()
        email = user.get()
        while not validate_email(email):
            messagebox.showerror('Invalid', 'Invalid Email')
            messagebox.destroy()

        password = code.get()
        copassword = ccode.get()
        while password != copassword:
            messagebox.showerror('Invalid', 'Password does not match')
            messagebox.destroy()

        mobphone = phone.get()
        while not validate_mobile(phone.get()):
            messagebox.showerror('Invalid', 'Invalid mobile phone format')
            messagebox.destroy()

        # Define the user details dictionary
        users_file = "users.json"

        # Add user to database
        userr = {
            "first_name": Firstname,
            "last_name": Lastname,
            "email": email,
            "password": password,
            "phone_number": mobphone
        }
        users.append(userr)
        save_json_data(users_file, users)

        messagebox.showinfo('Regestration', 'Regestration Succed')
        window.destroy()

    def sign():
        window.destroy()
    ########Image#########################
    img = PhotoImage(file='crowd_adobe_express.png')
    Label(window, image=img, bg='white').place(x=480, y=20)
    # *********
    # fframe=Frame(window,width=350,height=80,bg="yellow")
    # fframe.place(x=495,y=370)
    # *********
    frame = Frame(window, width=400, height=460, bg="white")
    frame.place(x=70, y=20)

    heading = Label(frame, text='Registrate', fg='#57f864', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=80, y=5)

    #################Reg############################

    # -----FName------#
    def on_enter(e):
        fname.delete(0, 'end')

    def on_leave(e):
        name = fname.get()
        if name == '':
            fname.insert(0, "First Name")

    fname = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    fname.place(x=30, y=80)
    fname.insert(0, 'First Name')
    fname.bind('<FocusIn>', on_enter)
    fname.bind('<FocusOut>', on_leave)

    Frame(frame, width=259, height=2, bg='black').place(x=25, y=107)

    # ----LName----#
    def on_enter(e):
        lname.delete(0, 'end')

    def on_leave(e):
        name = lname.get()
        if name == '':
            lname.insert(0, "Last Name")

    lname = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    lname.place(x=30, y=150)
    lname.insert(0, 'Last Name')
    lname.bind('<FocusIn>', on_enter)
    lname.bind('<FocusOut>', on_leave)

    Frame(frame, width=259, height=2, bg='black').place(x=25, y=177)

    # ----email----#
    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name == '':
            user.insert(0, "Email")

    user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    user.place(x=30, y=220)
    user.insert(0, 'Email')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame, width=259, height=2, bg='black').place(x=25, y=247)

    # ----Password---#
    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        name = code.get()
        if name == '':
            code.insert(0, "Password")

    code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    code.place(x=30, y=290)
    code.insert(0, 'Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    Frame(frame, width=259, height=2, bg='black').place(x=25, y=317)

    # ---PConfirm---#
    def on_enter(e):
        ccode.delete(0, 'end')

    def on_leave(e):
        name = ccode.get()
        if name == '':
            ccode.insert(0, "Confirm Password")

    ccode = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    ccode.place(x=30, y=360)
    ccode.insert(0, 'Confirm Password')
    ccode.bind('<FocusIn>', on_enter)
    ccode.bind('<FocusOut>', on_leave)

    Frame(frame, width=259, height=2, bg='black').place(x=25, y=387)

    # ---Phone---#
    def on_enter(e):
        phone.delete(0, 'end')

    def on_leave(e):
        name = phone.get()
        if name == '':
            phone.insert(0, "Your Mobile number(+20)")

    phone = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    phone.place(x=30, y=430)
    phone.insert(0, 'Your Mobile number(+20)')
    phone.bind('<FocusIn>', on_enter)
    phone.bind('<FocusOut>', on_leave)

    Frame(frame, width=259, height=2, bg='black').place(x=25, y=457)

    ############################
    ##button##

    Button(window, width=39, pady=7, text='Sign-up', bg='#57f864', fg='white', border=0, command=signup).place(x=555,
                                                                                                               y=375)
    label = Label(window, text="I have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
    label.place(x=560, y=420)

    login = Button(window, width=7, text='Login', border=0, bg='white', cursor='hand2', fg='#57f864',command=sign)
    login.place(x=680, y=422)

    # cpy=Label(window,text="©BassantAhmed",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    # cpy.place(x=370,y=390)
    window.mainloop()



#*************************************************************************************************

###########################################################
img=PhotoImage(file='crowd_adobe_express.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Login',fg='#57f864',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

#########User email##############
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,"Email")


user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Email')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=259,height=2,bg='black').place(x=25,y=107)
##########Pass#############
def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):
    name = code.get()
    if name == '':
        user.insert(0, "Password")


code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=259,height=2,bg='black').place(x=25,y=177)
############Login button############
Button(frame,width=39,pady=7,text='Login',bg='#57f864',fg='white',border=0,command=lambda: login(user, code)).place(x=25,y=204)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

registrate=Button(frame,width=7,text='Registrate',border=0,bg='white',cursor='hand2',fg='#57f864',command=signup_command)
registrate.place(x=215,y=270)
############COPYRIGHT################
cpy=Label(root,text="©BassantAhmed",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
cpy.place(x=370,y=390)
############################


#############################
root.mainloop()