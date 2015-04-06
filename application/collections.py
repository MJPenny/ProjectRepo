from application import db

class User(db.Document):
    email = db.EmailField(required=True)
    alias = db.StringField(required=True)
    password = db.StringField(required=True)
    emailVerified = db.BooleanField(default=False)
    lastLogin = db.DateTimeField()
    allowTracking = db.BooleanField(default=False)
    isMod = db.BooleanField(default=False)

class Posts(db.Document):
    #max length of title is 140 characters
    title = db.StringField(required=True, max_length=140)
    author= db.ReferenceField(User)
    #max length of content is 10000 characters
    content= db.StringField(max_length=10000)
    score = db.IntField(default=0)

class Following(db.Document):
    user = db.ReferenceField(User)
    following = db.ListField(db.ReferenceField(User))

class Kicked(db.Document):
    #stores temporary locks on user accounts
    user = db.ReferenceField(User)
    ends = db.DateTimeField(required=True)
    reason = db.StringField(max_length=1000)

class Banned(db.Document):
    #stores emails of people who are not allowed to make accounts
    email = db.EmailField(required=True)
    reason = db.StringField(max_length=1000)
