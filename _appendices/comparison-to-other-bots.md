---
title: Comparison to other bots (outdated)
migrated: true
source: wiki
order: 9000
---

This is an incomplete (and probably outdated) comparison of sopel, jenni, phenny, Supybot, Limnoria, and eggdrop. With Eggdrop, only limited research was done, so some information may be incorrect or missing.

# Core features

| Feature                          | sopel            | jenni            | phenny           | Supybot          | Limnoria         | Eggdrop          |
| -------------------------------- | ---------------- | ---------------- | ---------------- | ---------------- | ---------------- | ---------------- |
| Language                         | Python 2.7<br />Python 3 | Python 2.4-2.7 | Python 2.4-2.7 | Python 2.3-2.7   | Python 2.6-2.7<br />Python 3 | C, Tcl           |
| OS Support                       | Cross-platform   | Linux            | ?                | Cross-platform   | Cross-platform   | Cross-platform   |
| License                          | EFLv2            | EFLv2            | EFLv2            | BSD 3-clause     | BSD 3-clause     | GPL              |
| Last stable release              | 4.4.1; May 2014 | [N/A](#note1) | [N/A](#note1)    | 0.83.4.1; September 2012 | [N/A](#note1) | 1.8.1; March 2017 |
| Download sources                 | Fedora repos, AUR, PyPI, Git, tarball | Git, tarball | Git, tarball | Multiple Linux distro repos, Git, tarball | Multiple Linux distro repos, PyPI, Git, tarball | Multiple Linux distro repos, Git, tarball |
| Unicode support                  | Yes              | Limited          | Limited          | ?                | Yes              | Limited          |
| Dynamic plugin reloading         | Yes              | Yes              | Yes              | Yes              | Yes              | Yes              |
| Documented plugin API            | [Online]({{ site.docs }}) and in package | No | No | In package | [Online](http://limnoria.readthedocs.io/en/latest/develop/index.html) and in package | No            |
| API usability                    | Very simple, IDE friendly | Very simple | Very simple  | Complex, IDE friendly | ?           | Complex          |
| SSL support                      | Yes              | No               | No               | Yes              | Yes              | Yes              |
| Quickstart wizard                | Yes              | No               | No               | Yes              | Yes              | No               |
| Configuration                    | INI-like, dynamic | Python, static  | Python, static   | Flat text        | Flat text        | Flat text        |
| Daemonizable                     | Yes              | No               | No               | Yes              | Yes              | ?                |
| Daemonizable with systemd        | Yes              | No               | No               | No               | Yes              | Yes              |
| Persistent user/channel settings database | Yes     | No               | No               | Yes              | Yes              | No               |
| Safe inter-plugin communication  | Yes              | No               | No               | ?                | ?                | No               |
| RFC-compliant nick comparison    | Yes              | No               | No               | Yes              | Yes              | ?                |
| Command rate-limiting            | Yes              | Yes              | No               | Yes              | Yes              | ?                |
| Commands can override their rate limit (e.g. on failure) | Yes | No    | N/A              | No               | No               | ?                |
| Bot administration authentication | nick, hostmask  | nick, hostmask   | nick             | nick, hostmask   | nick, hostmask, GPG, network services | nick, hostmask, telnet  |
| Channel administration authentication | IRC modes   | Freenode services | N/A             | nick, hostmask   | nick, hostmask, GPG, network services | ?                |
| Unit testing system for core functionality | Yes    | No               | No               | Yes              | Yes              | ?                |
| Unit testing system for user plugins | Yes          | No               | No               | Yes              | Yes              | ?                |
| Block Disruptive Users           | [Yes]({% link _usage/ignoring-people.md %}) | [Yes](https://github.com/myano/jenni/wiki/Blocks) | No | Yes | Yes | Yes |
| [IRCv3](http://ircv3.org) support (including SASL authentication) | Yes | No | No | No | Yes | With third-party scripts               |
| IPv6                             | Yes              | No               | No               | Yes              | Yes              | Yes              |

1. <span id=note1 />phenny, jenni, and limnoria do not have discrete versioned releases. They are available as git repos or snapshot tarballs only.

# Plugin features

This section currently only compares between sopel, jenni, and phenny.

| Feature | sopel | jenni | phenny |
| ------- | ------ | ----- | ------ |
| Dynamic topic masks | Yes | No | No |
| Clock with per-user time zones | Yes, dynamic zones | Yes, static zones | Yes, static zones |
| Clock with per-channel time zones | Yes, dynamic zones | No | No |
| Weather information | Yahoo!, configurable default location | NOAA | NOAA |
| Meeting bot | Yes | No | No |


## Information provided for URLs

| Feature | sopel | jenni | phenny |
| ------- | ------ | ----- | ------ |
| Bugzilla bug data | Yes | No | No |
| Reddit post/user data | Yes | No | No |
| YouTube video data | Yes | No | No |
| Redmine ticket data | Third-party | No | No |
| Title | Yes | Yes | Yes |
