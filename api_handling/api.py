import requests

def fetch():
   res = requests.get('https://api.freeapi.app/api/v1/public/randomusers/13')
   data = res.json()

   if data ["success"] == True:
      user_data = data["data"]
      username = user_data["login"] ["username"]
      print(username)


   else:
      raise Exception("failed to fetch user data")

fetch()
