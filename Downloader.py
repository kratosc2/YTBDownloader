from __future__ import unicode_literals
import youtube_dl
from appJar import gui
import time
from ffprobe import FFProbe
from Tkinter import Tk
import tkFileDialog 

locat = '' 

def tkfl():
    global locat
    locat = tkFileDialog.askdirectory() + '/'
    print locat


app = gui('YouTubeAudioDownloader','1366x600')

class MyLogger(object):
    def debug(self,msg):
        app.addListItem('l5',msg)
    def warning(self,msg):
        app.addListItem('l5',msg)
    def error(self,msg):
        app.addListItem('l5',msg)



def my_hook(d):
    print d['status']
    if not d['status'] == 'finished':
        down = d['downloaded_bytes']
        filesiz = d['total_bytes']
        etc = down / (filesiz / 100)
        if etc > 0:
            app.setMeter('progress',etc)
    
        
        


    


def press(btn):
    if btn == "Download":
        optb = app.getOptionBox('Format')
        if optb == "best" or optb == None: 
            ydl_opts={'format:':optb,'outtml':'%(title)s', 'nonplaylist':True,'logger':MyLogger(),'progress_hooks':[my_hook],'outtmpl':locat+ '%(title)s'}
        else:
            ydl_opts={'format':optb,'outtml':'%(title)s','noplaylist':True,'logger':MyLogger(), 'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
        }]}
        durl = app.getEntry('e1')
        
        def getinfo():
            global locat
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                mt1 = ydl.extract_info(durl,download=False)
                mt1t = (str(mt1['title'].encode('ascii','replace')) )
                mt2u = (str(mt1['uploader'].encode('ascii','replace')) )
                mt3v = (str(mt1['view_count']) )
                mt4d = ((str(mt1['duration'] / 60) + ':'+ str(mt1['duration'] % 60) ) )
                mt5ud = (str(mt1['upload_date']) )
                mt6f = (str(mt1['format']))
                app.addGridRow('lb1',[mt1t,mt2u,mt3v,mt4d,mt5ud,mt6f])
                ydl.download([durl])
                print locat

        app.thread(getinfo) 


app.addEntry('e1',0,0)
app.setEntryDefault('e1','URL')
app.addButton('Download',press,0,1)
app.setButtonSticky('Download','news')
app.setButtonFg('Download','green')
app.addLabel('l2','Downloaded Items',1,0)
app.setLabelFg('l2','green')
app.setEntrySticky('e1','news')
app.addGrid('lb1',[['Title','Uploader','Views','Duration','Upload Date','Format']],2,0,2,2)
app.setGridSticky('lb1','news')
app.addLabelOptionBox('Format',['-Video-','best','-Audio-','bestaudio'],3,1)
app.addLabel('l4','Logger',4,0)
app.addLabel('l5b','',4,1)
app.setLabelBg('l5b','green')
app.setLabelBg('l4','green')
app.addListBox('l5','',5,0,2,2)
app.setListBoxSticky('l5','news')
app.addMeter('progress',3,0)
app.setMeterFill('progress','green')
app.addMenuList('File',['Select Download Folder'],tkfl)


app.go()




