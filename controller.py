import sqlite3

DB_FILE = "database/job_applications.db"

def add_job(company, position, status):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO jobs (company, position, status) VALUES (?, ?, ?)", 
                   (company, position, status))
    conn.commit()
    conn.close()
    print("✅ Job added successfully!")

def view_jobs():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, company, position, status FROM jobs")
    jobs = cursor.fetchall()
    conn.close()
    return jobs

def update_job_status(job_id, new_status):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("UPDATE jobs SET status = ? WHERE id = ?", (new_status, job_id))
    conn.commit()
    conn.close()
    print("✅ Job status updated!")

def delete_job(job_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM jobs WHERE id = ?", (job_id,))
    conn.commit()
    conn.close()
    print("✅ Job deleted successfully!")
