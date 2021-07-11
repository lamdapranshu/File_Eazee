
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import filedialog,messagebox
import Controller
from PIL import Image, ImageTk
from plyer import notification




Controller1=Controller.Controller("credfile.txt")


class fileeazeApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others

        container = tk.Frame(self)
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




        button = tk.Button(self, text="Home", height='1', width='5', bg='#c4c4c4', borderwidth=2,
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



        button = tk.Button(self, text="Back", height='1', width='5', bg='#000000', borderwidth=2,
                           command=lambda: controller.show_frame("StartPage"))
        text = tk.StringVar()
        text.set("")

        # putting the button in its place by
        # using grid
        button.grid(row=0, column=1, padx=10, pady=10)

        Browse_btn = tk.Button(self, text="Browse", height='2', width='14', bg='#6b9dc2', relief="raised", borderwidth=3,
                               command=fileDialog)

        Browse_btn.grid(row=2, column=4, padx=80, pady=50)
        browse_Label = tk.Label(self, width='40', relief="raised",textvariable=text)

        browse_Label.grid(row=2, column=5, padx=10, pady=10)
        upload_btn = tk.Button(self, text="upload", height='2', width='14', bg='#6b9dc2', relief="raised", borderwidth=3)
        upload_btn.grid(row=4, column=4, padx=10, pady=10)


class Cleaner(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        def showold():
            print("121")
            self.listbox.delete(0,tk.END)
            a=0
            old_files = Controller1.model.old_files
            for i in old_files:
                self.listbox.insert(0,i)

                a+=1
            self.listbox.grid(row=3, column=2, padx=10, pady=10, columnspan=5)


        old_file_text = tk.StringVar("")
        old_file_label = tk.Button(self,width=100,textvariable=old_file_text,relief="raised",command=showold)
        #old_file_label.bind("Button",showold)

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
                duplicate_file_text.set("No. of Files Scanned "+str(nF)+"\n No. of files deleted "+str(nD))
                duplicate_file_label.grid(row=2, column=2, padx=10, pady=10,columnspan=5)
                presentor()



        def presentor():
            old_files = Controller1.model.old_files
            large_files = Controller1.model.large_files
            old_file_text.set("Clean "+str(len(old_files))+" Files not Accessed from last Year")
            Large_file_text.set("Clean " + str(len(large_files)) + " Large Files")
            print(len(old_files))
            if len(old_files)>0:
                old_file_label.grid(row=6, column=2, padx=10, pady=10,columnspan=5)
            if len(large_files)>0:
                Large_file_label.grid(row=12, column=2, padx=10, pady=10,columnspan=5)




        button = tk.Button(self, text="Back", height='1', width='5', bg='#000000', borderwidth=2,
                           command=lambda: controller.show_frame("StartPage"))

        # putting the button in its place by
        # using grid
        button.grid(row=0, column=1, padx=10, pady=10)
        cleaner_button=tk.Button(self, text="Cleaner", height='1', width='5', bg='#FFFFFF', borderwidth=2,
                           command=clean)
        cleaner_button.grid(row=0, column=5, padx=10, pady=10)
        self.scrollbar = tk.Scrollbar(self)
        self.listbox = tk.Listbox(self, height=10,
                          width=30,
                          bg='#c4c4c4',
                          activestyle='dotbox',
                          font="Helvetica",
                          fg="black",yscrollcommand=self.scrollbar.set)


        class CircularProgressbar(object):

            def __init__(self, canvas, x0, y0, x1, y1, width=2, start_ang=0, full_extent=360):
                self.custom_font = tkFont.Font(family="Helvetica", size=42, weight='bold')
                self.canvas = canvas
                self.x0, self.y0, self.x1, self.y1 = x0 + width, y0 + width, x1 - width, y1 - width
                self.tx, self.ty = (x1 - x0) / 2, (y1 - y0) / 2
                self.width = width
                self.start_ang, self.full_extent = start_ang, full_extent
                # draw static bar outline
                w2 = width / 2
                self.oval_id1 = self.canvas.create_oval(self.x0 - w2, self.y0 - w2,
                                                        self.x1 + w2, self.y1 + w2)
                self.oval_id2 = self.canvas.create_oval(self.x0 + w2, self.y0 + w2,
                                                        self.x1 - w2, self.y1 - w2)
                self.running = False

            def start(self, interval=100):
                self.interval = interval
                self.increment = self.full_extent / interval
                self.extent = 0
                self.arc_id = self.canvas.create_arc(self.x0, self.y0, self.x1, self.y1,
                                                     start=self.start_ang, extent=self.extent,
                                                     width=self.width, style='arc')
                percent = '0%'
                self.label_id = self.canvas.create_text(self.tx, self.ty, text=percent,
                                                        font=self.custom_font)
                self.running = True
                self.canvas.after(interval, self.step, self.increment)

            def step(self, delta):
                """Increment extent and update arc and label displaying how much completed."""
                if self.running:
                    self.extent = (self.extent + delta) % 360
                    self.cur_extent = (self.extent + delta) % 360
                    self.canvas.itemconfigure(self.arc_id, extent=self.cur_extent)
                    percent = '{:.0f}%'.format(round(float(self.cur_extent) / self.full_extent * 100))
                    self.canvas.itemconfigure(self.label_id, text=percent)

                self.after_id = self.canvas.after(self.interval, self.step, delta)

            def toggle_pause(self):
                self.running = not self.running

        class Application(tk.Frame):
            def __init__(self, master=None):
                tk.Frame.__init__(self, master)
                self.grid()
                self.createWidgets()

            def createWidgets(self):
                self.canvas = tk.Canvas(self, width=200, height=200, bg='#000000')
                self.canvas.grid(row=0, column=0, columnspan=2)

                self.progressbar = CircularProgressbar(self.canvas, 0, 0, 200, 200, 20)

                self.pauseButton = tk.Button(self, text='Pause', command=self.pause)
                self.pauseButton.grid(row=1, column=0)
                self.quitButton = tk.Button(self, text='Quit', command=self.quit)
                self.quitButton.grid(row=1, column=1)

            def start(self):
                self.progressbar.start()
                self.mainloop()

            def pause(self):
                self.progressbar.toggle_pause()


class SetBackup(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.dirname=None
        def fileDialog():
            print("Executing")
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

        button = tk.Button(self, text="Back", height='1', width='5', bg='#000000', borderwidth=2,
                           command=lambda: controller.show_frame("Backup"))

        # putting the button in its place by
        # using grid
        button.grid(row=0, column=1, padx=10, pady=10)
        label_frequency = tk.Label(self, text="   Frequency   ", bg="sky blue", relief="raise", font="ariel")
        label_frequency.grid(row=4, column=4, padx=10, pady=10)
        frequency = tk.Entry(self, relief="raised")
        frequency.grid(row=4, column=5, padx=10, pady=10)

        Browse_btn = tk.Button(self, text="Browse", height='2', width='14', bg='#6b9dc2', relief="raised",
                               borderwidth=3,
                               command= fileDialog)

        Browse_btn.grid(row=2, column=4, padx=80, pady=50)
        browse_entry = tk.Entry(self, width='40', relief="raised")
        browse_entry.grid(row=2, column=5, padx=10, pady=10)
        upload_btn = tk.Button(self, text="upload", height='2', width='14', bg='#6b9dc2', relief="raised",
                               borderwidth=3,command=upload)

        upload_btn.grid(row=5, column=4, padx=10, pady=10)




class InstentBackup(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def browse_window():
            top = tk.Toplevel(bg='#6b9dc2')
            top.pack(padt=20)

        def fileDialog():
            self.listbox.delete(0,tk.END)
            self.filename = filedialog.askopenfilenames(initialdir="/", title="Select Files to Upload")
            a=0
            for i in self.filename:
                self.listbox.insert(0,i)
                a+=1
        def deleteSel():
            selected=self.listbox.curselection()
            for i in range(len(selected)):
                self.listbox.delete(i)
        def upload():

            print("Executing....")
            try:
                upload_btn["state"] = tk.DISABLED
                print("Executing....")

                try:
                    print("Executing....")
                    Controller1.authenticator()
                    try:
                        Controller1.backup(self.filename)
                        notifi("Completed","Successfully Uploaded all the files on your drive")
                    except Exception as e:
                        print(e)
                        messagebox.showerror("Upload Failed", "Please Check Your Network")
                except Exception as e:
                    print(e)
                    messagebox.showerror("Authentification Failed","Please try Again!!")

            except Exception as e:
                print(e)
            upload_btn["state"] = tk.NORMAL


        def addSel():
            selected = self.listbox.curselection()
            self.filename = filedialog.askopenfilenames(initialdir="/", title="Select Files to Upload")
            a = 0
            for i in self.filename:
                self.listbox.insert(0, i)
                a += 1

        button = tk.Button(self, text="Back", height='1', width='5', bg='#c4c4c4',fg='#000000', borderwidth=2,
                           command=lambda: controller.show_frame("Backup"))
        # putting the button in its place by
        # using grid
        button.grid(row=0, column=1, padx=10, pady=10)

        Browse_btn = tk.Button(self, text="Browse", height='2', width='14', bg='#c4c4c4',fg='#000000', relief="raised", borderwidth=3,
                               command=fileDialog)

        Browse_btn.grid(row=2, column=4, padx=80, pady=50)

        upload_btn = tk.Button(self, text="upload", height='2', width='14', bg='#c4c4c4',fg='#000000', relief="raised", borderwidth=3,command=upload)
        upload_btn.grid(row=7, column=4, padx=10, pady=10)
        remove_btn = tk.Button(self, text="-", height='1', width='1', bg='#c4c4c4',fg='#000000',  relief="raised",
                               borderwidth=3,command=deleteSel)
        add_btn = tk.Button(self, text="+", height='1', width='1',fg='#000000',  bg='#c4c4c4', relief="raised",
                               borderwidth=3, command=addSel)


        self.scrollbar = tk.Scrollbar(self)
        self.listbox = tk.Listbox(self, height=10,
                          width=30,
                          bg='#c4c4c4',
                          activestyle='dotbox',
                          font="Helvetica",
                          fg="yellow",yscrollcommand=self.scrollbar.set)


        self.scrollbar.config(command=self.listbox.yview)

        # Define a label for the list.
        label = tk.Label(self, text="Selected Files",bg='#2d2d2d')

        # insert elements by their
        # index and names.


        # pack the widgets
        label.grid(row=1, column=6, padx=10, pady=10)
        self.listbox.grid(row=2, column=6, padx=10, pady=10)
        self.scrollbar.grid(row=2, column=9, padx=10, pady=10)
        remove_btn.grid(row=7, column=6, padx=5, pady=5)
        add_btn.grid(row=7, column=7, padx=5, pady=5)

def notifi(title,message,appicon="C:/Users/lenovo/PycharmProjects/File_Eazee/Photos/fileeazee_YQC_icon.ico"):
    notification.notify(
        title=title,
        message=message,
        app_icon=appicon,
        # displaying time
        timeout=2)


if __name__ == "__main__":
    app = fileeazeApp()
    app.mainloop()
