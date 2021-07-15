import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import filedialog,messagebox
import Controller
import os
import time
#from PIL import Image, ImageTk




def start(pb,value_label,root):
    for i in range(100):
        pb['value']=i
        time.sleep(0.01)
        root.update_idletasks()
        value_label.configure(text="Loading.. "+str(i))
        if i==99:
            root.destroy()





def splash():
        splash_root = tk.Tk()
        splash_root.title("")
        splash_root.geometry("500x250")
        splash_root.overrideredirect(True)
        splash_root.eval('tk::PlaceWindow . center')
        bg = tk.PhotoImage(file="C:/Users/lenovo/PycharmProjects/File_Eazee/Photos/App_logo.png")

        # Show image using label
        label1 = tk.Label(splash_root, image=bg)
        label1.place(x=0, y=0)
        pb = ttk.Progressbar(
            splash_root,
            orient='horizontal',
            mode='determinate',
            length=280
        )
        # place the progressbar
        value_label = ttk.Label(splash_root)
        value_label.pack()
        pb.pack( side = tk.BOTTOM)
        start(pb,value_label,splash_root)


        # label


        # start button


        splash_root.mainloop()



# progressbar
splash()
Controller1=Controller.Controller("credfile.txt")

class fileeazeApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others

        container = tk.Frame(self)
        self.eval('tk::PlaceWindow . center')
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Backup, Organizer, Cleaner, SetBackup, InstentBackup):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.

            frame.configure(bg="#2d2d2d")
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        controller.title('FileEaze')
        controller.geometry("700x500")
        controller.resizable(False, False)


        button1 = tk.Button(self, text="Backup", height='4', width='12', bg="#c4c4c4", fg="#000000", relief="raised",
                            borderwidth=4,
                            command=lambda: controller.show_frame("Backup"))

        # putting the button in its place by
        # using grid
        button1.grid(row=2, column=4, padx=100, pady=50)

        button2 = tk.Button(self, text="Organizer", height='4', width='12', bg='#c4c4c4', fg="#000000", relief="raised",
                            borderwidth=4,
                            command=lambda: controller.show_frame("Organizer"))

        button2.grid(row=2, column=6, padx=100, pady=50)

        button3 = tk.Button(self, text="Cleaner", height='4', width='12', bg='#c4c4c4', fg="#000000", relief="raised",
                            borderwidth=4,
                            command=lambda: controller.show_frame("Cleaner"))

        button3.grid(row=2, column=5, padx=10, pady=10)




