from staticjinja import make_site

context = {
    'number_requisitions_start_page': 4,
    'number_requisitions_per_page': 8,
    'number_suppliers_info_per_page': 6,
    'number_reviews': 2,
    'username': 'Леонид Федорович',
    'STATIC_URL': 'static/',
}

if __name__ == '__main__':
    site = make_site(
        searchpath='templates',
        outpath='rendered_site',
        staticpaths=['static'],
        contexts=[
            ('.*.html', context),
        ],
    )
    site.render()
