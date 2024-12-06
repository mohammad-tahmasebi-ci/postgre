import psycopg2

connection = psycopg2.connect(database="chinook")

cursor = connection.cursor()

#cursor.execute('select * from "Artist"')
#cursor.execute('select "Name" from "Artist"')
#cursor.execute('select * from "Artist" where "Name" = %s', ["Queen"])
#cursor.execute('select * from "Artist" where "ArtistId" = %s', [51])
#cursor.execute('select * from "Album" where "ArtistId" = %s', [51])
cursor.execute('select * from "Track" where "Composer" = %s', ["Queen"])

#results = cursor.fetchall()
results = cursor.fetchone()

connection.close()

for result in results:
    print(result)

