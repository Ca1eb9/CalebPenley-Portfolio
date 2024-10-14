from tkinter import *
import time
import tkinter
import pathlib
import json
from time import strftime
import threading
import os.path
import requests
import sys
from io import BytesIO
import geocoder
from PIL import Image, ImageTk
from datetime import timedelta
import time
from datetime import datetime
import azure.cognitiveservices.speech as speechsdk
from util.client_config import APP_VERSION
from sys import platform
q=True
s=''
realconfig='''[config]\n
changelog = False\n
version = {ver}\n
'''.format(ver=APP_VERSION)
serveriph='http://23.239.9.14'
serverip='23.239.9.14'
serveriph2='http://104.38.188.173'
serverip2='104.38.188.173'
def quit(icon):
    global q
    q=False
    icon.stop()
    sys.exit(0)
def show_window(icon):
    root.deiconify()
    root.deiconify()
    icon.stop()
def tray():
    from pystray import MenuItem as item
    import pystray
    try:
        image=Image.open('icon.ico')
    except:
        image=Image.open(str(pathlib.Path(__file__).parent.resolve())+'/icon.ico')
    menu=(item('Quit', quit), item('Show', show_window, default=True))
    tray=pystray.Icon("Maya", image, "Maya", menu)
    tray.run()
def newinput(query, type):
    global s
    query = query.strip()
    if '-update' in query:
        query = query.replace('-update', '')
        query = query.strip()
        if query != '':
            from util.utils import update
            update(query, status)
            return
        else:
            return
    elif '-issue' in query:
        query = query.replace('-issue', '')
        query = query.strip()
        if query != '':
            type='issue'
        else:
            return
        query = query + ' Version: ' + APP_VERSION
    elif '-dev' in query:
        query = query.replace('-dev', '')
        query = query.strip()
        if query != '':
            try:
                config.add_section('dev')
            except:
                pass
            config.set('dev', 'password', query)
            import platformdirs
            with open(platformdirs.user_config_dir('Maya')+'config.ini', 'w') as f:
                config.write(f)
            config.read(platformdirs.user_config_dir('Maya')+'config.ini')
        else:
            return
        return
    
    try:
        if '-broadcast' in query:
            query = query.replace('-broadcast', '')
            query = query.strip()
            type='broadcast'
            if config.get("dev", "password") == '1943':
                pass
            else:
                return
    except:
        return
    if type != 'broadcast':
        query = query.lower()
        query = query.replace(',', '')
        query = query.replace('\"', '')
        query = query.replace('\'', '')
        query = query.strip()
    senddict = {
        'type':type,
        'query':query
    }
    s.send((json.dumps(senddict)).encode())
    mainwindow.see('end')
