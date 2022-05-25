import tkinter as tk
from tkinter import *
from turtle import color

h_m_s = tk.Tk()
h_m_s.title("Userguide")
h_m_s.geometry("670x700")



my_str1 = tk.StringVar()
l1 = tk.Label(h_m_s, textvariable=my_str1, font=('monospace', 30, 'bold'), )
l1.grid(row=1, column=2)
my_str1.set("Home Automation system")
my_str2 = tk.StringVar()
l1 = tk.Label(h_m_s, textvariable=my_str2, font=('monospace', 20, 'bold'))
l1.grid(row=2, column=2)
my_str2.set("What do you need helping with\n\n")


# add buttons
button_border1 = tk.Button(h_m_s, highlightbackground="white",
                           highlightthickness=4, bd=10)
button_border2 = tk.Button(h_m_s, highlightbackground="white",
                           highlightthickness=4, bd=10)
button_border3 = tk.Button(h_m_s, highlightbackground="white",
                           highlightthickness=4, bd=10)

b1 = tk.Button(h_m_s, button_border1, text='Products', font=('monospace', 18, 'bold'), fg="white", width=50, height=5,
               bd=0, cursor="hand2",
               command=lambda: my_open1())
b1.grid(row=3, column=2)

b2 = tk.Button(h_m_s, button_border2, text='Account', font=('monospace', 18, 'bold'), fg="white", width=50, height=5,
               bd=0, cursor="hand2",
               command=lambda: my_open2())
b2.grid(row=4, column=2)

b3 = tk.Button(h_m_s, button_border2, text='Printer Guide', font=('monospace', 18, 'bold'), fg="white", width=50,
               height=5, bd=0, cursor="hand2",
               command=lambda: my_open3())
b3.grid(row=5, column=2)






def my_open1():
    h_m_s_child = Toplevel(h_m_s)  # Child window
    h_m_s_child.geometry("700x700")
    h_m_s_child.title("Your userguide")

    ton1 = tk.Button(h_m_s_child, button_border1, text="connection issues: 1.I can not connect to the internet: \nMake Sure WiFi is Enabled on Your Computer Use Your Computer’s Diagnostics Tools  \n Make Sure There Is Not an Internet Outage in Your Area Forget and\n Re-Add Your WiFi Network I am connected but the wifi isn’t responding \nor its slow: Try Rebooting your router and modem Check Your WiFi Router’s \nLights See if Your WiFi is Working on Other Devices  Reset Your Router to\n Factory Settings Remove Any Obstructions Blocking Your WiFi Signal Use Your\n Computer’s Diagnostics Tools   .", font=('Arial', 15, 'bold'), fg="white",
                     width=70, height=10, bd=0, cursor="hand2")
    ton1.grid(row=2, column=2)

    button2 = tk.Button(h_m_s_child, button_border1, text="I am connected but the wifi isn’t responding or its slow: \n - Try Rebooting your router and modem Check Your WiFi Router’s Lights \n- See if Your WiFi is Working on Other Devices  \n - Reset Your Router to Factory Settings\n - Remove Any Obstructions Blocking Your WiFi Signal Use \nYour Computer’s Diagnostics Tools  ", font=('Arial', 15, 'bold'),
                        fg="white", width=70, height=10, bd=0, cursor="hand2")
    button2.grid(row=3, column=2)

    button3 = tk.Button(h_m_s_child, button_border1, text="Have you restarted the prodoct? \n - Make sure you are connected to Wifi \n- if yes try resetting the product from your app \n- if yes try cheking the internetconnection make sure it is connected\n ",
                        font=('Arial', 15, 'bold'), fg="white", width=70, height=10, bd=0, cursor="hand2")
    button3.grid(row=4, column=2)


    button4 = tk.Button(h_m_s_child, button_border3, text='Go Back'
                                                         'Go back', font=('monospace', 18, 'bold'), fg="white",
                        width=18, height=2, bd=0, cursor="hand2",
                        command=h_m_s_child.destroy)
    button4.grid(row=5 , column=2)


def my_open2():
    h_m_s_child = Toplevel(h_m_s)  # Child window
    h_m_s_child.geometry("700x700")  # Size of the window
    h_m_s_child.title("Your userguide")

    ton1 = tk.Button(h_m_s_child, button_border2, text="The best and most efficient way to install apps is to \nsearch for the app in Google. \n - When founded you have to install the app with the  instructions given on the website.\n  IOS/MAC \n -   Puch install when installed push the file that has been downloaded \n -Next stepp is drag and drop the app in the Download folder\n (you will be guided) \n - And so the app is installed\n IOS/IPhone \n - The best way to install the app on iphone is app-store you can search for our app \n (Control4) in the search bar. \n -  Then you puch get and you have the app installed ", font=('Arial', 15, 'bold'), fg="white",
                     width=70, height=10, bd=0, cursor="hand2")
    ton1.grid(row=2, column=2)

    button2 = tk.Button(h_m_s_child, button_border2, text="On-site Security\n – Our data center feature a secured perimeter with multi-level security zones,\n CCTV video surveillance, physical locks, and security breach alarms.\n   Monitoring – \nProduction network systems, networked devices, and circuits are\n continuously monitored and logically administered. \nPhysical security, power, and internet connectivity for cloud \nprovided services are proactively managed and monitored.", font=('Arial', 15, 'bold'),
                        fg="white", width=70, height=10, bd=0, cursor="hand2")
    button2.grid(row=3, column=2)

    button3 = tk.Button(h_m_s_child, button_border2, text="Your information – \n We do not share the visitors information under any circumstanses. \nWe esure our visitor full security and privacy.",
                        font=('Arial', 15, 'bold'), fg="white", width=70, height=10, bd=0, cursor="hand2")
    button3.grid(row=4, column=2)

    button4 = tk.Button(h_m_s_child, button_border3, text='Go back', font=('monospace', 18, 'bold'), fg="white",
                        width=18, height=2, bd=0, cursor="hand2",
                        command=h_m_s_child.destroy)
    button4.grid(row=5, column=2)


def my_open3():
    h_m_s_child = Toplevel(h_m_s)  # Child window
    h_m_s_child.geometry("700x700")  # Size of the window
    h_m_s_child.title("Your userguide")

    ton1 = tk.Button(h_m_s_child, button_border2,
                     text="Can’t connet to my printer: \n Make sure you printer is on the same Network otherwise make\n sure the bluetooth is on, on you printer. \n - To be able to connect a printer in to a Network you may even\n need to install the software required. if not you could go the old \nfashion way and use a USB cable \n  2. Other problems could such as a need of a Wifi\n setup ión the printer which is guided   ",
                     font=('Arial', 15, 'bold'), fg="white", width=70, height=10, bd=0, cursor="hand2")
    ton1.grid(row=2, column=2)

    button2 = tk.Button(h_m_s_child, button_border2, text="unexpected unwanted errors \nin case you run out of ink you should replace the Ink. \n Using the right paper size is also important\n for avoiding unexpected and unwanted errors   ", font=('Arial', 15, 'bold'),
                        fg="white", width=70, height=10, bd=0, cursor="hand2")
    button2.grid(row=3, column=2)


    button4 = tk.Button(h_m_s_child, button_border3, text='Go back', font=('monospace', 18, 'bold'), fg="white",
                        width=18, height=2, bd=0, cursor="hand2",
                        command=h_m_s_child.destroy)
    button4.grid(row=10, column=2)





h_m_s.mainloop()
