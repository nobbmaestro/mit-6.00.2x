# Getting Started

Download and save

[pset2.zip](https://courses.edx.org/assets/courseware/v1/08474dca92f419fd79431242447f6230/asset-v1:MITx+6.00.2x+1T2021+type@asset+block/pset2.zip): A zip file of all the files you need, including:

- ps2.py, a skeleton of the solution.
- ps2_visualize.py, code to help you visualize the robot's movement (an optional - but cool! - part of this problem set).
- ps2_verify_movement35.pyc, precompiled module for Python 3.5 that assists with the visualization code. In ps2.py you will uncomment this out if you have Python 3.5.
- ps2_verify_movement36.pyc, precompiled module for Python 3.6 that assists with the visualization code. In ps2.py you will uncomment this out if you have Python 3.6.
- ps2_verify_movement37.pyc, precompiled module for Python 3.7 that assists with the visualization code. In ps2.py you will uncomment this out if you have Python 3.7.

## REVIEW OBJECT ORIENTED PROGRAMMING AND CLASSES

This and future problem sets will require you to know OOP. If you need a refresher, please visit this link and make sure you are familiar with these topics.

- Implementing new classes and their attributes.
- Understanding class methods.
- Understanding inheritance.
- Telling the difference between a class and an instance of that class - recall that a class is a blueprint of an object, whilst an instance is a single, unique unit of a class.
- Utilizing libraries as black boxes.

**Note**: If you want to use numpy arrays, you should add the following lines at the beginning of your code for the grader:

```python
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
```

Then, do import numpy as np and use np.METHOD_NAME in your code.
