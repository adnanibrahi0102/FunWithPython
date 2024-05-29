import requests

def main():
    res = requests.get('https://api.freeapi.app/api/v1/public/randomusers/13')
    data = res.json()
    print(data)


if __name__ =="__main__":
    main()