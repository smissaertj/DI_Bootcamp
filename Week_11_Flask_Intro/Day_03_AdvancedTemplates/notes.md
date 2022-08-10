# Statements
Because html doesn’t support indentation, we close the statements with an {% endstatement %} section.

A few statements are available in jinja2, for example:
```
{% if %}
{% for %}
{% block %}
```
And their close statements:
```
{% endif %}
{% endfor %}
{% endblock %}
```

## If Statement
Jinja2 if statements behave exactly the same as python if and else, you just need to surround those statements with `{% %}`.
```
{% if name == "Rick" %}
    <p> Hello Rick </p>
{% else %}
    <p> Who are you ? </p>
{% endif %}
```
If the condition after the if is True, the code under the if will be generated, else, the code under the else will be 
added to the html.


## For Loops
For loops also exist in jinja2, the loop will generate some code into the html.
You can add variables in the loop to make your loop dynamic.
For example, we can populate a list with a for loop:

```
<ul>
{% for name in ["Rick", "Morty", "Summer"] %}
    <li><p> Hello {{ name }}! </p></li>
{% endfor %}
</ul>
```
The rendered code will be:
```
<ul>
    <li><p>Hello Rick!</p></li>
    <li><p>Hello Morty!</p></li>
    <li><p>Hello Summer!</p></li>
</ul>
```
---
# Template Inheritance: Add A Placeholder Block Of Code

The most powerful part of Jinja is template inheritance.

Template inheritance allows you to build a base “skeleton” template that contains all the common elements of your site and defines blocks that child templates can override.

Here is how to do it:

**In the parent template:**

`{% block my_block %}{% endblock %}` remain a part of code empty in a template.
This statement is a placeholder for some code that will be injected later in another template.

**In the child template:**

You need to specify that you are extending the parent template, with `{% extends "name_of_the_template.html" %}`.
Then you need to open the `{% block my_block %}` tag and write the code that you want to inject in the parent template.

You can add more than one block, and then give them another name.

**Example**
Parent:
```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>{% block title %}{% endblock %}</title>
    </head>
    <body>
    {% block body %}
        <h1>This heading is defined in the parent layout page</h1>
    {% endblock %}
    </body>
</html>
```

Child:
```
{% extends "layout.html" %}
{% block title %}Hello world!{% endblock %}
{% block body %}
    {{ super() }}
    <h2>This heading is defined in the child index page.</h2>
{% endblock %}
```

