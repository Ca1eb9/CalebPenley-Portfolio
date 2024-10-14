import socket
import threading
import sys
import json
import logging
import requests
import os
import time
from mindmeld.components.nlp import NaturalLanguageProcessor
nlp = NaturalLanguageProcessor(app_path='myapp')
dc = nlp.domain_classifier
nlp.load()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 5250
ip='IP'
try:
    s.bind((ip, port))
except:
    ip = 'IP'
    s.bind((ip, port))
s.listen(100)
clientlist = []
global introdict
introdict = {
    'type': 'intro',
    'status': '',
}
senddict = {
    'type':'',
    'domain':'',
    'domprob':'',
    'intent':'',
    'intprob':'',
    'entities':'',
    'query':''
}
def clientrec(c):
    ###intro
    introdict = {
    'type': 'intro',
    'status': '',
    }
    with open('broadcast.txt', 'r') as f:
        try:
            status = f.read()
        except:
            status = ''
        introdict['status'] = status
    c.send((json.dumps(introdict)).encode())
    while True:
                senddict = {
                    'type':'',
                    'domain':'',
                    'domprob':'',
                    'intent':'',
                    'intprob':'',
                    'entities':'',
                    'query':''
                }
        #try:
                recvdict= json.loads((c.recv(100000)).decode())
            #try:   
                print(recvdict)
                if recvdict:
                    #########start
                    if recvdict['type'] == 'issue':
                        with open(recvdict['query'][0:8]+'.txt', 'w') as f:
                            f.write(recvdict['query'])
                        continue
                    elif recvdict['type'] == 'broadcast':
                        msg = recvdict['query']
                        broadcast(msg)
                        continue
                    senddict['type'] = recvdict['type']
                    query = recvdict['query']
                    domain = dc.predict(query)
                    senddict['domprob'] = str(dc.predict_proba(query)[0][1])
                    ic = nlp.domains[domain].intent_classifier
                    intent = ic.predict(query)
                    senddict['intprob'] = str(ic.predict_proba(query)[0][1])
                    er = nlp.domains[domain].intents[intent].entity_recognizer
                    entities = er.predict(query)
                    senddict['domain'] = domain
                    senddict['intent'] = intent
                    senddict['entities'] = []
                    list = []
                    senddict['query'] = query
                    entity={
                            'type':'',
                            'entity':''
                        }
                    for i in entities:
                        entity['type']=(str(i).split('\'')[0].strip())
                        entity['entity']=(str(i).split('\'')[1])
                        senddict['entities'].append(entity)
                        entity={
                            'type':'',
                            'entity':''
                        }
                    if intent == 'play_audio':
                        try:
                            entity = senddict['entities'][0]
                        except:
                            continue
                        from yt_dlp import YoutubeDL
                        type = entity['type']
                        ent1 = entity['entity']
                        YDL_OPTIONS = {'format': 'bestaudio/best', 'noplaylist': 'True', 'novideo': 'True', 'default_search': 'auto'}
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
                            #print(info)
                            try:
                                entries = (entries)[0]
                            except:
                                return "I didnt find a video for that"
                                return
                            title = entries['title']
                            #try:
                            for i in range(len(entries['formats'])):
                                    print(entries['formats'][i])
                                    if 'manifest_url' in entries['formats'][i]:
                                        format = entries['formats'][i]
                                        break
                                #format= entries['formats'][3]
                                
                            URL = format['url']
            
                            #except:
                            #format= entries['formats'][3]
                            #URL = format['url']
                        entities=[]
                        urltitle={
                            'type':title,
                            'entity':URL
                            }
                        senddict['entities'].append(urltitle)

                    c.send((json.dumps(senddict)).encode())
                else:
                    """message may have no content if the connection
                    is broken, in this case we remove the connection"""
                    remove(c)
            #except:
                #continue
        #except:
            #remove(c)
            #break
def broadcast(msg):
    msgdict = {
        'type':'broadcast',
        'status':msg
    }
    with open('broadcast.txt', 'w') as f:
        f.write(msg)
    introdict['status'] = msg
    for client in clientlist:
        try: 
            client.send((json.dumps(msgdict)).encode())
        except:
            remove(client)
def remove(c):
    if c in clientlist:
        c.close()
        print(str(c)+' removed')
        clientlist.remove(c)
def main():
    with open('broadcast.txt', 'w') as f:
        f.write('')
    while True:
        c, addr = s.accept()
        clientlist.append(c)  
        print (addr[0] + " connected")
        threading.Thread(target=clientrec, args=(c,), daemon=True).start()
    c.close()
    s.close()
def updatesr():
    from flask import Flask, request, send_from_directory
    from werkzeug.utils import secure_filename
    import pathlib
    UPLOAD_FOLDER = str(pathlib.Path(__file__).parent.resolve())+'/deploy'
    LOCALHOST = ip
    logger = logging.getLogger(__name__)
    def RunFileServer(fileServerDir, fileServerPort):
        """
        Run a Flask file server on the given port.
        Explicitly specify instance_path, because Flask's
        auto_find_instance_path can fail when run in a frozen app.
        """
        app = Flask(__name__, instance_path=fileServerDir)
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
        @app.route('/fileserver-is-ready', methods=['GET'])
        def FileserverIsReady():  # pylint: disable=unused-variable
            """
            Used to test if file server has started.
            """
            return 'Fileserver is ready!'

        @app.route('/<path:filename>', methods=['GET'])
        def ServeFile(filename):  # pylint: disable=unused-variable
            """
            Serves up a file from PYUPDATER_FILESERVER_DIR.
            """
            return send_from_directory(fileServerDir, filename.strip('/'))

        def ShutDownServer():
            """
            Shut down the file server.
            """
            func = request.environ.get('werkzeug.server.shutdown')
            if func is None:
                raise RuntimeError('Not running with the Werkzeug Server')
            func()

        @app.route('/shutdown', methods=['POST'])
        def ShutDown():  # pylint: disable=unused-variable
            """
            Respond to a POSTed request to shut down the file server.
            """
            ShutDownServer()
            return 'Server shutting down...'
        @app.route('/send', methods=['POST'])
        def BeServedFile():
            if request.method == 'POST':
                try:
                    file = request.files['file']
                except:
                    return 'not a valid {file : }'
                if file:
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    return filename + ' has been uploaded succesfully to the Maya server'
        @app.route('/changelog', methods=['GET'])
        def ServeChnglog():
            try:
                with open(str(pathlib.Path(__file__).parent.resolve())+'/deploy'+'/changelog.txt') as f:
                    return f.read()
            except:
                return 'The changelog could not be retrieved on our end'
        app.run(host=LOCALHOST, port=fileServerPort)
    
    RunFileServer(str(pathlib.Path(__file__).parent.resolve())+'/deploy', 5375)




if __name__=='__main__':
    threading.Thread(target=updatesr, args=(), daemon=True).start()
    main()