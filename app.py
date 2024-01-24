from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db,add_application_to_db
# import mysql.connector, os


app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'UPLOAD_FOLDER'


@app.route("/")
def hello():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "NOT FOUND", 404
  return render_template('jobpage.html', job=job)

@app.route("/job/<id>/apply", methods=['POST'])
def apply_to_job(id):
    data = request.form
    job = load_job_from_db(id)
    add_application_to_db(id, data)
    return render_template('Application_submitted.html', application=data, job=job)

@app.route('/policy')
def policy():
    return render_template('policy.html')
@app.route('/tnc')
def tnc():
    return render_template('tnc.html')

# # **********************************
# @app.route('/job/<id>/apply/upload', methods=['POST'])
# def upload_resume():
#   if 'file' not in request.files:
#               return redirect(request.url)

#   resume_file = request.files['file']

#   if resume_file.filename == '':
#               return redirect(request.url)

#   if resume_file:
#               # Save the file to the upload folder
#               resume_filename =os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
#               resume_file.save(resume_filename)

#               # Insert file information into the database
#               conn = mysql.connector.connect('db_connection_string')
#               cursor = conn.cursor()
#               sql = "INSERT INTO applicants (resume) VALUES (%s)"
#               with open(resume_filename, 'rb') as resume_blob:
#                   resume_data = resume_blob.read()
#                   cursor.execute(sql, (resume_data,))
#               conn.commit()
#               cursor.close()
#               conn.close()

#   return 'Resume uploaded successfully!'
# # **********************************

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
