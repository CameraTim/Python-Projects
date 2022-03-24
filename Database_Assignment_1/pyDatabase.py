#Adding the sqlite module
import sqlite3

fileDisplay = ""

#
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mov', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#
sqlConn = sqlite3.connect('pyDatabase.db')

with sqlConn:
    #
    cur = sqlConn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_MainDirectory( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                File_Name TEXT \
                )")
    sqlConn.commit()

    #
    for i in fileList:
        if i.endswith('.txt'):
            cur.execute("INSERT INTO tbl_MainDirectory(File_Name) VALUES (?)", (i,))
            print(i)
        sqlConn.commit()
sqlConn.close()
