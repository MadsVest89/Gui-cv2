import tkinter as tk
from Video import VideoStream
import PIL.Image, PIL.ImageTk


class Gui:


    def __init__(self, master,video_source = 0):
        self.master = master
        self.frame = tk.Frame(self.master)
        master.title("A simple GUI")
        master.attributes("-fullscreen",True)
        master.configure(background="black")

        self.video_source  = video_source 
        self.vid = VideoStream()

        self.canvas = tk.Canvas(master, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()



        self.OnStatus()
        self.PowerLevel()
        self.SpeedLabel()
        self.udate()

        
        self.delay = 15
 


        

    def udate(self):
  


        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
            
        self.window.after(self.delay, self.update)


    def PowerLevel(self):

        PowerLevelVar = tk.StringVar()
        PowerLevelVar.set('tester1')

        powerLvl = tk.Label(text = "power: " + str(PowerLevelVar.get()),fg="white",bg="black",font=("Helvetica",16) )
        powerLvl.place(x=200,y=25)


    def SpeedLabel(self):
        
        speed = tk.IntVar()
        speed.set(666)

        speedometer= tk.Label(text = "Speed: " + str(speed.get()) + " m/s" ,fg="white",bg="black",font=("Helvetica",16))
        speedometer.place(x=40,y=25)


    def OnStatus(self):
        
        OnStatusSignal = 0

        ConDisplay = tk.Frame(width=30, height=30)
        ConDisplay.place(x=10,y=25)

        if OnStatusSignal == 1:
            ConDisplay.config(bg = "green")
        else:
            ConDisplay.config(bg = "red")

     
def main(): 
    root = tk.Tk()
    app = Gui(root)
    root.mainloop()


if __name__ == '__main__':
    main()


