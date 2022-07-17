import matplotlib.pyplot as plt

x = []
y = []
z=[]
counter = 0

for line in open(r'C:\Users\roige\Desktop\של רועי\ecosystem\data.txt', 'r'):
	lines = [i for i in line.split(',')]
	x.append(int(lines[0]))
	y.append(int(lines[1]))
	z.append(counter)
	counter+=1
	
plt.title("Rabbits/Foxes ratio")
plt.xlabel('time')
plt.ylabel('amount')
plt.plot(z, y, c = 'g',label='Rabbits')
plt.plot(z, x, c = 'r',label='Foxes')
leg = plt.legend(loc='upper center')

plt.show()