from customtkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
from tkinter import *
from gtts import gTTS
from PIL import Image
from playsound import playsound

set_appearance_mode("dark")

root = CTk()
root.title("Text Editor")
root.geometry("1700x900")
root.resizable(False, False)

global panel_position

open_img = CTkImage(Image.open("Images/open.png"), size=(40,40))
save_img = CTkImage(Image.open("Images/save.png"), size=(40,40))
saveas_img = CTkImage(Image.open("Images/saveas.png"), size=(40,40))
about_img = CTkImage(Image.open("Images/about.png"), size=(40,40))
read_img = CTkImage(Image.open("Images/read.png"), size=(40,40))
setting_img = CTkImage(Image.open("Images/setting.png"), size=(40,40))
help_img = CTkImage(Image.open("Images/help.png"), size=(40,40))
hide_img = CTkImage(Image.open("Images/hide.png"), size=(40,40))

themes = {"Default":"#3848ab", "Red":"#e53834", "Pink":"#d81b60", "Light-Green":"#7db242", 
          "Dark-Green":"#42a046", "Teal":"#00887a", "Orange":"#f5501e", "Brown":"#6d4d40", 
          "Grey":"#546f7b", "Black":"#333232", "Purple":"#8e25ab", "Dark-Purple":"#5e35b1", 
          "Blue":"#029ae5", "Yellow":"#fcd935", "Golden":"#fa8c01"}


def open_file():
    global file
    file = askopenfile(parent=root, title="Open file", filetypes=[("text files","*.txt"), ("python file", "*.py"), ("All file", "*.*")], mode="r+")
    if file:
        content = file.read()
        textbox.insert(INSERT, content)


def save_file():
    global file
    file = asksaveasfile(parent=root, title="Save file", filetypes=[("text files","*.txt"), ("python file", "*.py"), ("All file", "*.*")], mode="w")
    if file:
        content = textbox.get(0.0, END)
        file.write(content)


def clear():
    textbox.delete(1.0, END)


def saveas():
    file = asksaveasfile(parent=root, title="Save file as", filetypes=[("text file", "*.txt" ), ("python files", "*.py"), ("All files", "*.*")],
    mode = "w")
    content = textbox.get(0.0, END)
    file.write(content)
    file.close()


def exit_app():
    message = messagebox.askokcancel(title="Quit", message="Are you sure you want to exit the application. Don't forget to save your changes.")
    if message:
        root.quit()


def help():
    messagebox.showinfo(title="Help", message="This is a simple application help you to create, edit ot view you documents.")


def about():
    messagebox.showinfo(title="About", message="Simple Notepad || Version: 1.0")


def read_text():
    text_to_read = textbox.get(1.0, END)
    try:
        speak_text = gTTS(text=text_to_read)
        speak_text.save("tmpfile.mp3")
    except AssertionError:
        speak_text = gTTS(text="Sorry! but I don't find any text on the screen")
        speak_text.save("tmpfile.mp3")    
    playsound("tmpfile.mp3")
    os.remove("tmpfile.mp3")


def apply_color(color):

    btns = [open_btn, save_btn, save_as_btn, hide_btn, read_btn, help_btn,
            about_btn, settings_btn, theme_choice, font_choice, varient_choice, word_wrap_choice,
            position_choice, apply_btn]

    try:
        for btn in btns:
            btn.configure(fg_color=color)
    except:
        pass


def btns_placement(x, y, orientation):
    panel_btns = [open_btn, save_btn, save_as_btn, hide_btn, read_btn, help_btn,
                  about_btn, settings_btn]
    if orientation == "vertical":
        for btn in panel_btns:
                btn.place(x=x, y=y)
                y += 80
    else:
        for btn in panel_btns:
                btn.configure(width=180)
                btn.place(x=x, y=y)
                x += 210