def window():
    from tkinter import Button
    from tkinter import messagebox
    global root
    root = Tk()
    #root.resizable(width=FALSE, height=FALSE)
    def add_chat(disregard):
        msg = messagewindow.get()
        query = messagewindow.get()
        if msg=='':
            return
        msg = 'You: ' + msg
        messagewindow.delete(0,END)
        mainwindow.config(state='normal')
        mainwindow.insert('end', msg+'\n')
        mainwindow.config(state='disabled')
        #############
        ########
        type = 'nonaudio'
        threading.Thread(target=newinput, args=(query, type)).start()
    def close():
        if messagebox.showinfo("Close", "Maya will still run in the backround"):
                root.withdraw()
                tray()
    if platform == 'win32':
        root.iconbitmap(str(pathlib.Path(__file__).parent.resolve())+'/icon.ico')
    root.title("Maya")
    root.configure(background='black')
    root.geometry("400x500")
    root.minsize(400, 500)
    #root.wm_attributes('-transparent','#F93C39')
    #########################################
    temp=Label(root, fg='white', bg='black', font=("Arial", 9), state='disabled')
    #temp.place(x=83, y=0, height=80, width=80)
    #weathimage1=ImageTk.PhotoImage(Image.open(BytesIO(requests.get('http://openweathermap.org/img/wn/{icon}@2x.png'.format(icon='01d')).content)))
    current=''
    try:
        g = geocoder.ip('me').latlng
        lat=g[0]
        lon=g[1]
        key='5577d675a4db94ad5d593b15c918f676'
        url='https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=imperial&appid={API}'.format(lat=lat, lon=lon, API=key)
        weather_info = requests.get(url).json()
        current=weather_info['current']
        weathpic1=current['weather'][0]['icon']
        weathimage1=ImageTk.PhotoImage(Image.open(BytesIO(requests.get('http://openweathermap.org/img/wn/{icon}@2x.png'.format(icon=weathpic1)).content)))
        weathimage=Label(root, image=weathimage1, bg='black')
        weathimage.place(x=6, y=0, height=80, width=80)
    except:
        pass
    ver=Label(root, text='Maya Version: {ver}'.format(ver=APP_VERSION), fg='gray', bg='black',font=("Arial", 8))
    ver.place(x=6, y=439, height=12, width=100)
    global status
    status=Label(root, text='Disconnected', fg='#ff0000', bg='black',font=("Arial", 10))
    status.place(x=200, y=439, height=12, width=100)
    clockt=Label(root, text=strftime('%I:%M %p'), fg='#0000FF', bg='black',font=("Arial", 12))
    clockt.place(x=175, y=0)
    #red: #ff0000
    #green #00f05c
    ################################################
    global mainwindow
    mainwindow = Text(root, bd=1, bg="#36393f",  width="50", height="8", font=("Arial", 14), foreground="light gray", state="disabled")
    mainwindow.place(x=6,y=80, height=360, width=370)
    global messagewindow
    messagewindow = Entry(root, bd=1, bg="#36393f",width="32", font=("Arial", 17), foreground="light gray", state='readonly')
    messagewindow.place(x=116, y=450, height=44, width=260)
    messagewindow.bind('<Return>', add_chat)
    global statusmsg
    statusmsg=Label(root, text='Test', fg='white', bg='#F93C39',font=("Arial", 10), state=DISABLED)
    #statusmsg.place(x=6, y=82, height=25, width=370)
    scrollbar = Scrollbar(root, command=mainwindow.yview)
    mainwindow["yscrollcommand"] = scrollbar.set
    scrollbar.place(x=377,y=5.5, height=440, width=14)
    button = Button(root, text="Send",  width=10, height=3, bd=1, bg="#0080ff", activebackground="#00bfff",foreground='#ffffff',font=("Arial", 12), cursor="hand2")
    button.pack()
    button.place(x=6, y=450, height=44, width=88)
    button.bind("<Button-1>", add_chat)
    root.protocol("WM_DELETE_WINDOW", close)
    def weath(current):
            g = geocoder.ip('me').latlng
            try:
                lat=g[0]
                lon=g[1]
            except:
                return
            key='5577d675a4db94ad5d593b15c918f676'
            url='https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=imperial&appid={API}'.format(lat=lat, lon=lon, API=key)
            if current=='':
                weather_info = requests.get(url).json()
                current=weather_info['current']
            else:
                vis=current['visibility']
                sr=current['sunrise']
                sr = datetime.fromtimestamp(sr).strftime('%I:%M %p')
                ss=current['sunset']
                ss = datetime.fromtimestamp(ss).strftime('%I:%M %p')
                tempe=current['temp']
                like=current['feels_like']
                pres=current['pressure']
                pres=round(int(pres)*0.02953,2)
                hum=current['humidity']
                uv=current['uvi']
                weathpic1=current['weather'][0]['icon']
                if uv <=2:
                    uv='low'
                elif 2<uv<=5:
                    uv='moderate'
                elif 5<uv<=7:
                    uv='high'
                elif 7<uv<=10:
                    uv='very high'
                elif 10<uv:
                    uv='extreme'
                cloud=current['clouds']
                ws=current['wind_speed']
                wd=current['wind_deg']
                hilo=requests.get('https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={APIkey}'.format(lat=lat, lon=lon, APIkey=key)).json()
                hi=hilo['main']['temp_max']
                lo=hilo['main']['temp_min']
                temp.config(text='{temp}\n{like}\n{wind}'.format(temp=str(tempe)+'F', like='Like '+str(like)+'F', wind=str(ws)+'MPH'))
                current=''
                root.after(300000, weath, current)
    def clock():
        if not clockt['text']==strftime('%I:%M %p'):
            clockt.config(text = strftime('%I:%M %p'))
        root.after(1000, clock)
    def updatewindow():
        if not mainwindow.winfo_height()==0.72*root.winfo_height() or not mainwindow.winfo_width()==0.925*root.winfo_width():
            mainwindow.place(x=0.015*root.winfo_width(),y=0.16*root.winfo_height(), height=0.72*root.winfo_height(), width=0.925*root.winfo_width())
            try:
                if root.winfo_height()<800:
                    weathimage.place(x=0.015*root.winfo_width(), y=5, height=80, width=80)
                else:  
                    weathimage.place(x=0.015*root.winfo_width(), y=(0.16*root.winfo_height())/2, height=80, width=80)
            except:
                pass
            if statusmsg['state'] != DISABLED:
                statusmsg.place(x=0.015*root.winfo_width(), y=0.164*root.winfo_height(), height=0.05*root.winfo_height(), width=0.925*root.winfo_width())
        if root.winfo_width()>950 and temp['state']=='disabled':
            temp['font']=("Arial", str(round(0.02*root.winfo_height())))
            temp['state']='normal'
            temp.place(x=83, y=0, height=0.16*root.winfo_height(), width=0.15*root.winfo_width())
        elif root.winfo_width()<950 and temp['state']=='normal':
            temp['state']='disabled'
            temp.place_forget()
        if clockt.winfo_x()!=int((root.winfo_width()/2)-((root.winfo_width()/2)/8)):
            clockt.place(x=(root.winfo_width()/2)-((root.winfo_width()/2)/8) if root.winfo_width()<1000 else (root.winfo_width()/2), y=0)
            clockt.config(font = ("Arial", 15))
        elif str(clockt['font'])!= 'Arial 12':
            clockt.config(font = ("Arial", 12))
        if not button.winfo_height()==0.088*root.winfo_height() or not button.winfo_width()==0.22*root.winfo_width():
            button.place(x=0.015*root.winfo_width(), y=0.9*root.winfo_height(), height=0.088*root.winfo_height(), width=0.22*root.winfo_width())
        if not messagewindow.winfo_height()==0.088*root.winfo_height() or not messagewindow.winfo_width()==0.65*root.winfo_width():
            messagewindow.place(x=0.2875*root.winfo_width(), y=0.9*root.winfo_height(), height=0.088*root.winfo_height(), width=0.65*root.winfo_width())
        if not scrollbar.winfo_height()==0.88*root.winfo_height() or not scrollbar.winfo_width()==14:
            scrollbar.place(x=0.9425*root.winfo_width(),y=0.011*root.winfo_height(), height=0.88*root.winfo_height(), width=14)
        if not ver.winfo_y()+11==button.winfo_y() or not ver.winfo_x()==button.winfo_x():
            ver.place(x=button.winfo_x(), y=button.winfo_y()-11)
        if not status.winfo_y()+11==messagewindow.winfo_y() or not status.winfo_x()==0.5*root.winfo_width():
            status.place(x=0.5*root.winfo_width(), y=messagewindow.winfo_y()-16 if messagewindow.winfo_y()>450 else messagewindow.winfo_y()-11)
        if platform == "darwin" or platform.startswith('linux'):
            if q == False:
                sys.exit(0)
        root.after(10, updatewindow)
    import platformdirs
    from configparser import ConfigParser
    global config
    config = ConfigParser()
    config.read(platformdirs.user_config_dir('Maya')+'config.ini')
    try:
        if APP_VERSION != config.get("config", "version"):
            with open(platformdirs.user_config_dir('Maya')+'config.ini', 'w') as f: ######entire change log
                f.write(realconfig)
    except:
        os.makedirs(platformdirs.user_config_dir('Maya'))
        with open(platformdirs.user_config_dir('Maya')+'config.ini', 'w') as f:
            f.write(realconfig)
    config.read(platformdirs.user_config_dir('Maya')+'config.ini')
    if config.get("config", "changelog") == 'False':
        changelog = Toplevel(root)
        changelog.title("Change Log")
        changelog.geometry("400x500")
        
        if platform == 'win32':
            changelog.iconbitmap(str(pathlib.Path(__file__).parent.resolve())+'/icon.ico')
        class res:
            ok = True
        try:
            try:
                res = requests.get(serveriph + ':5375/changelog', timeout=3)
            except:
                res = res = requests.get(serveriph2 + ':5375/changelog', timeout=3)
        except:
            setattr(res, 'ok', False)
            pass
        realchnglog='Error getting the changelog'
        if res.ok:
            realchnglog = res.text
            if realchnglog != 'The changelog could not be retrieved on our end':
                config.set("config", "changelog", "True")
                with open(platformdirs.user_config_dir('Maya')+'config.ini', 'w') as f:
                    config.write(f)
                config.read(platformdirs.user_config_dir('Maya')+'config.ini')
        else:
            pass
        label = Label(changelog, text=realchnglog, fg='gray')
        label.pack()
    root.after(300, updatewindow)
    clock()
    weath(current)
    root.mainloop()
