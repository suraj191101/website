from tkinter import *
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title(" Website unBlocker")
Label(root, text ='WEBSITE UNBLOCKER' , font ='arial 20 bold').pack()
host_path =r"C:\Users\devin\OneDrive\Desktop\hosts"
ip_address = '127.0.0.1'
Label(root, text ='Enter Website :' , font ='arial 13 bold').place(x=5 ,y=60)
Websites = Text(root,font = 'arial 10',height='2', width = '40', wrap = WORD, padx=5, 
pady=5)
Websites.place(x= 140,y = 60)
def unblocker():
    website_lists = Websites.get(1.0,END)
    Website = list(website_lists.split(","))
    with open (host_path , 'r') as host_file:
        file_content = host_file.readlines()
        for website in Website:
            print(website)

            content=ip_address+" "+website
            #print(content)
            if content not in file_content:
                Label(root, text = 'Already UNBlocked' , font = 'arial 12 bold').place(x=200,y=200)
                pass
            else:
                with open(host_path,'w') as file:
                    for line in file_content:
                        if(line!=content):
                            file.write(line)
                file.close()
                Label(root, text = "UNBlocked", font = 'arial 12 bold').place(x=230,y =200)
block = Button(root, text = 'UNBlock',font = 'arial 12 bold',pady = 5,command =
unblocker ,width = 6, bg = 'royal blue1', activebackground='red')
block.place(x = 230, y = 150)
root.mainloop()