def createTopMenu():
    position_choice.set("Top Menu")
    btn_frame.place_forget()
    text_frame.place(x=0, y=0)
    text_frame.configure(width=1700, height=900)
    textbox.configure(width=1700, height=900)
    scroll.configure(height=textbox._current_height)
    scroll.place(x=(textbox._current_width-10), y=0)
    root.config(menu=menubar)
    menubar.config(bg="#202324", fg="#fff")
    filemenu = Menu(menubar, bg="#202324", tearoff=0, fg="#fff", borderwidth=0, font=("Raleway", 10))
    menubar.add_cascade(menu=filemenu, label="File")
    filemenu.add_command(label="Open", command=lambda:open_file())
    filemenu.add_command(label="Save", command=lambda:save_file())
    filemenu.add_command(label="Save As", command=lambda:saveas())
    filemenu.add_command(label="Exit", command=lambda:exit_app())

    editmenu = Menu(menubar, bg="#202324", tearoff=0, fg="#fff", borderwidth=0, font=("Raleway", 10))
    menubar.add_cascade(menu=editmenu, label="Edit")
    editmenu.add_command(label="Clear", command=lambda:clear())
    editmenu.add_command(label="Hide Panel", command=lambda:hide_panel()())

    settingsmenu = Menu(menubar, bg="#202324", tearoff=0, fg="#fff", borderwidth=0, font=("Raleway", 10))
    menubar.add_cascade(label="Settings", menu=settingsmenu)
    settingsmenu.add_command(label="Settings", command=lambda:settings())
    settingsmenu.add_command(label="Read Text", command=lambda:read_text())

    helpmenu = Menu(menubar, bg="#202324", tearoff=0, fg="#fff", borderwidth=0, font=("Raleway", 10))
    menubar.add_cascade(menu=helpmenu, label="Help")
    helpmenu.add_command(label="Help", command=lambda:help())
    helpmenu.add_command(label="About", command=lambda:about())
    

def apply_settings():
    global theme, theme_choice, panel_position, menubar, varient_choice, themes, varient

    theme = theme_choice.get()
    font_size = int(font_choice.get())
    panel_position = position_choice.get()
    word_wrap = word_wrap_choice.get()
    menubar = Menu(root, borderwidth=0)
    varient = varient_choice.get()
    varient_choice.set(f"{varient}")
    
    if theme == "Light":
        set_appearance_mode("light")
        theme_choice.set("Light")

    elif theme == "Dark":
        set_appearance_mode("dark")
        theme_choice.set("Dark")

    textbox.configure(font=("Raleway", font_size))
    font_choice.set(f"{font_size}")

    if panel_position == "Right Panel":
        root.config(menu=False)
        btn_frame.configure(height=900, width=230)
        btn_frame.place(x=1462, y=0)
        text_frame.configure(height=900, width=1462)
        text_frame.place(x=0, y=0)
        btns_placement(10, 15, "vertical")
        position_choice.set("Right Panel")
    
    elif panel_position == "Left Panel":
        root.config(menu=None)
        btn_frame.configure(height=900, width=230)
        btn_frame.place(x=0, y=0)
        text_frame.configure(height=900, width=1462)
        text_frame.place(x=230, y=0)
        btns_placement(10, 15, "vertical")
        position_choice.set("Left Panel")

    elif panel_position == "Top Panel":
        root.config(menu=None)
        btn_frame.configure(height=90, width=1700)
        btn_frame.place(x=0, y=0)
        text_frame.configure(height=810, width=1700)
        text_frame.place(x=0, y=90)
        textbox.configure(width=1700)
        scroll.place(x=(textbox._current_width-12), y=0)
        btns_placement(10, 15, "horizontal")
        position_choice.set("Top Panel")

    elif panel_position == "Bottom Panel":
        root.config(menu=None)
        btn_frame.configure(height=90, width=1700)
        btn_frame.place(x=0, y=810)
        text_frame.configure(height=810, width=1700)
        text_frame.place(x=0, y=0)
        textbox.configure(width=1700)
        scroll.place(x=(textbox._current_width-12), y=0)
        btns_placement(10, 15, "horizontal")
        position_choice.set("Bottom Panel")

    elif panel_position == "Top Menu":
        createTopMenu()

    if word_wrap == "Word Wrap":
        word_wrap_choice.set("Word Wrap")
        textbox.configure(wrap="word")

    elif word_wrap == "Character Wrap":
        word_wrap_choice.set("Character Wrap")
        textbox.configure(wrap="char")
    
    else:
        word_wrap_choice.set("No Wrap")
        word_wrap == "none"

    apply_color(themes[varient])


