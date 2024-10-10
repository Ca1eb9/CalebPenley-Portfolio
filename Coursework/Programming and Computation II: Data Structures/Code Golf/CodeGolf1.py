def grade_calculator(h,l,q,y,a,c,r,g):
    j=(5*(h*7+l*4+c)+(q+y)*13+a*6)/100+min(r,9)*2/9
    e=int(-(-(((dict(A=93,B=83,C=70,D=60,F=0)|{'A-':90,'B+':87,'B-':80,'C+':77})[g]-j)/.06)//1))
    
    #return #sum(x*(.4-.05*a.index(x)) for x in a[:6])
    return 'You '+[f'need a {max(e,0)}% to','cannot'][e>100]+f' get a {g} in the class'


grade_calculator=lambda h,l,q,y,a,c,r,g:(e:=int(-(-((dict(A=93,B=83,C=70,D=60,F=0)|{'A-':90,'B+':87,'B-':80,'C+':77})[g]-((5*(h*7+l*4+c)+(q+y)*13+a*6)/100+min(r,9)/9*2))/.06//1)),'You '+[f'need a {max(e,0)}% to','cannot'][e>100]+f' get a {g} in the class')[1]

#grade_calculator=lambda *a:(e:=int(-(-((dict(A=93,B=83,C=70,D=60,F=0)|{'A-':90,'B+':87,'B-':80,'C+':77})[a[7]]-(sum(i*[.35,.2,.13,.13,.06,.05][a.index(i)]for i in a[:6])+2/9*min(a[6],9)))/.06//1)),'You '+[f'need a {max(e,0)}% to','cannot'][e>100]+f' get a {a[7]} in the class')[1]

g='A'
#print([93,90,87,83,80,77,70,0,0,60,0,0,0,93]['ABCDF'.find(g[0])*3])
#print(dict(A=93,B=83,C=70,D=60,F=0))

str()

{'A':93,'A-':90,'B+':87,'B':83,'B-':80,'C+':77,'C':70,'D':60,'F':0}

#print()
def hi(g):
    r=100 - (ord(g[0])%32*10-3 +(3 if'-' in g else -4 if 'B+' in g else -7 if 'C+' in g else 0))
    r=100 - ord(g[0]) % 32 * 10 +(0 if '-' in g else 7 if '+' in g else -40 if 'F' in g else 3 if 'C' not in g and 'D' not in g else 0)

    return r

print(grade_calculator(0,0,0,0,0,0,1,'A-'))

#print(-.06//1)

e = 102
g = 'B-'
##print((f'You need a {max(e,0)}% to'if e<= 100 else'You cannot')+f' get a {g} in the class')
l = 'C'
#print(-('+'in l)*3)
#print([93,83,70,60,0,0][(ord(l[0]))-65]-(-('+'in l)or'-'in l)*3)