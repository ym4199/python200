add = lambda x,y: x+y
ret = add(1,3)
print(ret)

funcs = [lambda x: x+'.pptx', lambda x: x+'.docx']
ret1=funcs[0]('Intro')
ret2=funcs[1]('Report')

print(funcs[0]('Reprot'))

print(ret1)
print(ret2)

names = {'Many':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245}

ret3 = sorted(names.items(), key=lambda x:x[0])

print(names.items())
print(sorted(names.items()))

print(ret3)