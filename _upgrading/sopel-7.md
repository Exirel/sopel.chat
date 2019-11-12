---
title: Sopel 7.0 Migration
covers_from: 6.x
covers_to: 7.0
---

# Sopel 7.0 Migration

Sopel 7 lays the groundwork for a lot of awesome stuff! We have a major update
to Sopel's command-line interface in progress (which will be finished in Sopel
8), and some API updates that might affect a few existing plugins.

But first, we really need to talk briefly about Python.


## A note about Python versions

If you still use Sopel under Python 2, you might notice that Sopel 7 emits
warnings about version compatibility. The sad reality is, as of January 1, 2020,
Python 2.7 no longer receives any updates. While this doesn't mean we will
simply drop support for running Sopel under Python 2 immediately, it _does_ mean
that we will no longer reject ideas that would require doing so.

For the life of Sopel 7.x, we still plan to maintain compatibility with Python
2.7 unless it becomes absolutely necessary to drop it. For example, if a severe
bug is found in one of Sopel's dependencies, and the fix is only released for
Python 3, we would consider dropping Python 2 support in the next minor version.

From Sopel 8 onward, it would be much easier to implement new features and
enhancements if we dropped support for very old Python releases. For example,
Sopel's support for reloading plugins during runtime can be made much more
robust using features added to the language in Python 3.4.

The crux of the matter is this: Sopel's range of supported Python releases
remained stagnant for far too long. While the Sopel project was effectively
unmaintained between late 2016 and early 2018, Python 3.3 reached end-of-life
(September 29, 2017). During the lengthy development period of Sopel 7, Python
3.4 reached end-of-life (March 18, 2019). Sopel 7 is likely to be released very
close to the EOL of Python 2.7 (January 1, 2020).

We can't keep testing support for these old versions forever. At some point,
Sopel's core developers will lose the ability to run them locally. (Python 3.3
is already difficult—though not impossible—to install on current popular Linux
systems like Ubuntu 18.04 LTS.) Travis CI, our continuous integration testing
provider for contributions from both maintainers and the community alike, won't
keep supporting the installation of EOL Python releases indefinitely. We can't
support what we can't test.

Furthermore, it's a waste of effort to fix bugs in new code that, for whatever
reason, only affect old, disused versions of Python. The ratio of time spent
to users impacted becomes too high as more systems get upgraded.

And finally, supporting older Python releases sometimes prevents us from
making highly desirable improvements (see above, re: reloading things).

Keeping all this in mind, the current plan is as follows. Note that it is
subject to change, as Sopel's development pace remains quite leisurely relative
to the overall Python ecosystem.

  - Sopel 7 will maintain the same Python version compatibility range as 6.x,
    barring any major roadblocks
    - This may change as Sopel 7 gets closer to release, depending on how our
      testing infrastructure and dependencies look, but we're motivated to keep
      things as-is (one of Sopel's maintainers still runs a production instance
      on Python 2.7, and cannot upgrade that system to a compatible version of
      Python 3 without significant work)
  - Sopel 8 will drop support for EOL Python releases immediately at the start
    of its development cycle, and adjust version support based on the estimated
    release date target as that becomes clearer
    - This **definitely** means dropping 2.7, 3.3, and 3.4 (already EOL)
    - Python 3.5 support **might** be dropped, depending on timing; it's set
      to reach EOL around September 2020 (but no hard date yet)
    - Python 3.6 is [tentatively][PEP-494] EOL in December 2021, but Sopel 8
      should be finished long before then

[PEP-494]: https://www.python.org/dev/peps/pep-0494/


## Database support

Sopel 7 brings back support for databases other than SQLite—an often-requested
feature ever since Sopel went SQLite-only in version 5.

While we can't practically offer documentation on every possible setup, it
should be fairly easy to migrate an existing installation to any supported
database type with a bit of search-fu. Sopel's database support is built on
SQLAlchemy, which has [ample documentation][sqlalchemy-dialects] of its own
about getting up and running with various back-ends.

Please don't hesitate to offer feedback in [our IRC channel][sopel-freenode] or
[a GitHub issue][gh-new-issue]. This is a huge feature, and with a small team
it's simply not possible for us to test everything—especially the less common
database types (paid ones like Oracle, especially).

[gh-new-issue]: https://github.com/sopel-irc/sopel/issues/new
[sopel-freenode]: irc://chat.freenode.net/sopel
[sqlalchemy-dialects]: https://docs.sqlalchemy.org/en/13/dialects/index.html


