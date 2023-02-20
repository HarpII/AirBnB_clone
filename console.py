#!/usr/bin/python3
"""
Module - console
command interpreter
"""
import cmd
import re
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Entry to command interpreter
    """
    prompt = '(hbnb) '
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "City": City,
        "State": State,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_EOF(self, line):
        """ End of file command to interrupt the console \n"""
        return True

    def do_quit(self, line):
        """ Quit command to exit program \n"""
        return True

    def emptyline(self):
        """ Overwrite default emptyline method """
        pass

    def do_create(self, line):
        """
        Creates an instance of the class
        BaseModel and it's Subclasses \n
        """
        if len(line) == 0:
            print("** class name missing **")
        elif line not in self.classes.keys():
            print("** class doesn't exist **")
        else:
            instance = eval(line)()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """
        Shows an instance given
        the class name and id

        :param line:
        :return: \n
        """
        args = parse(line)
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        else:
            key = "{}.{}".format(args[0], args[1])
            obj_dict = storage.all()[key]
            print(obj_dict)

    def do_destroy(self, line):
        """
        Destroys an instance given the class name
        and id

        :param line:
        :return: \n
        """
        args = parse(line)
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        else:
            key = "{}.{}".format(args[0], args[1])
            del storage.all()[key]
            storage.save()

    def do_all(self, line):
        """
        prints all instances of a Class or
        subclass

        :param line:
        :return: \n
        """
        args = parse(line)
        obj_list = []
        if len(line) == 0:
            for obj in storage.all().values():
                obj_list.append(str(obj))
            print(obj_list)
        elif args[0] in self.classes.keys():
            for key, obj in storage.all().items():
                if args[0] in key:
                    obj_list.append(str(obj))
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Update an attribute of an instance
        given the class name, id, attribute name
        and attribute value

        :param line:
        :return:\n
        """
        args = parse(line)
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            cast = type(args[3])
            attrib_value = cast(args[3])
            setattr(storage.all()[key], args[2], attrib_value)
            storage.all()[key].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")

    def do_count(self, line):
        """
        count the number of a Class
        Usage: Class.count()

        Args:
            line \n
        """
        if line in self.classes:
            count = 0
            for key in storage.all().keys():
                if line in key:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")

    def default(self, line):
        args = parse(line)
        class_arg = (args[0].split("."))[0]
        command = ((args[0].split(".")[1]).split("("))[0]
        id_arg = (((args[0].split(".")[1]).split("("))[1]).strip(")")
        if len(args) == 1:
            print("*** Unknown syntax {}".format(line))
            return
        try:
            if command == 'all':
                HBNBCommand.do_all(self, class_arg)
            elif command == 'count':
                HBNBCommand.do_count(self, class_arg)
            elif command == 'show':
                arg = class_arg + ' ' + id_arg
                HBNBCommand.do_show(self, arg)
            elif command == 'destroy':
                arg = class_arg + ' ' + id_arg
                HBNBCommand.do_destroy(self, arg)
            elif command == 'update':
                name_arg = args[1]
                val_arg = args[2].strip(")")
                arg = class_arg + ' ' + id_arg + ' ' + name_arg + ' ' + val_arg
                HBNBCommand.do_update(self, arg)
            else:
                print("*** Unknown syntax {}".format(line))
        except IndexError:
            print("*** Unknown syntax {}".format(line))

def parse(arg):
    """
    Helper function to parse
    arguments
    Args:
        arg\n
    """
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


if __name__ == '__main__':
    HBNBCommand().cmdloop()