def show_panel():
    try:
        position = position_choice.get()
    except NameError:
        position = "Left Panel"

    if position == "Left Panel":
        btn_frame.place(x=0, y=0)
        text_frame.place(x=230, y=0)
        text_frame.configure(width=1462, height=900)
        textbox.configure(width=1462, height=900)
        scroll.place(x=(textbox._current_width-12), y=0)
        show_panel_btn.place_forget()

    elif position == "Right Panel":
        btn_frame.configure(height=900, width=230)
        btn_frame.place(x=1462, y=0)
        text_frame.configure(height=900, width=1462)
        text_frame.place(x=0, y=0)
        textbox.configure(width=1462, height=900)
        scroll.place(x=(textbox._current_width-12), y=0)
        show_panel_btn.place_forget()

    elif position == "Top Panel":
        btn_frame.configure(height=90, width=1700)
        btn_frame.place(x=0, y=0)
        text_frame.configure(height=810, width=1700)
        text_frame.place(x=0, y=90)
        textbox.configure(width=1700)
        scroll.place(x=(textbox._current_width-12), y=0)
        show_panel_btn.place_forget()

    elif position == "Bottom Panel":
        btn_frame.configure(height=90, width=1700)
        btn_frame.place(x=0, y=810)
        text_frame.configure(height=810, width=1700)
        text_frame.place(x=0, y=0)
        textbox.configure(width=1700)
        scroll.place(x=(textbox._current_width-12), y=0)
        show_panel_btn.place_forget()
         

def settings():
    global theme_choice, font_choice, position_choice, theme, word_wrap_choice, varient_choice, apply_btn, varinet
    setting_win = CTkToplevel(root)
    setting_win.geometry("800x600")
    setting_win.title("Settings")
    setting_win.resizable(False, False)

    try:
        colour = themes[varient]
    except NameError:
        colour = "#3848ab"

    frame = CTkFrame(setting_win, height=558, width=760, corner_radius=30)
    frame.place(x=20, y=20)

    head_label = CTkLabel(frame, text="Settings", font=("Raleway", 25))
    head_label.place(x=335, y=20)

    theme_label = CTkLabel(frame, text="Theme", font=("Raleway", 20))
    theme_label.place(x=20, y=120)

    theme_choice = CTkOptionMenu(frame, values=["Dark", "Light"], font=("Raleway", 17), corner_radius=10, fg_color=colour)
    theme_choice.place(x=130, y=120)

    varient_label = CTkLabel(frame, text="Varients", font=("Raleway", 20))
    varient_label.place(x=20, y=280)

    varient_choice = CTkOptionMenu(frame, values=["Default", "Teal", "Purple", "Dark-Purple", "Blue", "Dark-Blue", "Pink", "Orange", "Yellow", "Golden", "Red", "Green", "Dark-Green", "Brown", "Grey", "Black"], font=("Raleway", 17), corner_radius=10, fg_color=colour)
    varient_choice.place(x=140, y=280)
    
    font_label = CTkLabel(frame, text="Font Size", font=("Raleway", 20))
    font_label.place(x=435, y=120)

    font_choice = CTkComboBox(frame, values=["8", "12", "14", "16", "18", "20", "22", "24", "26", "28", "30", "32"], font=("Raleway", 17), corner_radius=10, fg_color=colour)
    font_choice.place(x=590, y=120)
    font = (textbox.cget("font"))
    font_choice.set(font[1])

    position_label = CTkLabel(frame, text="Layout", font=("Raleway", 20))
    position_label.place(x=20, y=200)

    position_choice = CTkOptionMenu(frame, values=["Left Panel", "Right Panel", "Top Panel", "Bottom Panel", "Top Menu"], font=("Raleway", 17), corner_radius=10, fg_color=colour)
    position_choice.place(x=130, y=200)
    position_choice.set("Left Panel")

    word_wrap_label = CTkLabel(frame, text="Word Wrap", font=("Raleway", 20))
    word_wrap_label.place(x=435, y=200)

    word_wrap_choice = CTkOptionMenu(frame, values=["Word Wrap", "Character Wrap", "No Wrap"], font=("Raleway", 17), corner_radius=10, fg_color=colour)
    word_wrap_choice.place(x=590, y=200)

    apply_btn = CTkButton(setting_win, text="Apply", font=("Raleway", 20), width=300, height=50, corner_radius=15, command=lambda: apply_settings(), fg_color=colour)
    apply_btn.place(x=270, y=450)

    setting_win.mainloop()


def hide_panel():
    global show_panel_btn, calc_state, panel_state
    btn_frame.place_forget()
    text_frame.place(x=20, y=20)
    text_frame.configure(width=1660, height=860)
    textbox.configure(width=1660, height=860)
    scroll.place(x=(textbox._current_width-12), y=0)
    show_panel_btn = CTkButton(root, text=">", width=8, command=lambda: show_panel())
    show_panel_btn.place(x=2, y=850)


