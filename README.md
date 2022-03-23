## Pytest
* It is testing framework for Python.
* It helps you to write simple and scalable test cases for databases, APIs, or UI. PyTest is mainly used for writing tests for APIs


## Why use PyTest?
* Very easy to start with because of its simple and easy syntax.
* Can run tests in parallel.
* Can run a specific test or a subset of tests
* Automatically detect tests
* Skip tests
* Open source

How to install PyTest
```bash
pip install pytest
```

pytest will run all files from the current and sub directories that end and start with test_*.py or *_test.py

let's start our first pytest test

```python
def test_1():
    x = 10
    y= 20
    assert x==y
```
It will fail because x is not equal to y

```bash
==================================== test session starts ====================================
platform win32 -- Python 3.8.10, pytest-7.1.1, pluggy-1.0.0
rootdir: C:\Users\Rajansahu\Desktop\pytest
collected 1 item

test_first.py F                                                                        [100%]

========================================= FAILURES ========================================== 
__________________________________________ test_1 ___________________________________________ 

    def test_1():
        x = 10
        y= 20
>       assert x==y
E       assert 10 == 20

test_first.py:4: AssertionError
================================== short test summary info ================================== 
FAILED test_first.py::test_1 - assert 10 == 20
===================================== 1 failed in 0.16s ===================================== 
```

we can provide a message to the user if the test fails

```python
def test_1():
    x = 10
    y= 20
    assert x==y, "x is not equal to y"
```
```
==================================================================== test session starts =====================================================================
platform win32 -- Python 3.8.10, pytest-7.1.1, pluggy-1.0.0
rootdir: C:\Users\Rajansahu\Desktop\pytest
collected 1 item

test_first.py F                                                                                                                                         [100%]

========================================================================== FAILURES ========================================================================== 
___________________________________________________________________________ test_1 ___________________________________________________________________________ 

    def test_1():
        x = 10
        y= 20
>       assert x==y,"x is not equal to y"
E       AssertionError: x is not equal to y
E       assert 10 == 20

test_first.py:4: AssertionError
================================================================== short test summary info =================================================================== 
FAILED test_first.py::test_1 - AssertionError: x is not equal to y
===================================================================== 1 failed in 0.14s ====================================================================== 
```
If it passes then it will print this

```python
def test_1():
    x = 10
    y= 10
    assert x==y, "x is not equal to y"
```
```bash
==================================================================== test session starts =====================================================================
platform win32 -- Python 3.8.10, pytest-7.1.1, pluggy-1.0.0
rootdir: C:\Users\Rajansahu\Desktop\pytest
collected 1 item

test_first.py .                                                                                                                                         [100%] 

===================================================================== 1 passed in 0.03s ====================================================================== 
```

pytest flags
```bash
pytest --version   # shows where pytest was imported from
pytest --fixtures  # show available builtin function arguments
pytest -h | --help # show help on command line and config file options
pytest -x           # stop after first failure
pytest --maxfail=2  # stop after two failures
pytest test_mod.py # run only tests in test_mod.py
pytest testing/ # run all tests in testing/

```
If you wanted to get the summary about the test cases
```bash
pytest test_first.py -rA
```

```bash
========================================== PASSES =========================================== 
================================== short test summary info ================================== 
PASSED test_first.py::test_1
PASSED test_first.py::test_2
PASSED test_first.py::test_3
===================================== 3 passed in 0.03s ===================================== 
```

if you wanted to run particular method in a file used
```bash
pytest test_first.py -rA -k test_1 
```
```bash
========================================== PASSES =========================================== 
================================== short test summary info ================================== 
PASSED test_first.py::test_1
============================== 1 passed, 2 deselected in 0.03s ============================== 
```

Marking test function

* Here are some of the builtin markers:
    * usefixtures - use fixtures on a test function or class
    * filterwarnings - filter certain warnings of a test function
    * skip - always skip a test function
    * skipif - skip a test function if a certain condition is met
    * xfail - produce an “expected failure” outcome if a certain condition is met
    * parametrize - perform multiple calls to the same test function.

You can also create your own markers by using the @pytest.mark.marker decorator.

but when you run this marker you will get warnings messages to avoid the warning messages you need to register the marker

## Registering marks
create a file with pytest.ini
inside the file write 
```python
[pytest]
markers =
    your_marker: your_marker_function
```

```python
import pytest

@pytest.mark.custom_marker_1
def test_1():
    print("test_1")

@pytest.mark.custom_marker_2
def test_2():
    print("test_2")

@pytest.mark.custom_marker_1
def test_3():
    print("test_3")
```

pytest.ini
```
[pytest]
markers=   
    custom_marker_1: custom_marker_1_description
    custom_marker_2: custom_marker_2_description
```

if you wanted to run particular marker the use
```bash
pytest -m custom_marker_1
```

```
pytest -m "custom_marker_1 or custom_marker_2"
```


