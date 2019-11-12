---
layout: default
title: Sopel - The Python IRC Bot
---

# Introduction

<span class="Sopel">Sopel</span> is a simple, easy-to-use, open-source IRC
utility bot, written in [Python](https://www.python.org/). It's designed to be
easy to use, easy to run, and easy to extend.

<span class="Sopel">Sopel</span> comes with a ton of ready-made features for
you to use. It can leave notes for people, give you reminders, and
[much more]({% link _usage/commands.md %}).

<span class="Sopel">Sopel</span> also comes with a [fully-documented](
{{ site.docs }}) and easy-to-use API, so you can write your own features.
There's also an [easy tutorial]({% link _tutorials/index.md %}) you can follow,
to help you get started.

Developing for <span class="Sopel">Sopel</span> is a great way to familiarize
yourself with Python. It's easy to start, but there's no limit to the cool
things you can do with it.

<span class="Sopel">Sopel</span> is available on the
[Python Package Index](https://pypi.org/project/sopel/), and in a
[tarball](https://github.com/sopel-irc/sopel/releases/latest).

# Features

* Fully [documented]({{ site.docs }}) API for writing new plugins
* SSL/TLS connection support
* [IRCv3](https://ircv3.net/) support, with SASL authentication
* Can authenticate admins with services on networks which support it
* Easy quickstart wizard
* Dynamic topic support using topic masks
* Numerous plugins: Wikipedia, Reddit, Bugzilla, unit conversion, and more
* Persistent user and channel settings/preferences database using SQLite
* Ability to easily run as a daemon
* Safe asynchronous inter-plugin communication
* And much, much more

# Project History

[Sean Palmer](http://inamidst.com/) was the original creator of the bot, which
he called phenny.

[Michael Yanovich](https://yanovich.net/) improved it, and changed the name to
[jenni](https://github.com/myano/jenni).

[Embolalia](https://embolalia.com/) improved it even more, with a lot of
help from [Dimitri Molenaars](http://tyrope.nl/) and
[Elad Alfassa](https://eladalfassa.com/), and renamed it to Willie, and later
Sopel.

[dgw](https://technobabbl.es/) took over the project from Embolalia but didn't
change the name (Yet™). This is the current and most advanced version of the bot.

A number of other people have helped out along the way, and they can be seen in
the [CREDITS](https://github.com/sopel-irc/sopel/blob/master/CREDITS) file in
Sopel's source code.

# Frequently Asked Questions

<dl class="faq">
<dt>Where can I report a problem with Sopel?</dt>
<dd>You can file a ticket in our <a href="{{ site.repo }}/issues">GitHub issue
tracker</a>, or join the developers in <a href="irc://irc.freenode.net/#sopel">
#sopel</a> on Freenode.</dd>

<dt>Is there somewhere I can go to find plugins other people have written for
Sopel?</dt>
<dd>You can install plugins from <a href="https://pypi.org/search/?q=%22sopel_modules%22">
PyPI</a>, or use your favorite search engine to find plugins on GitHub, etc.
There's also a <a href="https://github.com/sopel-irc/cookiecutter-sopel">
template</a> you can work from to publish your own plugins on PyPI.</dd>

<dt>Will phenny/jenni modules work with Sopel?</dt>
<dd><a href="{% link _appendices/phenny-compatibility.md %}">Probably</a>.
There are a small number of features in the older versions which are implemented
differently in Sopel. The vast majority of modules should work without problems,
though.</dd>

<dt>Can I use Sopel with Docker?</dt>
<dd>Probably, but there's not much reason to. We only provide support for one
version of Sopel at a time, and it already supports running multiple instances
side-by-side. If you really need to containerize dependencies, virtualenv is
probably a lot easier—but there is <a href="https://github.com/sopel-irc/sopel-docker">an
Officially Unofficial™ Docker container</a> available.</dd>

<dt>Does Sopel work on Google App Engine?</dt>
<dd>Probably not. App Engine doesn't currently support SQLite, which Sopel
requires for its database.</dd>

<dt>Does Sopel run on OSX? Windows? PyPy? Jython?</dt>
<dd>Probably, probably, probably, probably. Sopel itself is pure Python, and an
effort is made to be as platform-independent as possible. That said, most of
the development is done on Linux, so some platform-specific bugs may be missed.
If you do run into a bug, be sure to report it, because otherwise we won't know
about it.</dd>

<dt>How do I make Sopel give me ops when I enter a channel?</dt>
<dd>You should use your network's services to do this. If you're on a network
like EFnet which doesn't have services, you can write a plugin to make Sopel do
it. Sopel will never be as good at it as network services, though, so we don't
include that functionality in our default set of plugins.</dd>

<dt>Why is Sopel saying <code>...</code>?</dt>
<dd>Sopel is built to avoid being spammy as much as possible, so it keeps track
of the last few things it's said. If too many of those last few things are the
same, it says <code>...</code> a few times instead of repeating itself (and
then stops trying to say that thing entirely, until it's said some other
things). Usually, this happens because someone is spamming the same command
over and over, or something is just broken. It doesn't keep the bot from saying
anything else, and it can say the same thing as often as you want, as long as
it says some other stuff, too.</dd>

<dt>Why does Sopel spit out a bunch of warnings when I have the iPython plugin
loaded?</dt>
<dd>This is because by default, iPython re-enables the deprecation warnings
which python ignores most of the time. To suppress these warnings, put
<a href="https://github.com/sopel-irc/sopel/blob/5f60756e1a975a1a978c322949d8ba9b4a2b4d71/contrib/suppress-warnings.py">this
file</a> in <code>~/.ipython/profile_default/startup/</code></dd>
</dl>
