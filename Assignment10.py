import tkinter as tk
import webbrowser as wb

obj=tk.Tk(className="Reddit")

e=tk.Entry(obj,
           font=("Copper Black",25),
           width=50)
e.grid()

def display():
    s=e.get()
    print(s)
    wb.open("https://www.reddit.com/search?q="+s)
    print("you are navigating to Reddit search bar")
    

b=tk.Button(obj,text="Button",
            font=("Copper Black",25),
          
            activebackground="grey",command=display)

b.grid(row=0,column=1)
obj.mainloop()