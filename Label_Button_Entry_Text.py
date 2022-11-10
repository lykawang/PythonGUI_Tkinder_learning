# conference website: https://realpython.com/python-gui-tkinter/

import tkinter as tk

window = tk.Tk()



# Label widgets are used to display text or images. The text displayed by a Label widget can’t be edited by the user.
# It’s for display purposes only.
greeting = tk.Label(
    text="Hello, Tkinter",
    fg="white",  # Set the text color to white
    bg="#34A2FE",  # Set the background color to blue
    width=10,  # measured in text units
    height=10
)
greeting.pack()



# Button widgets are used to display clickable buttons.
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()



# Entry widget display a small text box that the user can type some text into.
entry1 = tk.Entry(fg="yellow", bg="blue", width=50)
entry1.pack()
entry2 = tk.Entry()

entry2.pack()

# some functions
name = entry2.get()  # retrieve the text and assign it to a variable
entry2.delete(0)  # takes a(two) integer argument that tells Python which character(s) to remove
entry2.delete(0, 4)
entry2.delete(0, tk.END)
entry2.insert(0, "Python")



# window.destroy()



# create a new blank window for text boxes which are much larger than Entry widgets by default.
text_box = tk.Text()
text_box.pack()
# the get() function requires argument <line>.<char>
text_box.get("1.0")  #"1.0" represents the first character on the first line
text_box.get("1.0", "1.5")
text_box.get("1.0", tk.END)
text_box.delete("1.0", "1.4")  # leave blank after deleting
text_box.delete("1.0")  #If you delete that character, then the rest of the contents of the text box will shift up a line
text_box.insert("1.0", "Hello")
text_box.insert("2.0", "\nWorld")
text_box.insert(tk.END, "\nPut me at the end!")



window.mainloop()