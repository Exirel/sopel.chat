---
title: "Sopel tutorial, Part 1: Introduction to writing plugins"
migrated: true
source: wiki
previously:
  - /tutorials/part-2-writing-modules/
  - /tutorials/part-1-writing-modules/
---

**NOTE: This guide is for Sopel 6.0+. If you are still using a version named
"Willie", we strongly encourage you to upgrade, as such old versions are no
longer supported.**

This tutorial is intended to give you an overview of all the features Sopel
has to offer. In this part, we'll make a simple "Hello, world!"" complete with
proper documentation. If you don't already have Sopel up and running, consult
the [installation guide]({% link _usage/installing.md %}). (We assume you are
running version 6.0 or higher of Sopel. You can find this by giving Sopel the
`.version` command.)

Sopel's tutorials require at least *some* familiarity with programming. You
should know the basics of what functions are and stuff like that. Since Sopel
is written in Python, knowing Python will help—but if you've worked pretty
much any other language(s) you should be able to infer enough from the
examples to get things done.

While this guide does cover a lot of what is available, there is much more than
can be described here. The API documentation is available [online]({{ site.docs }}),
and serves as a useful reference.

Now it's time to start writing your own plugins!

## Hello, World!

It's not a programming tutorial without a "Hello, world". We start by editing a
file in `~/.sopel/modules`. If you've run Sopel already, this folder should
already exist. Sopel will find plugins in here by default, but you can add
other folders for it to look in by modifying your config file.

A "Hello, world" command is very simple in Sopel. In the folder I mentioned
above, make a file called `helloworld.py`. In it, put the following and save:

```python
import sopel.module

@sopel.module.commands('helloworld')
def helloworld(bot, trigger):
    bot.say('Hello, world!')
```

The first line imports the `sopel.module` library. In this plugin, we only
really need this for the next line. This is called a decorator, and associates
the command "helloworld" with the function that comes right after it. A command
in Sopel is triggered when a line said in a channel starts with a period,
followed by the command (the prefix can be changed in the config file).

The next line defines a function, which takes two arguments. This is the
signature you'll see in nearly every function in Sopel plugins. The first
argument is usually called `bot`, and it represents the Sopel instance you're
running. It includes functions like `msg` and `say`, which we used above, that
make the bot interact with the IRC network. It also includes access to the
database and configuration, which will be discussed later. The second argument
is usually called `trigger`, and gives you access to information about the line
which "triggered" the "callable", which is what we call the functions that the
bot can call.

The last line does exactly as you'd expect; it says "Hello, world!" in the
channel where the command was triggered. In other words, if someone says
`.helloworld`, Sopel will say `Hello, world!`.

Let's take a look at another short example:

```python
from sopel import module

@module.commands('echo', 'repeat')
def echo(bot, trigger):
    bot.reply(trigger.group(2))
```

There are a few new concepts here. One is that I've imported the decorator a
bit differently. This is pretty standard in Python. You could also do
`from sopel.module import commands`, and then just do `@commands` for the
decorator. They all work the same way. I've also given it two arguments. As you
might expect, this means it'll respond to either `.echo` or `.repeat`.

The next new thing is `sopel.reply`. This is the same as `.say`, but it puts
the name of the person who triggered it at the beginning. Next, we have
`trigger.group(2)`. We'll go more into groups in the next section, but for now
you just need to know that, for commands like this, group 1 is the command
(`echo` or `repeat` in this case), and group 2 is everything after it.

So if I say `.echo Spam and eggs` or `.repeat Spam and eggs`, Sopel will
respond `Embolalia, Spam and eggs`.

## Regex Rules

