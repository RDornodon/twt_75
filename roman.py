for t in[0]*int(input()):print(sum((t:=((l:=5**(x%2)*10**(x//2)),-l)[l<t])for x in map('IVXLCDM'.find,input()[::-1])))