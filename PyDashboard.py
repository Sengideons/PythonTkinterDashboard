from tkinter import *
from PIL import ImageTk, Image
from datetime import *
import time
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np


class Dashboard:
    def __init__(self, window):
        self.window = window
        self.window.title('System Management Dashboard')
        self.window.geometry('1366x768')
        self.window.state('zoomed')
        self.window.resizable(0, 0)
        self.window.config(background='#eff5f6')
        # window Icon
        icon = PhotoImage(file='images\\pic-icon.png')
        self.window.iconphoto(True, icon)

        # =====================================================================================
        # ============================ HEADER =================================================
        # =====================================================================================
        self.header = Frame(self.window, bg='#009df4')
        self.header.place(x=300, y=0, width=1070, height=60)

        self.logout_text = Button(self.header, text='Logout', bg='#32cf8e', font=("", 13, "bold"), bd=0, fg='white',
                                  cursor='hand2', activebackground='#32cf8e')
        self.logout_text.place(x=950, y=15)

        # =====================================================================================
        # ============================ SIDEBAR =================================================
        # =====================================================================================
        self.sidebar = Frame(self.window, bg='#ffffff')
        self.sidebar.place(x=0, y=0, width=300, height=750)

        # Logo
        self.logoImage = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.logoImage)
        self.logo = Label(self.sidebar, image=photo, bg='#ffffff')
        self.logo.image = photo
        self.logo.place(x=70, y=80)

        # Name of brand/person
        self.brandName = Label(self.sidebar, text='Sen Gideons', bg='#ffffff', font=("", 15, "bold"))
        self.brandName.place(x=80, y=200)

        # Dashboard
        self.dashboardImage = Image.open('images\\dashboard-icon.png')
        photo = ImageTk.PhotoImage(self.dashboardImage)
        self.dashboard = Label(self.sidebar, image=photo, bg='#ffffff')
        self.dashboard.image = photo
        self.dashboard.place(x=35, y=289)

        self.dashboard_text = Button(self.sidebar, text='Dashboard', bg='#ffffff', font=("", 13, "bold"), bd=0,
                                     cursor='hand2', activebackground='#ffffff')
        self.dashboard_text.place(x=80, y=291)

        # Manage
        self.manageImage = Image.open('images\\manage-icon.png')
        photo = ImageTk.PhotoImage(self.manageImage)
        self.manage = Label(self.sidebar, image=photo, bg='#ffffff')
        self.manage.image = photo
        self.manage.place(x=35, y=340)

        self.manage_text = Button(self.sidebar, text='Manage', bg='#ffffff', font=("", 13, "bold"), bd=0,
                                  cursor='hand2', activebackground='#ffffff')
        self.manage_text.place(x=80, y=345)

        # Settings
        self.settingsImage = Image.open('images\\settings-icon.png')
        photo = ImageTk.PhotoImage(self.settingsImage)
        self.settings = Label(self.sidebar, image=photo, bg='#ffffff')
        self.settings.image = photo
        self.settings.place(x=35, y=402)

        self.settings_text = Button(self.sidebar, text='Settings', bg='#ffffff', font=("", 13, "bold"), bd=0,
                                    cursor='hand2', activebackground='#ffffff')
        self.settings_text.place(x=80, y=402)

        # Exit
        self.exitImage = Image.open('images\\exit-icon.png')
        photo = ImageTk.PhotoImage(self.exitImage)
        self.exit = Label(self.sidebar, image=photo, bg='#ffffff')
        self.exit.image = photo
        self.exit.place(x=25, y=452)

        self.exit_text = Button(self.sidebar, text='Exit', bg='#ffffff', font=("", 13, "bold"), bd=0,
                                cursor='hand2', activebackground='#ffffff')
        self.exit_text.place(x=85, y=462)





        # =====================================================================================
        # ============================ BODY =================================================
        # =====================================================================================
        self.heading = Label(self.window, text='Dashboard', font=("", 13, "bold"), fg='#0064d3', bg='#eff5f6')
        self.heading.place(x=325, y=70)

        # ======== Body Frame 1 =======
        self.bodyFrame1 = Frame(self.window, bg='#ffffff')
        self.bodyFrame1.place(x=328, y=110, width=1040, height=350)

        # ======== Body Frame 2 =======
        self.bodyFrame2 = Frame(self.window, bg='#009aa5')
        self.bodyFrame2.place(x=328, y=495, width=310, height=220)

        # ======== Body Frame 3 =======
        self.bodyFrame3 = Frame(self.window, bg='#e21f26')
        self.bodyFrame3.place(x=680, y=495, width=310, height=220)

        # ======== Body Frame 4 ======
        self.bodyFrame4 = Frame(self.window, bg='#ffcb1f')

        self.bodyFrame4.place(x=1030, y=495, width=310, height=220)

        # Pie Chart
        #self.PieChartImage = Image.open('images\\pie-graph1.png')
        #photo = ImageTk.PhotoImage(self.PieChartImage)
        #self.PieChart = Label(self.bodyFrame1, image=photo, bg='#ffffff')
        #self.PieChart.image = photo
        #self.PieChart.place(x=690, y=70)


        # Data Base
        data = pd.read_excel("C:\\Users\\User\\PycharmProjects\\MyYoutubeTutorials\\Book1.xlsx")

        sumjulius = sum(data['Julius'])
        sumgideons = sum(data['Gideons'])
        sumjustice = sum(data['Justice'])
        sumdaniel = sum(data['Daniel'])
        sumsimon = sum(data['Simon'])
        sumdennis = sum(data['Dennis'])

        #### Plotting pie chart #####
        fig = plt.figure(figsize=(5, 5), dpi=100)
        fig.set_size_inches(5, 3.5)

        # Data to plot
        labels = 'Julius', 'Gideons', 'Justice', 'Daniel', 'Simon', 'Dennis'
        sizes = [sumjulius, sumgideons, sumjustice, sumdaniel, sumsimon, sumdennis]
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'Orange', 'red']
        explode = (0.2, 0, 0, 0, 0, 0)

        # Plot pie chart
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

        plt.axis('equal')  # creates the pie chart like a circle

        canvasbar = FigureCanvasTkAgg(fig, master=self.window)
        canvasbar.draw()
        canvasbar.get_tk_widget().place(x=1120, y=285, anchor=CENTER)  # show the barchart on the ouput window



        # Graph
        #self.graphImage = Image.open('images\\graph.png')
        #photo = ImageTk.PhotoImage(self.graphImage)
        #self.graph = Label(self.bodyFrame1, image=photo, bg='#ffffff')
        #self.graph.image = photo
        #self.graph.place(x=40, y=70)

        fig = plt.figure(figsize=(5, 3.5), dpi=100)
        labels = ('Julius', 'Gideons', 'Justice', 'Daniel', 'Simon', 'Dennis')
        labelpos = np.arange(len(labels))
        studentsum = [sumjulius, sumgideons, sumjustice, sumdaniel, sumsimon, sumdennis]

        ##This section formats the barchart for output

        plt.bar(labelpos, studentsum, align='center', alpha=1.0)
        plt.xticks(labelpos, labels)
        plt.ylabel('Average raw mark')
        plt.xlabel('Students')
        plt.tight_layout(pad=2.2, w_pad=0.5, h_pad=0.1)
        plt.title('Average raw mark for all subjects')
        plt.xticks(rotation=30, horizontalalignment="center")

        # Applies the values on the top of the bar chart
        for index, datapoints in enumerate(studentsum):
            plt.text(x=index, y=datapoints + 0.3, s=f"{datapoints}", fontdict=dict(fontsize=10), ha='center',
                     va='bottom')



        ## This section draws a canvas to allow the barchart to appear in it
        canvasbar = FigureCanvasTkAgg(fig, master=self.window)
        canvasbar.draw()
        canvasbar.get_tk_widget().place(x=600, y=285, anchor=CENTER)  # show the barchart on the ouput window



        self.window.protocol("WM_DELETE_WINDOW", self.Exit)



        # Total People
        self.totalPeopleImage = Image.open('images\\left-icon.png')
        photo = ImageTk.PhotoImage(self.totalPeopleImage)
        self.totalPeople = Label(self.bodyFrame2, image=photo, bg='#009aa5')
        self.totalPeople.image = photo
        self.totalPeople.place(x=220, y=0)

        self.totalPeople_text = Label(self.bodyFrame2, text='230', bg='#009aa5', font=("", 25, "bold"))
        self.totalPeople_text.place(x=120, y=100)

        self.total_people = Label(self.bodyFrame2, text='Total People', bg='#009aa5', font=("", 13, "bold"))
        self.total_people.place(x=5, y=5)

        # Left
        self.people_who_leftImage = Image.open('images\\left-icon.png')
        photo = ImageTk.PhotoImage(self.people_who_leftImage)
        self.people_who_left = Label(self.bodyFrame3, image=photo, bg='#e21f26')
        self.people_who_left.image = photo
        self.people_who_left.place(x=220, y=0)

        self.people_who_left_text = Label(self.bodyFrame3, text='People Who Left', bg='#e21f26', font=("", 13, "bold"))
        self.people_who_left_text.place(x=5, y=5)

        self.people_who_left = Label(self.bodyFrame3, text='100', bg='#e21f26', font=("", 25, "bold"))
        self.people_who_left.place(x=120, y=100)

        # Earnings
        self.earnImage = Image.open('images\\earn3.png')
        photo = ImageTk.PhotoImage(self.earnImage)
        self.earn = Label(self.bodyFrame4, image=photo, bg='#ffcb1f')
        self.earn.image = photo
        self.earn.place(x=220, y=0)

        self.earn_text = Label(self.bodyFrame4, text='Earnings', bg='#ffcb1f', font=("", 13, "bold"))
        self.earn_text.place(x=5, y=5)

        self.earn_figure = Label(self.bodyFrame4, text='$40,000.00', bg='#ffcb1f', font=("", 25, "bold"))
        self.earn_figure.place(x=80, y=100)

        # ======= TIME AND DATE ============
        self.clock_image = Image.open('images\\time.png')
        photo = ImageTk.PhotoImage(self.clock_image)
        self.date_time_image = Label(self.sidebar, image=photo, bg='#ffffff')
        self.date_time_image.image = photo
        self.date_time_image.place(x=88, y=20)

        self.date_time = Label(self.window)
        self.date_time.place(x=115, y=15)
        self.show_time()

    def show_time(self):
        self.time = time.strftime("%H:%M:%S")
        self.date = time.strftime('%Y/%m/%d')
        set_text = f" {self.time} \n {self.date}"
        self.date_time.configure(text=set_text, font=("", 13, "bold"), bd=0, bg="white", fg="black")
        self.date_time.after(100, self.show_time)



    def Exit(self):
        self.window.quit()







def win():
    window = Tk()
    Dashboard(window)
    window.mainloop()

if __name__ =='__main__':
    plt.show()
    win()
