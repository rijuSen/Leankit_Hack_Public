import requests
import json
import csv
import datetime
import os.path


def updateTimeSheet(url, name, username, password):
  payload = {}
  response = requests.get(url=url, auth=(username,password))
  #response = requests.request("GET", url, headers=headers, data = payload)
  response_str = response.text.encode('utf8')
  json_object = json.loads(response_str)
  card_list = json_object['cards']
  for card in card_list:
    if not isinstance(card['connectedCardStats'], dict):
      for user in card['assignedUsers']:
        if user['fullName'] == name:
          #print(card)
          cardCSVWriter(card)

def cardCSVWriter(card):
    if not os.path.isfile('cardList.csv'):
        with open('cardList.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            # print(card.keys())
            writer.writerow(["ID", "Date", "Lean_Task_Name", "Actual_Time", "Running_Time"])

    if checkEntry(card['id']) == False:
        with open('cardList.csv', 'a', newline='') as file:
          writer = csv.writer(file)
          actualStart_date_time_str = card['actualStart']
          actualStart_date_time_obj = datetime.datetime.strptime(actualStart_date_time_str, '%Y-%m-%dT%H:%M:%SZ')
          movedOn_date_time_str = card['movedOn']
          movedOn_date_time_obj = datetime.datetime.strptime(movedOn_date_time_str, '%Y-%m-%dT%H:%M:%S.%fZ')
          time_diff = movedOn_date_time_obj - actualStart_date_time_obj
          seconds = time_diff.seconds
          m, s = divmod(seconds, 60)
          h, m = divmod(m, 60)
          diff_in_time_in_hr_min = f'{h:d}:{m:02d}'
          # print(diff_in_time_in_hr_min)
          writer.writerow([card['id'], actualStart_date_time_obj.date(), card['title'], '2 hrs', diff_in_time_in_hr_min])

def checkEntry(id):
  # print(id)
  with open('cardList.csv', newline='') as csvfile:
    readerDict = csv.DictReader(csvfile)
    # print(readerDict)
    for row in readerDict:
      # print(row)
      if id == row['ID']:
        return True
    else:
      # print('False')
      return False

if __name__=='__main__':
  name = input("Enter Name: ").upper()
  if not name:
    name = 'NAME'
  boardNumber = input("Leankit Board Number: ")
  # if not boardNumber:
  #   boardNumber = 'LEANKIT BOARD NUMBER'
  laneNumber = input("Leankit Lane Number: ")
  # if not laneNumber:
  #   laneNumber = 'LEANKIT LANE NUMBER'
  username = input("Enter LeanKit registered mail id: ")
  if not username:
    username = 'user.monash.edu'
  password = input("Enter your password: ")
  # if not password:
  #   password = PASSWORD
  url = 'https://monashie.leankit.com/io/user/me/card?board={0}&lanes={1}'.format(boardNumber, laneNumber)
  updateTimeSheet(url, name, username, password)