class Backup(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller




        button = tk.Button(self, text="Back", height='1', width='5', bg='#c4c4c4', borderwidth=2,
                           command=lambda: controller.show_frame("StartPage"))

        button.grid(row=0, column=1, padx=5, pady=5)

        browse_btn1 = tk.Button(self, text="Instant Backup", height='4', width='12', bg='#c4c4c4', relief="raised",
                               borderwidth=4, command=lambda: controller.show_frame("InstentBackup"))

        browse_btn1.grid(row=3, column=3, padx=10, pady=40)
        browse_btn = tk.Button(self, text="Set a Backup", height='4', width='12', bg='#c4c4c4', relief="raised",
                               borderwidth=4, command=lambda: controller.show_frame("SetBackup"))

        browse_btn.grid(row=4, column=3, padx=10, pady=40)


class Organizer(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def fileDialog():
            self.dirname = filedialog.askdirectory(title="Select A Folder")

            text.set(self.dirname)
            Controller1.organizer(self.dirname)



        button = tk.Button(self, text="Back", height='1', width='5', bg='#c4c4c4', borderwidth=2,
                           command=lambda: controller.show_frame("StartPage"))
        text = tk.StringVar()
        text.set("")

        # putting the button in its place by
        # using grid
        button.grid(row=0, column=1, padx=10, pady=10)

        Browse_btn = tk.Button(self, text="Browse", height='2', width='14', bg='#c4c4c4', relief="raised", borderwidth=3,
                               command=fileDialog)

        Browse_btn.grid(row=4, column=3, padx=40, pady=50)
        browse_Label = tk.Label(self, width='40', relief="raised",textvariable=text)

        browse_Label.grid(row=4, column=4, padx=10, pady=10)
        upload_btn = tk.Button(self, text="Organise", height='2', width='14', bg='#c4c4c4', relief="raised", borderwidth=3)
        upload_btn.grid(row=5, column=3, padx=10, pady=10)


class Cleaner(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        def showold():
            self.listbox.delete(0,tk.END)
            a=0
            old_files = Controller1.model.old_files
            for i in old_files:
                self.listbox.insert(0,i)
                a+=1



        old_file_text = tk.StringVar("")
        old_file_label = tk.Label(self,width=100,textvariable=old_file_text,relief="raised")
        old_file_label.bind("Button-1",showold)

        Large_file_text = tk.StringVar("")
        Large_file_label = tk.Label(self,width=100,textvariable=Large_file_text,relief="raised")

        duplicate_file_text = tk.StringVar("")
        duplicate_file_label = tk.Label(self,width=100,textvariable=duplicate_file_text,relief="raised")

        def clean():
            old_file_label.grid_forget()
            duplicate_file_label.grid_forget()
            Large_file_label.grid_forget()
            self.dirname = filedialog.askdirectory(initialdir="/", title="Select A Directory")
            if(self.dirname!=None):
                nF,nD = Controller1.cleaner(self.dirname)#nF---> No. of files cleaned#nD----> no of files deleted
                duplicate_file_text.set("No. of Files Scanned"+str(nF)+"\n No. of files deleted"+str(nD))
                duplicate_file_label.grid(row=2, column=2, padx=10, pady=10,columnspan=5)
                presentor()



        def presentor():
            old_files = Controller1.model.old_files
            large_files = Controller1.model.large_files
            old_file_text.set("Clean "+str(len(old_files))+" Files not Accessed from last Year")
            Large_file_text.set("Clean " + str(len(large_files)) + " Large Files")
            print(len(old_files))
            if len(old_files)>0:
                old_file_label.grid(row=12, column=2, padx=10, pady=10,columnspan=5)
            if len(large_files)>0:
                Large_file_label.grid(row=6, column=2, padx=10, pady=10,columnspan=5)




        button = tk.Button(self, text="Back", height='1', width='5', bg='#c4c4c4', borderwidth=2,
                           command=lambda: controller.show_frame("StartPage"))

        # putting the button in its place by
        # using grid
        button.grid(row=0, column=1, padx=10, pady=10)
        cleaner_button=tk.Button(self, text="Clean Now", height='1', width='8', bg='#c4c4c4', relief="raised", borderwidth=4,
                           command=clean)
        cleaner_button.grid(row=0, column=4, padx=250, pady=10)
        self.scrollbar = tk.Scrollbar(self)
        self.listbox = tk.Listbox(self, height=10,
                          width=30,
                          bg='#c4c4c4',
                          activestyle='dotbox',
                          font="Helvetica",
                          fg="yellow",yscrollcommand=self.scrollbar.set)


class SetBackup(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.dirname=None
        def fileDialog():
            print("check")
            self.dirname = filedialog.askdirectory(initialdir="/", title="Select A Directory")

        def upload():
            print("Executing....")
            try:
                upload_btn["state"] = tk.DISABLED
                print("Executing....")

                try:
                    print("Executing....")
                    Controller1.authenticator()
                    try:
                        Controller1.setbackup(self.dirname,frequency)
                    except Exception as e:
                        print(e)
                        messagebox.showerror("Upload Failed", "Please Check Your Network")
                except Exception as e:
                    print(e)
                    messagebox.showerror("Authentification Failed", "Please try Again!!")
            except Exception as e:
                print(e)

        button = tk.Button(self, text="Back", height='1', width='5', bg='#c4c4c4', borderwidth=2,
                           command=lambda: controller.show_frame("Backup"))

        # putting the button in its place by
        # using grid
        button.grid(row=0, column=1, padx=10, pady=10)
        label_frequency = tk.Label(self, text="   Frequency   ", bg='#2d2d2d', fg='#c4c4c4', relief="raise", font="ariel")
        label_frequency.grid(row=4, column=4, padx=10, pady=10)
        frequency = tk.Entry(self, relief="raised")
        frequency.grid(row=4, column=5, padx=10, pady=10)

        Browse_btn = tk.Button(self, text="Browse", height='2', width='14', bg='#c4c4c4', relief="raised",
                               borderwidth=3,
                               command= fileDialog)

        Browse_btn.grid(row=2, column=4, padx=80, pady=50)
        browse_entry = tk.Entry(self, width='40', relief="raised")
        browse_entry.grid(row=2, column=5, padx=10, pady=10)
        upload_btn = tk.Button(self, text="upload", height='2', width='14', bg='#c4c4c4', relief="raised",
                               borderwidth=3,command=upload)

        upload_btn.grid(row=5, column=4, padx=10, pady=10)




class InstentBackup(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.filename=None
        self.filelist=[]

        def browse_window():
            top = tk.Toplevel(bg='#6b9dc2')
            top.pack(padt=20)

        def enable(children):
            for child in children:
                try:
                    if type(child)==tk.Button:
                        child.configure(state='active')
                except:
                    pass
        def disable(children):
            for child in children:
                try:
                    if type(child)==tk.Button:
                        child.configure(state='disable')
                except:
                    pass
        def fileDialog():
            for record in self.listbox.get_children():
                self.listbox.delete(record)


            self.filename = filedialog.askopenfilenames(initialdir="/", title="Select Files to Upload")

            a=0
            for i in self.filename:
                name=os.path.basename(i)
                self.listbox.insert(parent="",index='end',iid=a,text="parent",values=(name,i,"Not Uploaded"))
                a+=1
        def deleteSel():
            for i in self.listbox.selection():
                self.listbox.delete(i)
        def upload():
            '''for line in self.listbox.get_children():

                for value in self.listbox.item(line)['values']:
                    self.filelist.append(value[1])'''

            print("Upload Begin")
            try:
                disable(self.winfo_children())

                print("Disabling buttons")
                if self.filename==None:
                    messagebox.showwarning("Warning","Please make a selection!!!")

                try:
                    print("Authentication Begins")
                    Controller1.authenticator()
                    try:
                        Controller1.backup(self.listbox)
                    except Exception as e:
                        print(e)
                        messagebox.showerror("Upload Failed", "Please Check Your Network")
                except Exception as e:
                    print(e)
                    messagebox.showerror("Authentification Failed","Please try Again!!")

            except Exception as e:
                print(e)
            enable(self.winfo_children())


        def addSel():
            fileDialog()

        button = tk.Button(self, text="Back", height='1', width='5', bg='#c4c4c4',fg='#000000', borderwidth=2,
                           command=lambda: controller.show_frame("Backup"))
        # putting the button in its place by
        # using grid
        button.grid(row=0, column=1, padx=10, pady=10)

        Browse_btn = tk.Button(self, text="Browse", height='1', width='8', bg='#c4c4c4',fg='#000000', relief="raised", borderwidth=3,
                               command=fileDialog)

        upload_btn = tk.Button(self, text="upload", height='1', width='8', bg='#c4c4c4',fg='#000000', relief="raised", borderwidth=3,command=upload)

        remove_btn = tk.Button(self, text="-", height='1', width='2', bg='#c4c4c4',fg='#000000',  relief="raised",
                               borderwidth=3,command=deleteSel)


        add_btn = tk.Button(self, text="+", height='1', width='2',fg='#000000',  bg='#c4c4c4', relief="raised",
                               borderwidth=3, command=addSel)



        self.scrollbar = tk.Scrollbar(self)
        self.listbox = ttk.Treeview(self, height=14,




                          yscrollcommand=self.scrollbar.set)
        self.listbox['columns'] = ("Filename","Path","Status")
        self.listbox.column("#0", width=0, stretch=tk.NO)
        self.listbox.column("Filename", width=100, minwidth=25)
        self.listbox.column("Path", width=200, minwidth=25)
        self.listbox.column("Status", width=100, minwidth=25)
        self.listbox.heading('Filename', text='Filename')
        self.listbox.heading('Path', text='Path')
        self.listbox.heading('Status', text='Status')




        self.scrollbar.config(command=self.listbox.yview)

        # Define a label for the list.
        label = tk.Label(self, text="Selected Files", bg="#2d2d2d", fg='#c4c4c4', font = 'bold')

        # insert elements by their
        # index and names.


        # pack the widgets

        Browse_btn.grid(row=2, column=2, padx=10, pady=10)
        upload_btn.grid(row=3, column=2, padx=10, pady=10)

        label.grid(row=0, column=3, padx=10, pady=10)
        self.listbox.grid(row=1, column=3, padx=10, pady=10)
        self.scrollbar.grid(row=1, column=4, padx=10, pady=10)
        remove_btn.grid(row=3, column=3, padx=10, pady=10)
        add_btn.grid(row=2, column=3, padx=10, pady=10)


if __name__ == "__main__":
    app = fileeazeApp()
    app.mainloop()
