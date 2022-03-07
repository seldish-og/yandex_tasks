from flask import Flask
from data import db_session
from data.users import User


def main(name):
    global_init(f"{name}")
    db_sess = create_session()
    for user in db_sess.query(User).filter(User.address == "module_1").all():
        print(user)


if __name__ == '__main__':
    name_db = input()
    main(name_db)
