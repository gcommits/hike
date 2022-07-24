from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Trail:
    db = 'hiking_app'
    def __init__(self, data):
        self.id = data['id']
        self.img = data['img']
        self.name = data['name']
        self.location = data['location']
        self.difficulty = data['difficulty']
        self.rating = data['rating']
        self.dateCompleted = data['dateCompleted']
        self.elevationGain = data['elevationGain']
        self.length = data['length']
        self.routeType = data['routeType']
        self.comments = data['comments']
        self.user_id = data['user_id']

    @classmethod
    def getAll(cls):
        query = "SELECT * FROM trail;"
        results = connectToMySQL(cls.db).query_db(query)
        alltrails = []
        for row in results:
            alltrails.append(cls(row))
        return alltrails

    @classmethod
    def getOne(cls,data):
        query = "SELECT * FROM trail WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def update(cls,data):
        query = 'UPDATE trail SET img=%(img)s, name=%(name)s, location=%(location)s, difficulty=%(difficulty)s, rating=%(rating)s, dateCompleted=%(dateCompleted)s, elevationGain=%(elevationGain)s, length=%(length)s, routeType=%(routeType)s, comments=%(comments)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM trail WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def save(cls,data):
        query = 'INSERT INTO trail (img, name, location, difficulty, rating, dateCompleted, elevationGain, length, routeType, comments, user_id) VALUES (%(img)s, %(name)s, %(location)s, %(difficulty)s, %(rating)s, %(dateCompleted)s, %(elevationGain)s, %(length)s, %(routeType)s, %(comments)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate(trail):
        isValid = True
        if len(trail['name']) < 3:
            isValid = False
            flash("Trail name must be at least 3 characters", "trail")
        if len(trail['location']) < 3:
            isValid = False
            flash("Trail location must be at least 3 characters", "trail")
        if len(trail['difficulty']) < 1:
            isValid = False
            flash("Please choose a trail difficulty", "trail")
        if len(trail['rating']) < 1:
            isValid = False
            flash("Please rate this trail", "trail")
        if len(trail['routeType']) < 1:
            isValid = False
            flash("Please specify the route type", "trail")

        return isValid


    

        