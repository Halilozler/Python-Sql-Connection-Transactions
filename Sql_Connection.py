import pyodbc

def sql_connection():
    """
    DRIVER:
        for drivers in pyodbc.drivers():
            print(drivers)
        Komutu ile yazan driver adlarından biridir. Genelde üçünden biri olur:
        {SQL Server}
        {SQL Server Native Client 11.0}
        {ODBC Driver 17 for SQL Server}

    SERVER:
        Serverimizin ismi.

    DATABASE:
        Erişmek istediğimiz veritabanı.

    Trusted_Connection=yes
        Eğer serverimizin erişiminde şifre yok ise direk bağlanmamızı sağlar

    Eğer kullanıcı adı ve şifremiz var ise:
    UID=kullanıcı_adı;
    PWD=şifre;

    """
    driver = "{ODBC Driver 17 for SQL Server}"
    server = "server_name"
    database = "Animals"

    connection = pyodbc.connect(
        f'DRIVER={driver}; SERVER={server}; DATABASE={database}; Trusted_Connection=yes'
    )

    cursor = connection.cursor()
    return cursor
