import pandas as pd

from difflib import SequenceMatcher
from collections import Counter
def load_data():
    original_data=pd.read_excel(r"C:\Users\pc\Downloads\archive\1000_raw_transction_data.xlsx")
    original_data["Price"] = pd.to_numeric(original_data["Price"], errors='coerce')
    original_data["Price"] = pd.to_numeric(original_data["Quantity"], errors='coerce')
    return original_data
pd.set_option('display.max_rows',None)
# dropes rows with missing data
def droping_nan(data,column_name):
    data=data.dropna(subset=[column_name])
    return data
# this function will evaluate the dates and if they are invalid it replaces them with NaT
def validate_dates(data):
    data["Transaction_Date"]=pd.to_datetime(data["Transaction_Date"],errors='coerce')
    return data
# THIS FUNCTION CLEANS THE NAME OF THE PRODUCT AND PRIDICT THE INCOMPLIT NAMES 
def clean_product_names(original_data):
    name={}
    original_data["Product_Name"]=original_data["Product_Name"].str.lower()
    for  item in original_data["Product_Name"]:
        typos=[]
        for value in original_data["Product_Name"]:
            ratio = SequenceMatcher(None, item, value).ratio()
            if ratio >= 0.62:
                typos.append(value)
        top = Counter(typos).most_common(1)[0][0]
        typos=set(typos)
        typos=list(typos)
        name[top]=typos
        better_name=name
    for key in name.keys():
        for item in name.keys():
            ratio=SequenceMatcher(None,key,item).ratio()
        if ratio >= 0.45:
            if len(key) > len(item):
                name[item]="incorrect"
            elif len(key) < len(item):
                name[key]="incorrect"
    for key in list(name):
        if name[key] == "incorrect":
            name.pop(key)
    for i in original_data.index:
        product = original_data.at[i, "Product_Name"]
        for key, value in name.items():
            if product in value:
                original_data.at[i, "Product_Name"] = key
                break
    return original_data

# THIS FUNCTION CHANGES NEGATIVE VALUES TO POSTIVE 
def neg_to_pos(original_data):
    original_data["Quantity"]=original_data["Quantity"].abs()
    original_data["Price"]=original_data["Price"].abs()
    return original_data
def transaction_states_cleaning(original_data):
    for i in original_data.index:
        states=original_data.at[i,"Transaction_Status"]
        if states=="Failed" or states=="failed":
            original_data.at[i, "Transaction_Status"] = None
    return original_data
def main():
    original_data=load_data()
    original_data=original_data.drop_duplicates() 
    original_data=droping_nan(original_data,"Transaction_ID")
    original_data=validate_dates(original_data)
    original_data=droping_nan(original_data,"Customer_ID")
    original_data=clean_product_names(original_data)
    original_data=droping_nan(original_data,"Quantity")
    original_data=droping_nan(original_data,"Price")
    original_data=neg_to_pos(original_data)
    original_data=transaction_states_cleaning(original_data)
    original_data=droping_nan(original_data,"Transaction_Status")
    print(original_data)
main()



