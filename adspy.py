from mitmproxy import http

def response(flow: http.HTTPFlow) -> None:
    if "Content-Type" not in flow.response.headers:
        return
    if flow.response.headers["Content-Type"].startswith("application/javascript"):
        flow.response.content = flow.response.content.replace(b"window.location.hostname", b'"app.adspy.com"')
        flow.response.content = flow.response.content.replace(b"api.adspy.com", b"localhost:8081")
    if flow.response.headers["Content-Type"].startswith("text/html"):
        flow.response.content = flow.response.content.replace(b"api.adspy.com", b"localhost:8081")
        flow.response.content = flow.response.content.replace(b'</body>', b'''
                <script>
                    if (!localStorage.auth_token) {
                        localStorage.auth_token = "Jba-Y3MuFI9OGe1Iz-I8KVmEWZ118w13klAyiEwqlf55rj1AXnzXepMDZ6zaYjCM5aZZynZlC21-MrOy2QcOKfryS01a_y4uUgtZ4RlyFS1bTCPNNwi5z0PoP7hd2INmgo8pqYv2FCPSlY1BezkKoi3yuS83PsmPxhAOm46-fqQMQGc0l0nzHhod2tTO8rCmOnGq0TdZ98yBlU4xFYKyOoLJYbWHQs0uYawXeaue5g1pfLIhwoMt4Ce_6fLNhF7vLhff9ZB5Hohfw91duO5q0TWF91KmA0cv1mzCRawqn1jAWFOBAb507dUgW_deqo-qvf3jFCNghBs1B7tALmxazuDRpr5I7SKGoUe1RT6BN0jonvv6RUD2fePFo1z5tqyZPXYrRN3m4LF7sU4yn7Ktmto9Gnlr71Yxt028mpkKC_WPAemLVmc6ddC7QwIUg9Nbn_MatRCY-2-K6qRBJJNQ7UYaBsXobinkFMT3FYxV2kSJjwbyO4FTuknHqydorxYM06fvLm1rV30Yxuz072YCdW4SkpNLld3_0wsSdlflAE8";
                        location.reload();
                    }
                    document.querySelector('.topbar-menu.fadeInDown').remove();
                </script>
            </body>
        ''')
