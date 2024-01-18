from flask import Flask, render_template,url_for,jsonify

app = Flask(__name__)             # app is object of class Flask

JOBS = [
    {
        'id':1,
        'title':"Web Development",
        'location': 'Remote' ,
        'enrollment_fee': 200
    },
    {
        'id':2,
        'title':"UI/UX",
        'location': 'Remote',
        'enrollment_fee': 100
    },
    {
        'id':3,
        'title':"Data Science",
        'location': 'Remote',
        'enrollment_fee': 200
    },
    {
        'id':4,
        'title':"Java Programming",
        'location': 'Remote',
        'enrollment_fee': 150
    },
    {
        'id':5,
        'title':"C++ Programming",
        'location': 'Remote',
        'enrollment_fee':100
    },
    {
        'id':6,
        'title':"Python Programming",
        'location': 'Remote',
        'enrollment_fee': 150
    },
    {
        'id':7,
        'title':"Artificial Intelligence",
        'location': 'Remote',
        'enrollment_fee': 200
    },
    {
        'id':8,
        'title':"Machine Learning",
        'location': 'Remote',
        'enrollment_fee': 200
    }
]

@app.route("/")
def hello():
    return render_template('home.html',jobs=JOBS, company_name="Neuralcraft")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__  ==  "__main__":
    app.run(host='0.0.0.0', debug=True)
    