def main():
    ####
    #####
    while q:
        try:
            requests.get('https://www.google.com', timeout=5)
        except (requests.ConnectionError, requests.Timeout) as exception:
            print('errorconnect')
            continue
        break
    import socket
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    while q:
        try:
            try:
                requests.get(serveriph + ':5375/fileserver-is-ready', timeout=3)
            except:
                requests.get(serveriph2 + ':5375/fileserver-is-ready', timeout=3)
            status.config(fg='#00f05c', text='Connecting . . .')
            while q:
                try:
                    try:
                        s.connect((serverip, 5250))
                    except:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((serverip2, 5250))
                except:
                    continue
                while True:
                    try:
                        time.sleep(3)
                        status.config(fg='#00f05c', text='Connected')
                        global messagewindow
                        messagewindow.config(state='normal')
                    except:
                        continue
                    break
                break
            break
        except:
            pass
    

    from util.utils import update
    update('stable', status)
    speech_config = speechsdk.SpeechConfig(subscription="5143e3c9837648d6a59de18853ae25aa", region="eastus")
    speech_config.speech_synthesis_voice_name ="en-US-SaraNeural"
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)#filename="file.wav"
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    sleep= False
    while q:
        #try:
            entities = ''
            ans=''
            try:
                resdict= json.loads((s.recv(100000)).decode())
            except:
                continue
            entity={
                    'type':'',
                    'entity':''
                }
            print(resdict)
            #setup with server
            #####start
            type = resdict['type']
            if type == 'intro' or type == 'broadcast':
                statmsg = resdict['status']
                if statmsg != '':
                    global statusmsg
                    statusmsg.config(state='normal')
                    statusmsg.config(text=statmsg)
                    global root
                    statusmsg.place(x=0.015*root.winfo_width(), y=0.164*root.winfo_height(), height=0.05*root.winfo_height(), width=0.925*root.winfo_width())
                elif statusmsg['state'] != DISABLED:
                    statusmsg.place_forget()
                continue

            else:
                #try:
                    #domain = resdict['domain']
                    #domprob = float(resdict['domprob'])
                intent = resdict['intent']
                    #intprob = float(resdict['intprob'])
                entities = resdict['entities']
                query = resdict['query']
                    #urltitle = resdict['urltitle']
                #except:
                    #continue 
                if sleep == False:
                    #######nextstart
                    #non_disc_commands
                    if intent==('sleep'):
                        sleep = True
                    elif intent==('roll_dice'):
                        from non_disc_commands import roll_dice
                        ans = roll_dice(entities)
                    elif intent==('pick_number'):
                        continue
                        from non_disc_commands import pick_number
                        ans = pick_number(entities)
                    #relational_dialogue
                    elif intent==('conversation'):
                        continue
                        from relational_dialogue import conversation
                        ans = conversation(query)
                    elif intent==('dismiss'):
                        continue
                        from relational_dialogue import dismiss
                        ans = dismiss()
                    elif intent==('exit'):
                        continue
                        from relational_dialogue import fakeexit
                        ans = fakeexit()
                    elif intent==('greet'):
                        continue
                        from relational_dialogue import greet
                        ans = greet()
                    elif intent==('thanks'):
                        continue
                        from relational_dialogue import thanks
                        ans = thanks()
                    #personal_disc_commands
                    elif intent==('add_todo'):
                        from personal_disc_commands import add_todo
                        ans = add_todo(entities)
                    elif intent==('chan_alarm'):
                        continue
                        from personal_disc_commands import chan_alarm
                        ans = chan_alarm(entities)
                    elif intent==('con_ba_que'):
                        continue
                        from personal_disc_commands import context_based_ques
                        ans = context_based_ques()
                    elif intent==('con_ba_sum'):
                        continue
                        from personal_disc_commands import context_based_sum
                        ans = context_based_sum()
                    elif intent==('loop_off_audio'):
                        from personal_disc_commands import loop_off
                        ans = loop_off()
                    elif intent==('loop_on_audio'):
                        from personal_disc_commands import loop_on
                        ans = loop_on()
                    elif intent==('pause_audio'):
                        from personal_disc_commands import pause_audio
                        ans = pause_audio()
                    elif intent==('play_audio'):
                        h = 0
                        from personal_disc_commands import play_audio
                        ans = play_audio(entities, h)
                    elif intent==('play_radio'):
                        from personal_disc_commands import play_radio
                        ans = play_radio(entities)
                    elif intent==('rem_alarm'):
                        continue
                        from personal_disc_commands import rem_alarm
                        ans = rem_alarm(entities)
                    elif intent==('rem_todo'):
                        from personal_disc_commands import rem_todo
                        ans = rem_todo(entities)
                    elif intent==('rep_audio'):
                        from personal_disc_commands import rep_audio
                        ans = rep_audio()
                    elif intent==('req_alarm'):
                        continue
                        from personal_disc_commands import req_alarm
                        ans = req_alarm(entities)
                    elif intent==('req_audio'):
                        from personal_disc_commands import req_audio
                        ans = req_audio()
                    elif intent==('req_todo'):
                        from personal_disc_commands import req_todo
                        ans = req_todo(entities)
                    elif intent==('res_audio'):
                        from personal_disc_commands import res_audio
                        ans = res_audio()
                    elif intent==('reset_timer'):
                        continue
                        from personal_disc_commands import reset_timer
                        ans = reset_timer(entities)
                    elif intent==('set_alarm'):
                        continue
                        from personal_disc_commands import set_alarm
                        ans = set_alarm(entities)
                    elif intent==('skip_audio'):
                        from personal_disc_commands import skip_audio
                        ans = skip_audio()
                    elif intent==('start_timer'):
                        continue
                        from personal_disc_commands import start_timer
                        ans = start_timer(entities)
                    elif intent==('stop_audio'):
                        from personal_disc_commands import stop_audio
                        ans = stop_audio()
                    elif intent==('stop_timer'):
                        continue
                        from personal_disc_commands import stop_timer
                        ans = stop_timer(entities)
                    #discovery
                    elif intent==('date'):
                        continue
                        from discovery import todaydate
                        ans = todaydate()
                    elif intent==('day'):
                        continue
                        from discovery import todayday
                        ans = todayday(entities)
                    elif intent==('weather'):
                        from discovery import weather
                        ans = weather(entities)
                    elif intent==('last_name'):
                        from discovery import last_name
                        ans = last_name()
                    elif intent==('middle_name'):
                        from discovery import middle_name
                        ans = middle_name()
                    elif intent==('month'):
                        continue
                        from discovery import todaymonth
                        ans = todaymonth()
                    elif intent==('name'):
                        from discovery import name
                        ans = name()
                    elif intent==('time'):
                        continue
                        from discovery import todaytime
                        ans = todaytime()
                    elif intent==('web_query'):
                        continue
                        from discovery import web_query
                        ans = web_query(query)
                    elif intent==('what_i_can_do'):
                        continue
                        from discovery import what_i_can_do
                        ans = what_i_can_do()
                    elif intent==('who_built'):
                        from discovery import who_built
                        ans = who_built()
                    elif intent==('wolf_query'):
                        continue
                        from discovery import wolf_query
                        ans = wolf_query(query)
                    elif intent==('year'):
                        continue
                        from discovery import todayyear
                        ans = todayyear()
                    #followup
                else:                    
                    if intent==('wake'):
                        sleep = False
                print(ans)
                if ans:
                    if type == 'nonaudio':
                        mainwindow.config(state='normal')
                        reply = 'Maya: '+str(ans)
                        mainwindow.insert('end', reply+'\n')
                        mainwindow.config(state='disabled')
                        mainwindow.see('end')
                    else:
                        try:
                            synthesizer.speak_text_async(ans)
                        except:
                            pass




        #except:
            #continue
    s.close()
    sys.exit(0)       
