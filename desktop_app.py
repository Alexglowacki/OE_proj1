import tkinter as tk
from tkinter import *
from tkinter.ttk import * 

from graphing import graph_values
from calculate import run_calculations

glob_method = ''

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('400x600')
        self.configure(background='#161b1c')
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.place(relx=0.5, rely=0.5, anchor=CENTER)

  
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg='#161b1c', borderwidth=1)
        
        def show():
            label.config(text=clicked.get())

        options = [
            "Default choice",
            "Select best",
            "Roulette",
            "Tournament",
        ]


        clicked = StringVar()
        clicked.set("Default choice")
        print(str(clicked.get()))

        drop = OptionMenu(self, clicked, *options,)
        drop.pack()

        tk.Button(self,
                  text="Choose a method", 
                  font=('arial', 10, 'bold'), 
                  bg="#20272b",
                  borderwidth='0', 
                  fg="white", 
                  command=show).pack(side="top")

        label = Label(self, text='')
        label.pack(side="top")

        glob_method = str(clicked.get())
        print(glob_method)

        tk.Button(self,
                  text="Calculate!",
                  command=lambda: master.switch_frame(ResultsPage),
                  bg="#20272b",
                  font=('arial', 10, 'bold'),
                  borderwidth = '0',
                  fg="white").pack(pady=5, padx=25)
        
        tk.Button(self,
                text="See plots",
                command=lambda: graph_values(),
                bg="#20272b",
                font=('arial', 10, 'bold'),
                borderwidth='0',
                fg="white").pack(side="top")
        
      
class ResultsPage(tk.Frame):
    def __init__(self, master):
        f3 = tk.Frame.__init__(self, master, bg='#161b1c')
        tk.Label(self, text="Results").pack(side="top", fill="x", pady=100)

        # hardocded for testing
        print(glob_method)
        run_calculations(method=glob_method)

        # go back button
        tk.Button(self,
                  text="Go back",
                  command=lambda: master.switch_frame(StartPage),
                  bg="#20272b",
                  font=('arial', 10, 'bold'),
                  borderwidth='0',
                  fg="white").pack(side="bottom")  
                
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()