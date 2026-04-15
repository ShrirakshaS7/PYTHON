# Dictionary methods
#Get method
#1
data={'ename':'smith','salary':98000}
print(data.get('ename'))

#2
data={'ename':'smith','salary':98000}
print(data.get('job'))

#Update method
#1
data={'ename':'smith','salary':98000}
data.update({'job':'analyst'})
print(data)

#2
data={'ename':'smith','salary':98000}
data.update({'salary':'98500'})
print(data)

#or
data={'ename':'smith','salary':98000}
data.update(salary=98900)
print(data)

#Item method
#1
data={'ename':'smith','salary':98000}
print(data.items())

#Keys method
#1
data={'ename':'smith','salary':98000}
print(data.keys())

#Value method
#1
data={'ename':'smith','salary':98000}
print(data.values())

#Pop method
#1
data={'ename':'smith','salary':98000}
data.pop('salary')
print(data)

#Pop item method
#1
data={'ename':'smith','salary':98000}
data.popitem()
print(data)

#Clear method
#1
data={'ename':'smith','salary':98000}
data.clear()
print(data)