from .interface import interface_call

def db_create(dbname, dbuser, dbpassword, dhost='localhost'):
    print("TODO: remove archived install mysql database")
    return True

def db_delete(dbname, dbuser, dbpassword, dhost='localhost'):
    print("TODO: remove archived install mysql database")
    return True

def db_permission(database, sitename, mode="W"):
    if mode == "N":
        path = "/dbs/permissions.html?set_none=" + sitename + "&db=" + database
    elif mode == "R":
        path = "/dbs/permissions.html?set_read=" + sitename + "&db=" + database
    else:
        path = "/dbs/permissions.html?set_write=" + sitename + "&db=" + database

    interface_call(path=path)