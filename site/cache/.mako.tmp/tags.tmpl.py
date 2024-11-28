# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1732806088.2880208
_enable_loop = True
_template_filename = '/usr/local/python/3.12.1/lib/python3.12/site-packages/nikola/data/themes/base/templates/tags.tmpl'
_template_uri = 'tags.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('feeds_translations', context._clean_inheritance_tokens(), templateuri='feeds_translations_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'feeds_translations')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        items = _import_ns.get('items', context.get('items', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        cat_items = _import_ns.get('cat_items', context.get('cat_items', UNDEFINED))
        cat_hierarchy = _import_ns.get('cat_hierarchy', context.get('cat_hierarchy', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        range = _import_ns.get('range', context.get('range', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        hidden_tags = _import_ns.get('hidden_tags', context.get('hidden_tags', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(feeds_translations.head(kind=kind, feeds=False)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        items = _import_ns.get('items', context.get('items', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        def content():
            return render_content(context)
        cat_items = _import_ns.get('cat_items', context.get('cat_items', UNDEFINED))
        cat_hierarchy = _import_ns.get('cat_hierarchy', context.get('cat_hierarchy', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        range = _import_ns.get('range', context.get('range', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        hidden_tags = _import_ns.get('hidden_tags', context.get('hidden_tags', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n<article class="tagindex">\n    <header>\n        <h1>')
        __M_writer(filters.html_escape(str(title)))
        __M_writer('</h1>\n        <div class="metadata">\n            ')
        __M_writer(str(feeds_translations.translation_link(kind)))
        __M_writer('\n        </div>\n    </header>\n')
        if cat_items:
            pass
            if items:
                __M_writer('            <h2>')
                __M_writer(str(messages("Categories")))
                __M_writer('</h2>\n')
            for text, full_name, path, link, indent_levels, indent_change_before, indent_change_after in cat_hierarchy:
                pass
                for i in range(indent_change_before):
                    __M_writer('                <ul class="postlist">\n')
                __M_writer('            <li><a class="reference" href="')
                __M_writer(str(link))
                __M_writer('">')
                __M_writer(str(text))
                __M_writer('</a>\n')
                if indent_change_after <= 0:
                    __M_writer('                </li>\n')
                for i in range(-indent_change_after):
                    __M_writer('                </ul>\n')
                    if i + 1 < len(indent_levels):
                        __M_writer('                    </li>\n')
            if items:
                __M_writer('            <h2>')
                __M_writer(str(messages("Tags")))
                __M_writer('</h2>\n')
        if items:
            __M_writer('        <ul class="postlist">\n')
            for text, link in items:
                pass
                if text not in hidden_tags:
                    __M_writer('                <li><a class="reference listtitle" href="')
                    __M_writer(str(link))
                    __M_writer('">')
                    __M_writer(filters.html_escape(str(text)))
                    __M_writer('</a></li>\n')
            __M_writer('        </ul>\n')
        __M_writer('</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/usr/local/python/3.12.1/lib/python3.12/site-packages/nikola/data/themes/base/templates/tags.tmpl", "uri": "tags.tmpl", "source_encoding": "utf-8", "line_map": {"23": 3, "29": 0, "50": 2, "51": 3, "56": 7, "61": 50, "67": 5, "77": 5, "78": 6, "79": 6, "85": 9, "103": 9, "104": 12, "105": 12, "106": 14, "107": 14, "108": 17, "110": 18, "111": 19, "112": 19, "113": 19, "114": 21, "116": 22, "117": 23, "118": 25, "119": 25, "120": 25, "121": 25, "122": 25, "123": 26, "124": 27, "125": 29, "126": 30, "127": 31, "128": 32, "129": 36, "130": 37, "131": 37, "132": 37, "133": 40, "134": 41, "135": 42, "137": 43, "138": 44, "139": 44, "140": 44, "141": 44, "142": 44, "143": 47, "144": 49, "150": 144}}
__M_END_METADATA
"""
