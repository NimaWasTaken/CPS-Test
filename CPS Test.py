from tkinter import *

root = Tk()
count = 0

def click():
    global count
    global score
    count += 1
    button.config(text= str(count) + " Clicks")
    score = count / 5
    button.after(5000, lambda: button.config(text=("Score: ",score),
                                        state=DISABLED,
                                        disabledforeground="#7289da"))
    
root.resizable(False,False)
root.title("CPS Test")
root.config(background="#7289da")
 
button = Button(root,
                text="Click me!",
                command=click,
                font=("Arial",30),
                fg="#7289da",
                bg="black",
                activeforeground="#7289da",
                activebackground="black")
button.pack()

button.after(5000, lambda: button.config(text=("Score: ",score),
                                        state=DISABLED,
                                        disabledforeground="#7289da"))
root.mainloop()