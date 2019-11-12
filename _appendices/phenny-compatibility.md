---
title: Phenny compatibility
migrated: true
source: wiki
order: 4000
---

Sopel is, by and large, compatible with Phenny and Jenni. It is a goal of the project that modules/plugins written for those bots will work with Sopel, with a minimal amount of effort. Plugins originally written for Willie (before the rename to Sopel) should work, too.

Note that the arguments to Sopel callables are conventionally referred to as `bot` and `trigger`. These are functionally the same as the `phenny` and `input` passed to phenny callables, and either naming convention will work.

Prior to the release of Sopel v4.1.0 (called Willie at the time), the following compatibility issues were known:

### Major issues
These are likely to affect many or all plugins and deployments.

* Sopel uses unicode more frequently and consistently than Phenny. `trigger` objects entering your callables will be unicode, and messages sent with `write`, `say`, `msg`, etc. must also be unicode objects.
* Configuration files are incompatible. A tool exists to assist in converting them to Sopel's newer, more versatile format.
* Imports of `web` and `tools` must be changed to `sopel.web` and `sopel.tools` respectively (or `from sopel import web, tools`).

### Minor issues
These only affect a small number of plugins, and/or will fail gracefully

* Phenny's `last_seen_uri` and `seen` are replaced by Sopel's [memory system]({% link _tutorials/part-3-memory-and-url-info-functions.md %}). Plugins using them will likely still work, but may not interoperate with newer plugins as expected.
* `phenny.stats` will be an empty dict, which will negatively impact any plugin which uses it. This is likely limited to the `.stats` command in Phenny's `info` plugin.
* Imports of `icao` are broken, as `icao.py` is not included in Sopel. This likely only breaks phenny's weather plugin, the functionality of which is replaced and improved in the third-party PyPI package [sopel-modules.weather](https://pypi.org/projects/sopel-modules.weather/).
* Imports of `bot` and `irc` are broken. There is not necessarily a simple solution, but the only plugin this is likely to affect is `reload`, the functionality of which is replaced and improved in Sopel.
* Callables that used the deprecated function signature from phenny (e.g. `def f_time(self, origin, match, args):` rather than `def f_time(phenny, input):`) are not supported. This will not affect the vast majority of plugins. Those that are affected can likely be made to work (though not necessarily meet current style guidelines) by removing the `origin`, `match`, and `args` arguments, adding a `trigger` argument, and making the following replacements:

|Replace this: | With this: |
|---|---|
|`origin`|`trigger`|
|`match`|`trigger.match`|
|`args[0]`|`trigger.bytes`|
|`args[1]`|`trigger.sender`|

There may be other issues, but they are not known at this time.

TODO: The following members of the `Jenni` class are used in jenni, and may or may not be present or have analogs in Willie. More research is needed:
rfn, rdb, reminders, bot, doc, data, variables, notice