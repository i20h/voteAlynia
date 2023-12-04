from datetime import datetime
import time, requests, os, json

def createJsonFile(result):
    folder = "Result"
    if not os.path.exists(folder):
        os.makedirs(folder)
    filePath = os.path.abspath(__file__) + "\\Result\\" + datetime.now().date().strftime("%Y-%m-%d") + ".json"
    fileName = "Result/" + datetime.now().date().strftime("%Y-%m-%d") + ".json"
    if os.path.exists(filePath):
        pass
    else:
        with open(fileName, 'w') as file:
            file.write(result)

def requestUrl():
    url = "https://api.top-serveurs.net/v1/servers/8OUJ3EOWKQ/players-ranking"
    resp = requests.get(url)
    if resp.status_code == 200:
        date = datetime.now().date()
        print("Récupération des votes le", date)
        data = resp.json()
        top5Players = [{"votes": player["votes"], "playername": player["playername"]} for player in data["players"][:5]]
        result = {
        "top_players": top5Players
        }
        result = json.dumps(result, indent=2)
        createJsonFile(result)
    else:
        print("Problème d'exeuction le", datetime.now().date())

def initTimer():
    hour = 22
    minute = 59
    while True:
        if datetime.now().hour == hour and datetime.now().minute == minute and not os.path.exists("Result\\" + datetime.now().date().strftime("%Y-%m-%d") + ".json"): 
            requestUrl()
        time.sleep(30)
    
if __name__ == '__main__':
    print("Lancement de l'application le", datetime.now().date())
    initTimer()