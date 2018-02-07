from __future__ import unicode_literals
import youtube_dl
from appJar import gui
import time
from ffprobe import FFProbe

app = gui('YouTubeAudioDownloader','1000x550')

class MyLogger(object):
    def debug(self,msg):
        app.queueFunction(app.addListItem,'l5',msg)
    def warning(self,msg):
        app.queueFunction(app.addListItem,'l5',msg)
    def error(self,msg):
        app.queueFunction(app.addListItem,'l5',msg)



    



def press(btn):
    if btn == "Download":
        app.clearListBox('lb2')
        optb = app.getOptionBox('Format')
        if optb == "best" or optb == None:
            
            ydl_opts={'format:':optb,'outtml':'%(title)s','nonplaylist':True,'logger':MyLogger()}
        else:
            print "else"
            ydl_opts={'format':optb,'outtml':'%(title)s','noplaylist':True,'logger':MyLogger(), 'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
        }]}
        durl = app.getEntry('e1')
        
        def getinfo():
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                mt1 = ydl.extract_info(durl)
                mt1t = ('Title:' + str(mt1['title'].encode('ascii','replace')) )
                mt2u = ('Uploader:' + str(mt1['uploader'].encode('ascii','replace')) )
                mt3v = ('Views:' + str(mt1['view_count']) )
                mt4d = ('Duration:' + str(mt1['duration']) )
                mt5ud = ('Upload Date:' + str(mt1['upload_date']) )
                mt6f = ('Format:' + str(mt1['format']))
                app.queueFunction(app.addListItems, 'lb2', [ mt1t, mt2u, mt3v,mt4d,mt5ud,mt6f] )
        if optb == None:
            optb = 'Video'
        app.thread(getinfo)
        app.addListItem('l5','Download Started as' + ' ' + optb + '...')

        def startDownload():
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
                mtt= mt['title'].encode('ascii','replace')
                app.clearEntry('e1')
                app.addListItem('lb1',(str(mtt) + '-  ////   -'+ str(optb) + ' ' + '-- OK'))
        app.thread(startDownload)


app.addEntry('e1',0,0)
app.setEntryDefault('e1','URL')
app.addButton('Download',press,0,1)
app.setButtonSticky('Download','news')
app.setButtonFg('Download','green')
app.addLabel('l2','Downloaded Items',1,0)
app.setLabelFg('l2','green')
app.setEntrySticky('e1','news')
app.addListBox('lb1','',2,0)
app.addListBox('lb2','',2,1)
app.addLabel('l3','Datas',1,1)
app.setLabelFg('l3','green')
app.addLabelOptionBox('Format',['-Video-','best','-Audio-','bestaudio'],3,0)
app.addLabel('l4','Logger',4,0)
app.addLabel('l5b','',4,1)
app.setLabelBg('l5b','green')
app.setLabelBg('l4','green')
app.addListBox('l5','',5,0,2,2)
app.setListBoxSticky('l5','news')
app.thread(MyLogger)
app.go()




