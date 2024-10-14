
from PIL import Image
global loopon
global dontplay
queue = []
chq=0
dontplay=False
loopon=False
playtype=''
URL = ''
def add_todo(entities):
    
    try:
        entity1 = entities[0]
    except:
        return "I didn't quite understand what you said"
    type1 = entity1['type']
    ent1 = entity1['entity']
    type2 = ''
    try:
        entity2 = entities[1]
        type2 = entity2['type']
        ent2 = entity2['entity']
    except:
        pass
    import os
    import platformdirs
    todofile=os.path.join(platformdirs.user_config_dir('Maya'), 'tododict.json')
    if os.path.isfile(todofile):
        #with open('tododict.json') as f:
            #todofile = f.read()
        #tododict = todofile
        todofile = open(todofile)
    else:
        #tododict = {"date":[], "thing":[]}
        
        todofile = open(todofile)
        todofile.write('')
        # todofile.write(json.dumps(tododict))
    from utils import finddate, specifydate
    import date
    import timedelta
    import json
    if type1 == "sys_time":
        ent1 = finddate(ent1)
        now = date.today()
        #(now+((ent2 - now) + timedelta(7)))
        if ent1 > (now+timedelta(7)):
            print('hi')
            return "Do you mean one, {date}, or, two, {date1}".format(date = ent1, date1 = ent1 - timedelta(7))
        #tododict["date"].append(ent1)
        todofile.write(json.dumps(ent1, indent=4, sort_keys=True, default=str)+' ')
        if type2 == "thing":
            #tododict["thing"].append(ent2)
            if 'my' in ent2:
                ent2 = ent2.replace('my', 'your')
            todofile.write(json.dumps(ent2, indent=4, sort_keys=True, default=str)+'\n')
            todofile.close()
            return "I just added that on, {date}, you have, {thing}".format(thing = ent2, date = ent1)
        else:
            #i = speech_recognizer.recognize_once_async().get()
            i = input()
            i = i.lower()
            if 'i' in i:
                i = i.replace('i', 'you')
            if 'my' in i:
                i = i.replace('my', 'your')
            todofile.write(json.dumps(i, indent=4, sort_keys=True, default=str)+'\n')
            todofile.close()
            return "I didn't quite understand,, could you say what you needed to do on, {date} again please".format(date = ent1)
    elif type2 == "sys_time":
        ent2 = finddate(ent2)
        print(ent2)
        print(ent2 - timedelta(7))
        now = date.today()
        #(now+((ent2 - now) + timedelta(7)))
        if ent2 > (now+timedelta(7)):
            print('hi')
            return "Do you mean one, {date1}, or, two, {date}".format(date = ent2, date1 = ent2 - timedelta(7))
            specifydate(ent2)
        #tododict["date"].append(ent2)
        #todofile = open("tododict.json", "w")
        #todofile.write(json.dumps(tododict, indent=4, sort_keys=True, default=str))
        #todofile.close()
        todofile.write(json.dumps(ent2, indent=4, sort_keys=True, default=str)+' ')
        if type1 == "thing":
            print('done')
            if 'i' in ent1:
                ent1 = ent1.replace('i', 'you')
            if 'my' in ent1:
                ent1 = ent1.replace('my', 'your')
            todofile.write(json.dumps(ent1, indent=4, sort_keys=True, default=str)+'\n')
            todofile.close()
            return "I just added that on, {date}, you have, {thing}".format(thing = ent1, date = ent2)
            #tododict["thing"].append(ent1)
            todofile.close()
        else:
            
            #i = speech_recognizer.recognize_once_async().get()
            i = input()
            i = i.lower()
            if 'i' in i:
                i = i.lower.replace('i', 'you')
            if 'my' in i:
                i = i.replace('my', 'your')
            todofile.write(json.dumps(i, indent=4, sort_keys=True, default=str)+'\n')
            todofile.close()
            return "I didn't quite understand, could you say what you needed to do on, {date} again please".format(date = ent2)
    elif type1 == "thing":
        #tododict["thing"].append(ent1)
        if 'i' in ent1:
                ent1 = ent1.replace('i', 'you')
        if 'my' in ent1:
            ent1 = ent1.replace('my', 'your')
        ent2 = date.today()
        todofile.write(json.dumps(ent2, indent=4, sort_keys=True, default=str)+' ')
        todofile.write(json.dumps(ent1, indent=4, sort_keys=True, default=str)+'\n')
        #tododict["date"].append(ent1)
        todofile.close()
        return "I just added that on, {date}, you have, {thing}".format(thing = ent1, date = ent2)
    elif type2 == "thing":
        #tododict["thing"].append(ent2)
        if 'i' in ent2:
                ent2 = ent2.replace('i', 'you')
        if 'my' in ent2:
            ent2 = ent2.replace('my', 'your')
        ent1 = date.today()
        todofile.write(json.dumps(ent1, indent=4, sort_keys=True, default=str)+' ')
        todofile.write(json.dumps(ent2, indent=4, sort_keys=True, default=str)+'\n')
        #tododict["date"].append(ent1)
        return "I just added that on, {date}, you have, {thing}".format(thing = ent2, date = ent1)
        todofile.close()