def voicedetect():
    speech_config = speechsdk.SpeechConfig(subscription="5143e3c9837648d6a59de18853ae25aa", region="eastus")
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    path = pathlib.Path(__file__).parent.resolve()
    try:
        model = speechsdk.KeywordRecognitionModel(str(path)+"\mayadetect.table")
    except:
        model = speechsdk.KeywordRecognitionModel(str(path)+"/mayadetect.table")
    keyword_recognizer = speechsdk.KeywordRecognizer()
    while True: 
        #try:
            result_future = keyword_recognizer.recognize_once_async(model)
            result = result_future.get()
            if result.reason == speechsdk.ResultReason.RecognizedKeyword:
                #try:
                    query = speech_recognizer.recognize_once_async().get()
                    query = str(query.text)
                    type = 'audio'
                    if query == '':
                        continue
                    threading.Thread(target=newinput, args=(query, type)).start()
                #except:
                    #pass
            continue
        #except:
            #print('error')
            #continue

if __name__ == '__main__':
    threading.Thread(target=voicedetect, daemon=True).start()
    if platform.startswith('linux'):
        try:
            threading.Thread(target=window, daemon=True).start()
            main()
        except:
            threading.Thread(target=main, daemon=True).start()
            window()
    elif platform == "darwin":
        #mac os
        threading.Thread(target=main, daemon=True).start()
        window()
    else:
        #windows
        threading.Thread(target=window, daemon=True).start()
        main()