from __future__ import unicode_literals
import youtube_dl
from appJar import gui
import time
from ffprobe import FFProbe
from Tkinter import Tk
import tkFileDialog 

locat = '/root/Downloads/' 

def tkfl():
    global locat
    locat = tkFileDialog.askdirectory() + '/'
    


app = gui('YouTubeAudioDownloader','1366x650')

class MyLogger(object):
    def debug(self,msg):
        if msg[5:13] == 'download':
            app.addListItem('l5',msg[14:])
        else:
            app.addListItem('l5',msg)
    def warning(self,msg):
        app.addListItem('l5',msg)
    def error(self,msg):
        app.addListItem('l5',msg)
        print msg



def my_hook(d):
    app.setStatusbar(d['status'])
    if not d['status'] == 'finished':
        down = d['downloaded_bytes']
        siz = d['total_bytes']
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
        }],'outtmpl':locat + '%(title)s'+'%(id)s'+'.' +'%(ext)s'}
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
                mt6ex = (str(mt1['ext']))
                mtf = (str(mt1['format']))
                app.addGridRow('lb1',[mt1t,mt2u,mt3v,mt4d,mt5ud,mt6ex,mtf])
                ydl.download([durl])
                print locat
                app.clearEntry('e1')
        app.thread(getinfo) 


app.addEntry('e1',0,0)
app.setEntryDefault('e1','URL')
app.addButton('Download',press,0,1)
app.setButtonSticky('Download','news')
app.setButtonFg('Download','seagreen')
app.addLabel('l2','Downloaded Items',1,0)
app.setLabelSticky('l2','ews')
app.addLabel('l7','',1,1)
app.setLabelBg('l7','seagreen')
app.setLabelSticky('l7','ews')
app.setLabelBg('l2','seagreen')
app.setEntrySticky('e1','news')
app.addGrid('lb1',[['Title','Uploader','Views','Duration','Upload Date','Ext','Format']],2,0,2,2)
app.setGridSticky('lb1','news')
app.addLabelOptionBox('Format',['-Video-','best','-Audio-','bestaudio'],3,1)
app.setOptionBoxSticky('Format','top')
app.addLabel('l4','Logger',4,0)
app.setLabelSticky('l4','news')
app.addLabel('l5b','',4,1)
app.setLabelSticky('l5b','news')
app.setLabelBg('l5b','seagreen')
app.setLabelBg('l4','seagreen')
app.addListBox('l5','',5,0,2,2)
app.setListBoxSticky('l5','news')
app.addMeter('progress',3,0)
app.setMeterSticky('progress','ews')
app.setMeterFill('progress','seagreen')
app.addMenuList('File',['Select Download Folder'],tkfl)
app.addStatusbar(fields=1,side="LEFT")
app.setStatusbarBg('seagreen')
app.setStatusbarWidth(200)
app.setSticky('news')
app.go()




