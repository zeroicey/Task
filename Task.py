import tkinter as tk
import tkinter.messagebox
import os, sys


class main_window:
    def __init__(self, path):
        self.task_name = []
        self.task_list = []
        self.task_ing = []
        self.delete_list = []
        self.delete_ing = []
        i = 0
        self.i = i
        self.history_name = []
        try:
            os.path.exists(path+'\\NAME.txt')
            self.opentxtn()
        except:
            with open("NAME.txt","w") as file6:
                    pass
        try:
            os.path.exists(path+'\\HISTORY.txt')
            self.opentxth()
        except:
            with open("HISTORY.txt","w") as file7:
                    pass


    def opentxtn(self):
        with open("NAME.txt", "r", encoding = "utf-8") as file4:
            for r in file4.readlines():
                if r == "\n":
                    break
                else:
                    r = r.strip()
                    self.task_name.append(r)


    def opentxth(self):
        with open("HISTORY.txt", "r", encoding = "utf-8") as file5:
            for r1 in file5.readlines():
                if r1 == "\n":
                    break
                else:
                    r1 = r1.strip()
                    self.history_name.append(r1)


    def add_past(self, ing, List):
        for task in self.task_name:
            ing.append(tk.IntVar())
            c = tk.Checkbutton(self.window, text=task, variable=ing[-1], onvalue=1, offvalue=0)
            c.place(x=1, y=self.i * 27)
            List.append(c)
            self.i += 1


    def add(self, y):
        self.task_name.append(self.g1)
        self.task_ing.append(tk.IntVar())
        c = tk.Checkbutton(self.window, text=self.g1, variable=self.task_ing[-1], onvalue=1, offvalue=0)
        c.place(x=1, y=y)
        self.task_list.append(c)
        self.Entry1.delete(0, tk.END)
        self.i += 1


    def add_new(self):
        g1 = self.Entry1.get()
        if g1.strip() == '':
            self.Entry1.delete(0, tk.END)
            tkinter.messagebox.showwarning(title='注意', message='任务不能为空')
            return
        self.g1 = "".join(g1.split())
        if len(self.task_name) == 0:
            if self.g1 != 0:
                self.add(0)
        else:
            if self.g1 not in self.task_name:
                if self.g1 != "":
                    if len(self.task_name) != 17:
                        self.add(self.i*27)
                    else:
                        self.Entry1.delete(0, tk.END)
                        tkinter.messagebox.showwarning(title='注意', message='任务太多啦!')
                else:
                    pass
            else:
                self.Entry1.delete(0, tk.END)
                tkinter.messagebox.showwarning(title='注意', message='请不要重复添加,\n先完成上一个任务哦!')

                
    def new_window(self):
        master = tk.Tk()
        master.title('New Task 加油呀！')
        master.geometry('300x100')
        master.resizable(0, 0)
        l1 = tk.Label(master, text="新建:", foreground='red', font=('Arial',10)).pack()
        Entry1 = tk.Entry(master, font=('Arial', 9), width=36)
        Entry1.pack()
        self.Entry1 = Entry1
        # print("111")
        tk.Button(master, text="添加", command=self.add_new).pack()
        master.mainloop()


    def delete_all(self):
        self.i = 0
        for d in self.task_list:
            d.destroy()
            self.task_list = []
            self.task_ing = []
            self.task_name = []


    def delete(self):
        delete_num = []
        delete_num1 = []
        for s4 in self.delete_ing:
            id2 = self.delete_ing.index(s4)
            s4 = str(s4.get())
            if s4 == "1":
                delete_num.append(self.task_ing[id2])
                delete_num1.append(self.task_name[id2])
            self.delete_list[id2].destroy()
        for s5 in delete_num:
            id3 = delete_num.index(s5)
            self.task_ing.remove(s5)
            self.task_name.remove(delete_num1[id3])
        self.delete_ing = []
        self.delete_list = []
        self.i = 0
        self.b1.destroy()
        for task in self.task_name:
            id4 = self.task_name.index(task)
            c = tk.Checkbutton(self.window, text=task, variable=self.task_ing[id4], onvalue=1, offvalue=0)
            c.place(x=1, y=self.i * 27)
            self.task_list.append(c)
            self.i += 1


    def delete_only(self):
        for s3 in self.task_list:
            s3.destroy()
        self.task_list = []
        self.i = 0
        self.add_past(self.delete_ing, self.delete_list)
        b1 = tk.Button(self.window, text="删除", command=self.delete)
        self.b1 = b1
        self.b1.pack(side = tk.BOTTOM, fill = tk.X)


    def exit_save(self):
        with open("NAME.txt", "w") as file2:
            for s1 in self.task_ing:
                id1 = self.task_ing.index(s1)
                s1 = str(s1.get())
                if s1 == "0":
                    file2.write(self.task_name[id1])
                    file2.write("\n")
                else:
                    self.history_name.append(self.task_name[id1])
        with open("HISTORY.txt", "w") as file3:
            for s2 in self.history_name:
                file3.write(s2)
                file3.write("\n")
        sys.exit()


    def history_window(self):
        root = tk.Tk()
        sb = tk.Scrollbar(root)
        sb.pack(side=tk.RIGHT, fill=tk.Y)

        thebox = tk.Listbox(root, yscrollcommand=sb.set)
        # sb.set:ÐÞ¸ÄlistboxµÄÎÄ×Ö
        thebox.pack(side=tk.LEFT, fill=tk.BOTH)

        for item in self.history_name:
            thebox.insert(tk.END, item)
            sb.config(command=thebox.yview)

        root.mainloop()


    def run(self):
        self.window = tk.Tk()
        self.window.title("计划表")
        self.window.geometry('260x500')
        self.window.resizable(0, 0)
        m1 = tk.Menu(self.window)
        m2 = tk.Menu(m1, tearoff=False)
        m1.add_command(label="New", command=self.new_window)
        m1.add_cascade(label="Delete", menu=m2)
        m2.add_command(label="Only", command=self.delete_only)
        m2.add_command(label="All", command=self.delete_all)
        m1.add_command(label="History", command=self.history_window)
        m1.add_command(label="Exit", command=self.exit_save)
        self.window.config(menu=m1)
        self.add_past(self.task_ing, self.task_list)
        self.window.mainloop()

def main():
    md = main_window(os.getcwd())
    md.run()
if __name__ == '__main__':
    main()

