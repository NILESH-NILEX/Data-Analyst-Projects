import pandas as pd 
print(pd.__version__)
df1 = pd.read_csv('C:\\Users\\PF4GM\\OneDrive\\Desktop\\RE.Hotel.Data\\HotelRe.data\\dim_date.csv')
print(df1)

print(df1.isnull().sum())


df1.to_csv('C:\\Users\\PF4GM\\OneDrive\\Desktop\\RE.Hotel.Data\\HotelRe.data\\dim_date.csv',index=False,na_rep='NULL')
print(df1)

print(df1.isnull().sum())

print(df1.duplicated().sum())

df1['date'] = pd.to_datetime(df1['date'], format="%d-%b-%y")
print(df1)


df2 = pd.read_csv('C:\\Users\\PF4GM\\OneDrive\\Desktop\\RE.Hotel.Data\\HotelRe.data\\dim_hotels.csv')
print(df2)

print(df2.isnull().sum())

print(df2.duplicated().sum())


df3 = pd.read_csv('C:\\Users\\PF4GM\\OneDrive\\Desktop\\RE.Hotel.Data\\HotelRe.data\\dim_rooms.csv')
print(df3)

print(df3.isnull().sum())

print(df3.duplicated().sum())

df4 = pd.read_csv('C:\\Users\\PF4GM\\OneDrive\\Desktop\\RE.Hotel.Data\\HotelRe.data\\fact_aggregated_bookings.csv')
print(df4)


print(df4.isnull().sum())

print(df4.duplicated().sum())

df4['check_in_date'] = pd.to_datetime(df4['check_in_date'], format="%d-%b-%y")
print(df4)


df5 = pd.read_csv('C:\\Users\\PF4GM\\OneDrive\\Desktop\\RE.Hotel.Data\\HotelRe.data\\fact_bookings.csv')
print(df5)



print(df4.isnull().sum())

print(df4.duplicated().sum())


print(df5['ratings_given'].median())

df5['ratings_given'] = df5['ratings_given'].fillna(df5['ratings_given'].median())
print(df5)




import socket
socket.getaddrinfo('localhost',8080)



from sqlalchemy import create_engine



engine = create_engine("mysql+pymysql://{user}:{pw}@localhost:3306/{db}".format(user="root",pw="NILESHPYTHON.",db = "powerbi_db"))


df1.to_sql(con=engine,name="dim_date",index=False,if_exists='replace')

df2.to_sql(con=engine,name="dim_hotels",index=False,if_exists='replace')

df3.to_sql(con=engine,name="dim_rooms",index=False,if_exists='replace')


df4.to_sql(con=engine,name="fact_aggregated_bookings",index=False,if_exists='replace')

df5.to_sql(con=engine,name="fact_bookings",index=False,if_exists='replace')