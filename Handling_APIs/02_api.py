import sqlite3
import requests

conn = sqlite3.connect('ecommerce.db')

cursor = conn.cursor()

def getApidata():
    url = 'https://api.freeapi.app/api/v1/public/randomproducts/product/random'
    response = requests.get(url)
    data = response.json()

    if data['statusCode'] and "data" in data:
        stockCount = data['data']['stock']
        item = data['data']['title']
        price = data['data']['price']
        return stockCount,item,price
    else:
        raise Exception("Fail to fetch stock details!")
    
def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products
        (
            'ID' INTEGER PRIMARY KEY AUTOINCREMENT,
            'STOCK' INTEGER,
            'ITEM' TEXT,
            'PRICE'  REAL
        )
    ''')
    conn.commit()

def insert_data(stockCount,item,price):
    cursor.execute("INSERT INTO Products (STOCK,ITEM,PRICE) VALUES (?,?,?)",(stockCount,item,price))
    conn.commit()

def dataList():
    cursor.execute("SELECT * FROM Products")
    for row in cursor.fetchall():
        print(row)
    conn.commit()
    
def main():
    try:
        create_table()
        stockCount,item,price = getApidata()
        insert_data(stockCount,item,price)
        print(f"Stock count : {stockCount}, \nproduct : {item} \nprice : {price}")
        print("Stock Data save successfully!")
        dataList()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
    

