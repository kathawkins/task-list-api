from app import db
from flask import make_response, abort

#A task can have MANY goals
class Goal(db.Model):
    goal_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)

    def to_dict(self):
        goal_as_dict = {}
        goal_as_dict["id"] = self.goal_id
        goal_as_dict["title"] = self.title
        return goal_as_dict

    @classmethod
    def instance_from_json(cls, task_req_body):
        try:
            new_goal = Goal(title=task_req_body["title"])
            return new_goal

        except KeyError:
            abort(make_response({"details": "Invalid data"}, 400))

    def update(self, req_body):
        try:
            self.title = req_body["title"]
        except KeyError as error:
            abort(make_response({"message": f"Missing attribute: {error}"}, 400))