import requests
data="2023/09/09"
with open ("dataset.csv", "w") as f:
    while data!="2018/12/30":
        response= requests.get(f"https://www.cbr-xml-daily.ru/archive/{data}/daily_json.js")
        f.write(f'{data} , {response.json()["Valute"]["USD"]["Value"]}\n')
        data=response.json()["PreviousDate"][:10].replace("-", "/")

