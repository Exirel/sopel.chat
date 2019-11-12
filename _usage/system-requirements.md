---
title: System requirements
migrated: true
source: wiki
order: -9999
---

Sopel is designed to run on Linux with Python 2.7 or 3.3+. It should probably work in other POSIX-compliant OSes, and seems to more-or-less work on Windows.

Sopel itself has few external dependencies, besides Python. There are a couple, though:

* [dnspython](https://github.com/rthalley/dnspython) - used internally to enhance connection reliability
* [requests](https://github.com/requests/requests) - used to maintain compatibility with old plugins that still try to use Sopel's `web` utility functions
* sqlite - included with all supported Python releases

Most of Sopel's dependencies are only needed for specific plugins. Below is a listing of some of these. If you don't want to use a specific plugin, you do not need its dependencies.

* [geoip2](https://github.com/maxmind/GeoIP2-python) - ip. You will also need the appropriate database files, which Sopel will download automatically if they are not found.
* [ipython](https://github.com/ipython/ipython) - ipython
* [praw](https://github.com/praw-dev/praw) - reddit
* [pyenchant](https://github.com/rfk/pyenchant) - spellcheck. You may also need to install the system-level `enchant` library.
* [pytz](https://launchpad.net/pytz) - remind, clock, seen, tell
* [requests](https://github.com/requests/requests) - [many]. Used by nearly every plugin that needs to talk to a web service.
* [xmltodict](https://github.com/martinblech/xmltodict) - bugzilla, search

Most of these packages can be installed through the `pip` command, or via your Linux distribution's software repository. If you install Sopel through `pip` or your distribution's package manager (on Fedora or Arch), all of these dependencies will be installed for you.
