# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1608250661.160765
_enable_loop = True
_template_filename = 'themes/jidn/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'sharing', 'bio']



def social_link(url):
    try:
        from urlparse import urlparse
    except ImportError:
        from urllib.parse import urlparse

    o = urlparse(url)
    site = o.netloc.lower()
    substitute = dict((('Github', 'GitHub'),
                     ('Stackoverflow', 'StackOverflow'),
                     ('stackoverflow', 'stack-overflow'),
                     ('Youtube', 'YouTube'),
                     ('Linkedin', 'LinkedIn'),
                     ('Whatsapp', 'WhatsApp'),
                     ('Bizsugar', 'BizSugar'),
                     ))
    if site == "plus.google.com":
        icon = "google-plus"
        title = "Google+"
    else:
        try:
            icon = o.netloc.split('.')[-2]
        except Exception as err:
            print(err)
            raise err
            return ''
        title = substitute.get(icon.title(), icon.title())
        icon = substitute.get(icon, icon)

    rv = '''<a href="{url}" target="_blank" arial-label="Go to {title}"> <i class="fa fa-fw fa-{icon}" aria-hidden="true" title="{title}" /></a>'''.format(url=url, icon=icon, title=title)
    return rv


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('pheader', context._clean_inheritance_tokens(), templateuri='post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pheader')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        pheader = _mako_get_namespace(context, 'pheader')
        math = _mako_get_namespace(context, 'math')
        comments = _mako_get_namespace(context, 'comments')
        def bio():
            return render_bio(context._locals(__M_locals))
        helper = _mako_get_namespace(context, 'helper')
        parent = context.get('parent', UNDEFINED)
        post = context.get('post', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        def sharing():
            return render_sharing(context._locals(__M_locals))
        JIDN = context.get('JIDN', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sharing'):
            context['self'].sharing(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bio'):
            context['self'].bio(**pageargs)
        

        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        math = _mako_get_namespace(context, 'math')
        parent = context.get('parent', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        helper = _mako_get_namespace(context, 'helper')
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if post.meta('keywords'):
            __M_writer('    <meta name="keywords" content="')
            __M_writer(filters.html_escape(str(post.meta('keywords'))))
            __M_writer('">\n')
        __M_writer('    <meta name="author" content="')
        __M_writer(filters.html_escape(str(post.author())))
        __M_writer('">\n')
        if post.prev_post:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(post.prev_post.permalink()))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.prev_post.title())))
            __M_writer('" type="text/html">\n')
        if post.next_post:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(post.next_post.permalink()))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.next_post.title())))
            __M_writer('" type="text/html">\n')
        if post.is_draft:
            __M_writer('        <meta name="robots" content="noindex">\n')
        __M_writer('    ')
        __M_writer(str(helper.open_graph_metadata(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.twitter_card_information(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.meta_translations(post)))
        __M_writer('\n    ')
        __M_writer(str(math.math_styles_ifpost(post)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        pheader = _mako_get_namespace(context, 'pheader')
        math = _mako_get_namespace(context, 'math')
        comments = _mako_get_namespace(context, 'comments')
        def bio():
            return render_bio(context)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        def content():
            return render_content(context)
        def sharing():
            return render_sharing(context)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<article class="post-')
        __M_writer(str(post.meta('type')))
        __M_writer(' h-entry hentry postpage" itemscope="itemscope" itemtype="http://schema.org/BlogPosting">\n    ')
        __M_writer(str(pheader.html_post_header()))
        __M_writer('\n    <section class="e-content entry-content" itemprop="articleBody text">\n    ')
        __M_writer(str(post.text()))
        __M_writer('\n    </section>\n    ')
        __M_writer(str(sharing()))
        __M_writer('\n    ')
        __M_writer(str(bio()))
        __M_writer('\n')
        __M_writer('\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('        <section class="comments hidden-print">\n        <h2>')
            __M_writer(str(messages("Comments")))
            __M_writer('</h2>\n        ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post._base_path)))
            __M_writer('\n        </section>\n')
        __M_writer('    ')
        __M_writer(str(math.math_scripts_ifpost(post)))
        __M_writer('\n</article>\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sharing(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def sharing():
            return render_sharing(context)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<aside class="sharing no-print">\n    <a href="#content" aria-label="Post beginning">\n       <i class="fa fa-2x fa-fw fa-arrow-circle-up" aria-hidden="true" title="Post beginning" />\n    </a>\n')
        if post.prev_post:
            __M_writer('    <a href="')
            __M_writer(str(post.prev_post.permalink(absolute=True)))
            __M_writer('" rel="prev" title="')
            __M_writer(filters.html_escape(str(post.prev_post.title())))
            __M_writer('">\n       <i class="fa fa-2x fa-fw fa-arrow-circle-left" aria-hidden="true" title="Previous post: ')
            __M_writer(filters.html_escape(str(post.prev_post.title())))
            __M_writer('" />\n    </a>\n')
        if post.next_post:
            __M_writer('    <a href="')
            __M_writer(str(post.next_post.permalink(absolute=True)))
            __M_writer('" rel="next" title="Next post: ')
            __M_writer(filters.html_escape(str(post.next_post.title())))
            __M_writer('" aria-label="Next post: ')
            __M_writer(filters.html_escape(str(post.next_post.title())))
            __M_writer('">\n       <i class="fa fa-2x fa-fw fa-arrow-circle-right" aria-hidden="true" />\n    </a>\n')
        __M_writer('    <span class="post-sharing">\n     <a href="http://twitter.com/share?text=')
        __M_writer(filters.url_escape(str(post.title())))
        __M_writer('&url=')
        __M_writer(filters.url_escape(str(post.permalink(absolute=True))))
        __M_writer('"\n      onclick="window.open(this.href, \'twitter-share\', \'width=550,height=235\');return false;"\n      aria-label="Share on Twitter">\n       <i class="fa fa-2x fa-fw fa-twitter-square" aria-hidden="true" title="Share on Twitter" /i>\n     </a>\n     <a href="https://www.facebook.com/sharer/sharer.php?u=')
        __M_writer(filters.url_escape(str(post.permalink(absolute=True))))
        __M_writer('"\n      onclick="window.open(this.href, \'facebook-share\',\'width=580,height=296\');return false;"\n      aria-label="Share on Facebook">\n       <i class="fa fa-2x fa-fw fa-facebook-square" style="margin-left: -8px" aria-hidden="true" title="Share of Facebook" /i>\n     </a>\n     <a href="https://plus.google.com/share?url=')
        __M_writer(filters.url_escape(str(post.permalink(absolute=True))))
        __M_writer('" aria-label="Share on Google+"\n      onclick="window.open(this.href, \'google-plus-share\', \'width=490,height=530\');return false;">\n       <i class="fa fa-2x fa-fw fa-google-plus-square" style="margin-left: -8px" aria-hidden="true" title="Share on Google+" /i>\n     </a>\n     </span>\n</aside>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bio(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bio():
            return render_bio(context)
        post = context.get('post', UNDEFINED)
        JIDN = context.get('JIDN', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div itemprop="author" itemscope itemtype="http://schema.org/Person">\n')
        if post.author() in JIDN:
            __M_writer('<footer class="byline author author-bio vcard">\n    <hr/>\n     <meta itemprop="image" content="')
            __M_writer(str(JIDN[post.author()]['image']))
            __M_writer('"/>\n     <div class="author-image" style="background: url(')
            __M_writer(str(JIDN[post.author()]['image']))
            __M_writer(')" />\n     <h3 class="byline-name fn" itemprop="name">')
            __M_writer(filters.trim(str(post.author())))
            __M_writer('\n')
            if 'email' in JIDN[post.author()]:
                __M_writer('        <span class=\'post-sharing\'>\n            <a href="mailto:')
                __M_writer(str(JIDN[post.author()]['email']))
                __M_writer('?subject=')
                __M_writer(filters.html_escape(str(post.title())))
                __M_writer('"\n            aria-label="Email author">\n            <i class="fa fa-2 fa-fw fa-envelope" aria-hidden="true" title="Email author" /i>\n            </a>\n        </span>\n')
            if 'social' in JIDN[post.author()]:
                __M_writer("        <span class='post-sharing'>\n")
                for url in JIDN[post.author()]['social']:
                    __M_writer('            ')
                    __M_writer(social_link(str(url)))
                    __M_writer('\n')
                __M_writer('        </span>\n')
            __M_writer('     </h3>\n')
            if 'bio' in JIDN[post.author()]:
                __M_writer('     <p class="bio">')
                __M_writer(str(JIDN[post.author()]['bio']))
                __M_writer('</p>\n')
            if 'map' in JIDN[post.author()]:
                __M_writer('     <p><i class="fa fa-map-marker"/> ')
                __M_writer(str(JIDN[post.author()]['map']))
                __M_writer('</p>\n')
            __M_writer('</footer>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/jidn/templates/post.tmpl", "uri": "post.tmpl", "source_encoding": "utf-8", "line_map": {"16": 126, "17": 127, "18": 128, "19": 129, "20": 130, "21": 131, "22": 132, "23": 133, "24": 134, "25": 135, "26": 136, "27": 137, "28": 138, "29": 139, "30": 140, "31": 141, "32": 142, "33": 143, "34": 144, "35": 145, "36": 146, "37": 147, "38": 148, "39": 149, "40": 150, "41": 151, "42": 152, "43": 153, "44": 154, "45": 155, "46": 156, "47": 157, "48": 158, "49": 159, "57": 2, "60": 3, "63": 4, "66": 5, "72": 0, "94": 2, "95": 3, "96": 4, "97": 5, "98": 6, "103": 27, "108": 54, "113": 88, "118": 124, "119": 158, "125": 8, "135": 8, "136": 9, "137": 9, "138": 10, "139": 11, "140": 11, "141": 11, "142": 13, "143": 13, "144": 13, "145": 14, "146": 15, "147": 15, "148": 15, "149": 15, "150": 15, "151": 17, "152": 18, "153": 18, "154": 18, "155": 18, "156": 18, "157": 20, "158": 21, "159": 23, "160": 23, "161": 23, "162": 24, "163": 24, "164": 25, "165": 25, "166": 26, "167": 26, "173": 29, "189": 29, "190": 30, "191": 30, "192": 31, "193": 31, "194": 33, "195": 33, "196": 35, "197": 35, "198": 36, "199": 36, "200": 44, "201": 45, "202": 46, "203": 47, "204": 47, "205": 48, "206": 48, "207": 51, "208": 51, "209": 51, "210": 53, "211": 53, "217": 56, "224": 56, "225": 61, "226": 62, "227": 62, "228": 62, "229": 62, "230": 62, "231": 63, "232": 63, "233": 66, "234": 67, "235": 67, "236": 67, "237": 67, "238": 67, "239": 67, "240": 67, "241": 71, "242": 72, "243": 72, "244": 72, "245": 72, "246": 77, "247": 77, "248": 82, "249": 82, "255": 91, "263": 91, "264": 93, "265": 94, "266": 96, "267": 96, "268": 97, "269": 97, "270": 98, "271": 98, "272": 99, "273": 100, "274": 101, "275": 101, "276": 101, "277": 101, "278": 107, "279": 108, "280": 109, "281": 110, "282": 110, "283": 110, "284": 112, "285": 114, "286": 115, "287": 116, "288": 116, "289": 116, "290": 118, "291": 119, "292": 119, "293": 119, "294": 121, "300": 294}}
__M_END_METADATA
"""
