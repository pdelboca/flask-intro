from project import db
from project.models import BlogPost

# create the database and the db tables based on models.py
db.create_all()

# insert
db.session.add(BlogPost("Good", "I\'m good.",2))
db.session.add(BlogPost("Well", "I\'m well.",2))
db.session.add(BlogPost("Flask", "discoverflask.com",2))
db.session.add(BlogPost("postgres", "we setup a local postgres instance",2))


# commit the changes
db.session.commit()