from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from text import A
root = Tk()
root.title("Sorting Data")
Label(root, text="Your Choice:").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(root, text="Emails ", variable=var1).grid(row=1, column=0)
var2 = IntVar()
Checkbutton(root, text="Domains", variable=var2).grid(row=1,column=1 )
var3 = IntVar()
Checkbutton(root, text=" URLS", variable=var3).grid(row=1, column=1,columnspan=5)
var4 = IntVar()
Checkbutton(root, text="IPs    ", variable=var4).grid(row=1, column=3)
var5 = IntVar()
Checkbutton(root, text="MAC    ", variable=var5).grid(row=2, column=0)
var6 = IntVar()
Checkbutton(root, text="Hash   ", variable=var6).grid(row=2, column=1)
var7 = IntVar()
Checkbutton(root, text="  Url with extention", variable=var7).grid(row=2, column=2)
var8 = IntVar()
ttk.Radiobutton(root, text="URL", variable=var8, value=2).grid(row=4, column=1)
ttk.Radiobutton(root, text="Text File", variable=var8, value=1).grid(row=4, column=2)
ttk.Label(root, text="Select Choice:").grid(row=4, column=0)
ttk.Label(root, text="URL").grid(row=5, column=0)
ttk.Label(root, text="Sorting Data CODED BY:' Ismael Al-safadi '").grid(row=6, column=1,columnspan=2)
Name = ttk.Entry(root, width=60)
Name.grid(row=5, column=1, columnspan=2)
buButton=ttk.Button(root,text="Submit")
buButton.grid(row=6,column=0)
buButton1=ttk.Button(root,text="Quit")
buButton1.grid(row=6,column=3)
def files_files():
    global path   
    path = askopenfilename()
    path=str(path)
    return path  

def urls_urls():
    global url
    url=Name.get()
    url=str(url)
    return url
	
def ButtunClick(files_files,urls_urls):
    
    choice=var8.get()
    if choice ==1:
        files_files=files_files()
    elif choice ==2:
        messagebox.showinfo(title="Wait", message="Please wait it will take seconds")
        urls_urls=urls_urls()
    if var1.get() ==1 :
        c=A(files_files,choice,urls_urls)
        c.emails()
    else:
        pass
    if var2.get() ==1 :
         c=A(files_files,choice,urls_urls)
         c.domains()
    else:
        pass
    if var3.get() ==1 :
       c=A(files_files,choice,urls_urls)
       c.urls()
    else:
        pass
    if var4.get() ==1:
        c=A(files_files,choice,urls_urls)
        c.ips()
    else:
        pass
    if var5.get() ==1:
        c=A(files_files,choice,urls_urls)
        c.macs()
    else:
        pass
    if var6.get() ==1:
        c=A(files_files,choice,urls_urls)
        c.hashes()
    else:
        pass
    if var7.get() ==1:
        c=A(files_files,choice,urls_urls)
        c.extention()
    else:
        pass
    messagebox.showinfo(title="Done", message="Done ^__^ the results save in the same file")
buButton.config(command=lambda:ButtunClick(files_files,urls_urls))
buButton1.config(command=root.destroy)
root.mainloop()

