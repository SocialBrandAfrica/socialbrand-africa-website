# htmlmd.py - dependency-free HTML -> Markdown extractor for llms-full.txt
#
# Why hand-rolled instead of a pip package: build.py's whole design point is
# "no build deps" (see its header comment) so `python3 build.py` always just
# works, on any machine, with nothing to install first. Pulls in stdlib
# html.parser only.
#
# Scope: this is NOT a general HTML->Markdown converter. It's tuned to the
# exact tag vocabulary content_*.py actually emits inside a page's <main>
# body (checked by grepping every content_*.py for tag usage before writing
# this). Decorative/interactive chrome - script, style, svg and its children,
# forms, buttons, the empty <i> icon slots this codebase uses - is dropped
# entirely so llms-full.txt reads as prose, not markup soup.

from html.parser import HTMLParser
from html import unescape
import re

# Tags whose content contributes nothing to a text digest: markup/decoration
# (script, style, svg internals), the empty <i></i> / <i class="key"></i>
# icon slots this codebase uses (never semantic italics - <em> is used for
# that), and interactive form chrome (labels, inputs, buttons, textareas).
SKIP_TAGS = {
    "script", "style", "svg", "path", "g", "rect", "circle", "polyline",
    "i", "form", "input", "textarea", "button", "label", "fieldset", "legend",
}

HEADING_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6"}


class _Extractor(HTMLParser):
    def __init__(self, base_url):
        super().__init__(convert_charrefs=True)
        self.base_url = base_url.rstrip("/")
        self.out = []
        self.skip_depth = 0
        self.link_stack = []  # resolved href (or "") per open <a>, stack for nesting safety

    def _resolve(self, href):
        if not href or href.startswith("#") or href.lower().startswith("javascript:"):
            return ""
        if href.startswith("/"):
            return self.base_url + href
        if href.startswith("http://") or href.startswith("https://"):
            return href
        return ""

    def handle_starttag(self, tag, attrs):
        if tag in SKIP_TAGS:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag in HEADING_TAGS:
            self.out.append("\n\n" + ("#" * int(tag[1])) + " ")
        elif tag == "p":
            self.out.append("\n\n")
        elif tag == "li":
            self.out.append("\n- ")
        elif tag == "blockquote":
            self.out.append("\n\n> ")
        elif tag == "br":
            self.out.append("\n")
        elif tag in ("strong", "b"):
            self.out.append("**")
        elif tag == "em":
            self.out.append("*")
        elif tag == "a":
            href = self._resolve(dict(attrs).get("href", ""))
            self.link_stack.append(href)
            if href:
                self.out.append("[")
        # div/span/section/article/ul/ol/figure/figcaption/small fall through
        # untouched - they're layout wrappers here, not content.

    def handle_endtag(self, tag):
        if tag in SKIP_TAGS:
            self.skip_depth = max(0, self.skip_depth - 1)
            return
        if self.skip_depth:
            return
        if tag in ("strong", "b"):
            self.out.append("**")
        elif tag == "em":
            self.out.append("*")
        elif tag == "a":
            href = self.link_stack.pop() if self.link_stack else ""
            if href:
                self.out.append(f"]({href})")
        elif tag == "p":
            self.out.append("\n")

    def handle_data(self, data):
        if self.skip_depth:
            return
        self.out.append(data)

    def text(self):
        raw = unescape("".join(self.out))
        raw = re.sub(r"[ \t]+", " ", raw)
        raw = re.sub(r" *\n *", "\n", raw)
        raw = re.sub(r"\n{3,}", "\n\n", raw)
        return raw.strip()


def html_to_markdown(body_html, base_url):
    """Convert a page's body-fragment HTML into readable markdown prose."""
    ex = _Extractor(base_url)
    ex.feed(body_html)
    ex.close()
    return ex.text()
