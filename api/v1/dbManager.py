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

dflt_points = 100
dflt_solved_count = 0
dflt_submit_count = 0

UNSOLVED = 0
SOLVED   = 1

#########################################################################
# DB: Cursor: 
#########################################################################
def getDbCursor():

  print "===="
  global db_cursor
  global db_con
  #print "3==>", str(db_cursor)
  if db_cursor:
    return db_cursor

  try:
    # DB: Connection: Create
    db_con = db.connect( DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    db_con.autocommit(True)
    
    # DB: Init: Success
    db_init_flag = True
    
    # DB: Cursor:
    db_cursor = db_con.cursor()
    
    # logLine( "DB: Connection: Create: Success:")

  except db.Error, e:
    db_cursor = None
    print "DB cursor error: ", e
  return db_cursor

################################################################
#  Name: getRandomName
################################################################
def getRandomProfileName():

  static_profile_name_list = [  'Aayla','Admiral','Admiral','Admiral','Ahsoka',
                                'Anakin','Asajj','Aurra','Bail','Barriss',
                                'Bastila','Ben','Bib','Biggs','Boba',
                                'Bossk','Boss','C3P0','Cad','Cade',
                                'Canderous','Captain','Chewbacca','Commander','Count',
                                'Dak','Darth','Darth','Darth','Darth',
                                'Darth','Darth','Darth','Darth','Darth',
                                'Dash','Dengar','Desann','Doctor','Durge',
                                'Emperor','Exar','General','General','Gilad',
                                'Grand','Grand','Greedo','Han','HK-47',
                                'Hondo','IG-88','Jabba','Jacen','Jaina',
                                'Jango','Jaxxon','Jek','Jerec','Joruus',
                                'Ki-Adi-Mundi','Kir','Kit','Kyle','Lando',
                                'Lobot','Luke','Luminara','Lumiya','Mace',
                                'Malakili','Mara','Max','Mon','Natasi',
                                'Nien','Noa','Obi-Wan','Oola','Padme',
                                'Plo','Princess','Prince','PROXY','Qui-Gon',
                                'Quinlan','R2-D2','RX-24','Salacious','Sebulba',
                                'Shaak','Starkiller','Talon','Uncle','Watto',
                                'Wedge','Wicket','Yaddle','Yoda','Zam']

  min_index = 0
  max_index = len(static_profile_name_list) 

  return static_profile_name_list[random.randint( min_index, max_index)].strip()

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
    profile_names 
    query  = 'insert into ' + UserTblName + ' values(' + '\''    +\
                db_con.escape_string(str(uuid)) + '\', ' + '\''  +\
                getRandomProfileName() + '\', '   +\
                str(dflt_points)       + ', ' +\
                str(dflt_solved_count) + ', ' +\
                str(dflt_submit_count) + ', ' +\
                ' now(),' + ' now())'
     
    utils.logLine(query)
    print "query: ", query
    db_cursor.execute(query)
    #db_cursor.execute("commit")

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


def postChallengeDB(uuid, bar_code, description):

  global db_con
  global db_cursor
  print "11"
  if uuid is None or bar_code is None or description is None:
    print "Invalid input to postChallengeDb"
    utils.logLine("Invalid input to postChallengeDb")
    return False

  print "12"
  try:
    
    db_cursor = getDbCursor()
    
    # Challenge: Duplicate: Check:
    query  = 'select * from ' + ChallengeTblName + ' where '
    query += 'barcode like \'' + db_con.escape_string(str(bar_code)) + '\''
    query += 'and uuid like \'' + db_con.escape_string(str(uuid)) + '\''
    utils.logLine(query)
    db_cursor.execute(query)
    if db_cursor.fetchone():
      err_msg = "Duplicate: Challenge: "
      print err_msg + query
      err_msg = ""
      return False
         
    # Challenge: Add: Query:
    query  = 'insert into ' + ChallengeTblName + '( barcode, description, status, uuid, time_created, time_updated)  values('
    query += '\''  + db_con.escape_string(str(bar_code)) + '\',' + '\'' +\
                     db_con.escape_string(str(description)) + '\',' +\
                     str(UNSOLVED) + ',' + '\''  +\
                     db_con.escape_string(str(uuid)) + '\',' + ' now(),' + ' now())'
    utils.logLine(query)
    print "13 -- query: ", query
    db_cursor.execute(query)
    
    # User: Update: Submit_count: Increment
    # User: Point: Count: Decrement
    table = 'user'
    query  = 'update ' + UserTblName +\
               ' set submit_count=submit_count+1, ' +\
               ' points=points-1 where' +\
               ' uuid=\''  + db_con.escape_string(str(uuid)) + '\''
    utils.logLine(query)
    db_cursor.execute( query)

    #db_cursor.execute("commit")
    return True
  except db.Error, e:
    print "DB update/insert error: ", e
    return False 
 

def solveChallengeDB(uuid, bar_code, cid):

  global db_con
  global db_cursor

  try:  
    # Challenge: Solve: Check:
    db_cursor = getDbCursor()
    column_list = 'barcode'  
    where_clause_unsolved_challenges = 'status=' + str(UNSOLVED)
    where_clause_not_post_by_current_user = ' uuid !=  \'' +\
      db_con.escape_string(str(uuid)) + '\''
  
    query  = 'select ' + column_list + ' from ' + ChallengeTblName + ' where '
    query += where_clause_unsolved_challenges
    query += ' and ' + where_clause_not_post_by_current_user
    query += ' and cid = ' + db_con.escape_string(str(cid))
    query += ' and barcode = \'' + db_con.escape_string(str(bar_code)) + '\' '
    utils.logLine(query)
    db_cursor.execute(query)
  
    # Failure: If there no match
    if not db_cursor.fetchone():
      print "Solve challenge==>, NO match found!!!, query was :: ", query
      return False
  
    # Challenge: Solve: Mark: Solved
    print "Solve challenge, going to run update==> "
    query  = 'update ' + ChallengeTblName + ' set status=' + str(SOLVED) +\
               ' where cid=' + db_con.escape_string(str(cid)) 
    utils.logLine(query)
    db_cursor.execute(query)
  
    # User: Increment: Solved: Count:
    # User: Increment: Solved: Count:
    query  = 'update ' + UserTblName +\
               ' set solved_count=solved_count+1, ' +\
               ' points=points+1 where uuid=\''  +\
               db_con.escape_string(uuid) + '\''
    utils.logLine(query)
    db_cursor.execute(query)

    #db_cursor.execute( "commit")
    return True
  except db.Error, e:
    print "DB solve challenge error: ", e
    return False
 