## CLI restructuring

Version 7 deprecates many of the command-line arguments that Sopel has used for
most of its life, in favor of a much more extensible command structure.

Instead of having arguments like `--quit` or `--configure-modules`, Sopel's CLI
now works on a sub-command system (like Git and other popular tools). This will
allow adding more functions without having to share one global argument
namespace, and make the commands more "speakable".

The full new command structure will be documented in the [Command-line
arguments]({% link _usage/command-line-arguments.md %}) after release, but as a
general overview of the old structure vs. the new:

|             This            |             Becomes            |
| :-------------------------- | :----------------------------- |
| `sopel --quit`              | `sopel quit`                   |
| `sopel --kill`              | `sopel quit --kill`            |
| `sopel --configure-all`     | `sopel configure`              |
| `sopel --configure-modules` | `sopel configure --plugins`    |
| `sopel --list`              | `sopel-config list`            |
| `sopel -v`                  | `sopel -V` / `sopel --version` |

There's one argument deserving of special mention: `--migrate`/`-m`. It will
be removed in Sopel 7, because it has been a no-op since version 4.0.0.
Someone deleted the code to handle it without saying so anywhere, but Sopel
has continued to carry around this useless argument since 2014. No more!

New commands are not always going to be shorter than the old ones (see the
`--kill` example), but we're looking at the future picture. This is just the
start of Sopel's CLI evolution, and more features will come based on this new
command structure.

### Removal of old commands

For the life of Sopel 7, the existing ("legacy") arguments are still supported,
just with deprecation notices in the `--help` output.

In Sopel 8, the old arguments from Sopel 6 and lower will be removed.

Most deprecated arguments in Sopel 7 will output warnings to the terminal when
used. Hopefully we remembered them all during development—but if we missed any,
please do let us know via the [issue tracker][gh-new-issue] or IRC.

### New helper commands

Some helper tools debut with Sopel 7. So far, they are `sopel-config` &
`sopel-plugins`. Both are intended to make the job of configuring a Sopel
instance easier, without needing to edit the config file manually.

#### `sopel-config`

The `sopel-config` tool supports `init`ializing a new config file, `list`ing
existing config files, and `get`ting values from an existing config file.

More features will likely be added along the road to Sopel 8. Suggestions are
welcomed and encouraged!

#### `sopel-plugins`

With the `sopel-plugins` command, you can `list` available plugins; `enable`
or `disable` plugins in a specific config file; and `show` details about a
specific plugin such as where it is on disk and whether it's enabled.

Here, too, more features will likely be added along the road to Sopel 8.
Suggestions are welcomed and encouraged!


## Sopel 7 API changes

### Managing URL callbacks

For quite a while, Sopel plugins wishing to override the `url.py` plugin's
automatic title-fetching for certain URLs have customarily done something along
these lines:

```python
# in the plugin's setup() function:
    if not bot.memory['url_callbacks']:
        bot.memory['url_callbacks'] = tools.SopelMemory()
    bot.memory['url_callbacks'][compiled_regex] = methodname
```

Similar manual manipulation of the object in memory was needed to unregister
handlers at plugin unload:

```python
# in the plugin's shutdown() function:
    try:
        del bot.memory['url_callbacks'][compiled_regex]
    except KeyError:
        pass
```

Going forward, a new set of API methods should be used instead:

  - `bot.register_url_callback(pattern, methodname)`, to call `methodname` when
    a URL in a message matches the `pattern`
  - `bot.unregister_url_callback(pattern)`, to unregister the `pattern` and its
    associated callback(s)
  - `bot.search_url_callbacks(url)`, to find callbacks matching the given `url`

Manually accessing `bot.memory['url_callbacks']` as before will continue to work
for the life of Sopel 7.x, at a minimum. However, doing so is considered
deprecated, leaving future versions free to move the callback storage if needed.

### Adding multiple command examples

Decorating a plugin callable like this was a great way to add documentation to
that command through Sopel's `help` plugin:

```python
from sopel import module

@module.example('.foo barbaz')
def foo_cmd(bot, trigger):
    bot.action('foos %s' % trigger.group(3))
```

