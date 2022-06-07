from CRM import CRM
from Databse import BankDB
import pathlib

# getting the bank data
dic_path = pathlib.Path().resolve().__str__()
file_path = dic_path + '\\bank_data.json'
db = BankDB(file_path)
bank = db.create_bank()

# start
crm = CRM(bank)
crm.start()

# writing the data
db.write(bank)
