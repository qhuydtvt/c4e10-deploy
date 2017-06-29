import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds131492.mlab.com:31492/haihoa

host = "ds131492.mlab.com"
port = 31492
db_name = "haihoa"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())