from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='mcni',
      version='0.1',
      description='A library built by the NI Raspberry Jam team that extends the Minecraft Pi Edition MCPI library to add additional functions for use at the Jam.',
      url='https://github.com/NIRaspberryJam/MCNI',
      maintainer='Northern Ireland Raspberry Jam',
      maintainer_email='gbaman@users.noreply.github.com',
      author='Jack Delaney',
      author_email='gbaman@users.noreply.github.com',
      license='MIT',
      py_modules=['mcni'],
      zip_safe=False,
      long_description=long_description,
      long_description_content_type="text/markdown",
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
)
