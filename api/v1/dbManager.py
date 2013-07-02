import MySQLdb as db
from v1 import utils
import random

from barwars_db.models import User, Challenge
from django.core.exceptions import ObjectDoesNotExist


UNSOLVED = 0
SOLVED   = 1

def postProfileDataDB(uuid):

  print "post profile - 1, uuid : ", uuid
  if uuid is None or uuid == '':
    return False
  user = User(uuid = uuid, profile_name = getRandomProfileName())
  user.save()
  return True

def getProfileDataDB(uuid):
  if uuid is None or uuid == '':
    return None
  user = User.objects.get(uuid=uuid)
  return (user.uuid, user.profile_name, user.points, user.solved_count, user.submit_count)  
 
def getChallengesListDB(uuid, filter = None):
  ch_list = []
  if uuid is None or uuid == '':
    return False
  #TODO: pending filter logic
  challenges = Challenge.objects.filter(status = 0).exclude(uuid = uuid)
  for challenge in challenges:
    ch_obj = {}
    ch_obj['cid'] = challenge.cid
    ch_obj['description'] = challenge.description
    ch_list.append(ch_obj)
  return ch_list

def postChallengeDB(uuid, bar_code, description):

  if uuid is None or bar_code is None or description is None:
    print "Invalid input to postChallengeDb"
    utils.logLine("Invalid input to postChallengeDb")
    return False

  try:
    challenge = Challenge.objects.get(barcode = bar_code, uuid = uuid)
    print "Duplicate submission"
    return False
  except ObjectDoesNotExist:
    print "Not a duplicate submission"
    
  user = User.objects.get(uuid = uuid)
  challenge= Challenge(uuid = user, barcode = bar_code, status = UNSOLVED)
  challenge.save()

  user = User.objects.get(uuid = uuid)
  user.submit_count = user.submit_count + 1
  user.points = user.points - 1
  user.save()

  return True 
 
def solveChallengeDB(uuid, bar_code, cid):

  try:
    user = User.objects.get(uuid = uuid)
    challenge = Challenge.objects.get(cid = cid, barcode = bar_code).exclude(uuid = user)  
  except ObjectDoesNotExist:
    print "No match found"
    return False

  challenge.status = SOLVED
  challenge.save()
  
  user = User.objects.get(uuid = uuid)
  user.solved_count = user.solved_count + 1
  user.points = user.points + 1
  user.save()

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

