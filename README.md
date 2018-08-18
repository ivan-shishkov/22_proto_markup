# Suppliers in Novosibirsk

This is an example of the responsive website which is created with using of:

* Bootstrap 4
* Jinja2 template engine

Online version of the site is hosted on GitHub Pages and available [here](https://ivan-shishkov.github.io/22_proto_markup/rendered_site/).

# Quickstart

All the site's templates is located in the `templates/` directory (including static files - styles, images, icons).

To render site you need to launch the **build.py** script file.

For script launch need to install Python 3.5 and then install all dependencies:

```bash

$ pip install -r requirements.txt

```

Usage:

```bash

$ python3 build.py

```

Example of script launch on Linux:

```bash

$ python3 build.py
Rendering catalog_suppliers_all.html...
Rendering catalog_suppliers_spec.html...
Rendering index.html...
Rendering requisitions.html...
Copying static/css/styles.css to rendered_site/static/css/styles.css.
Copying static/img/company_logo.png to rendered_site/static/img/company_logo.png.
Copying static/img/favicon.ico to rendered_site/static/img/favicon.ico.
Copying static/img/logo.png to rendered_site/static/img/logo.png.
Copying static/img/profile.png to rendered_site/static/img/profile.png.

```

Rendered site will be stored in the `rendered_site/` directory.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
