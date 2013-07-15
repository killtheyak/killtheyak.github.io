# -*- coding: utf-8 -*-

from urlparse import urljoin
from flask import render_template, request
from werkzeug.contrib.atom import AtomFeed
from flask_flatpages import pygments_style_defs
from app import app, pages

EXCLUDE_PAGES = ['contribute', 'TEMPLATE', 'example-dep', "README"]


def sort_by_updated(pages):
    '''Returns a list of pages sorted by the "updated" field.

    Exludes any of the pages in EXCLUDE_PAGES.
    '''
    return [page for page in sorted(pages,
                                    reverse=True,
                                    key=lambda p: p.meta['updated'])
                if page.path not in EXCLUDE_PAGES]

@app.route('/')
def home():
    all_pages = (p for p in pages if p.path not in EXCLUDE_PAGES)
    latest = sort_by_updated(all_pages)
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
    latest = sort_by_updated(filtered)
    return render_template('index.html', pages=latest, os=os)


@app.route('/tag/<string:tag>/')
def tag(tag):
    filtered = [p for p in pages if tag in p.meta.get('tags', [])]
    latest = sort_by_updated(filtered)
    return render_template('index.html', pages=latest, tag=tag)


def make_external(url):
    return urljoin(app.config["BASE_URL"], url)


@app.route('/feed/recent.atom')
def recent_feed():
    feed = AtomFeed('Kill The Yak - Recent Guides', feed_url=request.url,
        url=request.url_root)
    all_pages = [p for p in pages if p.path not in EXCLUDE_PAGES]
    if len(all_pages) >= 15:
        latest = sort_by_updated(all_pages)[:15]
    else:
        latest = sort_by_updated(all_pages)

    for page in latest:
        feed.add(page.meta['title'], page.body, content_type="html",
            author=page.meta.get('contributors', ["Anonymous"])[0],
            url=make_external(page.path),
            updated=page.meta['updated'],
            published=page.meta['updated'])
    return feed.get_response()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('manni'), 200, {'Content-Type': 'text/css'}
