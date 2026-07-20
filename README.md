# HTTP QUERY (RFC 10008) — ecosystem adoption

Day **0** = RFC publication **2026-06-16**. ★ Stars are approximate (fetched ~2026-07-20).

---

## Runtimes, frameworks & clients

| Stack | Status | Repo | ★ Stars | PR / issue | Days after RFC | Notes |
|---|---|---|---:|---|---|---|
| **Go (net/http)** | ⚠️ Manual | [golang/go](https://github.com/golang/go) | 135,304 | [Issue #80058](https://github.com/golang/go/issues/80058) — open · [PR #80134](https://github.com/golang/go/pull/80134) — open | **+2** issue · PR **+8** | Raw method strings work; `MethodQuery` proposal + PR not merged |
| **Node.js (core)** | ✅ Shipped | [nodejs/node](https://github.com/nodejs/node) | 118,327 | [v21.7.2 release](https://github.com/nodejs/node/releases/tag/v21.7.2) (llhttp 9.2.0) | **−804** | Earliest shipper |
| **Deno** | ⚠️ Open | [denoland/deno](https://github.com/denoland/deno) | 107,760 | [Issue #36186](https://github.com/denoland/deno/issues/36186) — open | **+34** | Feature request; `fetch()` may already accept method string |
| **FastAPI** | ❓ Nothing | [tiangolo/fastapi](https://github.com/tiangolo/fastapi) | 100,699 | none found | n/a | No dedicated RFC 10008 tracking found |
| **Bun** | ✅ Works (generic) | [oven-sh/bun](https://github.com/oven-sh/bun) | 94,911 | [Issue #34839](https://github.com/oven-sh/bun/issues/34839) — closed | **+34** | Bot verified `fetch` / `Bun.serve` / `node:http` + body; not full RFC semantics |
| **Django** | ❓ Nothing | [django/django](https://github.com/django/django) | 88,188 | none found | n/a | No dedicated RFC 10008 tracking found |
| **CPython (`http`)** | ⚠️ Open | [python/cpython](https://github.com/python/cpython) | 73,835 | [Issue #153309](https://github.com/python/cpython/issues/153309) — open · [PR #153310](https://github.com/python/cpython/pull/153310) — open | **+22** | Stdlib `http` module / method constant |
| **Express** | ✅ Works | [expressjs/express](https://github.com/expressjs/express) | 69,226 | [Issue #5615](https://github.com/expressjs/express/issues/5615) — closed completed | **−787** | No code PR; works on QUERY-capable Node |
| **Spring** | ❌ Not shipped | [spring-projects/spring-framework](https://github.com/spring-projects/spring-framework) | 60,128 | [PR #34993](https://github.com/spring-projects/spring-framework/pull/34993) — open (fixes [#32975](https://github.com/spring-projects/spring-framework/issues/32975)); [#36988](https://github.com/spring-projects/spring-framework/issues/36988) closed duplicate | **−378** · revived +15–17 | Community-approved Jul 3; still open |
| **Rails** | ⚠️ PR open | [rails/rails](https://github.com/rails/rails) | 58,634 | [PR #57973](https://github.com/rails/rails/pull/57973) — open ([forum](https://discuss.rubyonrails.org/t/proposal-support-for-the-http-query-method-rfc-10008/91255)) | **~+6** → PR **+17** | Core reviewed +30 |
| **requests** | ❌ Declined | [psf/requests](https://github.com/psf/requests) | 54,136 | [Issue #7558](https://github.com/psf/requests/issues/7558) — closed not planned · [PR #7577](https://github.com/psf/requests/pull/7577) — closed unmerged | **+18** / **+24** | No first-class `requests.query()`; raw method may still work |
| **curl** | ✅ Generic | [curl/curl](https://github.com/curl/curl) | 42,429 | none needed | n/a | `-X QUERY` works today |
| **PHP (CLI server)** | ✅ Merged | [php/php-src](https://github.com/php/php-src) | 40,245 | [PR #22615](https://github.com/php/php-src/pull/22615) — merged | **+20** · merged **+22** | Built-in dev server accepts QUERY (was 501) |
| **ASP.NET Core** | ⚠️ Preview | [dotnet/aspnetcore](https://github.com/dotnet/aspnetcore) | 38,222 | [PR #65714](https://github.com/dotnet/aspnetcore/pull/65714) — shipped in 11 Preview 4 | **−35** | OpenAPI recognizes QUERY as operation type |
| **Fastify** | ✅ Shipped (main) | [fastify/fastify](https://github.com/fastify/fastify) | 36,767 | [PR #6832](https://github.com/fastify/fastify/pull/6832) — merged · closes [#6807](https://github.com/fastify/fastify/issues/6807) | **+5** · merged **+30** | First-class QUERY; release tag TBC |
| **Laravel** | ⚠️ Partial | [laravel/framework](https://github.com/laravel/framework) | 34,802 | Client [PR #60663](https://github.com/laravel/framework/pull/60663) — merged · routing [PR #60810](https://github.com/laravel/framework/pull/60810) closed (defer L14); also [#60655](https://github.com/laravel/framework/pull/60655) | **+17** client | `Http::query()` on 13.x; full routing aimed at Laravel 14 |
| **OpenAPI** | ✅ Spec-level | [OAI/OpenAPI-Specification](https://github.com/OAI/OpenAPI-Specification) | 31,098 | [3.2.0 announcement](https://www.openapis.org/blog/2025/09/23/announcing-openapi-v3-2) | **−266** | — |
| **Axum** | ⚠️ Open | [tokio-rs/axum](https://github.com/tokio-rs/axum) | 26,571 | [Issue #3799](https://github.com/tokio-rs/axum/issues/3799) — open · [PR #3801](https://github.com/tokio-rs/axum/pull/3801) — open | **0** / **+1** | QUERY method routing |
| **Guzzle** | ✅ Works + redirects | [guzzle/guzzle](https://github.com/guzzle/guzzle) | 23,452 | [Issue #3699](https://github.com/guzzle/guzzle/issues/3699) — closed · [PR #3702](https://github.com/guzzle/guzzle/pull/3702) — merged | **+8** | Method string always worked; redirect middleware fixed for QUERY |
| **aiohttp** | ✅ Merged | [aio-libs/aiohttp](https://github.com/aio-libs/aiohttp) | 16,502 | [Issue #13160](https://github.com/aio-libs/aiohttp/issues/13160) — closed · [PR #13174](https://github.com/aio-libs/aiohttp/pull/13174) — merged | **+30** · merged **+34** | llhttp method table includes QUERY (C parser fix) |
| **hyper** | ✅ Via `http` | [hyperium/hyper](https://github.com/hyperium/hyper) | 16,232 | inherits [hyperium/http#798](https://github.com/hyperium/http/pull/798) | **0** | Uses `http::Method::QUERY` |
| **httpx** | ❓ Nothing | [encode/httpx](https://github.com/encode/httpx) | 15,356 | none found | n/a | Arbitrary methods usually work; no RFC tracking found |
| **reqwest** | ❌ Declined | [seanmonstar/reqwest](https://github.com/seanmonstar/reqwest) | 11,738 | [Issue #3056](https://github.com/seanmonstar/reqwest/issues/3056) — closed not planned | **0** | Re-exports / uses `http` crate methods |
| **Tomcat** | ✅ Merged | [apache/tomcat](https://github.com/apache/tomcat) | 8,211 | [PR #1026](https://github.com/apache/tomcat/pull/1026) — merged | **+15** | Release placement TBC |
| **undici** | ✅ Shipped | [nodejs/undici](https://github.com/nodejs/undici) | 7,651 | [Issue #5454](https://github.com/nodejs/undici/issues/5454) · [PR #5459](https://github.com/nodejs/undici/pull/5459) — merged | **+11** / **+13** · npm 8.6.0 at +16 | Node’s `fetch` implementation |
| **Jetty** | ⚠️ Open | [jetty/jetty.project](https://github.com/jetty/jetty.project) | 4,091 | [PR #15316](https://github.com/jetty/jetty.project/pull/15316) — open | **+5** | Targeted at Jetty 13.0.x (not 12.x) |
| **urllib3** | ❓ Nothing | [urllib3/urllib3](https://github.com/urllib3/urllib3) | 4,041 | none found | n/a | Underpins many Python clients |
| **Rust `http` crate** | ✅ Shipped | [hyperium/http](https://github.com/hyperium/http) | 1,362 | [PR #798](https://github.com/hyperium/http/pull/798) — merged · closes [#743](https://github.com/hyperium/http/issues/743) | **0** | `Method::QUERY`; safe + idempotent |
| **Jakarta Servlet** | ✅ Completed | [jakartaee/servlet](https://github.com/jakartaee/servlet) | 325 | [Issue #1068](https://github.com/jakartaee/servlet/issues/1068) — closed completed | **+9** · closed ≤+34 | Cites Tomcat PR |
| **W3C LWS** | ✅ Merged, contested | [w3c/lws-protocol](https://github.com/w3c/lws-protocol) | 26 | [PR #179](https://github.com/w3c/lws-protocol/pull/179) — merged | **+10** · merged **≈+34** | QUERY for Search / Type Index; GET/POST fallback still debated |

---

## Edge, proxies & caches

Infrastructure that sits in front of apps. Body-aware caching and method allow-lists matter most here (RFC 10008 §2.7).

| Stack | Status | Repo | ★ Stars | PR / issue | Days after RFC | Notes |
|---|---|---|---:|---|---|---|
| **Traefik** | ❓ Nothing | [traefik/traefik](https://github.com/traefik/traefik) | 64,053 | none found | n/a | No public RFC 10008 tracking found |
| **Kong** | ❓ Nothing | [Kong/kong](https://github.com/Kong/kong) | 43,822 | none found | n/a | No public RFC 10008 tracking found |
| **nginx** | ⚠️ Open | [nginx/nginx](https://github.com/nginx/nginx) | 31,171 | [PR #1488](https://github.com/nginx/nginx/pull/1488) — open · ([#1511](https://github.com/nginx/nginx/pull/1511) closed) | **+6** | Recognition only; body cache key TBD |
| **Envoy** | ❓ Nothing | [envoyproxy/envoy](https://github.com/envoyproxy/envoy) | 28,606 | none found | n/a | No public RFC 10008 tracking found |
| **Cloudflare workerd** | ⚠️ Open | [cloudflare/workerd](https://github.com/cloudflare/workerd) | 8,411 | [Issue #6849](https://github.com/cloudflare/workerd/issues/6849) — open | **+14** | Body-keyed QUERY caching (Cache API) |
| **HAProxy** | ❓ Nothing | [haproxy/haproxy](https://github.com/haproxy/haproxy) | 6,713 | none found | n/a | No public RFC 10008 tracking found |
| **Varnish** | ❓ Nothing | [varnishcache/varnish-cache](https://github.com/varnishcache/varnish-cache) | 4,049 | none found | n/a | Cache key for QUERY body untracked |
| **Apache httpd** | ❓ Nothing | [apache/httpd](https://github.com/apache/httpd) | 4,034 | none found | n/a | Passthrough / proxy path; discuss on [dev@httpd](https://lists.apache.org/list.html?dev@httpd.apache.org) |
| **Squid** | ❓ Nothing | [squid-cache/squid](https://github.com/squid-cache/squid) | 3,027 | none found | n/a | No public RFC 10008 tracking found |
| **Managed CDNs** (CloudFront, Fastly, Akamai, ALB, …) | ❓ Opaque | — | — | vendor docs / changelogs | n/a | Hard to track via GitHub; verify per product |

---

## Specs & documentation

| Stack | Status | Repo | ★ Stars | PR / issue | Days after RFC | Notes |
|---|---|---|---:|---|---|---|
| **WHATWG HTML** | ⚠️ Open | [whatwg/html](https://github.com/whatwg/html) | 9,329 | [Issue #12594](https://github.com/whatwg/html/issues/12594) — open | **+1** | `<form method="query">`; needs implementer interest |
| **MDN** | ⚠️ Open | [mdn/content](https://github.com/mdn/content) | 10,886 | [PR #44568](https://github.com/mdn/content/pull/44568) — open · [Issue #44665](https://github.com/mdn/content/issues/44665) — open | **+8** / **+22** | QUERY method + `Accept-Query` docs |
| **Browsers / fetch()** | ✅ Works, unofficial | [whatwg/fetch](https://github.com/whatwg/fetch) | 2,243 | [Issue #1938](https://github.com/whatwg/fetch/issues/1938) — open | **+14** | [Mozilla #1430](https://github.com/mozilla/standards-positions/issues/1430) open · [WebKit #692](https://github.com/WebKit/standards-positions/issues/692) closed invalid |
| **RFC 10008** | ✅ Published | [IETF HTTP WG](https://datatracker.ietf.org/wg/httpbis/) | — | [RFC 10008](https://datatracker.ietf.org/doc/rfc10008/) | **0** | IESG approval Nov 20, 2025 = −208; label [`query-method`](https://github.com/httpwg/http-extensions/labels/query-method) |

---

## Related trackers

- [jeswr/http-query-adoption](https://github.com/jeswr/http-query-adoption)
- Digest-based QUERY cache negotiation (proposal): [httpwg/http-extensions#3469](https://github.com/httpwg/http-extensions/issues/3469) → HTTP WG list
