import json
import os
from google.oauth2.service_account import Credentials

# Авторизация в Google API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials_info = json.loads(os.getenv("GOOGLE_CREDENTIALS"))
creds = Credentials.from_service_account_info(credentials_info, scopes=["https://www.googleapis.com/auth/spreadsheets"])
client = gspread.authorize(creds)

# Открываем таблицу
SPREADSHEET_ID = "1ZjwgxwkI22VcFphpab_YCnIEcXFPIhVs0ZtoRBjgWdI"
sheet = client.open_by_key(SPREADSHEET_ID).sheet1

# Функция для сохранения отзыва
def save_review(name, specialist, city, rating, review):
    sheet.append_row([name, specialist, city, rating, review])
