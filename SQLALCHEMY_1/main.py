import re
from flask import Flask, render_template
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    db_session.global_init(f"db/blocks.db")
    db_sess = db_session.create_session()
    colonists = db_sess.query(User).all()

    return render_template("journal.html", title="Журнал работ", colonists=colonists)


if __name__ == '__main__':
    app.run()

# def main(name):
#     db_session.global_init(f"db/{name}")
#     db_sess = db_session.create_session()
#     # `app.run()

#     user = User()
#     user.name = "Ridley"
#     user.surname = "Scott"
#     user.age = 21
#     user.position = "captain"
#     user.speciality = "research engineer"
#     user.address = "module_1"
#     user.email = "scott_chief@mars.org"
#     db_sess = db_session.create_session()
#     db_sess.add(user)

#     user2 = User()
#     user2.name = "Weir"
#     user2.surname = "Andy"
#     user2.age = 21
#     user2.position = "captain1"
#     user2.speciality = "research engineer"
#     user2.address = "module_2"
#     user2.email = "scott_chief@mars.org"
#     db_sess = db_session.create_session()
#     db_sess.add(user2)

#     user3 = User()
#     user3.name = "Ridley23"
#     user3.surname = "Scott23"
#     user3.age = 23
#     user3.position = "captain23"
#     user3.speciality = "research engineer23"
#     user3.address = "module_123"
#     user3.email = "scott23_chief@mars.org"
#     db_sess = db_session.create_session()
#     db_sess.add(user3)

#     user4 = User()
#     user4.name = "Bean"
#     user4.surname = "Sean"
#     user4.age = 23
#     user4.position = "captain4"
#     user4.speciality = "research engineer"
#     user4.address = "module_1"
#     user4.email = "scott_chief@mars.org"
#     db_sess = db_session.create_session()
#     db_sess.add(user4)

#     db_sess.commit()
#     for user in db_sess.query(User).filter(User.address == "module_1").all():
#         print(user)


# if __name__ == '__main__':
#     name_db = input()
#     main(name_db)
