import database1
# database1.add_one('karan','khurana','karan.khurana@gmail.com')
# database1.show_all()
# database1.delete_one('10')
database1.show_all()
stuff=[
     ('new','new','new@new.com'),
     ('old','old','old@old.com'),
     ('middle','middle','middle@middle.com')
    ]
database1.add_many(stuff)
# database1.email_lookup('new@new.com')
database1.show_all()