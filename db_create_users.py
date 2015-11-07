from project import db
from project.models import User

# insert data
db.session.add(User("pdelboca", "pdelboca@mail.com", "pdelboca"))
db.session.add(User("admin", "admin@mail.com", "admin"))
db.session.commit()