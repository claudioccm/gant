# -*- coding: utf-8 -*-

from os import path, getcwd, makedirs, listdir, remove
from yaml import load
from shutil import rmtree
from staticjinja import make_site

# We define constants for the deployment.
_SEARCHPATH = path.join(getcwd(), 'templates')
_OUTPUTPATH = path.join(getcwd(), 'site')

# We load the data we want to use in the templates.
_DATA = load(open('data/data.yaml'))


def load_data():
    ctx = {'data': _DATA, 'menu_sections': []}
    dic = {}

    # for index, item in enumerate(_DATA):
    #     aux = {'title': item['title'], 'url': 'article-%s.html' % index}

    #     if item['section'] not in dic:
    #         dic[item['section']] = [aux]

    #     else:
    #         dic[item['section']].append(aux)

    for section_name in sorted(dic.keys()):
        items = sorted(dic[section_name], key=lambda x: x['title'])

        ctx['menu_sections'].append({'name': section_name, 'items': items})

    return ctx


# def cleanup():
#     template = open('%s/article.html' % _SEARCHPATH).read()

#     # Remove publication templates that are no longer needed.
#     for filename in listdir(_SEARCHPATH):
#         filepath = '%s/%s' % (_SEARCHPATH, filename)

#         if filename.startswith('article-') and path.isfile(filepath):
#             remove(filepath)

#     # Clean the output folder.
#     if path.exists(_OUTPUTPATH):
#         rmtree(_OUTPUTPATH)

#     makedirs(_OUTPUTPATH)

#     for index, data in enumerate(_DATA):
#         new_file = open('%s/article-%s.html' % (_SEARCHPATH, index), 'w+')
#         new_page = template.replace('data[0]', 'data[%d]' % index)

#         new_file.write(new_page)
#         new_file.close()


if __name__ == '__main__':
    site = make_site(
        filters={},
        outpath=_OUTPUTPATH,
        contexts=[(r'.*.html', load_data)],
        searchpath=_SEARCHPATH,
        staticpaths=['static', '../data']
    )

    # cleanup()

    site.render(use_reloader=True)
