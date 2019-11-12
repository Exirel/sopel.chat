---
title: "Sopel tutorial, Part 5: Plugins in folders, and distributing to PyPI"
migrated: true
source: wiki
previously:
  - /tutorials/part-6-packaging-and-distributing-modules/
  - /tutorials/part-5-packaging-and-distributing-modules/
---

**NOTE: This guide is for Sopel 6.0+. If you are still using a version named
"Willie", we strongly encourage you to upgrade, as such old versions are no
longer supported.**

Sopel makes it easy to share plugins, and get plugins from other people,
through the Python Package Index. Even if you aren't sharing your plugin, if it
starts getting big and complex, you might want to rearrange it into a folder
just to keep it organized.

## Folder plugins

Putting your plugin in a folder is simple, especially if you're already
familiar with how Python modules work. Let's say you've been working with
`~/.sopel/modules/spam.py`. All you have to do is move it to
`~/.sopel/modules/spam/__init__.py`. Of course, you probably want to split it
out from that file a bit.

The first thing you want to do is put `from __future__ import absolute_import`
at the top of your `__init__.py`, and any other Python files you have in here.
If you're only going to use this plugin with Python 3, this isn't necessary,
but it clears up some weirdness with how imports work in Python 2.

You can split anything out to anywhere you want. The only rule is that the
things that the bot is searching for (basically, just the things that you're
decorating with the decorators in `sopel.module`) need to be present in that
`__init__.py`. So if you had a callable `eggs` in there, and you move it into
`~/.sopel/modules/spam/callables.py`, you'll want to have
`from .callables import eggs` (note that leading `.`, to say we want it from
the `callables` module in the same directory). It's worth noting that you won't
be able to import things from `__init__.py` in other files in the directory
reliably, so it's probably best to have `__init__.py` do nothing but import the
things it needs.

## Using the cookiecutter template

The easiest way to make a plugin in a folder, all prepped and ready to be
published to PyPI, is to use our
[cookiecutter template](https://github.com/sopel-irc/cookiecutter-sopel). It's
easy:

```sh
pip install cookiecutter
cookiecutter gh:sopel-irc/cookiecutter-sopel
```

Answer all the prompts, and you'll have a ready-made repo structure to plop
your plugin into.
