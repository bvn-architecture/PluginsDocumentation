---
layout: page
permalink: /docs.html
title: "Docs"
excerpt: "Page containing documentation to some BVN software projects."
date: 2017-02-01 20:56:14 +1100
---

<ul>
	{% for page in site.pages %}
		{% if page.layout == "sample" %}
			<li class="sampleList">
				<h3>
					<a href="{% if site.baseurl == "/" %}{{ page.url }}{% else %}{{ page.url | prepend: site.baseurl }}{% endif %}" title="{{ page.title }}">{{ page.title }}</a>
					</h3>
					<time datetime="{{ page.date | date_to_xmlschema }}" class="by-line"> <i>{%if page.date %}{{ page.date | date_to_string }}{% endif %}</i> </time>
					<p>{%if page.excerpt %}{{ page.excerpt | strip_html | truncatewords:50 }}{% endif %}</p>
			</li>
		{% endif %}
	{% endfor %}
</ul>