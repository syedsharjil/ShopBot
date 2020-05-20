from amazonbot import AmazonBot
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
#
# creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
# client = gspread.authorize(creds)
# sheet = client.open('ProductPrice').sheet1
#
# stuff = sheet.get_all_records()
# print(stuff)
class PriceUpdater(object):

    def __init__(self, spreadsheet_name):
        self.item_col = 1
        self.price_col = 2
        self.frequency_col = 3
        self.url_col = 4
        self.product_name_col = 5

        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']

        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',
                                                                 scope)
        client = gspread.authorize(creds)

        self.sheet = client.open(spreadsheet_name).sheet1

    def process_item_list(self):
        # Skip over the column heading in the spreadsheet.
        items = self.sheet.col_values(self.item_col)[1:]

        ab = AmazonBot(items)
        prices, urls, names = ab.searchitems()

        print("Updating spreadsheet.")
        for i in range(len(prices)):
            self.sheet.update_cell(i+2, self.price_col, prices[i])
            self.sheet.update_cell(i+2, self.url_col, urls[i])
            self.sheet.update_cell(i+2, self.product_name_col, names[i])


priceUpdater = PriceUpdater('ProductPrice')
priceUpdater.process_item_list()

