import sqlite3

conn = sqlite3.connect("road.db")
conn.execute("drop table if exists road")
conn.execute("CREATE TABLE road(pincode INTEGER  , roadname TEXT,Status integer ) ")

# This data is already added into the database table
conn.execute("INSERT INTO road(pincode,roadname,Status) VALUES(?,?,?)",(560037,"Outer Ring Road",0))
conn.execute("INSERT INTO road(pincode,roadname,Status) VALUES(?,?,?)",(560068,"Silk Board Junction Road",0))

conn.commit()

#Run this file to create table named road