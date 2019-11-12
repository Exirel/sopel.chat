---
title: Installing and running Sopel
order: -9100
previously:
  - /tutorials/part-1-installation/
  - /download.html
---

**NOTE: This guide is for Sopel 6.0+. If you are still using a version named
"Willie", we highly encourage you to upgrade, as such old versions are no
longer supported.**

## Installing Sopel

Sopel requires Python 2.7.x or Python 3.3+ to run. Under Python 2.7, Sopel
requires `backports.ssl_match_hostname` to be installed. Use `pip install
backports.ssl_match_hostname` or `yum install
python-backports.ssl_match_hostname` to install it, or download and install it
manually [from PyPI](https://pypi.org/project/backports.ssl_match_hostname).

There is also a detailed [system requirements]({% link
_usage/system-requirements.md %}) page that is kept more-or-less updated (by a
human) with what is required for each plugin.

If you want to use Python 3 on CentOS, you may want to see [this guide]({% link
_appendices/using-python-3-on-centos-7.md %}) on getting that set up easily.

### Latest stable release

On most systems where you can run Python, the best way to install Sopel is to
just `sudo pip install sopel`. (On Windows, leave out the `sudo`.) Installing
with pip will "just handle" dependencies for you, so you won't need to do so
manually (except for installing `backports.ssl_match_hostname` as described
[above](#installing-sopel), if you're on Python 2.7).

Nearly all Python versions Sopel supports should include pip out of the box. But
if your installation doesn't have it, you'll have to get it yourself. On Debian
and Ubuntu, you can do this by running `sudo apt-get install python-pip` in a
terminal. For macOS and Windows, follow the `pip` setup instructions
[here](https://pip.readthedocs.org/en/latest/installing/).

Arch users can install the `sopel` package from the [community] repository,
though new versions might take slightly longer to become available.

Failing both of those options, you can grab the latest tarball [from GitHub]({{
site.repo }}/releases/latest) and follow the steps for installing from the
latest source below.

### Latest source

First, either clone the repository with `git clone
git://github.com/sopel-irc/sopel.git` or download a tarball [from GitHub]({{
site.repo }}/releases/latest).

In the source directory (whether cloned or from the tarball) run `python
setup.py install`. You can then run `sopel` to configure and start the bot.
Alternately, you can just run the `sopel.py` file in the source directory.

You will need to download all of Sopel's dependencies and install them manually
as well. These can be found on the [Python Package Index](https://pypi.org/).
The only one that's needed for the bot itself to work is
[backports.ssl\_match\_hostname](https://pypi.org/project/backports.ssl_match_hostname/).
Other things are needed for plugins to work properly. If you get errors about
being unable to import plugins when you start the bot, search for them on PyPI.

### Upgrading

If you already have an older version of Sopel (or Willie) installed, and want
to upgrade to the newest version, you should consult the migration guides.

{% assign ups = site.upgrading | sort: "covers_to"
  %}{% for up in ups %}{%
    assign from_name = "Sopel" %}{%
    assign to_name = "Sopel" %}{%
    assign covers_from = up.covers_from | plus: 0 %}{%
    assign covers_to = up.covers_to | plus: 0 %}{%
    if covers_from < 6.0 %}{% assign from_name = "Willie" %}{% endif
    %}{%
    if covers_to < 6.0 %}{% assign to_name = "Willie" %}{% endif
%}  * [Upgrading from {{ from_name }} {{ up.covers_from }} to {{ to_name }} {{ up.covers_to }}]({{ up.url }})
{% endfor %}

You might need to read more than one if your existing Sopel instance is old
enough. Each guide only covers migrating from the previous major version. So
for example, if you still have Willie 4 running, and you want to get Sopel 6,
you should read the Willie 5 migration guide (covers going from 4 to 5) _and_
the Sopel 6 migration guide (covers going from 5 to 6).

## Creating a service (optional)

Sopel's source repository has example `systemd` unit files in [the `contrib`
folder]({{ site.repo }}/tree/master/contrib). Both single- (`sopel.service`)
and multi-instance (`sopel@.service`) examples exist.

If you create a script or configuration file to run Sopel under another init
system, feel free to submit it to [the repo]({{ site.repo }}) for other users'
convenience.

## First run

> If you're running Sopel on Windows, replace all following occurrences of `sopel` with `python sopel.py`

To run Sopel, just type the command `sopel` in your terminal. The first time
you run Sopel, it will bring you through a quick setup wizard. Most of the
questions should be pretty straightforward. When you see something in square
brackets, that's the default setting, and you can just hit enter to keep it.
When asked for the channels to connect to, enter them separated by commas
(e.g. `#spam,#eggs,#cheese`) This wizard doesn't cover every option, only the
ones which are needed to get the bot running. The core config settings are all
[documented]({{ site.docs }}config.html#the-core-configuration-section),
if you want to make other tweaks.

Finally, it will ask you about configuration settings for plugins. This will
automatically detect what plugins you have available, and run their
configuration utility if they have one.

Your configuration file will be stored in `~/.sopel`. The file will be called
`default.cfg` by default. You can access the configuration wizard again by
running `sopel -w`. You can also get just the plugin options with
`sopel --configure-modules`. You can specify another configuration file with
`sopel -c filename`. This works both for the configuration utility and for
running the bot. This way, you can keep multiple different config files for
different networks, for example. You can see a list of all these options by
running `sopel -h` or `sopel --help`.

Once you've finished the configuration tool, Sopel will automatically start,
connect to the network, and join the channels you specified.

## Authentication

Most IRC networks have a service that allows you to authenticate yourself as
the owner of a username. This is configurable in Sopel with these settings:
[`auth_method`]({{ site.docs }}config.html#sopel.config.core_section.CoreSection.auth_method),
[`auth_password`]({{ site.docs }}config.html#sopel.config.core_section.CoreSection.auth_password),
[`auth_target`]({{ site.docs }}config.html#sopel.config.core_section.CoreSection.auth_target),
and [`auth_username`]({{ site.docs }}config.html#sopel.config.core_section.CoreSection.auth_username).

----

Want to learn how to write plugins for Sopel? [Continue to the tutorial!]({% link _tutorials/part-1-writing-plugins.md %})

Just want to play around with your new IRC bot? [Read more usage articles!]({% link _usage/index.md %})