def hide_assistant():
    ai_assistant_btn = CTkButton(btn_frame, width=210, height=60, corner_radius=10, text="Assistant", command=lambda: show_assistant(), fg_color="#3848ab", image=setting_img, font=("Firacode", 20))
    ai_assistant_btn.place(x=10, y=705)

    text_frame.configure(width=1462)
    textbox.configure(width=1462)
    scroll.place(x=(textbox._current_width-12), y=0)

    assistant_hide_btn.place_forget()
    assistant_frame.place_forget()


def show_assistant():
    global assistant_frame, assistant_hide_btn

    text_frame.configure(width=1232)
    textbox.configure(width=1232)
    scroll.place(x=(textbox._current_width-12), y=0)

    assistant_hide_btn = CTkButton(btn_frame, width=210, height=60, corner_radius=10, text="Hide AI", command=lambda: hide_assistant(), fg_color="#3848ab", image=setting_img, font=("Firacode", 20))
    assistant_hide_btn.place(x=10, y=705)

    assistant_frame = CTkFrame(root, height=900, width=230, corner_radius=0)
    assistant_frame.place(x=1470,y=0)

    head_label = CTkLabel(assistant_frame, text="Text Assistant", font=("Firacode", 20))
    head_label.place(x=30, y=15)

    query_entry = CTkEntry(assistant_frame, font=("Firacode", 20), width=210)
    query_entry.place(x=10, y=60)
    
    ask_query_btn = CTkButton(assistant_frame, width=160, corner_radius=10, text="Ask Query", fg_color="#3848ab", font=("Firacode", 15))
    ask_query_btn.place(x=30, y=110)


btn_frame = CTkFrame(root, height=900, width=230, corner_radius=0)
btn_frame.place(x=0,y=0)

text_frame = CTkFrame(root, height=900, width=1462, corner_radius=0)
text_frame.place(x=230, y=0)

head_label = CTkLabel(btn_frame, text="Text Editor", font=("Firacode", 20))
head_label.place(x=50, y=15)

open_btn = CTkButton(btn_frame, width=210, height=60, corner_radius=10, text="Open", command=lambda: open_file(), fg_color="#3848ab", image=open_img, font=("Firacode", 20))
open_btn.place(x=10, y=65)

save_btn = CTkButton(btn_frame, width=210, height=60, corner_radius=10, text="Save", command=lambda: save_file(), fg_color="#3848ab", image=save_img, font=("Firacode", 20))
save_btn.place(x=10, y=145)

save_as_btn = CTkButton(btn_frame, width=210, height=60, corner_radius=10, text="Save As", command=lambda: saveas(), fg_color="#3848ab", image=saveas_img, font=("Firacode", 20))
save_as_btn.place(x=10, y=225)

hide_btn = CTkButton(btn_frame, width=210, height=60, corner_radius=10, text="Hide", fg_color="#3848ab", image=hide_img, font=("Firacode", 20), command=lambda: hide_panel())
hide_btn.place(x=10, y=305)

read_btn = CTkButton(btn_frame, width=210, height=60, corner_radius=10, text="Read", command=lambda: read_text(), fg_color="#3848ab", image=read_img, font=("Firacode", 20))
read_btn.place(x=10, y=385)

help_btn = CTkButton(btn_frame, width=210, height=60, corner_radius=10, text="Help", command=lambda: help(), fg_color="#3848ab", image=help_img, font=("Firacode", 20))
help_btn.place(x=10, y=465)

about_btn = CTkButton(btn_frame, width=210, height=60, corner_radius=10, text="About", command=lambda: about(), fg_color="#3848ab", image=about_img, font=("Firacode", 20))
about_btn.place(x=10, y=545)

settings_btn = CTkButton(btn_frame, width=210, height=60, corner_radius=10, text="Settings", command=lambda: settings(), fg_color="#3848ab", image=setting_img, font=("Firacode", 20))
settings_btn.place(x=10, y=625)

ai_assistant_btn = CTkButton(btn_frame, width=210, height=60, corner_radius=10, text="Assistant", command=lambda: show_assistant(), fg_color="#3848ab", image=setting_img, font=("Firacode", 20))
ai_assistant_btn.place(x=10, y=705)

textbox = CTkTextbox(text_frame, height=900, width=1462, font=("Raleway", 18))
textbox.place(x=0,y=0)

scroll = CTkScrollbar(text_frame, command=textbox.yview, height=textbox._current_height)
scroll.place(x=(textbox._current_width-12), y=0)

textbox.configure(yscrollcommand=scroll.set)

root.mainloop()