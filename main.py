import gspread

gc = gspread.service_account(filename=".\\key.json")

sheet_url = "https://docs.google.com/spreadsheets/d/1WY0pdiHgJ39govH042CNgQD_vKKYyTsTslZMYsEw1Og/edit#gid=942461385"

sht = gc.open_by_url(sheet_url)

print(sht.sheet1.get('A1'))