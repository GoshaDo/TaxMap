import requests
from pathlib import Path
from os import listdir

URL = 'https://www.gov.il/BlobFolder/generalpage/' \
      'income-tax-monthly-deductions-booklet/he/' \
      'itc_itc_necuyim2021-1.pdf#page=18'

if __name__ == '__main__':
    if 'metadata.pdf' not in listdir():
        page = requests.get(URL)
        filename = Path('metadata.pdf')
        filename.write_bytes(page.content)
