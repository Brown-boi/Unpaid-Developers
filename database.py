import pymysql
def database_connection():
    host = '13.211.131.22'
    user = 'unpaiddevelopers'
    password='002@Latrobe'
    #password = input("Enter your password")
    database = 'unpaiddevelopersdb'
    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 database=database)
    cursor = connection.cursor()
    return cursor,connection
def comparision(cursor,connection,data):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS comparison (
            course_id VARCHAR(50) PRIMARY KEY,
            exchange_program  VARCHAR(10) NOT NULL,
            location VARCHAR(100) NOT NULL,
            course_duration_full_time VARCHAR(255) NOT NULL,
            course_duration_part_time VARCHAR(255) NOT NULL,
            total_credit_points VARCHAR(255) NOT NULL 
        )
    """)
    connection.commit()
    query="select course_id from comparison where course_id=%s"
    cursor.execute(query,data[0])
    rows = cursor.fetchone()
    if rows is None:
        query = "INSERT INTO comparison VALUES (%s, %s, %s ,%s, %s, %s)"
        cursor.execute(query,data)
        connection.commit()
def jobs_list(cursor,connection,table_name,outcome,maj):
    table_name=table_name+"_jobs_list"
    query = """CREATE TABLE IF NOT EXISTS """ + table_name + """ (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    job_opportunities  VARCHAR(100) NOT NULL,
                    major_required VARCHAR(100) NOT NULL
                    );"""
    cursor.execute(query)
    connection.commit()
    for i in range(len(outcome)):
        query = "select * from " + table_name + " where job_opportunities=%s and major_required=%s"
        cursor.execute(query,(outcome[i],maj[i]))
        rows = cursor.fetchone()
        if rows is None:
            query = "INSERT INTO " + table_name +" (job_opportunities,major_required) VALUES (%s, %s)"
            cursor.execute(query, (outcome[i],maj[i]))
            connection.commit()
    connection.close()




def major(cursor,connection,table_name,data):

    query="""CREATE TABLE IF NOT EXISTS """  +table_name+ """ (
                course_code VARCHAR(50) PRIMARY KEY,
                credit_point  VARCHAR(4) NOT NULL,
                subject_name VARCHAR(300) NOT NULL,
                link VARCHAR(700) NOT NULL
            );"""
    cursor.execute(query)
    connection.commit()
    j=0
    for i in data["code"]:
        query = "select course_code from " + table_name + " where course_code = %s "
        cursor.execute(query,i)
        rows = cursor.fetchone()
        if rows is None:
            query = "INSERT INTO " + table_name + " VALUES (%s, %s, %s ,%s)"
            row = data.iloc[j].tolist()
            row = tuple(row)
            cursor.execute(query, row)
            connection.commit()
        j=j+1
    connection.close()

"""
cur,connection=database_connection()
major(cur,connection,'softwareengineering',1)
#comparision(cur,connection,("SBCS",123))
#connection.close()
"""