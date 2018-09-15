def puc():
	print('Hi there!')
	print('How are you?')


def hi(name):
	if name=='Joshua':
		print('Hi Joshua!')
	elif name=='Osafo':
		print('Hi Osafo!')
	else:
		print('Hi anonymous!')

def h(fname):
	print('Hi ' + fname + '!')

girls = ['Rachel','Monica','Phoebe','Ola','You']
for fname in girls:
	h(fname)
	#print('Next girl')

for i in range(6):
	print(i)
