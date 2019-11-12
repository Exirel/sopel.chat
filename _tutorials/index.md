---
title: Sopel tutorials
permalink: /tutorials/
---

Developers looking to write new functionality for Sopel should start here. This
tutorial sequence covers all the basics, from installing Sopel through to
documenting & distributing your plugins. We'll have you up to speed in no time!

Users who just want to _use_ Sopel without writing new code should read the
[installation tutorial]({% link _usage/installing.md %}) and then head for the
rest of the [usage]({% link _usage/index.md %}) articles.

{% assign tuts = site.tutorials | where_exp: "tut", "tut.url != page.url" %}
{% for tut in tuts %}
  * [{{ tut.title | replace: "Sopel tutorial, ", "" }}]({{ tut.url }})
{% endfor %}
