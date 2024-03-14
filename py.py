
from tkinter import *
from tkinter import ttk 

class todolist:
    def __init__(self, root):
        self.root = root 
        self.root.title('To-Do-list-Using-Python')
        self.root.geometry('650x410+300+150')

        self.label = Label(self.root,text='To-Do-list-App-Using-Python', font='ariel, 25 bold', width=15,bd=7, bg= 'green',fg='black')
        self.label.pack(side='top',fill=BOTH)

        self.label2 = Label(self.root,text='Add Task', font='ariel, 19 bold', width=15,bd=7, bg= 'green',fg='black')
        self.label2.place(x=40,y=67)

        self.label3 = Label(self.root,text='Tasks', font='ariel, 19 bold', width=10,bd=5, bg= 'green',fg='black')
        self.label3.place(x=320,y=67)

        self.main_text = Listbox(self.root, height=8, bd=5, width=20, font ="ariel, 22 italic bold")
        self.main_text.place(x=280, y=120)
         
        self.text= Text(self.root, bd=5,height= 2, width= 30, font="ariel, 11 bold")
        self.text.place(x=20,y=130)


        def add():
            con= self.text.get(1.0, END)
            self.main_text.insert(END, con)
            with open('ram.txt','a') as file:
                file.write(con)
                file.seek(0)
                file.close()
            self.text.delete(1.0, END)

        def delete():
            delete_= self.main_text.curselection()
            look = self.main_text.get(delete_)
            with open ('ram.txt','r+') as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    item= str(look)
                    if item not in line:
                        f.write(line)
                    f.truncate()
            self.main_text.delete(delete_)
        with open('ram.txt', 'r') as file:
            read = file.readlines()
            for i in read:
                ready= i.split()
                self.main_text.insert(END, ready)
            file.close()
        self.button = Button(self.root, text="Add", font='serif 20 bold italic', width=10, bg='Green', fg='black', command=add)
        self.button.place(x=30, y=180)


        self.button = Button(self.root, text="DELETE", font='serif 20 bold italic', width=10, bg='Green', fg='black', command=delete)
        self.button.place(x=30, y=280)

        
def main():
    root = Tk()
    ui = todolist(root)
    root.mainloop()

if __name__ == "__main__":  
    main()
