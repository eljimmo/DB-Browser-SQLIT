# DB-Browser-SQ LIT BECAUSE DATA IS LIT

--- lots of ways to clean data, but generally you want to do it before extraction to DB to make it easier. ----
---- We can also use Python Scripts to clean & parse data for extraction. ------- 


Basic Steps for SQL DB browser, cleaning of data and parsing, creation of data tables, etc... 

- after creating your table, SQL is basically just that, Structured Query Langauge, it is incredible easy to use as well. 


below is the data we inserted, our data at this point will be the columns, we need to keep this script handy because thats how it will recognize
the langauge commands for inserted values into these parameters.

###*insert into facts (facts being the name of our table, the rest is the values. remember you may need to clean the data if you copy and paste
###*meaning you cannot have empty spaces or " / " but you can replace with a " _ " )

insert into facts
(
Country,
Area_sq_km,
BirthRate_births_1000,
CurrentAccountBal,
DeathRate_deaths_1000,
Debt_external,
Electricity_consumption_kWh
)

###*The syntax to add values is: values("first column row, second column row, third column row, etc... 
###*remember that only STRINGS and EMPTY ROW VALUES NNED TO BE IN '' all numerical data types will be plaintext)

values ('Azerbaijan',86600,20.40,-2899000000,9.86,1832000000,17370000000)



here we are using default configuration DB Browser for SQLite 

Execute (run)

Remember to "write" like in vim for changes to be saved.


Remember Power Query in Excel

######-------####

-> 21 Revenue Limited (notice the syntax)

Table.TransformColumnTypes(#"Promoted Headers",{{"Date", type date}, {" Revenue ", Currency.Type}, {"Freight Remit", type text}, {"QuickPay/Factoring", type text}, {"Brokerage", type text}, {"Load #", type text}, 

https://docs.python.org/3/library/sqlite3.html

import sqlite3
con = sqlite3.connect('example.db')

;) 
