from __future__ import unicode_literals
import youtube_dl
from appJar import gui
import time

app = gui('YouTubeAudioDownloader','1000x500')

class MyLogger(object):
    def debug(self,msg):
        app.queueFunction(app.addListItem,'l5',msg)
    def warning(self,msg):
        app.queueFunction(app.addListItem,'l5',msg)
    def error(self,msg):
        app.queueFunction(app.addListItem,'l5',msg)


app.addListBox('l5','',5,0,2,2)
app.setListBoxSticky('l5','news')

    



def press(btn):
    if btn == "Download":
        app.clearListBox('lb2')
        optb = app.getOptionBox('Format')
        ydl_opts={'format':optb,'outtml':'%(title)s','noplaylist':True,'logger':MyLogger()}
        durl = app.getEntry('e1')
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            mt1 = ydl.extract_info(durl)
            app.addListItems('lb2', [('Title: ' + str(mt1['title'])), ('Uploader:' + str(mt1['uploader'])), ('Views:' +str(mt1['view_count'])),('Duration:' + str(mt1['duration'])),('Upload Date:' + str(mt1['upload_date'])),('Format :' + str(mt1['format']))  ])
            if optb == None:
                optb = 'Video'
            app.addListItem('l5','Download Started as' + ' ' + optb + '...')

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            optb = app.getOptionBox('Format')
            if optb == 'best':
                optb = 'Video'
            elif optb == None:
                    optb = 'Video' 
            else:
                optb = 'Audio'
            ydl.download([durl])
            mt = ydl.extract_info(durl)
            app.clearEntry('e1')
            app.warningBox('Download','Complete')
            app.addListItem('lb1',(str(mt['title']) + '-  ////   -'+ str(optb) + ' ' + '-- OK'))



app.addEntry('e1',0,0)
app.addButton('Download',press,0,1)
app.setButtonSticky('Download','news')
app.addLabel('l2','Downloaded Items',1,0)
app.setLabelFg('l2','green')
app.setEntrySticky('e1','news')
app.addListBox('lb1','',2,0)
app.addListBox('lb2','',2,1)
app.addLabel('l3','Datas',1,1)
app.setLabelFg('l3','green')
app.addLabelOptionBox('Format',['-Video-','best','-Audio-','bestaudio'],3,0)
app.addLabel('l4','')
app.thread(MyLogger)
app.go()




