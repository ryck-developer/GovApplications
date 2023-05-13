from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    _req_cookies_str = flow.request.headers.get("cookie", "")
    
    if _req_cookies_str:
        cookies = _req_cookies_str + '; hash=myAvMrR6XaFIYTAqh6xfYC9aNiPfng1O'
        flow.request.headers["cookie"] = cookies

def response(flow: http.HTTPFlow) -> None:
    if flow.response.headers["Content-Type"].startswith("text/html"):
        flow.response.content = flow.response.content.replace(b'class="kt-header__topbar-wrapper" data-toggle="dropdown" data-offset="0px,0px"', b'class="kt-header__topbar-wrapper"')
        flow.response.content = flow.response.content.replace(b'''<li class="kt-menu__item kt-menu__item--rel kt-menu__item--hover kt-menu__item--active kt-menu__item--here">
                                   <a href="/partners/" class="kt-menu__link">
                                     <span class="kt-menu__link-text kt-font-brand">Parceiros</span>
                                   </a>
                                </li>
                                <li class="kt-menu__item kt-menu__item--rel kt-menu__item--hover">
                                  <a href="https://t.me/adheart_english" class="kt-menu__link" target="_blank">
                                    <span class="kt-menu__link-text kt-font-brand"><i class="la pr-2"></i>Canal do Telegram</span>
                                  </a>
                                </li>''', b'')
        flow.response.content = flow.response.content.replace(b'''<li class="kt-menu__item kt-menu__item--rel kt-menu__item--hover ">
                                   <a href="/partners/" class="kt-menu__link">
                                     <span class="kt-menu__link-text kt-font-brand">Parceiros</span>
                                   </a>
                                </li>
                                <li class="kt-menu__item kt-menu__item--rel kt-menu__item--hover">
                                  <a href="https://t.me/adheart_english" class="kt-menu__link" target="_blank">
                                    <span class="kt-menu__link-text kt-font-brand"><i class="la pr-2"></i>Canal do Telegram</span>
                                  </a>
                                </li>''', b'')
