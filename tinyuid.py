from uuid import uuid4

def uuid():
    uid = uuid4()
    uid = str(uid).split("-")
    uid = uid[0]
    return uid
