---
title: Appendices
permalink: /appendix/
---

This appendix augments the [tutorials]({% link _tutorials/index.md %}) with
additional technical details for advanced plugin-writing, and includes some
older [usage]({% link _usage/index.md %}) guide material that probably isn't
relevant to most users.

{% assign docs = site.appendices | where_exp: "doc", "doc.url != page.url" | sort: "order" %}
{% for doc in docs %}
  * [{{ doc.title }}]({{ doc.url }})
{% endfor %}
