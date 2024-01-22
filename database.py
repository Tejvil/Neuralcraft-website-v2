from sqlalchemy import create_engine, text

import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
    })

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = [dict(row._asdict()) for row in result.fetchall()]  # Convert each Row to a dictionary
        return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
      query = text("select * from jobs where id = :val").bindparams(val=id)
      result = conn.execute(query)
      rows = result.fetchall()
      if len(rows) == 0:
          return None
      else:
      # Build a dictionary by iterating over the columns
        row_dict = {column: value for column, value in zip(result.keys(), rows[0])}
      return row_dict


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO applications(job_id, full_name, email, linkedin_url, education, resume_url) VALUES(:job_id, :full_name, :email, :linkedin_url, :education, :resume_url)")
    conn.execute(query, {
        'job_id': job_id,
        'full_name': data.get('full_name'),
        'email': data.get('email'),
        'linkedin_url': data.get('linkedin_url'),
        'education': data.get('education'),
        'resume_url': data.get('resume_url')})
