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
