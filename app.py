from flask import Flask ,render_template,request

app=Flask(__name__, template_folder='Template')



@app.route('/greet',methods=['POST'])
def greet():
    import random
    name = request.form.get('name')
    age = int(request.form.get('age'))
    if age < 18:
        jokes = [
            "Why did the kid bring a ladder to school? Because he wanted to go to high school!",
            "What do you call fake spaghetti? An impasta!",
            "Why don't eggs tell jokes? They'd crack each other up!",
            "Why did the student eat his homework? Because the teacher said it was a piece of cake!",
            "What did one wall say to the other wall? I'll meet you at the corner!"
        ]
    elif 18 <= age < 30:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the math book look sad? Because it had too many problems.",
            "What do you call a bear with no teeth? A gummy bear!",
            "Why did the computer go to the doctor? Because it had a virus!",
            "What do you call a fish wearing a bowtie? Sofishticated!"
        ]
    elif 30 <= age < 50:
        jokes = [
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don't skeletons fight each other? They don't have the guts.",
            "What did the grape say when it got stepped on? Nothing, it just let out a little wine.",
            "Why did the coffee file a police report? It got mugged!",
            "What do you call an old snowman? Water!"
        ]
    else:
        jokes = [
            "Why did the bicycle fall over? It was two-tired!",
            "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
            "What do you call a factory that makes okay products? A satisfactory.",
            "Why did the belt get arrested? For holding up a pair of pants!",
            "What did the zero say to the eight? Nice belt!"
        ]
    joke = random.choice(jokes)
    return render_template('greet.html', name=name, age=age, joke=joke)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
