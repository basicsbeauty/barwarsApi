import MySQLdb as db
from v1 import utils
import random

DB_HOST     = 'localhost'
DB_USER     = 'u_barwars'
DB_PASSWORD = 'barwars'
DB_NAME     = 'db_barwars'
 
db_cursor = None
db_con    = None

UserTblName = "user"
UsrTblColList = ['uuid', 'profile_name', 'points', 'solved_count', 'submit_count']
UserTblCol = {
  'uuid': 0,
  'profile_name': 1,
  'points': 2, 
  'solved_count': 3,
  'submit_count': 4
} 

ChallengeTblName = "challenge"
ChallengeTblColList = ['cid', 'description']
ChallengeTblCol = {
  'cid': 0,
  'description': 1
}

dflt_points = 128
dflt_solved_count = 0
dflt_submit_count = 0

#########################################################################
# DB: Cursor: 
#########################################################################
def getDbCursor():

  print "===="
  global db_cursor
  global db_con
  #print "3==>", str(db_cursor)
  if db_cursor:
    print "3"
    return db_cursor

  try:
    # DB: Connection: Create
    print "31"
    db_con = db.connect( DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    print "32"
    
    # DB: Init: Success
    db_init_flag = True
    
    # DB: Cursor:
    db_cursor = db_con.cursor()
    print "4"
    
    # logLine( "DB: Connection: Create: Success:")

  except db.Error, e:
    print "4 - err"
    db_cursor = None
    print "DB cursor error: ", e
  return db_cursor


def getProfileDataDB(uuid):
  global db_con
  global db_cursor
  if uuid is None or uuid == '':
    return None
  try:
    db_cursor = getDbCursor()
    #column_list = ' uuid, profile_name, points, solved_count, submit_count'
    column_list = ', '.join(UsrTblColList)
    print column_list
    query  = 'select ' + column_list + ' from ' + UserTblName +\
               ' where uuid=\'' + db_con.escape_string(str(uuid)) + '\''
                  
    print "query"
    utils.logLine(query)
    db_cursor.execute( query)            
    db_record = db_cursor.fetchall()
    if not db_record:
      print "Unable to retrieve user record!!"
      return None
    print "db rec::=>", db_record
    # Only return first record
    return db_record[0]
  except db.Error, e:
    print "DB error: ", e
    logLine("DB query error: " + str(e))
    return None
   
def postProfileDataDB(uuid):
  global db_con
  global db_cursor

  if uuid is None or uuid == '':
    return False
  try:
    db_cursor = getDbCursor()
    profile_names = [ 'Detective', 'Discoverer', 'Hunter'] 
    query  = 'insert into ' + UserTblName + ' values(' + '\''    +\
                db_con.escape_string(str(uuid)) + '\', ' + '\''  +\
                profile_names[random.randint(0, 2)]   + '\', '   +\
                str(dflt_points)       + ', ' +\
                str(dflt_solved_count) + ', ' +\
                str(dflt_submit_count) + ', ' +\
                ' now(),' + ' now())'
     
    utils.logLine(query)
    print "query: ", query
    db_cursor.execute(query)
    db_cursor.execute("commit")

  except db.Error, e:
    print "DB creation error: ", str(e)
    utils.logLine("DB creation error: " + str(e))
    return False

  return True

def getChallengesListDB(uuid, filter = None):
  global db_con
  global db_cursor

  if uuid is None or uuid == '':
    return False
  try:
    db_cursor = getDbCursor()
    # Query:
    column_list = ', '.join(ChallengeTblColList)
    query  = 'select ' + column_list + ' from ' + ChallengeTblName +\
             ' where status=0 and uuid != \'' +\
             db_con.escape_string(str(uuid)) + '\' '
    if filter:
        query += 'and description like \'%' + str(filter) + '%\' '
    
    query += ' group by description'
    print "query: ", query
    db_cursor.execute( query)
    db_records = db_cursor.fetchall()
    
  except db.Error, e:
    print "DB error: ", e
    return None

  return db_records


