---
title: "Sopel tutorial, Part 2: The config file, and the configure & setup functions"
migrated: true
source: wiki
previously:
  - /tutorials/part-3-config-wizard-and-setup-functions/
---

**NOTE: This guide is for 6.0. Most of this will not work in lower versions,
due to significant changes in the config module. If you are still using a
version named "Willie", we strongly encourage you to upgrade, as such old
versions are no longer supported.**

Sopel has a config file, written in an INI-like format. It can provide
configuration options not just for the bot itself, but for modules as well.
Here, we're going to cover how you can leverage that configuration, as well as
how to make your module configurable in the wizard like we showed in [the
installation guide]({% link _usage/installing.md %}).

## Config Basics

The config file is made up of a number of *sections*, each of which has a number
of *keys* or *attributes*. If you open up your config file, you'll see
something like this.

```conf
[core]
nick = Sopel
host = irc.dftba.net
use_ssl = False
port = 6667
owner = Embolalia
channels =
    "#YourPants"
    "#tech"

[admin]
hold_ground = False

[bugzilla]
domains =
    bugzilla.redhat.com
    bugzilla.gnome.org
```

Here, `core`, `admin`, and `bugzilla` are sections. As you may have guessed,
`core` contains attributes relevant to the bot's core functionality - it's
nick, the host to connect to, etc., and `bugzilla` and `admin` contain
attributes relevant to two of the bot's modules.

In the context of your callable, the config file is available as an attribute
of the `bot` parameter. Each section is an attribute of the config file, and
each key in a section is an attribute of its respective section. For example,
if we wanted to get the owner of the bot, we would use `bot.config.core.owner`.

## Configuring your module

There are two ways you can use the config. The first is super easy; if you have
`eggs=parrot` set in the `spam` section, and you do `bot.config.spam.eggs`,
you'll get `'parrot'`. If you don't, you'll get `None`. Simple as that.

Only, you'll want to know if that value is valid. You could check that every
time you use it, or you could use `StaticSection`s to define what you need your
config values to look like ahead of time. If you've used an ORM like SQLAlchemy
this will look very familiar, but if you haven't it's easy to learn.

A config section is defined by a class, subclassing `StaticSection`
and with any number of `ValidatedAttribute`s (or other subclasses of
`BaseValidated`; see [the docs]({{ site.docs }}config.html) for more detail)
on it. So if you want to have a key `velocity` in the `swallow` section always
be a number, you can do this:

```py
from sopel.config.types import StaticSection, ValidatedAttribute
class SwallowSection(StaticSection):
    velocity = ValidatedAttribute('velocity', int)

def setup(bot):
    bot.config.define_section('swallow', SwallowSection)

def configure(config):
    config.define_section('swallow', SwallowSection, validate=False)
    config.swallow.configure_setting('velocity',
                                     'What is the speed of an unladen swallow?')
```

Now, when you use `bot.config.swallow.velocity`, you will always get an
integer. If you hadn't defined it, you would've gotten a string that you'd have
to make an integer yourself, and handle if it wasn't something you could make
an integer.

There are a few things that need explaining here, though. First,
`ValidatedAttribute` takes a number of arguments. The first is the only one
that's required; it's the name of the config attribute being described. The
second one is the function used to parse what's in the config file. Here, it's
`int` to make it an integer, but other things work like `float`, `bool`, and
`json.loads`. You can also pass an argument like `default=3` so that, if it's
not set, it will just give you that default value.

`setup` is a special function that is run when the bot is loading the module.
You can do anything you need to here (and we'll touch on a few other uses later
in the tutorial), but all we do here is set up our config definition. The
`define_section` function gets our section name and our definition class, and
sets it up. Since this happens before the module starts getting messages from
IRC, you'll be able to do `bot.config.swallow.velocity` and get your value back
in all your triggered functions. It also means that you can't send messages to
IRC; `bot.say` is defined here, but it won't do anything. If `setup` raises any
sort of exception, the module will be disabled. Since `define_section` raises
an exception by default when there's an invalid config setting, this is all you
have to do to make sure your config is valid.

The next function is `configure`. This is a special function which will be run
when you're going through the setup wizard. You don't have to have it in order
for your config definition to work, but it's a good idea if you're going to be
sharing your module, so that others will have an easier time setting it up.

Again, we define the config section, but we don't want it to validate what's
already in the config, in case someone edited the file manually and put in a
bad value. The next thing we do is configure the setting. If there's a bad
value already in the config, or the user tries to put in a bad value, we'll
~~cast them into the Gorge of Eternal Peril~~ give them an error and ask them
again.

Want to learn about URLs and remembering things?
[Continue to part 3!]({% link _tutorials/part-3-memory-and-url-info-functions.md %})
