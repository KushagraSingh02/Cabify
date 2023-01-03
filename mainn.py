#file for creation and filling of the database 
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

#Creating 
# c.execute('CREATE TABLE IF NOT EXISTS platform(city_id integer not null ,city varchar(20) not null, city_head varchar(20),primary key(city_id))')
# c.execute('CREATE TABLE IF NOT EXISTS customer(user_id varchar(20) not null unique,password varchar(20) not null,city varchar(20) not null,name varchar(20),phone bigint,city_id integer,primary key(user_id),foreign key(city_id) references platform(city_id))')
# c.execute('CREATE TABLE IF NOT EXISTS admin(admin_id varchar(20) not null unique,password varchar(20) not null,city varchar(20) not null,name varchar(20),phone bigint,city_id integer,primary key(admin_id),foreign key(city_id) references platform(city_id))')
# c.execute('CREATE TABLE IF NOT EXISTS driver(driver_id varchar(20) not null unique,password varchar(20) not null,city varchar(20) not null,name varchar(20),phone bigint,city_id integer,primary key(driver_id),foreign key(city_id) references platform(city_id))')
# c.execute('CREATE TABLE IF NOT EXISTS vehicle(vehicle_id varchar(20) not null unique,vehicle_no varchar(20) not null,vehicle_type varchar(20) ,driver_id varchar(20) not null,primary key(vehicle_id),foreign key(driver_id) references driver(driver_id))')
# c.execute('CREATE TABLE IF NOT EXISTS trip(trip_id varchar(20) not null unique,pickup varchar(20) ,droploc varchar(20),vehicle_id varchar(20) not null,user_id varchar(20) not null,primary key(trip_id) ,Foreign key(vehicle_id) references vehicle(vehicle_id),Foreign key(user_id) references customer(user_id))')
# c.execute('CREATE TABLE IF NOT EXISTS payment(payment_id varchar(20) not null unique,trip_id varchar(20) not null unique,amount integer,primary key(payment_id,trip_id),foreign key(trip_id) references trip(trip_id))')


#Populating the tables 

# c.execute('insert into platform values ('Bangalore',1,'harvey' ),('Chennai',2,'Mike' ),('Delhi',3,'Donna' ),('Mumbai',4,'Jessica' ) ')

# c.execute("insert into admin values ('evan@gmail.com',3456,'Bangalore','evan',1234567890,1),('steve@gmail.com',1234,'Delhi','steve',2345678901,3),('harry@gmail.com',9874,'Mumbai','harry',1234567899,3),('marvel@gmail.com',8678,'Chennai','marvel',4321567890,2),('pratt@gmail.com',1249,'Delhi','pratt',1276549890,3)")

# c.execute("insert into driver values ('john@gmail.com',3456,'Bangalore','john',1234567890,1),('hemsworth@gmail.com',1234,'Delhi','hemsworth',2345678901,3),('khan@gmail.com',9874,'Mumbai','khan',1234567899,4),('ram@gmail.com',8678,'Mumbai','ram',4321567890,4),('shyam@gmail.com',1249,'Delhi','shyam',1276549890,3)")
# c.execute("insert into vehicle values ((1,'KA01ML3689','sedan', 'john@gmail.com'),(2,'MH01HQ6789','sedan', 'khan@gmail.com'),(3,'DL01ML1239','mini', 'hemsworth@gmail.com'),(4,'MH01HQ1234','SUV', 'ram@gmail.com'),(5,'DL51RL4567','sedan', 'shyam@gmail.com'))")
# insert into trip values ('101','hsr','jayanagar','1','thor@gmail.com'),('102','agara','hebal','1','thor@gmail.com'),('103','navi','bandra','2','robert@gmail.com'),('104','juhu','bandra','2','robert@gmail.com'),('105','CP','rajpath','5','wanda@gmail.com')

mydb.commit()