from pathlib import Path

import gspread
from oauth2client.service_account import ServiceAccountCredentials

HERE: Path = Path(__file__).resolve().parent
ROOT: Path = HERE.parent

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

cred = ServiceAccountCredentials.from_json_keyfile_name()


def main():
    pass


if __name__ == "__main__":
    main()
