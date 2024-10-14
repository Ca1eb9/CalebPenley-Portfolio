
def todaydate():
    print('hi')

def todayday(entities):
    print('hi')

def weather(entities):
    print('hi')
    type=''
    for i in entities:
        if 'location' in str(i):
            ent1s = i
            type = ent1s['type']
            location = ent1s['entity']
    print('hi')
    import geocoder
    g = geocoder.ip('me').latlng
    currentlat=g[0]
    currentlon=g[1]
    key='secret'
    import requests
    import datetime
    if 'location' in type:
        geo=requests.get('http://api.openweathermap.org/geo/1.0/direct?q={cityname}&limit=1&appid={APIkey}'.format(cityname=location, APIkey=key)).json()
        lat=geo[0]['lat']
        lon=geo[0]['lon']
    else:
        lat=currentlat
        lon=currentlon
    url='https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=imperial&appid={API}'.format(lat=lat, lon=lon, API=key)
    weather_info = requests.get(url).json()
    current=weather_info['current']
    res=''
    vis=''
    sr=''
    ss=''
    temp=''
    pres=''
    hum=''
    uv=''
    cloud=''
    ws=''
    wd=''
    if 'visibility' in str(entities):
        vis=current['visibility']
        if res!='':
            res+=' and'
        res+=' visibility is '+str(vis)+' miles'
    if 'sunrise' in str(entities):
        sr=current['sunrise']
        if res!='':
            res+=' and'
        sr = datetime.fromtimestamp(sr).strftime('%I:%M %p')
        res+=' sunrise is at '+str(sr)
    if 'sunset' in str(entities):
        ss=current['sunset']
        if res!='':
            res+=' and'
        ss = datetime.fromtimestamp(ss).strftime('%I:%M %p')
        res+=' sunset is at '+str(ss)
    if 'temp' in str(entities):
        temp=current['temp']
        feeltemp=current['feels_like']
        if res!='':
            res='and '+res
        res='The temperature is '+str(temp)+'F'+' while it feels like '+str(feeltemp)+'F'+res
    if 'pres' in str(entities):
        pres=current['pressure']
        if res!='':
            res+=' and'
        pres=round(int(pres)*0.02953,2)
        res+=' air pressure is '+str(pres)+' inHg'
    if 'humi' in str(entities):
        hum=current['humidity']
        if res!='':
            res+=' and'
        res+=' humidity is '+str(hum)+' percent'
    if 'uv' in str(entities) or 'ultra' in str(entities):
        uv=current['uvi']
        if res!='':
            res+=' and'
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
        res+=' uv index is '+uv
    if 'cloud' in str(entities):
        cloud=current['clouds']
        if res!='':
            res+=' and'
        res+=' cloud coverage is '+str(cloud)+' percent'
    if 'speed' in str(entities):
        ws=current['wind_speed']
        if res!='':
            res+=' and'
        res+=' wind speed is '+str(ws)+' miles per hour'
    if 'direction' in str(entities):
        wd=current['wind_deg']
        if res!='':
            res+=' and'
        res+=' wind direction is '+str(wd)
    if 'hi' in str(entities):
        hilo=requests.get('https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={APIkey}'.format(lat=lat, lon=lon, APIkey=key)).json()
        hi=hilo['main']['temp_max']
        if res!='':
            res+=' and'
        res+=' the high is '+str(hi)+'F'
    if 'lo' in str(entities):
        hilo=requests.get('https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={APIkey}'.format(lat=lat, lon=lon, APIkey=key)).json()
        lo=hilo['main']['temp_min']
        if res!='':
            res+=' and'
        res+=' the low is '+str(lo)+'F'
    if res=='':
        temp=current['temp']
        feeltemp=current['feels_like']
        desc=current['weather'][0]['description']
        print('It is currently '+str(temp)+'F'+' or '+str(feeltemp)+'F'+' with wind chill '+ 'with '+desc)
        res='It is currently '+str(temp)+'F'+' or '+str(feeltemp)+'F'+' with wind chill '+ 'with '+desc
    res=res.strip()
    print(res)
    return res
    
def last_name():
    print('hi')
    return "I do not have a last name"

def middle_name():
    print('hi')
    return "I do not have a middle name"

def todaymonth():
    print('hi')

def name():
    print('hi')
    return "My name is Maya"

def todaytime():
    print('hi')

def web_query(query):
    print('hi')
    subscription_key = "secret"
    assert subscription_key
    search_url = "https://api.bing.microsoft.com/v7.0/search"
    import requests
    from bs4 import BeautifulSoup
    from urllib.request import Request, urlopen
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {"q": query,}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    res = response.json()
    def html_parser(req):
        html_page = urlopen(req)
        soup = BeautifulSoup(html_page, "html.parser")
        htmltext = soup.get_text()
        text=htmltext
        #for line in htmltext:
            #if not line.isspace():
                #text += line
        return text
    import pprint
    pprint.pprint(res)
    try:
        if res['computation']:
            print(res['computation']['value'])
    except:
        #from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
        #tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2")
        #model = AutoModelForQuestionAnswering.from_pretrained("deepset/roberta-base-squad2")
        #contextnlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
        #try:
            #if res['entities']:
                #print('here')
                #print(res['entities']['value'][0]['contractualRules'][1]['url'])
                #response = requests.get(res['entities']['value'][0]['contractualRules'][1]['url'])
                #pprint.pprint(response)
                #req = Request(res['entities']['value'][0]['contractualRules'][1]['url'])
                #text = html_parser(req)
        #except:
        #try:
                print(res['webPages']['value'][0]['url'])
                #response = requests.get(res['webPages']['value'][0]['snippet'])
                #pprint.pprint(response)
                text = res['webPages']['value'][0]['snippet']
                # req = Request(res['webPages']['value'][0]['snippet'])
                #text = html_parser(req)
                index = text.find('.')
                #if not text[index+1].isupper():
                    #text = text.replace(text[index], '')
                index = text.find('.')
                print(text[0: index])
                ans = text[0: index]
                return ans
        #except:
                #return
        #QA_input = {'question': query, 'context': text}
        #resp = contextnlp(QA_input)['answer']
        #print(text)
        #print(resp)
        #synthesizer.speak_text_async(resp)
    return
def what_i_can_do():
    print('hi')

def who_built():
    print('hi')
    return "Caleb Penley developed me"

def wolf_query(query):
    print('hi')

def todayyear():
    print('hi')