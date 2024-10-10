

def snake():
    for n in range(2, 7):
        for i in range((n+1)//2):
            print(' '*((n-1)//2-i)+'/')
        for i in range(n-1):
            for h in range(n):
                print(((' '*(n-h-1))+'/' if i % 2 else (' '*(h))+'\\'))
        for k in range(-(-n//2)-1):
            print(((' '*(n-k-1))+'/' if h % 2 else (' '*(k))+'\\'))
        print(' '*(n//2)+'O\n')

def snake():
    r=range
    for n in range(2,7):
        for i in range(-~n//2):
            print(' '*(~-n//2-i)+'/')
            
            
        for i in range(n*[-(-n//2)-1,n][i<=n-2]-n//2-1):
            print([(' '*(i%n))+'\\',(' '*(n-i%n-1))+'/'][(i//n)%2])
            
        print(' '*(n//2)+'O\n')

#snake()


def snake():
 p,r=print,range
 for n in r(2,7):
  for i in r(-~n//2):p(' '*(~-n//2-i)+'/')
  for i in r(n*[n,-(-n//2)-1][i>n-2]-n//2-1):p([(' '*(i%n))+'\\',(' '*(n-i%n-1))+'/'][i//n%2])
  p(' '*(n//2)+'O\n')

#snake()
def snake():
    p,r=print,range
    for n in r(2,7):
        for i in r(-~n//2):p(' '*(2-i)+'/')
        for i in r(n*[n,-(-n//2)-1][i>n-2]-n//2-1):p([(' '*(i%n))+'\\',(' '*(n-i%n-1))+'/'][i//n%2])
        p(' '*(n//2)+'O\n')


 
    
#snake()


def snake(n=2):
 p,r,j,q=print,range,' ','for i in r('
 exec(f'''for n in r(2,7):
  h=~-n//2
  {q}h+1):p(j*(h-i)+'/')
  {q}n*[n,h][i>n]-n//2-1):p([i%n*j+'\\\\',~i%n*j+'/'][i//n%2])
  p(n//2*j+'O\\n')''')

#snake()
def snake():
 p,r,j=print,range,' '
 for n in r(2,7):
  h=~-n//2
  for i in r(h+1):p(j*(h-i)+'/')
  for i in r(n*[n,h][i>n]-n//2-1):p([i%n*j+'\\',~i%n*j+'/'][i//n%2])
  p(n//2*j+'O\n')
#snake()

def snake(n=2):
 p,r,j,h=print,range,' ',~-n//2
 for i in r(h+1):p(j*(h-i)+'/')
 for i in r(n*[n,h][i>n]-n//2-1):p([i%n*j+'\\',~i%n*j+'/'][i//n%2])
 p(n//2*j+'O\n')
 if n<6:snake(n+1)
snake()
def snake(n=2):
 p,r,j,h,o,y=print,range,' ',~-n//2,'for i in r(','n//2'
 exec(f'''{o}h+1):p(j*(h-i)+'/')
{o}n*[n,h][i>n]-{y}-1):p([i%n*j+'\\\\',~i%n*j+'/'][i//n%2])
p({y}*j+'O\\n')
if n<6:snake(n+1)''')

#snake()

def snake():
 p,r,j=print,range,' '
 for n in r(2,7):
    h=~-n//2
    for i in r(h+1):
        #p(j*(h-i)+'/')
       pass
    #print(~-(~-n//2)+2)
    print(n//2)
    
    #print(n//2)
    for i in r(n*[n,h][i>n-2]-n//2-1):
        
        #p([(j*(i%n))+'\\',(j*(~i%n))+'/'][i//n%2])
        pass
    #p(j*(n//2)+'O\n')
#snake()


#snake()
'''
x=5
y=7
a=2
for a in range(2,x*(-~a//2)):
    print(a%(-~a))
    pass

for a in range(x):
    #print()
    for b in range((-~a//2)):
        #print(b)
        pass
        '''
r=range
x=5
y=1
#list(map(print,x))
#print()
#print((y>x|x==5))
'''
for a in range(10):
   print(a)

for b in range(27):
   print(b)'''

def snake():p,r,j,i=print,range,' ',0;[[h:=~-n//2,[p(j*(h-i)+'/')for i in r(h+1)],[p((j*(i%n))+'\\',[(j*(~i%n))+'/'][i//n%2])for i in r(n*[n,h][i>n-2]-n//2-1)],p(j*(n//2)+'O\n')] for n in r(2,7)]
  
#snake()

#exec("def snake(n):[print(' '*~-n//2-i*'/'if i<~-n//2else[' '*(i%n)+'\\',' '*(n-i%n-1)+'/'][i//n%2])for i in range(-~n//2+n*[-(-n//2)-1,n][i<=n-2]-n//2-1)]")

# Example usage:
#snake(10)

#print('''hi %s'''%'kale')

