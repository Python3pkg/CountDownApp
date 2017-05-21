import datetime as dt
import six

if six.PY2:
    from tkinter import *

if six.PY3:
    from tkinter import *

class CountDownTimer:

    dark  = '#333333'
    white = '#D0D6D3'
    master = None
    titleLabel = None
    countLabel = None
    footerLabel = None
    
    initWidth = None
    initHeight = None
    initFlag = True
    
    labelMargin = 30
    
    resizeCoeff = 1.0
    
    width = None
    height = None
    
    def __init__(self, titleText="", finishTime="", footerText="", baseFontSize=100):
        self.titleText = titleText
        self.finishTime = finishTime
        self.footerText = footerText
        self.baseFontSize = int(baseFontSize)
        self.nomarl_font = ("Helvetica", baseFontSize)
        self.large_font  = ("Helvetica", int(baseFontSize * 1.5))

    def countDown(self):
        self.countLabel.configure(text=self.getRemainingTimeText())
        self.master.after(1000, self.countDown)

    def getRemainingTimeText(self):
        current_time = dt.datetime.now()
        finish_time  = dt.datetime.strptime(self.finishTime, '%Y-%m-%d %H:%M:%S')
        diff_time    = finish_time - current_time
        total_second = diff_time.seconds

        days = diff_time.days
        hour = total_second // 3600
        minute = (total_second - 3600 * hour) // 60
        second = total_second - 3600 * hour - 60 * minute 
        
        return "{0} Days\n {1:02d}:{2:02d}:{3:02d}".format(days, hour, minute, second)

    def getWindowSize(self, event):
        self.width = self.master.winfo_width()
        self.height = self.master.winfo_height()
        
        if self.initFlag:
            self.initWidth = self.master.winfo_width()
            self.initHeight = self.master.winfo_height()
            self.initFlag = False
        
        self.resizeCoeff = self.height / self.initHeight
        self.updateFontSize()
        self.updateGridSize()
        
    def updateFontSize(self):
        baseFontSize = int(self.baseFontSize * self.resizeCoeff)
        self.nomarl_font = ("Helvetica", baseFontSize)
        self.large_font  = ("Helvetica", int(baseFontSize * 1.5))
    
        self.titleLabel.configure(font=self.nomarl_font)
        self.countLabel.configure(font=self.large_font)
        self.footerLabel.configure(font=self.nomarl_font)
    
    def updateGridSize(self):
        labelMargin = int(self.labelMargin * self.resizeCoeff)
        self.titleLabel.grid(pady=(labelMargin, 0))
        self.countLabel.grid(pady=(labelMargin, labelMargin))
        self.footerLabel.grid(pady=(0, labelMargin))
    
    def run(self):
        self.master = Tk()
        self.master.configure(background=self.dark)
        self.master.bind("<Configure>", self.getWindowSize)
        self.master.columnconfigure(0, weight=1)
        self.master.title("Count Down Timer")
        
        self.titleLabel = Label(text=self.titleText, font=self.nomarl_font, fg=self.white, bg=self.dark)
        
        self.countLabel = Label(text=self.getRemainingTimeText(), font=self.large_font, fg=self.dark, bg=self.white)
        self.master.after(1000, self.countDown)
        
        self.footerLabel = Label(text=self.footerText, font=self.nomarl_font, fg=self.white, bg=self.dark)
        
        self.titleLabel.grid(row=0, column=0, pady=(self.labelMargin, 0), sticky=W+E+N+S)
        self.countLabel.grid(row=1, column=0, pady=(self.labelMargin, self.labelMargin), sticky=W+E+N+S)
        self.footerLabel.grid(row=2, column=0, pady=(0, self.labelMargin), sticky=W+E+N+S)
        
        self.master.mainloop()

if __name__ == '__main__':
    app = CountDownTimer(
      titleText="Title Text", 
      finishTime="2017-01-01 00:00:00",  # Format: YYYY-mm-DD HH:MM:SS
      footerText="Footer Text", 
      baseFontSize=100
    )
    app.run()

    
    