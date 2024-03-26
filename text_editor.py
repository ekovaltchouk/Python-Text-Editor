import tkinter as tk
from tkinter import font
from tkinter.colorchooser import askcolor
from tkinter.font import families

def apply_tag(text_edit, tag):
    try:
        # Check if there is a selection in the text widget
        if text_edit.tag_ranges("sel"):
            # Get the font weight from the selected text
            font_weight = font.BOLD if tag == 'bold' else font.NORMAL
            # Get the indices of the selected text
            start_index = text_edit.index("sel.first")
            end_index = text_edit.index("sel.last")
            # Apply the tag and configure the font properties
            text_edit.tag_add(tag, start_index, end_index)
            text_edit.tag_configure(tag, font=(text_edit.tag_cget(start_index, "font"), font_weight, 'italic' if tag == 'italic' else 'roman', 'underline' if tag == 'underline' else 'normal'))
        else:
            # If there's no selection, do nothing
            pass
    except tk.TclError as e:
        # Handle the case when there's no selection
        print("Error:", e)

def change_font(text_edit, font_var):
    selected_font = font_var.get()
    if selected_font in families():
        text_edit.configure(font=(selected_font, 18))

def change_color(text_edit):
    new_color = askcolor()
    if new_color:
        text_edit.tag_add("color", "sel.first", "sel.last")
        text_edit.tag_configure("color", foreground=new_color[1])

def main():
    # Main window
    window = tk.Tk()
    window.title("Text Editor")

    text_edit = tk.Text(window, font=("Times New Roman", 18))
    text_edit.pack(expand=True, fill="both")

    font_var = tk.StringVar()
    font_var.set("Times New Roman")
    font_dropdown = tk.OptionMenu(window, font_var, *families(), command=lambda x: change_font(text_edit, font_var))
    font_dropdown.pack()

    color_button = tk.Button(window, text="Change Color", command=lambda: change_color(text_edit))
    color_button.pack()

    window.mainloop()

if __name__ == "__main__":
    main()
