from time import sleep
import tkinter as tk
from tkinter import *
from tkinter.ttk import * 

from graphing import graph_results
from calculate import Calculations

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
                                 fg="white").pack(pady=5, padx=25)
        
        range_start_label = tk.Label(self, 
                                 text="Enter range start:",                 
                                 bg=background_colour,
                                 font=('arial', 10),
                                 borderwidth = '0',
                                 fg="white").pack(pady=5, padx=25)

        range_start = tk.Text(self, 
                          height=1, 
                          width=5)
        range_start.pack(pady=5, padx=25)
        
        
        range_end_label = tk.Label(self, 
                                 text="Enter range end",                 
                                 bg=background_colour,
                                 font=('arial', 10),
                                 borderwidth = '0',
                                 fg="white").pack(pady=5, padx=25)

        range_end = tk.Text(self, 
                          height=1, 
                          width=5)
        range_end.pack(pady=5, padx=25)
        
        epoch_label = tk.Label(self, 
                                 text="Enter number of epochs:",                 
                                 bg=background_colour,
                                 font=('arial', 10),
                                 borderwidth = '0',
                                 fg="white").pack(pady=5, padx=25)

        epoch = tk.Text(self, 
                          height=1, 
                          width=5)
        epoch.pack(pady=5, padx=25)
        
        elite_strategy_label = tk.Label(self, 
                                        text="Enter elite strategy [%]",                 
                                        bg=background_colour,
                                        font=('arial', 10),
                                        borderwidth = '0',
                                        fg="white").pack(pady=5, padx=25)

        elite_strategy = tk.Text(self, 
                                height=1, 
                                width=5)
        elite_strategy.pack(pady=5, padx=25)
        
        cross_probability_label = tk.Label(self, 
                                        text="Enter cross probability [%]",                 
                                        bg=background_colour,
                                        font=('arial', 10),
                                        borderwidth = '0',
                                        fg="white").pack(pady=5, padx=25)

        cross_probability_size = tk.Text(self, 
                                height=1, 
                                width=5)
        cross_probability_size.pack(pady=5, padx=25)
        

        mutation_probability_label = tk.Label(self, 
                                        text="Enter mutation probability [%]",                 
                                        bg=background_colour,
                                        font=('arial', 10),
                                        borderwidth = '0',
                                        fg="white").pack(pady=5, padx=25)

        mutation_probability_size = tk.Text(self, 
                                height=1, 
                                width=5)
        mutation_probability_size.pack(pady=5, padx=25)

        inversion_probability_label = tk.Label(self, 
                                        text="Enter inversion probability [%]",                 
                                        bg=background_colour,
                                        font=('arial', 10),
                                        borderwidth = '0',
                                        fg="white").pack(pady=5, padx=25)

        inversion_probability_size = tk.Text(self, 
                                height=1, 
                                width=5)
        inversion_probability_size.pack(pady=5, padx=25)

        # checkbox for minimalisation problem
        state = IntVar()
        roulette_checkbox = tk.Checkbutton(self, 
                                           text="Minimalisation problem", 
                                           bg=background_colour,
                                           font=('arial', 10, 'bold'),
                                           borderwidth = '0',
                                        # fg="white", for whatever reason this makes the checkbox unclickable
                                           variable=state, 
                                           )
        roulette_checkbox.pack(pady=5, padx=25)

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
        
        percent_label = tk.Label(self, 
                                 text="Enter percent for select best [%]",                 
                                 bg=background_colour,
                                 font=('arial', 10),
                                 borderwidth = '0',
                                 fg="white").pack(pady=5, padx=25)

        percent = tk.Text(self, 
                          height=1, 
                          width=5)
        percent.pack(pady=5, padx=25)
        
        tournament_size_label = tk.Label(self, 
                                        text="Enter tournament size",                 
                                        bg=background_colour,
                                        font=('arial', 10),
                                        borderwidth = '0',
                                        fg="white").pack(pady=5, padx=25)

        tournament_size = tk.Text(self, 
                                height=1, 
                                width=5)
        tournament_size.pack(pady=5, padx=25)

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
                command=lambda: [Calculations.run_calculations(
                                 range_start.get(1.0, "end-1c"), 
                                 range_end.get(1.0, "end-1c"), 
                                 epoch.get(1.0, "end-1c"),
                                 elite_strategy.get(1.0, "end-1c"),
                                 cross_probability_size.get(1.0, "end-1c"),
                                 mutation_probability_size.get(1.0, "end-1c"),
                                 inversion_probability_size.get(1.0, "end-1c"),
                                 str(selection_clicked.get()), 
                                 percent.get(1.0, "end-1c"),
                                 tournament_size.get(1.0, "end-1c"),
                                 str(cross_clicked.get()), 
                                 str(mutation_clicked.get()),
                                 bool(state.get())),
                                 master.switch_frame(ResultsPage)],
                bg=button_bg_colour,
                font=('arial', 10, 'bold'),
                borderwidth = '0',
                fg="white").pack(pady=5, padx=25)
        
        tk.Button(self,
                text="See plots",
                command=lambda: graph_results(),
                bg=button_bg_colour,
                font=('arial', 10, 'bold'),
                borderwidth='0',
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

        time_result = tk.Label(self, 
                               text=f"Working time: {Calculations.algorithm_time}", 
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