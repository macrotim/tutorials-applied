from flask.ext.script import Command, Manager, Option, Shell, prompt_bool

from app import app, db
import model

manager = Manager(app)

@manager.command
def hello(name="Tim"):
    print "hello %s via @manager.command" % name

class Hello(Command):
    """Prints hello world"""

    option_list = (
        Option('--name', '-n', dest='name'),
    )

    def run(self, name):
        print "Hello %s via class Hello" % name

manager.add_command('hello2', Hello())

@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to lose all your data"):
        print "Replace with db.drop_all()"

def _make_context():
    return dict(app=app, db=db, model=model)

manager.add_command("shell", Shell(make_context=_make_context))

if __name__ == "__main__":
    manager.run()
