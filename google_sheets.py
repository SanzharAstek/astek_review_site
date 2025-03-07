import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Авторизация в Google API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("flask-google-sheets-123456.json", scope)
client = gspread.authorize(creds)

# Открываем таблицу
SPREADSHEET_ID = "1ZjwgxwkI22VcFphpab_YCnIEcXFPIhVs0ZtoRBjgWdI"
sheet = client.open_by_key(SPREADSHEET_ID).sheet1

# Функция для сохранения отзыва
def save_review(name, specialist, city, rating, review):
    sheet.append_row([name, specialist, city, rating, review])
