# -*- coding: utf-8 -*-

from flask import render_template
from flask_flatpages import pygments_style_defs
from app import app, pages

EXCLUDE_PAGES = ['contribute', 'TEMPLATE', 'example-dep', "README"]


@app.route('/')
def home():
    all_pages = (p for p in pages if p.path not in EXCLUDE_PAGES)
    latest = sorted(all_pages, reverse=True, key=lambda p: p.meta['updated'])
    return render_template('index.html', pages=latest)


@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    dep_list = page.meta.get('deps', [])
    dep_pages = [pages.get(dep) for dep in dep_list]
    template = page.meta.get('template', 'page.html')
    return render_template(template, page=page, deps=dep_pages)


@app.route('/contribute/')
def contribute():
    page = pages.get_or_404('contribute')
    return render_template('page.html', page=page)


@app.route('/os/<string:os>/')
def os(os):
    filtered = [p for p in pages if os in p.meta.get('os', [])]
    # Fix capitalization of MacOSX
    if os.lower() == 'macosx':
        os = 'MacOSX'
    else:
        os = os
    return render_template('index.html', pages=filtered, os=os)


@app.route('/tag/<string:tag>/')
def tag(tag):
    filtered = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('index.html', pages=filtered, tag=tag)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('manni'), 200, {'Content-Type': 'text/css'}
