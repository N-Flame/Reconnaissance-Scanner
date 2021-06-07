from Port_Service_Name import Port_Service_Info
from tkinter import *
from tkinter import ttk 
from PIL import ImageTk, Image
from IP_Address import *
from Location_WS import *
from Ports_Open import *
from Port_Service_Name import *
from Robots_File import *
from Tech_used import *
from OS_Info import *

root = Tk()
root.geometry("1600x900")

root.title("Recconaisance Scanner")

menu = Menu(root)
new_item = Menu(menu)

tab_control = ttk.Notebook(root)
tab_control.pack(pady=15)

bgimg = ImageTk.PhotoImage(Image.open("imgs/scannerbg.jpg").resize((1, 1), Image.ANTIALIAS))
tab1.background = img  # Keep a reference in case this code is put in a function.
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

tab1 = Frame(tab_control, bg = '')
tab_control.add(tab1, text='Scanner')

tab2 = Frame(tab_control)
tab_control.add(tab2, text='Team')

tab3 = Frame(tab_control)
tab_control.add(tab3, text='Help')

root.config(menu=menu)

####################    Tool page    ########################

Ttitle = Label(tab1, text='Recconaisance Scanner', font=('Verdana', 24, 'bold'), fg='white').grid(row = 0, column = 1,pady=20)

inptxt = Text(tab1, height=2)

ipadd = ""

def printIP():
    global ipadd
    inp = inptxt.get(1.0, "end-1c")
    ip_output, ipadd = IP_Address(inp)
    outLabel.config(text = "OUTPUT: \n"+ip_output)
    
def printLoc():
    # inp = inptxt.get(1.0, "end-1c")
    loc_output = Location_WS(ipadd)
    outLabel.config(text = "OUTPUT: \n"+loc_output)

def printPortOpen(): 
    global ipadd   
    # inp = inptxt.get(1.0, "end-1c")
    oport_output = Ports_Open(ipadd)
    outLabel.config(text = "OUTPUT: \n"+oport_output)

def printDirs():    
    inp = inptxt.get(1.0, "end-1c")
    dir_output = Robots_File(inp)
    outLabel.config(text = "OUTPUT: \n"+dir_output)

def prinTech():    
    inp = inptxt.get(1.0, "end-1c")
    tec_output = Tech_used(inp)
    outLabel.config(text = "OUTPUT: \n"+tec_output)

def printOS():
    global ipadd
    os_output = OS_Info(ipadd)
    outLabel.config(text = "OUTPUT: \n"+os_output)
    
def printPortServ():    
    inp = inptxt.get(1.0, "end-1c")
    serv_output = Port_Service_Info(inp)
    outLabel.config(text = "OUTPUT: \n"+serv_output)

inptxt.grid(row = 1, column = 1, pady = 40, padx= 310)

# Create the Enter button
ipbtn = Button(tab1, text= "Ipaddress", width=15, height=3, command = printIP)
portbtn = Button(tab1, text= "Location", width=15, height=3, command = printLoc)
locbtn = Button(tab1, text= "Ports Open", width=15, height=3, command = printPortOpen)
dirbtn = Button(tab1, text= "Open Directories", width=15, height=3, command = printDirs)
techbtn = Button(tab1, text= "Tech Stack", width=15, height=3, command = prinTech)
osbtn = Button(tab1, text= "OS info", width=15, height=3, command = printOS)
servbtn = Button(tab1, text= "Port service info", width=15, height=3, command = printPortServ)

ipbtn.grid(row = 3, column = 0, pady = 10, padx = 40)
portbtn.grid(row = 4, column = 0, pady = 10, padx = 40)
locbtn.grid(row = 5, column = 0, pady = 10, padx = 40)
dirbtn.grid(row = 6, column = 0, pady = 10, padx = 40)
techbtn.grid(row = 7, column = 0, pady = 10, padx = 40)
osbtn.grid(row = 8, column = 0, pady = 10, padx = 40)
servbtn.grid(row = 9, column = 0, pady = 10, padx = 40)


outLabel = Label(tab1, text="OUTPUT:\n\n", anchor='w', justify=LEFT, wraplength=800)
outLabel.place(x=510, y=180)

####################    Team page    ########################

Ttitle = Label(tab2, text='Our Team', pady= 10).grid(row = 0, column = 2, padx=150)

img1 = ImageTk.PhotoImage(Image.open(r'C:\Users\WELCOME\Desktop\Python Project\imgs\kesha.jpg'))
name1 = Label(tab2, text='Kesha K. Kaneria', pady = 50, font=('Verdana', 24, 'bold'), fg='white')
img2 = ImageTk.PhotoImage(Image.open(r'C:\Users\WELCOME\Desktop\Python Project\imgs\nidhi.jpg'))
name2 = Label(tab2, text='Nidhi Shah', pady = 50,font=('Verdana', 24, 'bold'), fg='white')
img3 = ImageTk.PhotoImage(Image.open(r'C:\Users\WELCOME\Desktop\Python Project\imgs\deva.jpg'))
name3 = Label(tab2, text='Devanshi Harsora', pady = 50,font=('Verdana', 24, 'bold'), fg='white')
img4 = ImageTk.PhotoImage(Image.open(r'C:\Users\WELCOME\Desktop\Python Project\imgs\khubu.jpg'))
name4 = Label(tab2, text='Khushbu Parmar', pady = 50,font=('Verdana', 24, 'bold'), fg='white')

mt= Label(tab2, text=' ')
kk = Label(tab2, image = img1, text = 'Kesha K. Kaneria')
ns = Label(tab2, image = img2)
dh = Label(tab2, image = img3)
kp = Label(tab2, image = img4)

mt.grid(row=0, column=0, padx=160)
kk.grid(row = 1, column = 1, pady=120, padx=20)
name1.grid(row = 2, column = 1)
dh.grid(row = 1, column = 3)
name2.grid(row = 2, column = 3)
ns.grid(row = 3, column = 1)
name3.grid(row = 4, column = 1)
kp.grid(row = 3, column = 3)
name4.grid(row = 4, column = 3)

####################    Help page    ########################

Htitle = Label(tab3, text='Help', pady = 50)
Htitle.pack()

HelpLabel = Label(tab3, text="This Scanner will provide you the information like ipAddress, open ports, location, Tech stack used, Ports service Info, Public directory. For eg. If you want to find an ipAddress of a particular website, just paste the site in the search bar and click the ipAddress button, it will provide you the ipAddress of that website. \nIp Address it will provide ipAddress of that particular website. \nOpen ports, it will provide you all the ports of the website which are currently open. \nLocation, it will provide the location of the domain. \nTech stack used, it will provide you with all the technology which is used to develop a particular website like by which programming language this website is developed, which database is used for storing information, which servers are used by the website etc. \nPort service Info, it will provide information about port services available. \nPublic directories, it will provide a robot.txt file that tells search engine crawlers which pages or files the crawler can or can't request from your site. This is used mainly to avoid overloading your site with requests.", anchor=W, justify=LEFT, wraplength=1000)
HelpLabel.pack()

tab_control.pack(expand=1, fill='both')

root.mainloop()