---
title: "Sopel tutorial, Part 4: The .help command"
migrated: true
source: wiki
previously:
  - /tutorials/part-5-the-help-command/
---

**NOTE: This guide is for Sopel 6.0+. If you are still using a version named
"Willie", we strongly encourage you to upgrade, as such old versions are no
longer supported.**

Sopel has a built in `.help` command that can be used to get information about a
particular command. You can add information to `.help` about your command in two
basic ways. The first is to add a docstring and the second is to add an example
usage with the ```@example``` decorator. Take the following plugin for example:

```py
@sopel.module.commands('hello')
def helloworld(bot, trigger):
    bot.say('Hello, %s!' % (trigger.group(2),))
```

It has no docstring or example so saying `.help hello` will do nothing. If the
program is modified to include either of them like so:

```py
@sopel.module.commands('hello')
@sopel.module.example('.hello world', 'Hello, world!')
def helloworld(bot, trigger):
    """Replies with what ever the first parameter is."""
    bot.say('Hello, %s!' % (trigger.group(2),))
```

Then we might get the following output:

    User> .help hello
    Sopel> User: Replies with what ever the first parameter is.
    Sopel> e.g. .hello world

## Unit tests with the `@example` decorator

The second parameter of `@example` is optional and provides a way of
documenting what the expected output is. If you do add the expected output
however, Sopel will automatically make unit-tests to check that the example
output is what really results from calling the command with the example input.

To run the unit tests and see the results you must have pytest installed and run
`pytest_run.py` in Sopel's directory. You should see something like the following:

    C:\Users\Venti\workspace2\sopel>python pytest_run.py
    ============================= test session starts =============================
    platform win32 -- Python 2.7.5 -- pytest-2.3.5
    collected 27 items / 12 errors
    
    sopel/modules/calc.py .FF.
    sopel/modules/dice.py .......
    sopel/modules/exampletest.py .
    sopel/modules/rand.py .....
    sopel/modules/units.py .........
    sopel/modules/url.py .
    =================================== ERRORS ====================================
    (stuff removed for brevity)
    ================ 2 failed, 25 passed, 12 error in 4.63 seconds ================

You can also run the unit tests of your plugin directly by appending the
following to the end of your plugin:

```py
if __name__ == "__main__":
    from sopel.test_tools import run_example_tests
    run_example_tests(__file__)
```

Now if you run the the plugin directly in your IDE or in command line, you
should get something like the following:

    C:\Users\Venti\workspace2\sopel>set PYTHONPATH=C:\Users\Venti\workspace2\sopel
    C:\Users\Venti\workspace2\sopel>python sopel\modules\exampletest.py
    ============================= test session starts ==============================
    platform win32 -- Python 2.7.5 -- pytest-2.3.5
    collected 1 items
    
    exampletest.py .
    
    =========================== 1 passed in 0.01 seconds ===========================

Although only the first example will be added to the .help command, as many
`@example` decorators as needed can be added for unit tests. This can be quite
useful when making changes or adding new features.

We could for example add a test for the edge condition of calling `.hello` with
no arguments:

```py
@sopel.module.example('.hello', 'Hello, !')
```

And then we can rerun the tests without restarting Sopel or even reloading the
plugin, instantly seeing the difference between expectation and reality:

    ============================= test session starts ==============================
    platform win32 -- Python 2.7.5 -- pytest-2.3.5
    collected 2 items
    
    exampletest.py F.
    
    =================================== FAILURES ===================================
    __________________________ test_example_helloworld_0 ___________________________
    Traceback (most recent call last):
      File "C:\Users\Venti\workspace2\sopel\sopel\test_tools.py", line 112, in test
        assert result == output
    AssertionError: assert 'Hello, !' == 'Hello, None!'
      - Hello, !
      + Hello, None!
      ?        ++++
    ====================== 1 failed, 1 passed in 0.03 seconds ======================

## Using regular expressions with the `@example` decorator

TODO

Want to distribute your plugin as a package on [PyPI](https://pypi.org/)?
[Continue to part 5!]({% link _tutorials/part-5-packaging-and-distributing-plugins.md %})
