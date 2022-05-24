from setuptools import setup
import os

def open_file(fname):
   return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
   name="snake_game",            # name of your package
   version="0.0.1",
   description="a terminal based snake game",
   long_description=open_file("README.md"),  # only if you have a README.md
   author="Spiced Academy",
   author_email="foo@bar.com",
   packages=["snake"],      # same as name
   url="https://github.com/RosiNantis/snake_game",
   license="MIT",
   classifiers=[
      "Programming Language :: Python :: 3.8",
   ]
)