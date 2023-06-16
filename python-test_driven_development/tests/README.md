# Testing Python Functions in Interactive Mode

Testing your Python functions in interactive mode is a great way to see the output in real time and to quickly understand how your code behaves under different conditions. This guide will walk you through the steps to interactively test a Python function and document your findings.

**1 - Start Python Interactive Mode**

First, open your terminal and start Python's interactive mode by typing `python` or `python3` (depending on your Python installation). You should see the Python version and the `>>>` prompt.

```python
$ python3
 >>>
```

**2 - Import the Function to be Tested**

Next, import the function that you want to test. In this guide, we will test the `add_integer` function from the `0-add_integer` module.

```python
>>> add_integer = __import__('0-add_integer').add_integer
>>>
```


**3 - Test the Function with Valid Arguments**

Test the function with valid arguments and observe the output. For example:
    
    
```python
>>> add_integer(1, 2)
3
```


**4 - Test Edge Cases**

Test how the function handles edge cases, such as incorrect input types. Document the behavior of the function when it receives such input. For instance:

```python
>>> add_integer(None, 2)
Traceback (most recent call last):
...
TypeError: a must be an integer`
```
**5 - Document the Testing Process and Results**

As you test the function and its edge cases, document the process and the results. You can use this template as a starting point:

```markdown

`The ``0-add_integer`` module
======================

Using ``add_integer``
-------------------

**1 argument**
>>> add_integer(1)
99

**2 floats**
>>> add_integer(3.6, 2.4)
5

**str input(b)**
>>> add_integer(4, 'str')
Traceback (most recent call last):
...
TypeError: b must be an integer

**None input**
>>> add_integer(None, 2)
Traceback (most recent call last):
...
TypeError: a must be an integer

**No input**
>>> add_integer()
Traceback (most recent call last):
...
TypeError: add_integer() missing 1 required positional argument: 'a'` 
```

Remember to test and document all possible edge cases a user might encounter when using the function. This includes invalid input types and special floating-point values like NaN and infinity. By including these in the documentation, you help users avoid potential issues and understand how the function behaves under different conditions.
