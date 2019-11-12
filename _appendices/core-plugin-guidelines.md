---
title: Guidelines for writing core plugins
migrated: true
source: wiki
order: 3000
previously:
  - /appendix/core-module-guidelines/
---

In order to keep the bot easy to set up and run, and avoid bunches of unknown code cluttering things up and creating maintenance burden, there are a few things that should be considered before a plugin is added to the default set. None of them is a hard requirement, but they're important.

* Is the plugin useful to a broad audience? Not everyone has to find it useful, but it should be something common.
* Does the plugin require configuration to be useful? Preferably, the plugin should at least do *something* without being configured. More wizard questions means more effort when you first start using it, so a plugin should be able to function without making the user answer them. Configuration making the plugin work better is fine (see `safety` and `bugzilla` from 6.0).
    * This *especially* applies to plugins that require keys from third-party APIs. It sucks, because so many useful APIs need keys even for read-only access, but a user should not have to open a browser during the config wizard; every question should have an obvious answer.
* Is the plugin robust? Sometimes, it's better not to include a plugin than to include a really buggy version of it, even if it's useful.