import requests
data="2023/09/26"
while data!="":
    response= requests.get(f"https://www.cbr-xml-daily.ru/archive/{data}/daily_json.js", headers={"User-Agent":"Mozilla/5.0"})
    dates = f'{data},{response.json()["Valute"]["USD"]["Value"]}'
    data=response.json()["PreviousDate"][:10].replace("-", "/")
    with open("dataset.csv", "a") as f:
        f.write(f'{dates}\n')

