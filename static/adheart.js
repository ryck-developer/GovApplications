document.addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
});

async function handleRequest(request) {
  const newRequest = new Request(request)
  newRequest.headers.set("Referer", 'https://adheart.me/');
  newRequest.headers.set("Cookie", request.headers.get("Cookie") + '; hash=BdmJxIlRQpUpIzNCvmXRp3ZgPXbWSQ3v');
  var url = new URL(request.url)
  url.hostname = "adheart.me"
  let response = await fetch(url, newRequest)
    if (response.headers.get('Content-Type') && response.headers.get('Content-Type').startsWith("text/html")) {
    let html = await response.text();
    html = html.replace('</body>', `<script>
document.addEventListener("DOMContentLoaded", () => {const elm = document.querySelectorAll('.kt-header__topbar-item.kt-header__topbar-item--user')[2];elm.remove();});                </script>
            </body>`);
    html = html.replace('/cdn-cgi/challenge-platform/h/b/scripts/alpha', '');
    return new Response(html, {
      headers: response.headers
    });
  }
    console.log(response);
  return response;
}
