# geometry managers
# .pack()
# .place()
# .grid()
# Each window or Frame in your application can use only one geometry manager.
# However, different frames can use different geometry managers,
# even if they’re assigned to a frame or window using another geometry manager.

# import tkinter as tk
#
# window = tk.Tk()
#
# frame1 = tk.Frame(master=window, height=100, bg="red")  # also can add width=100
# frame1.pack(fill=tk.X)
#
# frame2 = tk.Frame(master=window, height=50, bg="yellow")
# frame2.pack(fill=tk.X)
#
# frame3 = tk.Frame(master=window, height=25, bg="blue")
# frame3.pack(fill=tk.X)
#
# window.mainloop()



# some other options
# tk.TOP
# tk.BOTTOM
# tk.LEFT
# tk.RIGHT


# import tkinter as tk
#
# window = tk.Tk()
#
# frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
# frame1.pack(fill=tk.Y, side=tk.LEFT)
#
# frame2 = tk.Frame(master=window, width=100, bg="yellow")
# frame2.pack(fill=tk.Y, side=tk.LEFT)
#
# frame3 = tk.Frame(master=window, width=50, bg="blue")
# frame3.pack(fill=tk.Y, side=tk.LEFT)
#
# window.mainloop()



import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop()