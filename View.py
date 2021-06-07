import tkinter as tk
from tkinter import ttk


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
        for F in (StartPage, Backup, organized, Cleaner,SetBackup,InstentBackup):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.configure(bg="#6b9dc2")
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

        # label of frame Layout 2
        label = ttk.Label(self, text="Startpage")

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = tk.Button(self, text="Backup", height = '4', width = '12', bg='#6b9dc2',borderwidth=4,
                            command=lambda: controller.show_frame("Backup"))

        # putting the button in its place by
        # using grid
        button1.grid(row=2, column=4, padx=100, pady=50)

        button2 = tk.Button(self, text="organized", height = '4', width = '12', bg='#6b9dc2',borderwidth=4,
                            command=lambda: controller.show_frame("organized"))

        button2.grid(row=2, column=6, padx=100, pady=50)

        button3 = tk.Button(self, text="Cleaner", height='4', width='12', bg='#6b9dc2',borderwidth=4,
                            command=lambda: controller.show_frame("Cleaner"))

        button3.grid(row=4, column=5, padx=10, pady=10)

class Backup(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #lable=tk.Label(self,text="Backup",bg="#6b9dc2")
        #lable.grid(row=0,column=5)

        #function to call new browse_window
        def browse_window():
            top=tk.Toplevel(bg='#6b9dc2')
            top.pack(padt=20)

        #button for browser window

        button = tk.Button(self, text="Home", height='1', width='5', bg='white', borderwidth=2,
                           command=lambda: controller.show_frame("StartPage"))

        button.grid(row=0, column=1, padx=5, pady=5)

        browse_btn = tk.Button(self, text="InstentBackup", height='4', width='12', bg='#6b9dc2',borderwidth=4,command=lambda: controller.show_frame("InstentBackup"))

        browse_btn.grid(row=3, column=3, padx=10, pady=40)
        browse_btn = tk.Button(self, text="SetBackup", height='4', width='12', bg='#6b9dc2',borderwidth=4,command=lambda: controller.show_frame("SetBackup"))

        browse_btn.grid(row=4, column=3, padx=10, pady=40)





class organized(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #label = ttk.Label(self, text="organized")
        #label.grid(row=0, column=4, padx=10, pady=10)

        button = tk.Button(self, text="Back", height = '1', width = '5', bg='white', borderwidth=2,
                            command=lambda: controller.show_frame("StartPage"))

        # putting the button in its place by
        # using grid
        button.grid(row=0, column=1, padx=10, pady=10)
        Browse_btn = tk.Button(self, text="upload", height = '2', width = '14',bg='#6b9dc2',borderwidth=5)

        Browse_btn.grid(row=4, column=6, padx=100, pady=200)
        Browse_btn = tk.Button(self, text="browse", height = '2', width = '14',bg='#6b9dc2',borderwidth=5)

        Browse_btn.grid(row=4, column=7, padx=10, pady=10)

class Cleaner(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #label = ttk.Label(self, text="Page 3")
        #label.grid(row=0, column=4, padx=10, pady=10)

        button = tk.Button(self, text="Back", height = '1', width = '5', bg='white', borderwidth=2,
                            command=lambda: controller.show_frame("StartPage"))

        # putting the button in its place by
        # using grid
        button.grid(row=0, column=1, padx=10, pady=10)


class SetBackup(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #label = ttk.Label(self, text="Backup")
        #label.grid(row=0, column=4, padx=10, pady=10)

        button = tk.Button(self, text="Back", height = '1', width = '5', bg='white',borderwidth=2,
                            command=lambda: controller.show_frame("Backup"))

        # putting the button in its place by
        # using grid
        button.grid(row=0, column=1, padx=10, pady=10)
        label_frequency= tk.Label(self, text="Frequency", bg="#6b9dc2", font="bold")
        label_frequency.grid(row=4, column=4, padx=10, pady=10)
        frequency=tk.Entry(self)
        frequency.grid(row=4,column=5,padx=10,pady=10)
        #label_browse = ttk.Label(self, text="Choose desire browser!!")
        #label_browse.grid(row=2, column=3, padx=10, pady=10)
        Browse_btn = tk.Button(self, text="Browse", height = '2', width = '14',bg='#6b9dc2',borderwidth=5)

        Browse_btn.grid(row=2, column=4, padx=80, pady=50)
        browse_entry = tk.Entry(self, width='40')
        browse_entry.grid(row=2, column=5, padx=10, pady=10)
        upload_btn = tk.Button(self, text="upload", height = '2', width = '14',bg='#6b9dc2',borderwidth=5)

        upload_btn.grid(row=5, column=4, padx=10, pady=10)
class InstentBackup(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        def browse_window():
            top=tk.Toplevel(bg='#6b9dc2')
            top.pack(padt=20)
        #label = tk.Label(self, text="InstentBackup")
        #label.grid(row=0, column=4, padx=10, pady=10)

        button = tk.Button(self, text="Back", height = '1', width = '5', bg='white',borderwidth=2,
                            command=lambda: controller.show_frame("Backup"))
        # putting the button in its place by
        # using grid
        button.grid(row=0, column=1, padx=10, pady=10)
        #label_browse = tk.Label(self, text="Choose desire browser", bg="#6b9dc2")
        #label_browse.grid(row=2, column=3, padx=10, pady=10)
        Browse_btn = tk.Button(self, text="Browse", height = '2', width = '14',bg='#6b9dc2',borderwidth=5,command=browse_window)

        Browse_btn.grid(row=2, column=4, padx=80, pady=50)
        browse_entry=tk.Entry(self, width = '40')
        browse_entry.grid(row=2,column=5,padx=10,pady=10)
        upload_btn = tk.Button(self, text="upload", height = '2', width = '14',bg='#6b9dc2',borderwidth=5)
        upload_btn.grid(row=4,column=4, padx=10, pady=10)



if __name__ == "__main__":
    app = fileeazeApp()
    app.mainloop()
