# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1665151168.7740605
_enable_loop = True
_template_filename = 'themes/jidn/templates/base.tmpl'
_template_uri = 'base.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'extra_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

    ns = runtime.TemplateNamespace('header', context._clean_inheritance_tokens(), templateuri='base_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'header')] = ns

    ns = runtime.TemplateNamespace('footer', context._clean_inheritance_tokens(), templateuri='base_footer.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'footer')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        date_fanciness = _import_ns.get('date_fanciness', context.get('date_fanciness', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        momentjs_locales = _import_ns.get('momentjs_locales', context.get('momentjs_locales', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        JIDN_theme = _import_ns.get('JIDN_theme', context.get('JIDN_theme', UNDEFINED))
        header = _mako_get_namespace(context, 'header')
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        footer = _mako_get_namespace(context, 'footer')
        js_date_format = _import_ns.get('js_date_format', context.get('js_date_format', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer(str(set_locale(lang)))
        __M_writer('\n')
        __M_writer(str(base.html_headstart()))
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        __M_writer(str(template_hooks['extra_head']()))
        __M_writer('\n</head>\n')
        if JIDN_theme:
            __M_writer('<body class="')
            __M_writer(str(JIDN_theme))
            __M_writer('">\n')
        else:
            __M_writer('<body>\n')
        __M_writer('    <a href="#content" class="sr-only sr-only-focusable">')
        __M_writer(str(messages("Skip to main content")))
        __M_writer('</a>\n    <!-- Target for toggling the sidebar `.sidebar-checkbox` is for regular\n            styles, `#sidebar-checkbox` for behavior. -->\n    <input type="checkbox" class="sidebar-checkbox" id="sidebar-checkbox">\n\n    <!-- Toggleable sidebar -->\n    <div class="sidebar" id="sidebar">\n')
        __M_writer('\n        ')
        __M_writer(str(header.html_navigation_links()))
        __M_writer('\n    </div>\n\n    <!-- Wrap is the content to shift when toggling the sidebar. We wrap the\n         content to avoid any CSS collisions with our real content. -->\n    <div class="wrap">\n      <div class="masthead">\n        <div class="container">\n          ')
        __M_writer(str(header.html_site_title()))
        __M_writer('\n        </div>\n      </div>\n      <div class="container content" id="content">\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n        ')
        __M_writer(str(footer.html_footer()))
        __M_writer('\n      </div>\n    </div>\n    <label for="sidebar-checkbox" class="sidebar-toggle"></label>\n    ')
        __M_writer(str(body_end))
        __M_writer('\n    ')
        __M_writer(str(template_hooks['body_end']()))
        __M_writer('\n    ')
        __M_writer(str(base.late_load_js()))
        __M_writer('\n    <!-- fancy dates -->\n    <script>\n    moment.locale("')
        __M_writer(str(momentjs_locales[lang]))
        __M_writer('");\n    fancydates(')
        __M_writer(str(date_fanciness))
        __M_writer(', ')
        __M_writer(str(js_date_format))
        __M_writer(');\n    </script>\n    <!-- end fancy dates -->\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/jidn/templates/base.tmpl", "uri": "base.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 0, "59": 2, "60": 3, "61": 4, "62": 5, "63": 5, "64": 6, "65": 6, "70": 9, "71": 10, "72": 10, "73": 12, "74": 13, "75": 13, "76": 13, "77": 14, "78": 15, "79": 17, "80": 17, "81": 17, "82": 29, "83": 30, "84": 30, "85": 38, "86": 38, "91": 42, "92": 43, "93": 43, "94": 47, "95": 47, "96": 48, "97": 48, "98": 49, "99": 49, "100": 52, "101": 52, "102": 53, "103": 53, "104": 53, "105": 53, "110": 56, "116": 7, "126": 7, "132": 42, "147": 56, "162": 147}}
__M_END_METADATA
"""