def chan_alarm(entities):
    print('hi')

def context_based_ques():
    print('hi')
    #startwindow if its not open
    synthesizer.speak_text_async("Please input context or a correct file path to an image with textual context")
    ctx = (input("Context or file path: ")).lower()
    print(ctx)
    entities = '()'
    print(entities)
    if str(entities) == '()':
        ctx = ctx
    else:
        ctx = ''
        for i in entities:
            entity1 = i
            ent1s = str(entity1).split('\'')
            type1 = ent1s[0].strip()
            ent1 = ent1s[1]
            if type1 == 'img_path':
                if ent1.endswith('.pdf'):
                    from pdf2image import convert_from_path
                    images = convert_from_path(str(ent1), poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
                    for i in range(len(images)):
                        path = ent1.replace('.pdf', '')
                        images[i].save(path+ str(i) +'.jpg', 'JPEG')
                        ent1 = path+str(i)+'.jpg'
                        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
                        pytesseract.tesseract_cmd = path_to_tesseract
                        img = Image.open(ent1)
                        ctx += pytesseract.image_to_string(img)
                else:
                    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
                    pytesseract.tesseract_cmd = path_to_tesseract
                    img = Image.open(ent1)
                    ctx += pytesseract.image_to_string(img)
                print(ctx)
            else:
                synthesizer.speak_text_async("Not a valid input,, returning")
        ctx = ctx.replace('  ', '')
    model_name = "deepset/roberta-base-squad2"
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    # a) Get predictions
    contextnlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
    synthesizer.speak_text_async("I have the context you have gave me,, now you can ask me any question regarding it")

    while True:
        ques = (input("Question: ")).lower()
        if ques == 'exit':
            break
        elif ques == 'quit':
            break
        else:
            QA_input = {
            'question': ques,
            'context': ctx}
            #model = AutoModelForQuestionAnswering.from_pretrained(model_name)
            #tokenizer = AutoTokenizer.from_pretrained(model_name)
            res = contextnlp(QA_input)
            print(res['answer']+' Score:'+str(round(res['score'], 2)))
    return

def context_based_sum():
    print('hi')
    print('hi')
    #startwindow if its not open
    synthesizer.speak_text_async("Please input context or a correct file path to an image with textual context")
    ctx = (input("Context or file path: ")).lower()
    print(ctx)
    entities = '()'
    print(entities)
    if str(entities) == '()':
        ctx = ctx
    else:
        ctx = ''
        for i in entities:
            entity1 = i
            ent1s = str(entity1).split('\'')
            type1 = ent1s[0].strip()
            ent1 = ent1s[1]
            if type1 == 'img_path':
                if ent1.endswith('.pdf'):
                    from pdf2image import convert_from_path
                    images = convert_from_path(str(ent1), poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
                    for i in range(len(images)):
                        path = ent1.replace('.pdf', '')
                        images[i].save(path+ str(i) +'.jpg', 'JPEG')
                        ent1 = path+str(i)+'.jpg'
                        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
                        pytesseract.tesseract_cmd = path_to_tesseract
                        img = Image.open(ent1)
                        ctx += pytesseract.image_to_string(img)
                else:
                    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
                    pytesseract.tesseract_cmd = path_to_tesseract
                    img = Image.open(ent1)
                    ctx += pytesseract.image_to_string(img)
                print(ctx)
            else:
                synthesizer.speak_text_async("Not a valid input,, returning")
        ctx = ctx.replace('  ', '')
    model_name = "facebook/bart-large-cnn"
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # a) Get predictions
    summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
    summary = summarizer(ctx, max_length=350, min_length=20, do_sample=False)
    print(summary[0]['summary_text'])
    synthesizer.speak_text_async("Here is the summary i have created")

    return

def loop_off():
    global loopon
    if loopon:
        loopon=False
    else:
        return "There is no loop active"

def loop_on():
    import time
    import vlc
    global loopon
    global player
    global queue
    time.sleep(5)
    def mainloop():
        global loopon
        global URL
        global player
        while True:
            print(loopon)
            print(int(player.is_playing()))
            print(dontplay)
            if loopon and int(player.is_playing())==0 and dontplay== False:
                time.sleep(1)
                if int(player.is_playing())==0:
                    print('here`1')
                    player = vlc.MediaPlayer(URL)
                    player.audio_set_volume(50)
                    player.play()
                    time.sleep(5)
                    continue
                else:
                    return
            else:
                if not loopon:
                    break
    try:
        if loopon:
            return
        else:
            if int(player.is_playing())==1:
                import threading
                loopon=True
                threading.Thread(target=mainloop, args=()).start()   
            else:
                return
    except:
        pass
def pause_audio():
    global player
    global playtype
    global dontplay
    print('hi')
    try:
        if playtype=='radio':
            if dontplay:
                dontplay = False
                rep_audio()
            else:
                dontplay = True
                player.stop()
        else:
            player.pause()
            if dontplay:
                dontplay=False
            else:
                dontplay = True
            print('dontplaydown')
            print(dontplay)
    except:
        return "There is no audio playing"

def play_audio(entities, h):
    global title
    global URL
    print(entities)
    #entity=entities[1]
    try:
        entities=entities[1]
    except:
        pass
    from yt_dlp import YoutubeDL
    #type = entity['type']
    #ent1 = entity['entity']
    YDL_OPTIONS = {'format': 'bestaudio/best', 'default_search': 'auto', 'forceipv4': 'True', 'ignoreerrors': 'True', 'flatplaylist': 'True'}
    '''try:
        print(type)
        if type == 'url':
            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(ent1, download=False)
            try:
                URL = info['url']
            except:
                URL = info['formats'][0]['url']
            title = info['title']
        elif type == 'title':
            ent1 = ent1.replace(' ', '')
            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(ent1, download=False)
            entries = info['entries']
            try:
                entries = (entries)[0]
            except:
                return "I didnt find a video for that"
            title = entries['title']
            try:
                format= entries['formats'][0]
                URL = format['url']
            
            except:
                format= entries['formats'][1]
                URL = format['url']
            entities=[]
                
            urltitle={'type':title,
                    'entity':URL
            }
            entities.append(urltitle)
    except:
        return
    '''
    global player
    global queue
    global chq
    global dontplay
    global loopon
    global playtype
    import time
    if playtype=='radio':
        stop_audio()
    def checkqueue(queue, chq):
        time.sleep(3)
        while True:
            if int(player.is_playing())==0 and dontplay==False and loopon==False:
                time.sleep(1)
                if int(player.is_playing())==0 and len(queue) > 0:
                    print('here`1')
                    entities = queue.pop(0)
                    print('chqdown1')
                    print(chq)
                    print(entities)
                    print(queue)
                    if entities != '[]':
                        '''try:
                            h = 0
                            entities = queue.pop(0)
                            play_audio(entities, h)
                            break
                        except:
                            pass'''
                        if len(queue) > 0:
                            print('heressss')
                            h =1
                            play_audio(entities, h)
                            break
                        else:
                            h = 0
                            play_audio(entities, h)
                            chq=0
                            break
                    else:
                        break
            else:
                continue
        try:
            try:
                entities=entities[1]
            except:
                pass
            print('hellooooooo')
            title = entities['type'] 
            return title
        except:
            pass
    try:
        if int(player.is_playing())==1 or dontplay==1:
            queue.append(entities)
            print(queue)
            print('yeassss')
            if chq == 0:

                import threading
                threading.Thread(target=checkqueue, args=(queue, chq)).start()
                chq = 1
                return
            else:
                return
    except:
        pass
    print('hihere')
    #try:
    print(entities)
    URL = entities['entity']
    #except:
        #return "I didn't quite understand what you said"
    title = entities['type']
    print(title)
    global instance
    import vlc
    instance = vlc.Instance("--no-video")
    ########
    #######
    player = instance.media_player_new(URL)
    player.audio_set_volume(70)
    player.play()
    playtype = 'nonradio'
    if h == 1:
            print('hjereicmni')
            import threading
            threading.Thread(target=checkqueue, args=(queue, chq)).start()
            chq = 1
    del entities
    #queue doesnt send return to main
    return "Now playing, {title}".format(title=title)
    return

def play_radio(entities):
    global playtype
    global player
    global URL
    import vlc
    print('hi')
    try:
        if int(player.is_playing())==1:
            global loopon
            loopon=False
            global queue
            queue=[]
            player.stop()
            print('hi')
    except:
        print('hi')
    try:
        entity1 = entities[0]
    except:
        return "I didn't quite understand what you said"
        return
    type1 = entity1['type']
    ent1 = entity1['entity']
    print(type1)
    global instance
    instance = vlc.Instance("--no-video")
    if 'pop' in ent1:
        pop_radio='https://stream.revma.ihrhls.com/zc185/hls.m3u8'
        type='Pop Radio'
        URL = pop_radio
    elif 'rock' in ent1:
        rock_radio='https://stream.revma.ihrhls.com/zc5523/hls.m3u8'
        type='Rock Radio'
        URL = rock_radio
    elif 'oldies' in ent1 or '90' in ent1 or '80' in ent1 or '70' in ent1 or 'classics' in ent1:
        oldies_radio='https://stream.revma.ihrhls.com/zc4455/hls.m3u8'
        type='Oldies Radio'
        URL = oldies_radio
    elif 'jazz' in ent1 or 'jazzy' in ent1:
        jazz_radio='https://stream.revma.ihrhls.com/zc4242/hls.m3u8'
        type='Jazz Radio'
        URL = jazz_radio
    elif 'hiphop' in ent1 or 'rap' in ent1 or 'r and b' in ent1 or 'r & b' in ent1 or 'hip hop' in ent1:
        hiphop_radio='https://stream.revma.ihrhls.com/zc4429/hls.m3u8'
        type='HipHop Radio'
        URL = hiphop_radio
    elif 'dance' in ent1 or 'edm' in ent1 or 'electronic dance music' in ent1:
        dance_radio='https://stream.revma.ihrhls.com/zc5953/hls.m3u8'
        type='Dance Radio'
        URL = dance_radio
    elif 'country' in ent1:
        country_radio='https://stream.revma.ihrhls.com/zc2337/hls.m3u8'
        type='Country Radio'
        URL = country_radio
    elif 'classical' in ent1:
        classical_radio='https://stream.revma.ihrhls.com/zc6377/hls.m3u8'
        type='Classical Radio'
        URL = classical_radio
    elif 'christmas' in ent1:
        christmas_radio='https://stream.revma.ihrhls.com/zc4596/hls.m3u8'
        type='Christmas Radio'
        URL = christmas_radio
    elif 'christian' in ent1 or 'relig' in ent1:
        christian_radio='https://stream.revma.ihrhls.com/zc7203/hls.m3u8'
        type='Christian Radio'
        URL = christian_radio
    elif 'alternative' in ent1:
        alt_radio='https://stream.revma.ihrhls.com/zc201/hls.m3u8'
        type='Alternative Radio'
        URL = alt_radio
    player = instance.media_player_new(URL)
    player.audio_set_volume(50)
    player.play()
    playtype = 'radio'
    try:
        print(type)
    except:
        pass
    return "Now playing, {type}".format(type=type)

def rem_alarm(entities):
    print('hi')

def rem_todo(entities):
    ent1 =''
    from utils import finddate
    import os
    try:
        entity1 = entities[0]
        ent1 = entity1['entity']
        type1 = entity1['type']
    except:
        pass
    ent1 = finddate(ent1)
    if os.path.isfile('tododict.json'):
        todofile = open("tododict.json", "r")
    else:
        return "You have not scheduled anything at all"
        return
    ent1 = str(ent1)
    print(ent1)
    flag = 0
    with open('tododict.json', 'r') as fr:
        # reading line by line
        lines = fr.readlines()
         
        # pointer for position
        ptr = 1
     
        # opening in writing mode
        with open('tododict.json', 'w') as fw:
            for line in lines:
                if ent1 not in line:
                    fw.write(line)
                if ent1 in line:
                    flag = 1
            
    if flag == 0:
        return "On, {date} your schedule was already free".format(date = ent1)
    else:
        return "Your schedule for, {date}, is now free".format(date = ent1)
    todofile.close()

def rep_audio():
    print('hi')
    import vlc
    global player
    global URL
    player.stop()
    player = vlc.MediaPlayer(URL)
    player.audio_set_volume(50)
    player.play()


def req_alarm(entities):
    print('hi')

def req_audio():
    print('hi')
    global title
    global playtype
    global player
    global URL
    try:
        if int(player.is_playing())==0:
            return "Nothing is currently playing"
            return
        elif playtype=='nonradio':
            return "{title} is currently playing".format(title=title)
            return
        elif playtype=='radio':
            import requests
            r = requests.get(URL)
            print(r)
            r = str(r.text)
            r = r.split('\n')
            url = ''
            for line in r:
                if  '.m3u8' in line:
                    url = line
                    break
            print(url)
            r = requests.get(url)
            title = re.search('le=\"(.*)\",a', r.text).group(1)
            print(title)
            artist = re.search('st=\"(.*)\",', r.text).group(1)
            print(artist)
            return "{title} by {artist} is currently playing".format(title=title, artist=artist)
        else:
            return "Nothing is currently playing"
            return
    except:
        return
    

def req_todo(entities):  
    from utils import finddate
    import os
    ent1=''
    try:
        entity1 = entities[0]
        type1 = entity1['type']
        ent1 = entity1['entity']
    except:
        pass
    ent1 = finddate(ent1)
    print(ent1)
    if os.path.isfile('tododict.json'):
        todofile = open("tododict.json", "r")
    else:
        return "You have not scheduled anything at all"
        return
    #todaydate = time.strftime('%Y-%m-%d')
    print(ent1)
    ent1 = str(ent1)
    flag = 0
    #try:
    ent2 = ''
    for line in todofile:
        if ent1 in line:
            line = line.split('" "')
            flag = 1
            try:
                ent2 = ent2+line[1].replace('"','')
                ent2 = ent2.replace('\n','')
                ent2 = ent2+', '
                print(ent2)
            except:
                return "On, {date} your schedule is free".format(date = ent1)
    if flag == 0:
        return "On, {date} your schedule is free".format(date = ent1)
    else:
        return "On, {date} you have, {thing}".format(thing = ent2, date = ent1)
    #except:
        #synthesizer.speak_text_async("Sorry, something went wrong")
    todofile.close()

def res_audio():
    try:
        global dontplay
        print(dontplay)
        if dontplay:
            dontplay=False
            player.pause()
        else:
            pass
    except:
        return "There is no audio playing"

def reset_timer(entities):
    print('hi')

def set_alarm(entities):
    print('hi')

def skip_audio():
    global loopon
    loopon=False
    try:
        player.stop()
        if len(queue) > 0:
            entities = queue.pop(0)
            print('heraaaaa')
            print('chqdown1')
            print(entities)
            print(queue)
            if entities == '()':
                try:
                    h = 0
                    entities = queue.pop(0)
                    return play_audio(entities, h)
                    
                except:
                    return "There is no more audio to play"
            if len(queue) > 0:
                print('heressss')
                h =1
                return play_audio(entities, h)
                
            else:
                h = 0
                return play_audio(entities, h)
        else:
            return "There is no more audio to play"

    except:
        return "There is no audio playing"

def start_timer(entities):
    print('hi')

def stop_audio():
    global loopon
    loopon=False
    global queue
    try:
        queue=[]
        player.stop()
    except:
        return "There is no audio playing"

def stop_timer(entities):
    print('hi')