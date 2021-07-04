import numpy as np
import matplotlib.pyplot as plt
import os
import glob

def readFile(name='input.txt'):
	x = []
	y = []
	with open(name, 'r') as f:
		for line in f.readlines():
			line = line.strip() #Remove '\n'
			data = line.split()
			x.append((1.0, float(data[0]), float(data[1])))
			y.append(int(data[2]))
	return (np.array(x), np.array(y))

def findError(w, x, y):
	#Check if there is an error
	for j in range(x.shape[0]):
		predict = 1 if np.inner(w, x[j]) >= 0 else -1
		if predict != y[j]:
			return (x[j], y[j])
	return None

def pla(x, y, maxLoop = 100):
	w = np.zeros(3)
	for i in range(maxLoop):
		if findError(w, x, y) != None:
			(xError, yError) = findError(w, x, y)
			draw(x, y, w, i+1)
			#Update W: Wt+1 = Wt + y*x
			w = w + yError*xError		
		else:
			print('w0: ' + str(w[0]))
			print('w1: ' + str(w[1]))
			print('w2: ' + str(w[2]))
			draw(x, y, w, i+1)
			break
			
def draw(x, y, w, loopTime):
	fig = plt.figure()
	ax = plt.subplot(1, 1, 1)
	#Draw the data points
	for i in range(x.shape[0]):
		color = 'b' if np.inner(w, x[i]) >= 0 else 'r'
		if y[i] == 1:
			ax.scatter(x[i][1], x[i][2], s=20, c=color, marker="o")
		else:
			ax.scatter(x[i][1], x[i][2], s=20, c=color, marker="x")
	#Draw the boundary generated by the perceptron
	if w[2]!=0:
		a,b = -w[1]/w[2], -w[0]/w[2]
		l = np.linspace(np.min(x[:,1])-5, np.max(x[:,1])+5)
		ax.plot(l, a*l + b, 'b-')
	ax.set_xlim(np.min(x[:,1])-5, np.max(x[:,1])+5)
	ax.set_ylim(np.min(x[:,2])-5, np.max(x[:,2])+5)
	fig.savefig('img/pla_at'+str(loopTime)+'.png')
	plt.close(fig)

# Remove all pictures of the result before
files = glob.glob('img/*png')
for f in files:
    os.remove(f)

#Read data from input.txt
trainX, trainY = readFile()
print(trainX.shape)
#print(trainX)
print(trainY.shape)
#print(trainY)
pla(trainX, trainY)