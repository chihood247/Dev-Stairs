from customtkinter import *

from tkinter import ttk

from PIL import Image, ImageTk

from resources import image

from matplotlib.figure import Figure

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

import numpy

import math

class App:
    def __init__(self):
        self.bg = '#404040'
        
        self.framebg = '#4F4F4F'
        
        self.font = 'Manrope'  
        
        self.main = CTk()
        
        self.main.state('zoomed')
        
        self.main.overrideredirect(True)
        
        self.main.config(bg = self.bg)
        
        self.main.update_idletasks()
        
        self.width = self.main.winfo_width()
        
        self.height = self.main.winfo_height()
        
        self.hiddenbg = '#43464B'
        
        self.plotbg = '#A9A9A9'
        
        self.closebtn = CTkButton(
            master = self.main,
            text = '\u00D7',
            font = (self.font, 20, 'bold'),
            text_color = 'white',
            bg_color = self.bg,
            fg_color = self.bg,
            hover_color = 'red',
            corner_radius = 0,
            border_width = 0,
            command = self.main.destroy
            )
        
        self.closebtn.place(relx = 0.965, rely = 0.01, relwidth = 0.03, relheight = 0.03)
        
        self.sideframe = CTkFrame(
            master = self.main,
            fg_color = self.framebg,
            bg_color = self.bg,
            )
        
        self.sideframe.place(relx = 0, rely = 0, relwidth = 0.2, relheight = 1)
        
        self.head_text = CTkLabel(
            master = self.sideframe,
            text = 'Plot Modes',
            font = (self.font, 40, 'bold'),
            text_color = 'white',
            bg_color = self.framebg,
            fg_color = self.framebg,
            )
        
        self.head_text.place(relx = 0.1, rely = 0.05)
        
        self.function = CTkButton(
            master = self.sideframe,
            text = 'Function',
            font = (self.font, 20),
            text_color = 'white',
            fg_color = '#696969',
            bg_color = self.framebg,
            corner_radius = 40,
            border_width = 0,
            hover_color = '#565656',
            command = self.function_mode
            )
        
        self.function.place(relx = 0.1, rely = 0.2, relwidth = 0.8, relheight = 0.1)
        
        self.table = CTkButton(
            master = self.sideframe,
            text = 'Table',
            font = (self.font, 20),
            text_color = 'white',
            fg_color = '#696969',
            bg_color = self.framebg,
            corner_radius = 40,
            border_width = 0,
            hover_color = '#565656',
            command = self.table_mode
            )
        
        self.table.place(relx = 0.1, rely = 0.35, relwidth = 0.8, relheight = 0.1)
        
        self.regression = CTkButton(
            master = self.sideframe,
            text = 'Regression',
            font = (self.font, 20),
            text_color = 'white',
            fg_color = '#696969',
            bg_color = self.framebg,
            corner_radius = 40,
            border_width = 0,
            hover_color = '#565656',
            command = self.reg_mode
            )
        
        self.regression.place(relx = 0.1, rely = 0.5, relwidth = 0.8, relheight = 0.1)
        
        self.vector = CTkButton(
            master = self.sideframe,
            text = 'Vector',
            font = (self.font, 20),
            text_color = 'white',
            fg_color = '#696969',
            bg_color = self.framebg,
            corner_radius = 40,
            border_width = 0,
            hover_color = '#565656',
            command = self.vector_mode
            )
        
        self.vector.place(relx = 0.1, rely = 0.65, relwidth = 0.8, relheight = 0.1)
        
        self.theme_state = IntVar(value = 1)
        
        self.theme_switch = CTkSwitch(
            master = self.sideframe,
            text = '  Dark',
            fg_color = '#F7F7F7',
            progress_color = '#4267B2',
            text_color = 'white',
            button_color = 'white',
            button_hover_color = 'white',
            font = (self.font, 15, 'bold'),
            border_width = 0,
            variable = self.theme_state,
            onvalue = 1,
            offvalue = 0,
            command = self.change_theme
            )
        
        self.theme_switch.place(relx = 0.1, rely = 0.9)
        
        self.mainframe = CTkFrame(
            master = self.main,
            corner_radius = 40,
            bg_color = self.bg,
            fg_color = self.framebg
            )
        
        self.mainframe.place(relx = 0.25, rely = 0.06, relwidth = 0.705, relheight = 0.88)
        
        self.intro_text = CTkLabel(
            master = self.mainframe,
            text = '"Create Something"',
            font = (self.font, 50, 'bold'),
            bg_color = self.bg,
            fg_color = self.framebg,
            text_color = '#FFD700'
            )
        
        self.intro_text.place(relx = 0.25, rely = 0.45)
        
        self.intro_text_attr = {
            'relx': 0.25,
            'rely': 0.45,
            }
        
        def intro_text_event_enter(event):
            self.main.update_idletasks()
            
            if self.theme_state.get() == 1:
                self.intro_text.configure(text_color = '#F7DC6F')
                
            else:
                self.intro_text.configure(text_color = '#4682B4')
            
        def intro_text_event_leave(event):
            self.main.update_idletasks()
            
            if self.theme_state.get() == 1:
                self.intro_text.configure(text_color = '#FFD700')
                
            else:
                self.intro_text.configure(text_color = '#032B44')
            
        self.intro_text.bind('<Enter>', intro_text_event_enter)
        
        self.intro_text.bind('<Leave>', intro_text_event_leave)
        
        self.frame = CTkFrame(
            master = self.mainframe,
            bg_color = self.framebg,
            fg_color = self.hiddenbg,
            corner_radius = 40
            )
        
        self.frame.place(relx = 0.02, rely = 0.02, relwidth = 0.6, relheight = 0.96)
        
        self.frame_attr = {
            'relx': 0.02,
            'rely': 0.02,
            'relwidth': 0.6,
            'relheight': 0.96
            }
        
        self.frame.place_forget()
        
        self.main.update_idletasks()
        
        def close_frame():
            self.frame.place_forget()
            
            self.plotframe.place_forget()
            
            self.intro_text.place(**self.intro_text_attr)
        
        self.frameclose = CTkButton(
            master = self.frame,
            text = '\u00D7',
            text_color = 'white',
            fg_color = self.hiddenbg,
            bg_color = self.hiddenbg,
            hover_color = 'red',
            border_width = 0,
            command = close_frame
            )
        
        self.frameclose.place(
            relx = 0.95,
            rely = 0,
            relwidth = 0.05,
            relheight = 0.05
            )
       
        self.frameclose_attr = {
            'relx': 0.95,
            'rely': 0,
            'relwidth': 0.05,
            'relheight': 0.05
            }
       
        self.frameclose.place_forget()
        
        self.titlebar = CTkLabel(
            master = self.frame,
            text = 'Function',
            text_color = 'white',
            font = (self.font, 30, 'bold'),
            bg_color = self.hiddenbg,
            fg_color = 'gray',
            corner_radius = 30
            )
        
        self.titlebar.place(relx = 0.03, rely = 0.025, relwidth = 0.8, relheight = 0.3)
        
        self.titlebar_attr = {
            'relx': 0.03,
            'rely': 0.025,
            'relwidth': 0.8,
            'relheight': 0.3
            }
        
        self.titlebar.place_forget()
        
        self.plotframe = CTkFrame(
            master = self.mainframe,
            bg_color = self.framebg,
            fg_color = self.plotbg,
            corner_radius = 40
            )
        
        self.plotframe.place(
            relx = 0.65,
            rely = 0.02,
            relwidth = 0.33,
            relheight = 0.96
            )
        
        self.plotframe_attr = {
            'relx': 0.65,
            'rely': 0.02,
            'relwidth': 0.33,
            'relheight': 0.96
            }
        
        self.plotframe.place_forget()
        
        def closeplt():
            self.plotframe.place_forget()
            
            for item in self.config.winfo_children():
                item.place_forget()
        
        self.closepltframe = CTkButton(
            master = self.plotframe,
            text = '\u00D7',
            font = (self.font, 20, 'bold'),
            text_color = 'white',
            bg_color = self.plotbg,
            fg_color = self.plotbg,
            hover_color = 'red',
            corner_radius = 10,
            border_width = 0,
            command = closeplt
            )
        
        self.closepltframe.place(relx = 0.5, rely = 0.01, relwidth = 0.1, relheight = 0.1)
        
        self.closepltframe_attr = {
            'relx': 0.9,
            'rely': 0,
            'relwidth': 0.1,
            'relheight': 0.05
            }
        
        self.closepltframe.place_forget()
        
        self.plt = CTkToplevel(self.main)
        
        self.plt.state('zoomed')
        
        self.plt.overrideredirect(True)
        
        self.plt.config(bg = 'grey')
        
        self.plt.withdraw()
        
        self.closeplt = CTkButton(
            master = self.plt,
            text = '\u00D7',
            text_color = 'white',
            bg_color = 'grey',
            fg_color = 'grey',
            hover_color = 'red',
            command = self.plt.withdraw
            )
        
        self.closeplt.place(relx = 0, rely = 0, relwidth = 0.1, relheight = 0.1)
        
        self.closeplt_attr = {
            'relx': 0.00625,
            'rely': 0.01,
            'relwidth': 0.025,
            'relheight': 0.025
            }
        
        self.closeplt.place_forget()
        
        self.hiddencanvas = CTkCanvas(
            master = self.frame,
            bg = self.hiddenbg,
            height = 2 * self.height,
            bd = 0,
            highlightthickness = 0
            )
        
        self.hiddencanvas.place(relx = 0, rely = 0.3, relwidth = 1)
        
        self.hiddencanvas_attr = {
            'relx': 0,
            'rely': 0.35,
            'relwidth': 1
            }
        
        self.hiddencanvas.place_forget()
        
        self.run()
        
    def change_theme(self):
        if self.theme_state.get() == 0:
            self.bg = '#D5D5D5'
            
            self.framebg = '#B8B8B8'
            
            self.hiddenbg = '#8B8B8B'
            
            self.main.config(bg = self.bg)
            
            self.closebtn.configure(
                text_color = 'black',
                bg_color = self.bg,
                fg_color = self.bg
                )
            
            self.sideframe.configure(
                fg_color = self.framebg,
                bg_color = self.bg
                )
            
            self.mainframe.configure(
                fg_color = self.framebg,
                bg_color = self.bg
                )
            
            self.head_text.configure(
                text_color = 'black',
                fg_color = self.framebg,
                bg_color = self.framebg
                )
            
            self.function.configure(
                text_color = 'black',
                bg_color = self.framebg,
                fg_color = '#D7D7D7',
                hover_color = '#C2C2C2'
                )
            
            self.table.configure(
                text_color = 'black',
                bg_color = self.framebg,
                fg_color = '#D7D7D7',
                hover_color = '#C2C2C2'
                )
            
            self.regression.configure(
                text_color = 'black',
                bg_color = self.framebg,
                fg_color = '#D7D7D7',
                hover_color = '#C2C2C2'
                )
            
            self.vector.configure(
                text_color = 'black',
                bg_color = self.framebg,
                fg_color = '#D7D7D7',
                hover_color = '#C2C2C2'
                )
            
            self.theme_switch.configure(
                button_color = 'black',
                text_color = 'black',
                button_hover_color = 'black',
                border_width = 0
                )
            
            self.intro_text.configure(
                bg_color = self.bg,
                fg_color = self.framebg,
                text_color = '#032B44'
                )
            
            self.frame.configure(
                bg_color = self.framebg,
                fg_color = self.hiddenbg
                )
            
            if self.frame.winfo_viewable() == 1:
                self.titlebar.configure(bg_color = self.hiddenbg)
                
                self.frameclose.configure(
                    bg_color = self.hiddenbg,
                    fg_color = self.hiddenbg
                    )
                
                self.polytext.configure(
                    bg_color = self.hiddenbg,
                    fg_color = self.hiddenbg
                    )
                
                self.trigtext.configure(
                    bg_color = self.hiddenbg,
                    fg_color = self.hiddenbg
                    )
                
                self.exptext.configure(
                    bg_color = self.hiddenbg,
                    fg_color = self.hiddenbg
                    )
                
                self.customtext.configure(
                    bg_color = self.hiddenbg,
                    fg_color = self.hiddenbg
                    )
                
                self.polybtn.configure(bg_color = self.hiddenbg)
                
                self.trigbtn.configure(bg_color = self.hiddenbg)
                
                self.expbtn.configure(bg_color = self.hiddenbg)
                
                self.custombtn.configure(bg_color = self.hiddenbg)
            
            self.main.update_idletasks()
            
        else:
            self.bg = '#404040'
            
            self.framebg = '#4F4F4F'
            
            self.hiddenbg = '#43464B'
            
            self.main.config(bg = self.bg)
            
            self.closebtn.configure(
                text_color = 'white',
                bg_color = self.bg,
                fg_color = self.bg
                )
            
            self.sideframe.configure(
                fg_color = self.framebg,
                bg_color = self.bg
                )
            
            self.mainframe.configure(
                fg_color = self.framebg,
                bg_color = self.bg
                )
            
            self.head_text.configure(
                text_color = 'white',
                fg_color = self.framebg,
                bg_color = self.framebg
                )
            
            self.function.configure(
                text_color = 'white',
                fg_color = '#696969',
                bg_color = self.framebg,
                hover_color = '#565656'
                )
            
            self.table.configure(
                text_color = 'white',
                fg_color = '#696969',
                bg_color = self.framebg,
                hover_color = '#565656'
                )
            
            self.regression.configure(
                text_color = 'white',
                fg_color = '#696969',
                bg_color = self.framebg,
                hover_color = '#565656'
                )
            
            self.vector.configure(
                text_color = 'white',
                fg_color = '#696969',
                bg_color = self.framebg,
                hover_color = '#565656'
                )
            
            self.theme_switch.configure(
                button_color = 'white',
                button_hover_color = 'white',
                border_width = 0,
                fg_color = '#F7F7F7',
                text_color = 'white'
                )
            
            self.intro_text.configure(
                bg_color = self.bg,
                fg_color = self.framebg,
                text_color = '#FFD700'
                )
            
            self.frame.configure(
                bg_color = self.framebg,
                fg_color = self.hiddenbg,
                )
            
            self.main.update_idletasks()
            
            if self.frame.winfo_viewable() == 1:
                self.titlebar.configure(bg_color = self.hiddenbg)
                
                self.frameclose.configure(
                    bg_color = self.hiddenbg,
                    fg_color = self.hiddenbg
                    )
                
                self.polytext.configure(
                    bg_color = self.hiddenbg,
                    fg_color = self.hiddenbg
                    )
                
                self.trigtext.configure(
                    bg_color = self.hiddenbg,
                    fg_color = self.hiddenbg
                    )
                
                self.exptext.configure(
                    bg_color = self.hiddenbg,
                    fg_color = self.hiddenbg
                    )
                
                self.customtext.configure(
                    bg_color = self.hiddenbg,
                    fg_color = self.hiddenbg
                    )
                
                self.polybtn.configure(bg_color = self.hiddenbg)
                
                self.trigbtn.configure(bg_color = self.hiddenbg)
                
                self.expbtn.configure(bg_color = self.hiddenbg)
                
                self.custombtn.configure(bg_color = self.hiddenbg)
            
            self.main.update_idletasks()
            
    def function_mode(self):
        for item in self.mainframe.winfo_children():
            item.place_forget()
            
        for item in self.frame.winfo_children():
            item.place_forget()
        
        self.main.update_idletasks()
        
        self.frame.place(**self.frame_attr)
        
        self.frameclose.place(**self.frameclose_attr)
        
        self.titlebar.place(**self.titlebar_attr)
        
        self.titlebar.configure(text = 'Function')
        
        self.confirmbtn = CTkButton(
            master = self.plotframe,
            text = 'Confirm',
            text_color = 'white',
            font = (self.font, 15),
            bg_color = self.plotbg,
            fg_color = '#4267B2',
            hover_color = '#2C3E50',
            corner_radius = 10,
                )
            
        self.confirmbtn.place(relx = 0.1, rely = 0.2, relwidth = 0.3)
        
        self.confirmbtn_attr = {
            'relx': 0.1,
            'rely': 0.2,
            'relwidth': 0.3
            }
        
        self.confirmbtn.place_forget()
        
        self.config = CTkFrame(
            master = self.plotframe,
            bg_color = self.plotbg,
            fg_color = self.plotbg,
            corner_radius = 20
            )
        
        self.config.place(relx = 0, rely = 0.4, relwidth = 1, relheight = 0.5)
        
        self.config_attr = {
            'relx': 0,
            'rely': 0.4,
            'relwidth': 1,
            'relheight': 0.5
            }
        
        self.config.place_forget()
        
        self.plotbtn = CTkButton(
            master = self.config,
            text = 'Plot',
            text_color = 'white',
            font = (self.font, 15),
            bg_color = self.plotbg,
            fg_color = '#4267B2',
            hover_color = '#2C3E50',
            corner_radius = 10
            )
                
        self.plotbtn.place(relx = 0.1, rely = 0.5, relwidth = 0.3)
                
        self.plotbtn_attr = {
            'relx': 0.1,
            'rely': 0.5,
            'relwidth': 0.3
            }
        
        self.plotbtn.place_forget()
        
        self.config_head = CTkLabel(
            master = self.config,
            text = 'Configure Plot',
            text_color = 'white',
            font = (self.font, 18, 'bold'),
            bg_color = self.plotbg,
            fg_color = 'gray',
            corner_radius = 10
            )
        
        self.config_head.place(relx = 0.05, rely = 0, relheight = 0.25, relwidth = 0.9)
        
        self.config_head_attr = {
            'relx': 0.05,
            'rely': 0,
            'relheight': 0.2,
            'relwidth': 0.9
            }
        
        self.config_head.place_forget()
        
        self.titlebar.place(**self.titlebar_attr)
        
        self.polytext = CTkLabel(
            master = self.frame,
            text = 'Polynomial',
            font = (self.font, 18),
            text_color = 'white',
            bg_color = self.hiddenbg,
            fg_color = self.hiddenbg
            )
        
        def polynomial():
            for element in self.plotframe.winfo_children():
                element.place_forget()
                
            self.plotframe.place(**self.plotframe_attr)
            
            self.closepltframe.place(**self.closepltframe_attr)
            
            self.select_text = CTkLabel(
                master = self.plotframe,
                text = 'Select a power: ',
                font = (self.font, 15),
                text_color = 'black',
                bg_color = self.plotbg,
                fg_color = self.plotbg
                )
            
            self.select_text.place(relx = 0.1, rely = 0.1)
        
            powers = ttk.Combobox(self.plotframe)
            
            powers['values'] = [1, 2, 3]
            
            powers.set(1)
            
            powers.place(relx = 0.46, rely = 0.1)
            
            def config():
                self.config.place(**self.config_attr)
                
                self.config_head.place(**self.config_head_attr)
                
                if powers.get() == '1':
                    for item in self.config.winfo_children():
                        item.place_forget()
                        
                    self.config_head.place(**self.config_head_attr)
                    
                    self.plotbtn.place(**self.plotbtn_attr)
                    
                    ytext = CTkLabel(
                        master = self.config,
                        text = 'y = ',
                        text_color = 'black',
                        font = (self.font, 15),
                        bg_color = self.plotbg,
                        fg_color = self.plotbg
                        )
                    
                    ytext.place(relx = 0.05, rely = 0.3)
                    
                    a = CTkEntry(
                        master = self.config,
                        bg_color = self.plotbg,
                        fg_color = 'white',
                        text_color = 'black',
                        border_width = 0
                        )
                    
                    a.place(relx = 0.15, rely = 0.3, relwidth = 0.1)
                    
                    xtext = CTkLabel(
                        master = self.config,
                        text = 'x + ',
                        text_color = 'black',
                        font = (self.font, 15),
                        bg_color = self.plotbg,
                        fg_color = self.plotbg
                        )
                    
                    xtext.place(relx = 0.26, rely = 0.3)
                    
                    b = CTkEntry(
                        master = self.config,
                        bg_color = self.plotbg,
                        fg_color = 'white',
                        text_color = 'black',
                        border_width = 0
                        )
                    
                    b.place(relx = 0.35, rely = 0.3, relwidth = 0.1)
                    
                    def pltline():
                        x = numpy.linspace(-1000, 1000, 1000000)
                        
                        m = float(a.get())
                        
                        c = float(b.get())
                        
                        y = m * x + c
                        
                        scale = max((abs(m), abs(c))) + 5
                        
                        figure = Figure(dpi = 72)
                        
                        plt = figure.add_subplot()
                        
                        plt.plot(x, y)
                        
                        plt.set_xlim(-scale, scale)
                        
                        plt.set_ylim(-scale, scale)
                        
                        plt.grid(True)
                        
                        plt.axhline(0, color = 'black')
                        
                        plt.axvline(0, color = 'black')
                        
                        canvas = FigureCanvasTkAgg(figure, master = self.plt)
                        
                        self.plt.deiconify()
                        
                        self.closeplt.place(**self.closeplt_attr)
                        
                        canvas.draw()
                        
                        canvas_widget = canvas.get_tk_widget()
                        
                        canvas_widget.place(relx = 0.2, rely = 0, relwidth = 0.8, relheight = 1)
                    
                    self.plotbtn.configure(command = pltline)
                    
                elif powers.get() == '2':
                    for item in self.config.winfo_children():
                        item.place_forget()
                        
                    self.config_head.place(**self.config_head_attr)
                    
                    self.plotbtn.place(**self.plotbtn_attr)
                        
                    ytext = CTkLabel(
                        master = self.config,
                        text = 'y = ',
                        text_color = 'black',
                        font = (self.font, 15),
                        bg_color = self.plotbg,
                        fg_color = self.plotbg
                        )
                    
                    ytext.place(relx = 0.05, rely = 0.3)
                    
                    a = CTkEntry(
                        master = self.config,
                        bg_color = self.plotbg,
                        fg_color = 'white',
                        text_color = 'black',
                        border_width = 0
                        )
                    
                    a.place(relx = 0.15, rely = 0.3, relwidth = 0.1)
                    
                    x2text = CTkLabel(
                        master = self.config,
                        text = 'x\u00B2 + ',
                        text_color = 'black',
                        font = (self.font, 15),
                        bg_color = self.plotbg,
                        fg_color = self.plotbg
                        )
                    
                    x2text.place(relx = 0.26, rely = 0.3)
                    
                    b = CTkEntry(
                        master = self.config,
                        bg_color = self.plotbg,
                        fg_color = 'white',
                        text_color = 'black',
                        border_width = 0
                        )
                    
                    b.place(relx = 0.35, rely = 0.3, relwidth = 0.1)
                    
                    xtext = CTkLabel(
                        master = self.config,
                        text = 'x + ',
                        text_color = 'black',
                        font = (self.font, 15),
                        bg_color = self.plotbg,
                        fg_color = self.plotbg
                        )
                    
                    xtext.place(relx = 0.46, rely = 0.3)
                    
                    c = CTkEntry(
                        master = self.config,
                        bg_color = self.plotbg,
                        fg_color = 'white',
                        text_color = 'black',
                        border_width = 0
                        )
                    
                    c.place(relx = 0.55, rely = 0.3, relwidth = 0.1)
                    
                    def plotquad():
                        p = float(a.get())
                        
                        q = float(b.get())
                        
                        k = float(c.get())
                        
                        x = numpy.linspace(-1000, 1000, 1000000)
                        
                        y = p * (x ** 2) + q * x + k
                        
                        scale = max((abs(p), abs(q), abs(k))) + 5
                        
                        figure = Figure(dpi = 72)
                        
                        plt = figure.add_subplot()
                        
                        plt.plot(x, y)
                        
                        plt.set_xlim(-scale, scale)
                        
                        plt.set_ylim(-scale, scale)
                        
                        plt.axhline(0, color = 'black')
                        
                        plt.axvline(0, color = 'black')
                        
                        plt.grid(True)
                        
                        canvas = FigureCanvasTkAgg(figure, master = self.plt)
                        
                        self.plt.deiconify()
                        
                        self.closeplt.place(**self.closeplt_attr)
                        
                        canvas.draw()
                        
                        canvas_widget = canvas.get_tk_widget()
                        
                        canvas_widget.place(relx = 0.2, rely = 0, relwidth = 0.8, relheight = 1)
                    
                    self.plotbtn.configure(command = plotquad)
                    
                else:
                    for item in self.config.winfo_children():
                        item.place_forget()
                        
                    self.config_head.place(**self.config_head_attr)
                    
                    self.plotbtn.place(**self.plotbtn_attr)
                        
                    ytext = CTkLabel(
                        master = self.config,
                        text = 'y = ',
                        text_color = 'black',
                        font = (self.font, 15),
                        bg_color = self.plotbg,
                        fg_color = self.plotbg
                        )
                    
                    ytext.place(relx = 0.05, rely = 0.3)
                    
                    a = CTkEntry(
                        master = self.config,
                        bg_color = self.plotbg,
                        fg_color = 'white',
                        text_color = 'black',
                        border_width = 0
                        )
                    
                    a.place(relx = 0.15, rely = 0.3, relwidth = 0.1)
                    
                    x3text = CTkLabel(
                        master = self.config,
                        text = 'x\u00B3 + ',
                        text_color = 'black',
                        font = (self.font, 15),
                        bg_color = self.plotbg,
                        fg_color = self.plotbg
                        )
                    
                    x3text.place(relx = 0.26, rely = 0.3)
                    
                    b = CTkEntry(
                        master = self.config,
                        bg_color = self.plotbg,
                        fg_color = 'white',
                        text_color = 'black',
                        border_width = 0
                        )
                    
                    b.place(relx = 0.35, rely = 0.3, relwidth = 0.1)
                    
                    x2text = CTkLabel(
                        master = self.config,
                        text = 'x\u00B2 + ',
                        text_color = 'black',
                        font = (self.font, 15),
                        bg_color = self.plotbg,
                        fg_color = self.plotbg
                        )
                    
                    x2text.place(relx = 0.46, rely = 0.3)
                    
                    c = CTkEntry(
                        master = self.config,
                        bg_color = self.plotbg,
                        fg_color = 'white',
                        text_color = 'black',
                        border_width = 0
                        )
                    
                    c.place(relx = 0.55, rely = 0.3, relwidth = 0.1)
                    
                    xtext = CTkLabel(
                        master = self.config,
                        text = 'x + ',
                        text_color = 'black',
                        font = (self.font, 15),
                        bg_color = self.plotbg,
                        fg_color = self.plotbg
                        )
                    
                    xtext.place(relx = 0.66, rely = 0.3)
                    
                    d = CTkEntry(
                        master = self.config,
                        bg_color = self.plotbg,
                        fg_color = 'white',
                        text_color = 'black',
                        border_width = 0
                        )
                    
                    d.place(relx = 0.75, rely = 0.3, relwidth = 0.1)
                    
                    def plotcubic():
                        p = float(a.get())
                        
                        q = float(b.get())
                        
                        r = float(c.get())
                        
                        k = float(d.get())
                        
                        x = numpy.linspace(-1000, 1000, 1000000)
                        
                        y = p * (x ** 3) + q * (x ** 2) + r * x + k
                        
                        scale = max((abs(p), abs(q), abs(r), abs(k))) + 5
                        
                        figure = Figure(dpi = 72)
                        
                        plt = figure.add_subplot()
                        
                        plt.plot(x, y)
                        
                        plt.set_xlim(-scale, scale)
                        
                        plt.set_ylim(-scale, scale)
                        
                        plt.axhline(0, color = 'black')
                        
                        plt.axvline(0, color = 'black')
                        
                        plt.grid(True)
                        
                        canvas = FigureCanvasTkAgg(figure, master = self.plt)
                        
                        self.plt.deiconify()
                        
                        self.closeplt.place(**self.closeplt_attr)
                        
                        canvas.draw()
                        
                        canvas_widget = canvas.get_tk_widget()
                        
                        canvas_widget.place(relx = 0.2, rely = 0, relwidth = 0.8, relheight = 1)
                    
                    self.plotbtn.configure(command = plotcubic)
            
            self.confirmbtn.place(**self.confirmbtn_attr)
           
            self.confirmbtn.configure(command = config)
        
        self.polytext.place(relx = 0.145, rely = 0.625)
        
        polybtn_image = image('C:/Users/VICTOR/Desktop/Plotter/poly.png', (150, 120))
        
        self.polybtn = CTkButton(
            master = self.frame,
            text = '',
            bg_color = self.hiddenbg,
            fg_color = '#4267B2',
            hover_color = '#4267B2',
            corner_radius = 40,
            image = polybtn_image,
            command = polynomial
            )
        
        self.polybtn.image = polybtn_image
        
        self.polybtn.place(relx = 0.05, rely = 0.4)
        
        self.trigtext = CTkLabel(
            master = self.frame,
            text = 'Trigonometry',
            font = (self.font, 18),
            text_color = 'white',
            bg_color = self.hiddenbg,
            fg_color = self.hiddenbg
            )
        
        self.trigtext.place(relx = 0.685, rely = 0.625)
        
        trig_image = image('C:/Users/VICTOR/Desktop/Plotter/trig.png', (150, 120))
        
        def trig():
            for element in self.plotframe.winfo_children():
                element.place_forget()
                
            self.plotframe.place(**self.plotframe_attr)
            
            self.closepltframe.place(**self.closepltframe_attr)
            
            select_text = CTkLabel(
                master = self.plotframe,
                text = 'Select a function:',
                font = (self.font, 15),
                text_color = 'black',
                bg_color = self.plotbg,
                fg_color = self.plotbg
                )
            
            select_text.place(relx = 0.1, rely = 0.1)
            
            ratios = ttk.Combobox(self.plotframe)
            
            ratios['values'] = ['sine', 'cosine', 'tan']
            
            ratios.set('sine')
            
            ratios.place(relx = 0.5, rely = 0.1)
            
            def config():
                self.config.place(**self.config_attr)
                
                if ratios.get() == 'sine':
                    for item in self.config.winfo_children():
                        item.place_forget()
                
                    self.config_head.place(**self.config_head_attr)
                    
                    ytext = CTkLabel(
                        master = self.config,
                        text = 'y = ',
                        text_color = 'black',
                        font = (self.font, 15),
                        bg_color = self.plotbg,
                        fg_color = self.plotbg
                        )
                    
                    ytext.place(relx = 0.05, rely = 0.3)
                    
                    k1 = CTkEntry(
                        master = self.config,
                        bg_color = self.plotbg,
                        fg_color = 'white',
                        text_color = 'black',
                        border_width = 0
                        )
                    
                    k1.place(relx = 0.15, rely = 0.3, relwidth = 0.1)
                    
                    text1 = CTkLabel(
                        master = self.config,
                        text = 'sin( ',
                        text_color = 'black',
                        font = (self.font, 15),
                        bg_color = self.plotbg,
                        fg_color = self.plotbg
                        )
                    
                    text1.place(relx = 0.26, rely = 0.3)
                    
                    k2 = CTkEntry(
                        master = self.config,
                        bg_color = self.plotbg,
                        fg_color = 'white',
                        text_color = 'black',
                        border_width = 0
                        )
                    
                    k2.place(relx = 0.36, rely = 0.3, relwidth = 0.1)
                    
                    text2 = CTkLabel(
                        master = self.config,
                        text = 'x + ',
                        text_color = 'black',
                        font = (self.font, 15),
                        bg_color = self.plotbg,
                        fg_color = self.plotbg
                        )
                    
                    text2.place(relx = 0.47, rely = 0.3)
                    
                    k3 = CTkEntry(
                        master = self.config,
                        bg_color = self.plotbg,
                        fg_color = 'white',
                        text_color = 'black',
                        border_width = 0
                        )
                    
                    k3.place(relx = 0.57, rely = 0.3, relwidth = 0.1)
                    
                    text3 = CTkLabel(
                        master = self.config,
                        text = ') + ',
                        text_color = 'black',
                        font = (self.font, 15),
                        bg_color = self.plotbg,
                        fg_color = self.plotbg
                        )
                    
                    text3.place(relx = 0.68, rely = 0.3)
                    
                    k4 = CTkEntry(
                        master = self.config,
                        bg_color = self.plotbg,
                        fg_color = 'white',
                        text_color = 'black',
                        border_width = 0
                        )
                    
                    k4.place(relx = 0.78, rely = 0.3, relwidth = 0.1)
                    
                    def plotsine():
                        a = float(k1.get())
                        
                        b = float(k2.get())
                        
                        c = float(k3.get())
                        
                        k = float(k4.get())
                        
                        x = numpy.linspace(-5 * numpy.pi, 5 * numpy.pi, 1000000)
                        
                        y = a * (numpy.sin(b * x + c)) + k
                        
                        xscale = abs(c) + 5
                        
                        yscale = max((abs(a), abs(k))) + 5
                        
                        figure = Figure(dpi = 72)
                        
                        plt = figure.add_subplot()
                        
                        plt.plot(x, y)
                        
                        plt.set_xlim(-xscale, xscale)
                        
                        plt.set_ylim(-yscale, yscale)
                        
                        plt.axvline(0, color = 'black')
                        
                        plt.axhline(0, color = 'black')
                        
                        plt.grid(True)
                        
                        canvas = FigureCanvasTkAgg(figure, master = self.plt)
                        
                        self.plt.deiconify()
                        
                        self.closeplt.place(**self.closeplt_attr)
                        
                        canvas.draw()
                        
                        canvas_widget = canvas.get_tk_widget()
                        
                        canvas_widget.place(relx = 0.2, rely = 0, relwidth = 0.8, relheight = 1)
                    
                    self.plotbtn.place(**self.plotbtn_attr)
                    
                    self.plotbtn.configure(command = plotsine)
                    
                elif ratios.get() == 'cosine':
                    for item in self.config.winfo_children():
                        item.place_forget()
                
                    self.config_head.place(**self.config_head_attr)
                    
                    ytext = CTkLabel(
                        master = self.config,
                        text = 'y = ',
                        text_color = 'black',
                        font = (self.font, 15),
                        bg_color = self.plotbg,
                        fg_color = self.plotbg
                        )
                    
                    ytext.place(relx = 0.05, rely = 0.3)
                    
                    k1 = CTkEntry(
                        master = self.config,
                        bg_color = self.plotbg,
                        fg_color = 'white',
                        text_color = 'black',
                        border_width = 0
                        )
                    
                    k1.place(relx = 0.15, rely = 0.3, relwidth = 0.1)
                    
                    text1 = CTkLabel(
                        master = self.config,
                        text = 'cos( ',
                        text_color = 'black',
                        font = (self.font, 15),
                        bg_color = self.plotbg,
                        fg_color = self.plotbg
                        )
                    
                    text1.place(relx = 0.26, rely = 0.3)
                    
                    k2 = CTkEntry(
                        master = self.config,
                        bg_color = self.plotbg,
                        fg_color = 'white',
                        text_color = 'black',
                        border_width = 0
                        )
                    
                    k2.place(relx = 0.36, rely = 0.3, relwidth = 0.1)
                    
                    text2 = CTkLabel(
                        master = self.config,
                        text = 'x + ',
                        text_color = 'black',
                        font = (self.font, 15),
                        bg_color = self.plotbg,
                        fg_color = self.plotbg
                        )
                    
                    text2.place(relx = 0.47, rely = 0.3)
                    
                    k3 = CTkEntry(
                        master = self.config,
                        bg_color = self.plotbg,
                        fg_color = 'white',
                        text_color = 'black',
                        border_width = 0
                        )
                    
                    k3.place(relx = 0.57, rely = 0.3, relwidth = 0.1)
                    
                    text3 = CTkLabel(
                        master = self.config,
                        text = ') + ',
                        text_color = 'black',
                        font = (self.font, 15),
                        bg_color = self.plotbg,
                        fg_color = self.plotbg
                        )
                    
                    text3.place(relx = 0.68, rely = 0.3)
                    
                    k4 = CTkEntry(
                        master = self.config,
                        bg_color = self.plotbg,
                        fg_color = 'white',
                        text_color = 'black',
                        border_width = 0
                        )
                    
                    k4.place(relx = 0.78, rely = 0.3, relwidth = 0.1)
                    
                    def plotcos():
                        a = float(k1.get())
                        
                        b = float(k2.get())
                        
                        c = float(k3.get())
                        
                        k = float(k4.get())
                        
                        x = numpy.linspace(-5 * numpy.pi, 5 * numpy.pi, 1000000)
                        
                        y = a * (numpy.cos(b * x + c)) + k
                        
                        xscale = abs(c) + 5
                        
                        yscale = max((abs(a), abs(k))) + 5
                        
                        figure = Figure(dpi = 72)
                        
                        plt = figure.add_subplot()
                        
                        plt.plot(x, y)
                        
                        plt.set_xlim(-xscale, xscale)
                        
                        plt.set_ylim(-yscale, yscale)
                        
                        plt.axvline(0, color = 'black')
                        
                        plt.axhline(0, color = 'black')
                        
                        plt.grid(True)
                        
                        canvas = FigureCanvasTkAgg(figure, master = self.plt)
                        
                        self.plt.deiconify()
                        
                        self.closeplt.place(**self.closeplt_attr)
                        
                        canvas.draw()
                        
                        canvas_widget = canvas.get_tk_widget()
                        
                        canvas_widget.place(relx = 0.2, rely = 0, relwidth = 0.8, relheight = 1)
                    
                    self.plotbtn.place(**self.plotbtn_attr)
                    
                    self.plotbtn.configure(command = plotcos)
                    
                else:
                    for item in self.config.winfo_children():
                        item.place_forget()
                
                    self.config_head.place(**self.config_head_attr)
                    
                    ytext = CTkLabel(
                        master = self.config,
                        text = 'y = ',
                        text_color = 'black',
                        font = (self.font, 15),
                        bg_color = self.plotbg,
                        fg_color = self.plotbg
                        )
                    
                    ytext.place(relx = 0.05, rely = 0.3)
                    
                    k1 = CTkEntry(
                        master = self.config,
                        bg_color = self.plotbg,
                        fg_color = 'white',
                        text_color = 'black',
                        border_width = 0
                        )
                    
                    k1.place(relx = 0.15, rely = 0.3, relwidth = 0.1)
                    
                    text1 = CTkLabel(
                        master = self.config,
                        text = 'tan( ',
                        text_color = 'black',
                        font = (self.font, 15),
                        bg_color = self.plotbg,
                        fg_color = self.plotbg
                        )
                    
                    text1.place(relx = 0.26, rely = 0.3)
                    
                    k2 = CTkEntry(
                        master = self.config,
                        bg_color = self.plotbg,
                        fg_color = 'white',
                        text_color = 'black',
                        border_width = 0
                        )
                    
                    k2.place(relx = 0.36, rely = 0.3, relwidth = 0.1)
                    
                    text2 = CTkLabel(
                        master = self.config,
                        text = 'x + ',
                        text_color = 'black',
                        font = (self.font, 15),
                        bg_color = self.plotbg,
                        fg_color = self.plotbg
                        )
                    
                    text2.place(relx = 0.47, rely = 0.3)
                    
                    k3 = CTkEntry(
                        master = self.config,
                        bg_color = self.plotbg,
                        fg_color = 'white',
                        text_color = 'black',
                        border_width = 0
                        )
                    
                    k3.place(relx = 0.57, rely = 0.3, relwidth = 0.1)
                    
                    text3 = CTkLabel(
                        master = self.config,
                        text = ') + ',
                        text_color = 'black',
                        font = (self.font, 15),
                        bg_color = self.plotbg,
                        fg_color = self.plotbg
                        )
                    
                    text3.place(relx = 0.68, rely = 0.3)
                    
                    k4 = CTkEntry(
                        master = self.config,
                        bg_color = self.plotbg,
                        fg_color = 'white',
                        text_color = 'black',
                        border_width = 0
                        )
                    
                    k4.place(relx = 0.78, rely = 0.3, relwidth = 0.1)
                    
                    def plot_tan():
                        a = float(k1.get())
                        
                        b = float(k2.get())
                        
                        c = float(k3.get())
                        
                        k = float(k4.get())
                        
                        lis = []
                        
                        x = numpy.linspace(-5 * numpy.pi, 5 * numpy.pi, 1000000)
                        
                        for val in x:
                            if numpy.cos(val) == 0:
                                del x[x.index(val)]
                                
                                lis.append(0)
                                
                            else:
                                pass
                        
                        print(len(lis))
                        
                        y = a * (numpy.tan(b * x + c)) + k
                        
                        xscale = abs(c) + 5
                        
                        yscale = max((abs(a), abs(k))) + 5
                        
                        figure = Figure(dpi = 72)
                        
                        plt = figure.add_subplot()
                        
                        plt.plot(x, y)
                        
                        plt.set_xlim(-xscale, xscale)
                        
                        plt.set_ylim(-yscale, yscale)
                        
                        plt.axvline(0, color = 'black')
                        
                        plt.axhline(0, color = 'black')
                        
                        plt.grid(True)
                        
                        canvas = FigureCanvasTkAgg(figure, master = self.plt)
                        
                        self.plt.deiconify()
                        
                        self.closeplt.place(**self.closeplt_attr)
                        
                        canvas.draw()
                        
                        canvas_widget = canvas.get_tk_widget()
                        
                        canvas_widget.place(relx = 0.2, rely = 0, relwidth = 0.8, relheight = 1)
                    
                    self.plotbtn.place(**self.plotbtn_attr)
                    
                    self.plotbtn.configure(command = plot_tan)
            
            self.confirmbtn.place(**self.confirmbtn_attr)
            
            self.confirmbtn.configure(command = config)
        
        self.trigbtn = CTkButton(
            master = self.frame,
            text = '',
            bg_color = self.hiddenbg,
            fg_color = '#4267B2',
            hover_color = '#4267B2',
            corner_radius = 40,
            image = trig_image,
            command = trig
            )
        
        self.trigbtn.image = trig_image
        
        self.trigbtn.place(relx = 0.625, rely = 0.4)
        
        self.exptext = CTkLabel(
            master = self.frame,
            text = 'Exponential',
            font = (self.font, 18),
            text_color = 'white',
            bg_color = self.hiddenbg,
            fg_color = self.hiddenbg
            )
        
        self.exptext.place(relx = 0.13, rely = 0.925)
        
        exp_image = image('C:/Users/VICTOR/Desktop/Plotter/exp.png', (150, 120))
        
        self.expbtn = CTkButton(
            master = self.frame,
            text = '',
            bg_color = self.hiddenbg,
            fg_color = '#4267B2',
            hover_color = '#4267B2',
            corner_radius = 40,
            image = exp_image
            )
        
        self.expbtn.image = exp_image
        
        self.expbtn.place(relx = 0.05, rely = 0.7)
        
        self.customtext = CTkLabel(
            master = self.frame,
            text = 'Custom',
            font = (self.font, 18),
            text_color = 'white',
            bg_color = self.hiddenbg,
            fg_color = self.hiddenbg
            )
        
        self.customtext.place(relx = 0.73, rely = 0.925)
        
        custom_image = image('C:/Users/VICTOR/Desktop/Plotter/custom.png', (150, 120))
        
        self.custombtn = CTkButton(
            master = self.frame,
            text = '',
            bg_color = self.hiddenbg,
            fg_color = '#4267B2',
            hover_color = '#4267B2',
            corner_radius = 40,
            image = custom_image
            )
        
        self.custombtn.image = custom_image
        
        self.custombtn.place(relx = 0.625, rely = 0.7)
    
    def table_mode(self):
        for item in self.mainframe.winfo_children():
            item.place_forget()
            
        for item in self.frame.winfo_children():
            item.place_forget()
            
        self.frame.place(**self.frame_attr)
        
        self.frameclose.place(**self.frameclose_attr)
            
        self.titlebar.configure(text = 'Table')
                    
        self.titlebar.place(**self.titlebar_attr)
        
        self.hiddencanvas.place(**self.hiddencanvas_attr)
        
        self.scroll = CTkScrollbar(
            master = self.hiddencanvas,
            corner_radius = 5,
            bg_color = self.hiddenbg,
            command = self.hiddencanvas.yview
            )
        
        self.scroll.place(relx = 0.975, rely = 0.35, relwidth = 0.025)
        
        self.hiddencanvas.configure(yscrollcommand = self.scroll.set)
        
        tableframe = CTkFrame(
            master = self.hiddencanvas,
            bg_color = 'red',
            fg_color = 'red',
            height = 800
            )
        
        self.hiddencanvas.create_window(0, 0, window = tableframe)
        
        entry1 = CTkEntry(
            master = tableframe,
            fg_color = 'white'
            )
        
        entry1.place(x = 400, y = 400)
    
    def reg_mode(self):
        pass
    
    def vector_mode(self):
        pass
        
    def run(self):
        if __name__ == '__main__':
            self.main.mainloop()
            
App()
