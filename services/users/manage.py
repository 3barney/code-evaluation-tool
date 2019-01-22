from flask.cli import FlaskGroup

from project import app

# instantiate the app
cli = FlaskGroup(app)

# Load  and Set config
app.config.from_object('project.config.DevelopmentConfig')

if __name__ == '__main__':
  cli()