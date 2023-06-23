import confuse

config = confuse.Configuration('myapp', __name__)
config.set_file('config.yaml')