import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open('ETM')

team = sheet.worksheet('team')
task = sheet.worksheet('task')
meet = sheet.worksheet('meet')
project = sheet.worksheet('project')


def get_task(username):
    task = sheet.worksheet('task')
    all_records = task.get_all_records()
    list = []
    for i in all_records:
        if i['assign_to'] == username:
            list.append(i)

    return list


# def get_task(username):
#     task = sheet.worksheet('task')
#     filter = task.findall(username)
#     list = []
#     for i in filter:
#         tittle = task.cell(i.row,2).value
#         project = task.cell(i.row,3).value
#         details = task.cell(i.row,4).value
#         docs = task.cell(i.row,6).value
#         allocation = task.cell(i.row,7).value
#         deadline = task.cell(i.row,8).value
#
#         dict = {'tittle':tittle,'project':project,'details':details,'docs':docs,'allocation':allocation,'deadline':deadline}
#         list.append(dict)
#
#     return list


def get_team():
    team = sheet.worksheet('team')
    dict = team.get_all_records()

    return dict

def get_meet():
    meet = sheet.worksheet('meet')
    dict = meet.get_all_records()

    return dict


def get_profile(username):
    team = sheet.worksheet('team')
    all_records = team.get_all_records()
    list = []
    for i in all_records:
        if i['username'] == username:
            list.append(i)

    return list



# def get_profile(username):
#     team = sheet.worksheet('team')
#     filter = team.find(username)
#     username = team.cell(filter.row, 1).value
#     name = team.cell(filter.row, 2).value
#     link = team.cell(filter.row, 3).value
#     email = team.cell(filter.row, 4).value
#     phone = team.cell(filter.row, 5).value
#     birthday = team.cell(filter.row, 6).value
#     role = team.cell(filter.row, 7).value
#     project = team.cell(filter.row, 8).value
#     join_date = team.cell(filter.row, 9).value
#
#     dict = {
#         'username':username,
#         'name':name,
#         'link':link,
#         'email':email,
#         'phone':phone,
#         'birthday':birthday,
#         'role':role,
#         'project':project,
#         'join_date':join_date
#
#     }
#
#     return dict

