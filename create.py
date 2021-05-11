from apppysql import db, users

db.drop_all()
db.create_all()

testuser = users(first_name='Grooty',last_name='Toot') # Extra: this section populates the table with an example entry
db.session.add(testuser)
db.session.commit()