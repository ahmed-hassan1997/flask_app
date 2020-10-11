from flask import Flask , render_template

app = Flask(__name__)


@app.route('/')
def home_page():
	return render_template('index.html')


all_posts = [

			{'title' : 'post1' , 'content' : 'hello from first post ' , 'author' :'ahmed'},
			{'title' : 'post2' , 'content' : 'hello from second post '}

]

@app.route('/posts')
def show_all_posts():
	return render_template('posts.html' , posts = all_posts)



@app.route('/home/<string:name>/<int:id>')
def hello_world(name , id):
	return "hello , " + name + " your id is " + str(id)



@app.route('/blogs' , methods = ['GET'])
def blogs_ur():
	return "you enter this blogs"



if __name__ == "__main__":

	app.run(debug =True)
