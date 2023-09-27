import requests
data="2023/09/26"
dates=[]
with open ("dataset.csv", "w") as f:
    while data!="2018/12/30":
        response= requests.get(f"https://www.cbr-xml-daily.ru/archive/{data}/daily_json.js", headers={"User-Agent":"Mozilla/5.0"})
        dates.append(f'{data},{response.json()["Valute"]["USD"]["Value"]}')
        data=response.json()["PreviousDate"][:10].replace("-", "/")
    dates = reversed(dates)
    for date in dates:
        f.write(f"{date}\n")