Regular expressions, or regexes, are incredibly powerful tools for matching
patterns in text. I'll explain the regexes I use in this section, but you
should probably check out a quick guide to them before continuing.
[This page](http://www.regular-expressions.info/quickstart.html) gives you a
good quick overview, and the same site has a
[reference sheet](http://www.regular-expressions.info/reference.html) which
comes in handy. [This site](http://www.gskinner.com/RegExr/) has a tool to
test regexes, and show you what's matching which part of the pattern.

To make a callable trigger on a rule, use the `@sopel.module.rule` decorator.
It takes a string with a regex in it, and matches that against the lines it
sees. Here's an example:

```python
from sopel import module

@module.rule('hello!?')
def hi(bot, trigger):
    bot.say('Hi, ' + trigger.nick)
```

The rule, `hello!?`, matches the word "hello", possibly followed by an 
exclaimation point. So if someone says either "hello" or "hello!", this
rule will match, and this function will be called. Sopel will then say
`Hi, Embolalia`, where "Embolalia" is the nickname of whoever triggered the
callable ( `trigger.nick` gives you the triggerer's nickname).

A trick you might want to keep in mind is Python's "raw strings". As you'll
shortly find, regular expressions contain quite a few backslashes, which can
sometimes lead to unexpected results. Putting the letter `r` before a string
means Python interprets that string exactly as it looks. So the string `r'\n'`,
for example, is actually a backslash and then an n, and not a newline character.

### Nickname commands

Another decorator that takes rules, `@sopel.module.nickname_command`, is
provided for convenience. This is basically the same as a regular rule, but it
prefixes it with the name of the bot, followed by either a comma or a colon.

So, for example, if the above command had instead had the decorator
`@module.nickname_command('hello!?')`, and if the bot were running with the
nickname "Sopel", it would have matched on `Sopel, hello`, `Sopel: hello!`,
etc.

### Regex groups

Using groups in your regular expressions is very helpful. For example, if you
wanted to match a [NANP](https://en.wikipedia.org/wiki/North_American_Numbering_Plan)
phone number, you could use the regular expression 
`\D?(\d{3})\s?\D(\d{3})\D(\d{4})`. Going through this piece by piece, we have
`\D` (which matches anything that isn't a digit 0-9) followed by a question
mark (which makes it optional). Then we have a group which matches exactly
three digits (`\d` is any digit 0-9, and `{3}` means to repeat the previous
thing three times). Then we have `\s`, which matches any space character,
followed by a question mark to make it optional. Then another non-digit,
another 3 digits, another non-digit, and then another four digits. This is a
bit liberal, in that it will accept not just normally formatted numbers like
`(614)867-5309`, but also some weird stuff like `!614* 867+5309`, and it
doesn't match numbers given without area codes. Finding a perfect regex for
that is left as a reader exercise.

If this were assigned as a rule to a callable, any line which started with a
NANP phone number would be matched. (You could add `.*`, which means any number
of any characters, to the beginning to make it match if the number is anywhere
in the line.) To get the pieces of the number out, you could use
`trigger.group(1)`, `trigger.group(2)`, and `trigger.group(3)`. Or, if for
example you wanted to put it into a more common format, you could do
`'(%s) %s-%s' % trigger.groups()`, which will give you (for example)
`(614) 867-5309`.

## Documentation

The final basic thing to know is how to document your code in a way Sopel can
use. This is done using Python's "docstrings". When a string is put immediately
below a variable or function, or at the top of a file, without being assigned
to anything else, it becomes that variable/function/file's docstring.
The first one you'll want to do is one for your file. You should include a
simple description of what the plugin does on the first line, with more
detailed information below. For example:

```python
"""Frobnication plugin for Sopel

Includes commands for frobnicating synchronous and asyncronous Werlingford
paradigms. Uses a configurable HPADP endpoint to defalicate user-provided
almication schemata.
"""
```

The triple quotes are Python's way of having a string across multiple lines.
Yours doesn't have to look exactly like this, of course, but it'll give you a
general idea of what to include.

You should also put a docstring on all of the callables you have. This should
be a short message describing what the callable does. This is what Sopel will
reply with when you use the `.help` command on something.

There is also a `@sopel.module.example` decorator, which you can give a string
containing an example of a valid command. An example of an example might be
`.t America/New_York` for the time command.

## Gotchas

### Rate-limiting scheduled commands

Note that if you use the Python `sched` package from within your callable to
schedule commands to execute in the future, your callable will not return until
that scheduler has finished. Sopel will therefore not update its last-used time
until that point.

For commands that use `@sopel.module.rate`, it is better to use
`threading.Timer()` instead of `sched.scheduler()` to ensure correct
rate-limiting (see [issue 824](https://github.com/sopel-irc/sopel/issues/824)).

Want to learn about the configuration wizard?
[Continue to part 2!]({% link _tutorials/part-2-config-wizard-and-setup-functions.md %})