However, *only one example* could ever appear in the `help` output. This was
[confusing](https://github.com/sopel-irc/sopel/issues/1200) to plugin authors.

Furthermore, if more than one example was defined:

```python
from sopel import module

@module.example('.foo barbaz')
@module.example('.foo spam eggs sausage bacon')
def foo_cmd(bot, trigger):
    bot.action('foos %s' % ', '.join(trigger.group(2).split())
```

It was not necessarily intuitive which example would be displayed if a user
did `.help foo`. The code says it would use `example[0]`. That's the first one
in the list, which makes sense. But take a guess which of the two above would
be used—`.foo barbaz` or `.foo spam eggs sausage bacon`?

Ready to see if you were right?

Sopel would use `.foo spam eggs sausage bacon` as the example, because due to
how decorators work, it ends up first in the internal list despite appearing
last in the source code. Not very intuitive for beginning plugin writers…

So, in Sopel 7, there is a `user_help` argument to `@module.example`. If at
least one of a callable's examples has this attribute set to `True`, all such
examples will be used when outputting help for that command:

```python
from sopel import module

@module.example('.foo barbaz', 'foos barbaz', user_help=True)
@module.example('.foo', "I can't foo that!")
@module.example('.foo egg sausage bacon', 'foos egg, sausage, bacon', user_help=True)
def foo_cmd(bot, trigger):
    if not trigger.group(2):
        return bot.say("I can't foo that!")
    bot.action('foos %s' % ', '.join(trigger.group(2).split())
```

Here, Sopel's help output will show both `.foo barbaz` and `.foo egg sausage
bacon` as examples. Plain `.foo` does not have `user_help=True` (it's purely
there for testing), and so it will not be shown.

Of course, backwards compatibility is important! That's why we used this
approach. Callables without any `user_help=True` examples will behave just
like they would have in Sopel 6 and older: The "first" example (the one
closest to the function's `def` line, last in the source line order) will
appear in `help`'s output.

Making `user_help=True` the default would make *a ton* of sense, definitely!
But if we did that, many (many) existing Sopel (and Willie) plugins would
potentially output "bad" help information—so we elected to keep the old
behavior by default in an effort to minimize any "breakage".

### Logging API rework

Plugins should use the new `sopel.tools.get_logger()` function to get a
logging object, starting with Sopel 7.0. It takes the same argument (the
plugin's name) as its predecessor, `sopel.logger.get_logger()`.

`sopel.logger.get_logger()` will have an extended deprecation cycle, to allow
ample time for the ecosystem to adapt without spamming too many log files at
first. The old function's behavior has been tweaked to work reasonably nicely
with the harmonized logging system implemented for Sopel 7.

Calls to `sopel.logger.get_logger()` will begin emitting deprecation warnings
in Sopel 8.0, to alert stragglers (or users of possibly-abandoned code). We
will remove this function from the API in Sopel 9.0.


## Sopel 7 plugin changes

### Reminder DB migration

Sopel 7 refers to specific instances by config file name whenever possible,
instead of using other pieces of config data such as `nick` or `host` that are
more likely to change. The `remind` and `tell` plugins have been updated with
this in mind, and will attempt to automatically convert their respective data
files to the new name format if the old filename exists.

You probably will not need to do anything. However, if the automatic migration
does fail, it will output (and log) information about what it was trying to
do, and link to this section of the Sopel 7 upgrade guide for convenience.

**If a migration failure brought you here:** Above the link you should find
the old and new filenames the plugin was attempting to use.

**Important:** Ensure the associated instance of Sopel is NOT running
before doing anything. Tampering with the reminder files while Sopel is
running can result in data loss.

In most error cases, migration will fail because the new filename already
exists. The simplest fix is to move or rename the conflicting file, and run
Sopel again so the migration can complete.

If both the old and new files are non-empty, you might want to peek inside
them with a text editor to see what's there before deciding which to keep. The
current format for both plugins' data files is essentially <abbr
title="Tab-Separated Values">TSV</abbr>, and they can be merged by hand
(again, _with Sopel stopped_) if both the old _and_ new files somehow contain
meaningful, unique entries.

And of course, if you need more in-depth assistance with fixing a failed
migration, [our IRC channel][sopel-freenode] always welcomes questions.

### Rewrite of `spellcheck`

As of February 2018, the Python bindings for `enchant` [became unmaintained][
pyenchant-unmaintained]. This made it increasingly difficult to install the
dependencies required for the `spellcheck` plugin work, and often [caused][
windows-enchant] [problems][linux-enchant] with new installations.

Because of this, the `spellcheck` plugin was rewritten to use `aspell` instead.
In the process, it also gained support for a custom word list, managed by a set
of new commands:

  - `.scadd` - stages a word for adding to the bot's word list
  - `.scpending` - lists words pending addition to the bot's custom list
  - `.scdel` - removes a word from the pending list
  - `.scsave` - commits pending words to the bot's word list
  - `.scclear` - clears the list of pending words without saving

Unfortunately, the `aspell` API only supports *adding* words to the custom
dictionary. To *remove* a custom word, a user must manually edit the dictionary
file, so we decided to go with a two-step process. Hopefully it will help Sopel
admins around the world avoid adding typos to their bots' custom dictionaries!

Depending on how much trouble the `aspell` dependencies cause, support for the
`spellcheck` plugin might become a setuptools extra. Feedback is welcome!

  [pyenchant-unmaintained]: https://github.com/rfk/pyenchant/commit/4df35b7
  [windows-enchant]: https://github.com/sopel-irc/sopel/issues/1142
  [linux-enchant]: https://github.com/sopel-irc/sopel/pull/1454


## Planned user-facing changes

A "user" here is someone who *runs* (or is responsible for *maintaining*) one
or more Sopel bots. If you're reading this, that *probably* describes you.
(Unless you're some kind of weirdo who only writes plugins for other people to
use, and never tests them… Seriously, who does that?)

You might need to edit your bot's configuration in the future due to these
plans. Sopel might take care of them on its own, too. But in case human
intervention is required, here are the details.

### Config format change for list values

Since the new config system was introduced, lists of values have been
represented in the config file as strings separated by commas (`,`). Sopel 7
adds support for storing these lists as multi-line strings instead, with
values separated by newlines.

Here's what that means in practice:

```conf
# Current format
[core]
enable = admin,reddit,wikipedia,wiktionary

# New format
[core]
enable =
    admin
    reddit
    wikipedia
    wiktionary
```

Note that Sopel 7 will upgrade the stored format of any comma-separated list
value if the config is saved (with `.save`) after editing the value via IRC
(with `.set section.option_name list,of,values`).

**Important: The new format requires any value beginning with `#` to be
quoted.** Automatic conversion will handle this, but be aware of it if you're
tweaking your config file(s) by hand during the upgrade process. You will need
to be careful with the `core.channels` list, in particular. Most updated
`core.channels` values should look like this:

```conf
[core]
channels =
    "#spam"
    "#eggs"
    "#bacon"
    "#snakes"
```

Unquoted values beginning with `#` *might* work properly on certain Python
versions *if indented*, but you should quote them anyway to be safe.

In Sopel 7, this is just a convenience change. It means that lists stored in
the new format can support commas within the values, without any annoying
escape-character shenanigans (which was our first plan). Old-style values (all
on a single line) will continue to be split on commas when reading config
files, as before, and will be updated to the new format as described above.

**Eventually, in Sopel 9, we plan to remove this fallback behavior.** Sopel 8
may emit a warning to the console and/or log file at startup if old-style list
values are present in the loaded config file, but we encourage updating your
config files *long* before then.

### Modules vs. plugins

Sopel has long used the term "module" in reference to Python files (or folders
thereof) that add functionality to the bot. This is reflected even in the
layout of Sopel's data folder: `~/.sopel/modules` is so named because that's
where the modules go! We'd like to change that, though.

The simplified explanation is that Python already has "modules". Add-ons for
Sopel are also Python modules, but not all Python modules are Sopel add-ons.
This overlap gets confusing for developers sometimes.

Many similar projects call this kind of add-on a "plugin". We've already
started using the term "plugin" in our documentation, in place of "module",
when referring to these add-ons.

As a user, you'll notice only small changes related to this shift. The
restructured CLI [described above](#cli-restructuring), for example, uses
`sopel configure --plugins` to replace `sopel --configure-modules`. Our
documentation will continue to move toward consistently referring to "plugins"
and "modules" as distinct concepts. We'll also change the default search
location for plugins from `~/.sopel/modules` to `~/.sopel/plugins` in a future
release (probably Sopel 8), but it will be easy to re-add the old folder if
you like via the `core.extra` setting.


## Planned future API changes

This section is all about stuff that won't cause problems *now*, but *will*
break in a future release if not updated. Most of these are planned removals of,
or changes to, API features deprecated long ago.

We suggest reviewing these upcoming changes, and updating your own plugins if
they still use anything listed here, as soon as possible. Updating plugins
published to PyPI should take priority, especially plugins written for Sopel 6
that are not future-proofed by capping Sopel's version in their requirements.

If you use third-party plugins that have not been updated, we encourage you to
inform the author(s) politely that they need to update. Or better yet, submit a
pull request or patch yourself!

### Removal of `bot.privileges`

Sopel 7.x will be the last release series to support the `bot.privileges` data
structure (deprecated in [Sopel 6.2.0][v6.2.0], released January 16, 2016).

Beginning in Sopel 8, `bot.privileges` will be removed and plugins trying to
access it will throw an exception. `bot.channels` will be the _only_ place to
get privilege data going forward.

### Removal of `bot.msg()`

[Back in 6.0][v6.0.0], Sopel's API standardized around a consistent argument
order for messaging functions: `message` first, then an optional `recipient` (or
`destination`, if you like). Part of the old API, `bot.msg()`, has stuck around
since then because it was, [quote][msg-hard-comment], "way too much of a pain to
remove". In fact, it turned out to be quite easy to remove.

None of Sopel's own code uses this old method any more, and we will remove it
entirely in 8.0. Uses of `bot.msg()` in 7.0 will emit a deprecation warning, so
any remaining third-party code that still uses it can be found and patched.

  [msg-hard-comment]: https://git.io/sopel-msg-pain

### Rename/cleanup of `sopel.web`

While the whole `sopel.web` module was marked as deprecated in [Sopel
6.2.0][v6.2.0], because it largely serves as a wrapper around the `requests`
library, parts of it seem to be useful enough that they should be kept around.

For Sopel 8, we intend to move `sopel.web` to `sopel.tools.web`. The new
location is available in Sopel 7 to provide a transitional period. Similar to
how importing from both `willie` and `sopel` worked in the run-up to Sopel 6.0,
it is possible to do any of the following during Sopel 7's life cycle:

  - `import sopel.web`
  - `from sopel import web`
  - `import sopel.tools.web`
  - `from sopel.tools import web`

In Sopel 8, we will remove the pointers from `sopel.web` to the new location.
These explicitly deprecated functions will also be removed at the same time:

  - `sopel.web.get()` — use `requests.get()` directly instead
  - `sopel.web.head()` — use `requests.head()` directly instead
  - `sopel.web.post()` — use `requests.post()` directly instead
  - `sopel.web.get_urllib_object()` — really, just use [`requests`][requests]

We will also tweak the module constants:

  - `sopel.web.default_headers`: renamed to `sopel.tools.web.DEFAULT_HEADERS`
  - `sopel.web.ca_certs`: removed in `sopel.tools.web` — it no longer has any
    function (and was probably not useful for Sopel plugins to import, anyway)

New additions to Sopel's web tools made during the life of 7.x will be
available only in `sopel.tools.web`. Functions and constants that we plan to
remove in Sopel 8 (as listed above) will be available only from the old
`sopel.web` module.

  [requests]: https://pypi.org/project/requests/
  [v6.0.0]: {% link _changelogs/6.0.0.md %}
  [v6.2.0]: {% link _changelogs/6.2.0.md %}

### Finalizing the "plugin" transition

As described [above](#modules-vs-plugins), we're trying to get away from the
ambiguity of calling Sopel add-ons "modules", because that term is already
used by Python itself. All Sopel add-ons are Python modules, but not all
Python modules are Sopel add-ons. Many people in the Sopel community have
tripped over this blurred line, and we have plans to change more than just
documentation eventually.

Already, in Sopel 7, the internal mechanisms for handling add-on code are all
about "plugins" now. The module responsible is named `sopel.plugins`, and its
submodules & members all agree on this nomenclature. But you, a _plugin_
developer, must—confusingly—still import the "_module_" module from `sopel` to
use any of the decorators that make Sopel plugins work. Annoying, isn't it?

Rest assured that we're not done yet. Future releases of Sopel will support
(even encourage) importing `sopel.plugin` instead, which will be the new home
of all plugin-related decorators & constants. `sopel.module` won't go away any
time soon, though. It predates even the name "Willie", after all—we can't just
yank it out without a _long_ deprecation cycle. We might just leave it as a
permanent alias to `sopel.plugin`. (The plan is still [up for
discussion][#1738], if you're interested.)

But, once available, you should _definitely_ use `sopel.plugin` in your new
code. It's the future!

  [#1738]: https://github.com/sopel-irc/sopel/issues/1738
