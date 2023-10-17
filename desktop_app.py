import tkinter as tk
from tkinter import *
from tkinter.ttk import * 

from graphing import graph_results
from calculate import run_calculations

background_colour = '#161b1c'
button_bg_colour = '#20272b'

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('400x1000')
        self.configure(background=background_colour)
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
        tk.Frame.__init__(self, master, bg=background_colour, borderwidth=1)

        window_label = tk.Label(self, 
                                 text="Genetic algorith for optimization in Rana function",                 
                                 bg=background_colour,
                                 font=('arial', 10, 'bold'),
                                 borderwidth = '0',
                                 fg="white").pack(pady=15, padx=25)
        range_start_label = tk.Label(self, 
                                 text="Enter range start:",                 
                                 bg=background_colour,
                                 font=('arial', 10),
                                 borderwidth = '0',
                                 fg="white").pack(pady=5, padx=25)

        range_start = tk.Text(self, 
                          height=1, 
                          width=5).pack(pady=5, padx=25)
        
        range_end_label = tk.Label(self, 
                                 text="Enter range end",                 
                                 bg=background_colour,
                                 font=('arial', 10),
                                 borderwidth = '0',
                                 fg="white").pack(pady=5, padx=25)

        range_end = tk.Text(self, 
                          height=1, 
                          width=5).pack(pady=5, padx=25)
        
        percent_label = tk.Label(self, 
                                 text="Enter percent for select best:",                 
                                 bg=background_colour,
                                 font=('arial', 10),
                                 borderwidth = '0',
                                 fg="white").pack(pady=5, padx=25)

        percent = tk.Text(self, 
                          height=1, 
                          width=5).pack(pady=5, padx=25)
        
        tournament_size_label = tk.Label(self, 
                                        text="Enter tournament size",                 
                                        bg=background_colour,
                                        font=('arial', 10),
                                        borderwidth = '0',
                                        fg="white").pack(pady=5, padx=25)

        tournament_size = tk.Text(self, 
                                height=1, 
                                width=5).pack(pady=5, padx=25)

        cross_probablity_label = tk.Label(self, 
                                        text="Enter cross probability",                 
                                        bg=background_colour,
                                        font=('arial', 10),
                                        borderwidth = '0',
                                        fg="white").pack(pady=5, padx=25)

        cross_probablity_size = tk.Text(self, 
                                height=1, 
                                width=5).pack(pady=5, padx=25)
        

        mutation_probablity_label = tk.Label(self, 
                                        text="Enter mutation probability",                 
                                        bg=background_colour,
                                        font=('arial', 10),
                                        borderwidth = '0',
                                        fg="white").pack(pady=5, padx=25)

        mutation_probablity_size = tk.Text(self, 
                                height=1, 
                                width=5).pack(pady=5, padx=25)

        inversion_probablity_label = tk.Label(self, 
                                        text="Enter inversion probability",                 
                                        bg=background_colour,
                                        font=('arial', 10),
                                        borderwidth = '0',
                                        fg="white").pack(pady=5, padx=25)

        inversion_probablity_size = tk.Text(self, 
                                height=1, 
                                width=5).pack(pady=5, padx=25)

        # checkbox for minimalisation problem
        roulette_checkbox = tk.Checkbutton(self, 
                                           text="Minimalisation problem", 
                                           bg=background_colour,
                                           font=('arial', 10, 'bold'),
                                           borderwidth = '0',
                                        #    fg="white", for whatever reason this makes the checkbox unclickable
                                           onvalue=1, 
                                           offvalue=0).pack(pady=5, padx=25)

        selection_methods = [
            "Pick a selection method",
            "Select best",
            "Roulette",
            "Tournament",
        ]

        selection_clicked = StringVar()
        selection_clicked.set(selection_methods[0])
  
        selection_drop = OptionMenu(self, 
                          selection_clicked, 
                          *selection_methods).pack(pady=5, padx=25)

        cross_methods = [
            "Pick a crossover method",
            "1 Point",
            "2 Point",
            "3 Point",
            "Uniform"
        ]

        cross_clicked = StringVar()
        cross_clicked.set(cross_methods[0])
  
        cross_drop = OptionMenu(self, 
                          cross_clicked, 
                          *cross_methods).pack(pady=5, padx=25)
        
        mutation_methods = [
            "Pick a mutation method",
            "Edge",
            "1 Point",
            "2 Point"
        ]

        mutation_clicked = StringVar()
        mutation_clicked.set(mutation_methods[0])
  
        mutation_drop = OptionMenu(self, 
                          mutation_clicked, 
                          *mutation_methods).pack(pady=5, padx=25)

        tk.Button(self,
                text="Calculate!",
                command=lambda: [run_calculations(str(selection_clicked.get())), master.switch_frame(ResultsPage)],
                bg=button_bg_colour,
                font=('arial', 10, 'bold'),
                borderwidth = '0',
                fg="white").pack(pady=5, padx=25)
        
class ResultsPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg=background_colour, borderwidth=1) 

        window_label = tk.Label(self, 
                                 text="Genetic algorith for optimization in Rana function - Results:",                 
                                 bg=background_colour,
                                 font=('arial', 10, 'bold'),
                                 borderwidth = '0',
                                 fg="white").pack(pady=15, padx=25, side='top')

        tk.Button(self,
                text="See plots",
                command=lambda: graph_results(),
                bg=button_bg_colour,
                font=('arial', 10, 'bold'),
                borderwidth='0',
                fg="white").pack(pady=5, padx=25)
        
        tk.Button(self,
            text="OK",
            command=lambda: master.quit(),
            bg=button_bg_colour,
            font=('arial', 10, 'bold'),
            borderwidth='0',
            fg="white").pack(pady=5, padx=25)
        

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()