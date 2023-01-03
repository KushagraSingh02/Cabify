# pip install mysql-connector-python
import mysql.connector

# import mariadb
    
# mydb =  mariadb.connect(
#   host="localhost",
#   user="root",
# #   password="%T5687j5IiYe"
#     database="ebike"
# )
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    # password="password",
    database="cs657_project"
)
c = mydb.cursor()
# c.execute('CREATE TABLE IF NOT EXISTS temp(dealer_id TEXT, dealer_name TEXT, dealer_city TEXT, dealer_pin TEXT, '
#               'dealer_street TEXT)')

def create_table():
    # c.execute('CREATE TABLE IF NOT EXISTS DEALER(dealer_id TEXT, dealer_name TEXT, dealer_city TEXT, dealer_pin TEXT, '
            #   'dealer_street TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS customer(user_id varchar(20) not null unique,password varchar(20) not null,city varchar(20) not null,name varchar(20),phone bigint,city_id integer,primary key(user_id),foreign key(city_id) references platform(city_id))')
    

# print("hello")
def add_data(user_id, password, city, name, phone,city_id):
    print("hello2")
    c.execute('INSERT INTO CUSTOMER(user_id,password, city, name,phone, city_id) VALUES (%s,%s,%s,'
              '%s,%s,%s)',
              (user_id, password, city, name, phone,city_id))
    mydb.commit()


def view_all_data():
    c.execute('SELECT * FROM customer')
    data = c.fetchall()
    return data


def view_only_customer_ids():
    c.execute('SELECT user_id FROM customer')
    data = c.fetchall()
    return data


def get_dealer(user_id):
    c.execute('SELECT * FROM customer WHERE user_id="{}"'.format(user_id))
    data = c.fetchall()
    return data


def edit_dealer_data(new_user_id, new_password, new_city, new_name, new_phone,new_city_id,user_id, password, city, name, phone,city_id):
    c.execute("UPDATE customer SET user_id=%s, password=%s, city=%s, name=%s, phone=%s,city_id=%s WHERE "
              "user_id=%s and password=%s and city=%s and name=%s and phone=%s and city_id=%s", (new_user_id, new_password, new_city, new_name, new_phone,new_city_id,user_id, password, city, name, phone,city_id))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_data(user_id):
    c.execute('DELETE FROM customer WHERE user_id="{}"'.format(user_id))
    mydb.commit()
