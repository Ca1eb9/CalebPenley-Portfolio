def successorss(text):
    
    
        
    words = text.split()
    
    words.insert(0, ".") #### create ability for first word to be a successors to '.'
    
    final_lst = []
    
    output_dict = {}
    

    temp = '' #Create temporary string to manipulate
    for i in (words):
        sym = False
        if "," in i:
            sym = True
            temp = i.split(",")
            temp.insert(1, ",")   ###implements comma as an element
            final_lst.extend(temp)

        if "." in i:
            sym = True
            temp = i.split(".")
            temp.insert(1, ".") ###implements period as an element
            final_lst.extend(temp)
        if "!" in i:
            sym = True
            temp = i.split("!")
            temp.insert(1, "!") ###implements '!' as an element
            final_lst.extend(temp)


        if sym == False: #### word has no symbols
            final_lst.append(i)
    
    for i in final_lst: #### overall checks for an empty list
        if not i:
            final_lst.remove(i)
    
    
    for i in range(len(final_lst) - 1): ####adds succesors to their respective predesorces
        current_element = final_lst[i]
        next_element = final_lst[i + 1]

        if current_element not in output_dict:
            output_dict[current_element] = []

        if next_element not in output_dict[current_element]:
            output_dict[current_element].append(next_element)

    return output_dict

def successorss(t):
 d,e,p={},[],''
 for i in t+'.':e,p=[(e+[p]+[i],''),(e,p+i)][i.isalnum()^i.isnumeric()]
 p='.'
 while e!=[]:
  w,*e=e
  if w.strip():d[p],p=d.get(p,[])+[w]*(w not in d.get(p,[])),w
 return d

def successorss(t):
 t+='.'
 d = {}
 e=[]
 p=''
 for i in t:
  if i.isalnum() and not i.isnumeric():p+=i
  else:e+=[p]+[i];p=''
 p='.'
 while e!=[]:
  w,*e=e
  if w not in '\n\t ':
   if p in d:
    if w not in d[p]:
     d[p]+=[w]
   else:
    d[p] = [w]
   p = w
 return d

def successorss(t):
    """
        >>> text = "!`zT"
        >>> successors(text)
        {'.': ['one'], 'one': [',', '2'], ',': ['two', 'one'], 'two': ['-'], '-': ['three'], 'three': [';'], ';': ['Four'], 'Four': ['+'], '+': ['five'], 'five': ['*'], '*': ['six'], 'six': ['seven'], 'seven': ['('], '(': ['eight'], 'eight': [')'], ')': ['9'], '9': ['ten'], 'ten': ['1'], '1': ['one', '3'], '2': ['1'], '3': ['.']}
    """
    t+='.'
    d = {}
    e=[]
    p=''
    for i in t:
        if i.isalnum() and not i.isnumeric():p+=i
        else:e+=[p]+[i];p=''
    p='.'
    while len(e)>0:
        w=e.pop(0)
        if w not in '\n\t ':
            d=d|{p:([d[p],[]][p not in d ]+[[w],[]][w in d.get(p,[])])}
            p = w
    return d
#p=[(e:=e+[p]+[i],'')[1],p+i][i.isalnum() and not i.isnumeric()]
'''
def successors(t):
 d,e,v,p={},[],'','.'
 for i in t+p:e,v=[(e+[v]+[i],''),(e,v+i)][i.isalpha()]
 e+=[v]
 for w in e:
  if w.strip():d[p],p=d.get(p,[])+[w]*(not w in d.get(p,[])),w
 return d
'''
'''
def successors(t):
 d,e,v,p={},[],'','.'
 for i in t+p:e,v=[(e+[v]+[i],''),(e,v+i)][i.isalpha()]
 for w in e:
  if w.strip():k=d.get(p,[]);d[p],p=k+[w]*(not w in k),w
 return d
'''


def successors(t):
 import re;d,p={},'.'
 for w in re.findall('[a-zA-Z]+|\S',t+p):k=d.get(p,[]);d[p],p=k+[w]*(not w in k),w
 return d

import re
#successors=lambda t,d={},p='.':[(e:=re.findall(r'\d|[a-zA-Z]+|\S',t+'.')),p:=w for w in e]

import re

#successors=lambda t,d={},p='.':([p:=[p,w][not(d.update({p:d.get(p,[])+[w]*(w not in d.get(p,[]))}))]for w in (re.findall(r'\d|[a-zA-Z]+|\S',t+'.'))],d)[1]



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)