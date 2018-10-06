from flask import Flask, render_template
from flask import url_for

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
	names = []
	time = []
	filename = []
	ptr = []

	F = open("names.txt","r")
	s = F.read().split("\n")
	for i in range(int(len(s)/3)):
		ptr += [i]


	for i in range(len(s)):

		if (i%3 == 0):		
			names += [s[i]]
		elif(i%3==1):
			image_src = url_for('static', filename = 'images/' + s[i])
			filename += [image_src]
		else:
			time += [s[i]]

		
	return render_template('index2.html', filename = filename, names = names, time = time, ptr = ptr)

if __name__ == '__main__':
	app.run(debug = True)