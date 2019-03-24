---
title: Sopel 6.0 Name Change and Migration
covers_from: 5.x
covers_to: 6.0
previously:
  - /willie_6.html
---

# Sopel 6.0 Name Change and Migration

Writing Sopel modules is cool. But what's cooler is *sharing* them. We want to
make that easier. With that in mind, we're preparing for Sopel 6 to focus on
enabling that. It will include some new features to make it easier to share and
enjoy modules.

However, in order to facilitate these changes, we do have to make some breaking
changes. This page tells you what you need to do to account for them. It will
be updated with more information as development toward Sopel 6 continues.
Don't worry; this will likely be the last release with breaking changes for a
while.

An early alpha version is available [here](https://github.com/sopel-irc/sopel/releases/tag/6.0.0a4).

## Name change

For a number of reasons, we're changing Willie's name to Sopel. This will have
a very big impact on everyone. Users will need to install the bot using the new
package name. Module authors will need to import things from the new package
name (that is, replacing `import willie.module` and the like with
`import sopel.module`).

## Login configurations

This is the only user-facing breaking change we're planning. In 5.3.0, the
`auth_password`, `auth_user`, and `auth_method` settings in the config, were
added, and apply to all the different ways of authenticating that Sopel
supports. They will replace the old settings (like `nickserv_password`) which
will be removed in 6.0.  If you configure with the wizard, you won't notice
this change; it only really concerns you if you're manually editing the config
file.

## Messaging function changes

The functions used in modules to send messages have been made more consistent
with each other, and between triggered (like in commands) and un-triggered
contexts (like in @interval callables). The changes are as follows:

* The arguments of `notice()` are reversed in un-triggered context; it now
  takes the message as the first argument, and the destination as the second,
  as it always had in triggered contexts.
* `say()` and `action()` are now available all the time. When not in a
  triggered context, they take an additional argument `destination`. When in a
  triggered context, this argument is optional and defaults to the trigger
  sender. If you were passing `recipient` as a keyword (rather than positional)
  argument to `action()`, you'll need to change it appropriately.
* `reply()` is also available all the time, with new arguments
  `destination` and `reply_to`, the latter being the name to prepend to the
  message. These are optional in triggered contexts, and default to the
  trigger's sender and triggering nick. The `notice` argument is always
  optional, as before. However, if you were passing it positionally, its
  position has changed to accommodate the other new arguments, so you'll need
  to change that.
* `msg()` is considered deprecated, and will be removed from the documentation.
  However, since it would obviously be a serious pain for everyone to actually
  move away from it, it will continue to work without a warning for the time
  being.


## Reorganization of `sopel.tools`

A few things have been shifted around in `sopel.tools` for 5.3.0, splitting
the module up into a few smaller, easier to maintain modules. While they're
still importable directly from `willie.tools` in 5.3.0, they'll only be
importable from their new locations in 6.0.

## Static configuration sections

The documentation for the core configuration settings has always been lacking,
so we've come up with a way to make it document itself the same way we document
the API. However, to force ourselves to document it, we'll be disabling the
magic that lets you grab arbitrary keys from the core config. You'll only be
able to use the pre-defined ones. The sections for your own modules will stay
the same as they are now, unless you want to use this new functionality for
them. Only `config.core`, and possibly the sections for some of the modules we
include by default, will change.

## Refactoring of module loading

A bunch of stuff is getting moved around and refactored so that we can load
modules from folders. Unless you're messing with the loading internals in your
modules, this won't break anything for you.

## Removing ancient rule formats

This really only affects you if you're porting a phenny or jenni module. Those
bots supported callables with a tuple in the rule attribute. Willie quietly
accepted this, when you set the attribute directly rather than with a
decorator, though it was considered deprecated from 3.1. It added confusing
code with no clear benefit, so we've removed it.
