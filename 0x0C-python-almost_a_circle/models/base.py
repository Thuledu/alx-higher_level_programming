#!/usr/bin/python3
import turtle
import json
import csv

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as jsonfile:
            list_dicts = [o.to_dictionary() for o in list_objs] if list_objs else []
            jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        if not json_string or json_string == "[]":
            return []
        return json.loads(json_string)
		
	@classmethod
    def create(cls, **dictionary):
        init_params = {
            "Rectangle": (1, 1),
            "Square": (1,),
        }
        if dictionary and dictionary != {}:
            new = cls(*init_params.get(cls.__name__))
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
            except IOError:
                return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as csvfile:
            fieldnames = ["id", "width", "height", "x", "y"] if cls.__name__ == "Rectangle" else ["id", "size", "x", "y"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if list_objs:
                writer.writerows([obj.to_dictionary() for obj in list_objs])

    @classmethod
    def load_from_file_csv(cls):
        filename = f"{cls.__name__}.csv"
        try:
		     with open(filename, "r", newline="") as csvfile:
                fieldnames = ["id", "width", "height", "x", "y"] if cls.__name__ == "Rectangle" else ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items()) for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(cls, list_rectangles, list_squares):
    pen = turtle.Turtle()
    
    figures = list_rectangles + list_squares
    
    for fig in figures:
        pen.up()
        pen.goto(fig.x, fig.y)
        pen.down()
        
        for _ in range(2):
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)
        
    turtle.done()
