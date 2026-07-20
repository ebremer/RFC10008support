# HTTP QUERY (RFC 10008) — ecosystem adoption

Day **0** = RFC publication **2026-06-16**. ★ Stars are approximate (fetched ~2026-07-20).

Tracking is split by role: **servers** (inbound), **clients** (outbound), **edge** (proxies/caches), and **specs/docs**. The same monorepo can appear in more than one table when server and client surfaces differ (e.g. Spring Framework). Stack names link to the project home when available.

---

## Servers & frameworks (inbound)

Stacks that **accept** or **route** QUERY.

| Stack | Status | ★ Stars | PR / issue | Days after RFC | Notes |
|---|---|---:|---|---|---|
| [**Go (net/http)**](https://github.com/golang/go) | ⚠️ Manual | 135,304 | [Issue #80058](https://github.com/golang/go/issues/80058) — open · [PR #80134](https://github.com/golang/go/pull/80134) — open | **+2** issue · PR **+8** | Raw method strings work; `MethodQuery` not merged |
| [**Node.js (core)**](https://github.com/nodejs/node) | ✅ Shipped | 118,327 | [v21.7.2 release](https://github.com/nodejs/node/releases/tag/v21.7.2) (llhttp 9.2.0) | **−804** | Earliest shipper (parse/route QUERY) |
| [**Deno**](https://github.com/denoland/deno) | ⚠️ Open | 107,760 | [Issue #36186](https://github.com/denoland/deno/issues/36186) — open | **+34** | Feature request; `Deno.serve` may accept method string |
| [**FastAPI**](https://github.com/tiangolo/fastapi) | ❓ Nothing | 100,699 | none found | n/a | No dedicated RFC 10008 tracking found |
| [**Bun**](https://github.com/oven-sh/bun) | ✅ Works (generic) | 94,911 | [Issue #34839](https://github.com/oven-sh/bun/issues/34839) — closed | **+34** | `Bun.serve` + body verified; not full RFC semantics |
| [**Django**](https://github.com/django/django) | ❓ Nothing | 88,188 | none found | n/a | No dedicated RFC 10008 tracking found |
| [**CPython (`http.server`)**](https://github.com/python/cpython) | ⚠️ Open | 73,835 | [Issue #153309](https://github.com/python/cpython/issues/153309) — open · [PR #153310](https://github.com/python/cpython/pull/153310) — open | **+22** | Stdlib HTTP support / method constant (shared issue with client) |
| [**Express**](https://github.com/expressjs/express) | ✅ Works | 69,226 | [Issue #5615](https://github.com/expressjs/express/issues/5615) — closed completed | **−787** | Works on QUERY-capable Node |
| [**Spring MVC / WebFlux**](https://github.com/spring-projects/spring-framework) | ❌ Not shipped | 60,128 | [PR #34993](https://github.com/spring-projects/spring-framework/pull/34993) — open (fixes [#32975](https://github.com/spring-projects/spring-framework/issues/32975)); [#36988](https://github.com/spring-projects/spring-framework/issues/36988) closed duplicate | **−378** · revived +15–17 | `RequestMethod` / `@RequestMapping` QUERY; community-approved Jul 3 |
| [**Rails**](https://github.com/rails/rails) | ⚠️ PR open | 58,634 | [PR #57973](https://github.com/rails/rails/pull/57973) — open ([forum](https://discuss.rubyonrails.org/t/proposal-support-for-the-http-query-method-rfc-10008/91255)) | **~+6** → PR **+17** | Core reviewed +30 |
| [**PHP (CLI server)**](https://github.com/php/php-src) | ✅ Merged | 40,245 | [PR #22615](https://github.com/php/php-src/pull/22615) — merged | **+20** · merged **+22** | Built-in dev server accepts QUERY (was 501) |
| [**ASP.NET Core**](https://github.com/dotnet/aspnetcore) | ⚠️ Preview | 38,222 | [PR #65714](https://github.com/dotnet/aspnetcore/pull/65714) — shipped in 11 Preview 4 | **−35** | Server + OpenAPI operation type |
| [**Fastify**](https://github.com/fastify/fastify) | ✅ Shipped (main) | 36,767 | [PR #6832](https://github.com/fastify/fastify/pull/6832) — merged · closes [#6807](https://github.com/fastify/fastify/issues/6807) | **+5** · merged **+30** | First-class QUERY routing; release tag TBC |
| [**Laravel (routing)**](https://github.com/laravel/framework) | ⚠️ Deferred | 34,802 | [PR #60810](https://github.com/laravel/framework/pull/60810) closed (L14); [#60655](https://github.com/laravel/framework/pull/60655) | **+30** | Full route support aimed at Laravel 14 |
| [**Axum**](https://github.com/tokio-rs/axum) | ⚠️ Open | 26,571 | [Issue #3799](https://github.com/tokio-rs/axum/issues/3799) — open · [PR #3801](https://github.com/tokio-rs/axum/pull/3801) — open | **0** / **+1** | QUERY method routing |
| [**aiohttp (server)**](https://github.com/aio-libs/aiohttp) | ✅ Merged | 16,502 | [Issue #13160](https://github.com/aio-libs/aiohttp/issues/13160) — closed · [PR #13174](https://github.com/aio-libs/aiohttp/pull/13174) — merged | **+30** · merged **+34** | C parser recognizes QUERY |
| [**Tomcat**](https://github.com/apache/tomcat) | ✅ Merged | 8,211 | [PR #1026](https://github.com/apache/tomcat/pull/1026) — merged | **+15** | Release placement TBC |
| [**Jetty**](https://github.com/jetty/jetty.project) | ⚠️ Open | 4,091 | [PR #15316](https://github.com/jetty/jetty.project/pull/15316) — open | **+5** | Targeted at Jetty 13.0.x (not 12.x) |
| [**Undertow**](https://github.com/undertow-io/undertow) | ❓ Nothing | 3,756 | none found | n/a | Servlet container (Spring Boot option); no RFC tracking found |
| [**Jakarta Servlet**](https://github.com/jakartaee/servlet) | ✅ Completed | 325 | [Issue #1068](https://github.com/jakartaee/servlet/issues/1068) — closed completed | **+9** · closed ≤+34 | Spec-level container contract; cites Tomcat PR |
| [**W3C LWS**](https://github.com/w3c/lws-protocol) | ✅ Merged, contested | 26 | [PR #179](https://github.com/w3c/lws-protocol/pull/179) — merged | **+10** · merged **≈+34** | QUERY for Search / Type Index; GET/POST fallback debated |

---

## Clients (outbound)

Stacks that **send** QUERY.

| Stack | Status | ★ Stars | PR / issue | Days after RFC | Notes |
|---|---|---:|---|---|---|
| [**Go (net/http)**](https://github.com/golang/go) | ⚠️ Manual | 135,304 | [Issue #80058](https://github.com/golang/go/issues/80058) — open · [PR #80134](https://github.com/golang/go/pull/80134) — open | **+2** · **+8** | `NewRequest("QUERY", …)` works; constant pending |
| [**Node.js / undici**](https://github.com/nodejs/undici) | ✅ Shipped | 7,651 | [Issue #5454](https://github.com/nodejs/undici/issues/5454) · [PR #5459](https://github.com/nodejs/undici/pull/5459) — merged | **+11** / **+13** · npm 8.6.0 at +16 | Node’s `fetch` implementation; body-aware cache key work |
| [**Deno (`fetch`)**](https://github.com/denoland/deno) | ⚠️ Open | 107,760 | [Issue #36186](https://github.com/denoland/deno/issues/36186) — open | **+34** | Feature request; method string may already work |
| [**Bun (`fetch` / node:http)**](https://github.com/oven-sh/bun) | ✅ Works (generic) | 94,911 | [Issue #34839](https://github.com/oven-sh/bun/issues/34839) — closed | **+34** | Client + body verified |
| [**CPython (`http.client`)**](https://github.com/python/cpython) | ⚠️ Open | 73,835 | [Issue #153309](https://github.com/python/cpython/issues/153309) — open · [PR #153310](https://github.com/python/cpython/pull/153310) — open | **+22** | Stdlib client / method constant |
| [**Spring RestClient / WebClient**](https://github.com/spring-projects/spring-framework) | ❓ Via mapping PR | 60,128 | Same Framework track as server ([#34993](https://github.com/spring-projects/spring-framework/pull/34993)); no RestClient-specific issue found | **−378**+ | Fluent clients (`spring-web`); method usually delegated to JDK HC / Apache HC5 / Netty |
| [**requests**](https://github.com/psf/requests) | ❌ Declined | 54,136 | [Issue #7558](https://github.com/psf/requests/issues/7558) — closed not planned · [PR #7577](https://github.com/psf/requests/pull/7577) — closed unmerged | **+18** / **+24** | No first-class `requests.query()` |
| [**curl**](https://github.com/curl/curl) | ✅ Generic | 42,429 | none needed | n/a | `-X QUERY` works today |
| [**Laravel `Http::query()`**](https://github.com/laravel/framework) | ✅ Merged | 34,802 | [PR #60663](https://github.com/laravel/framework/pull/60663) — merged | **+17** | Client helper on 13.x (routing separate) |
| [**Guzzle**](https://github.com/guzzle/guzzle) | ✅ Works + redirects | 23,452 | [Issue #3699](https://github.com/guzzle/guzzle/issues/3699) — closed · [PR #3702](https://github.com/guzzle/guzzle/pull/3702) — merged | **+8** | Method string + redirect middleware fixed for QUERY |
| [**aiohttp (client)**](https://github.com/aio-libs/aiohttp) | ✅ Merged | 16,502 | [Issue #13160](https://github.com/aio-libs/aiohttp/issues/13160) · [PR #13174](https://github.com/aio-libs/aiohttp/pull/13174) — merged | **+30** · **+34** | Shared parser fix benefits client + server |
| [**hyper**](https://github.com/hyperium/hyper) | ✅ Via `http` | 16,232 | inherits [hyperium/http#798](https://github.com/hyperium/http/pull/798) | **0** | `http::Method::QUERY` |
| [**httpx**](https://github.com/encode/httpx) | ❓ Nothing | 15,356 | none found | n/a | Arbitrary methods usually work |
| [**reqwest**](https://github.com/seanmonstar/reqwest) | ❌ Declined | 11,738 | [Issue #3056](https://github.com/seanmonstar/reqwest/issues/3056) — closed not planned | **0** | Uses `http` crate methods |
| [**urllib3**](https://github.com/urllib3/urllib3) | ❓ Nothing | 4,041 | none found | n/a | Underpins many Python clients |
| [**Rust `http` crate**](https://github.com/hyperium/http) | ✅ Shipped | 1,362 | [PR #798](https://github.com/hyperium/http/pull/798) — merged · closes [#743](https://github.com/hyperium/http/issues/743) | **0** | `Method::QUERY`; safe + idempotent |
| [**Inrupt solid-client (JS)**](https://github.com/inrupt/solid-client-js) | ❓ Nothing | 244 | none found | n/a | Solid data client; needed once pods speak QUERY |
| [**Inrupt solid-client-authn (JS)**](https://github.com/inrupt/solid-client-authn-js) | ❓ Nothing | 77 | none found | n/a | Authenticated `fetch` wrapper |
| [**Inrupt solid-client (Java)**](https://github.com/inrupt/solid-client-java) | ❓ Nothing | 16 | none found | n/a | Java Solid client |

---

## Edge, proxies & caches

Infrastructure in front of apps. Body-aware caching and method allow-lists matter most (RFC 10008 §2.7).

| Stack | Status | ★ Stars | PR / issue | Days after RFC | Notes |
|---|---|---:|---|---|---|
| [**Traefik**](https://github.com/traefik/traefik) | ⚠️ Open | 64,053 | [Issue #13544](https://github.com/traefik/traefik/issues/13544) — open | **+34** (Jul 20) | End-to-end QUERY: forward, middlewares, body-keyed cache |
| [**Kong**](https://github.com/Kong/kong) | ⚠️ Open | 43,822 | [Discussion #14944](https://github.com/Kong/kong/discussions/14944) — open | **+34** (Jul 20) | Proxy, plugins, body-keyed Proxy Cache; retries list missing QUERY |
| [**nginx**](https://github.com/nginx/nginx) | ⚠️ Open | 31,171 | [PR #1488](https://github.com/nginx/nginx/pull/1488) — open · ([#1511](https://github.com/nginx/nginx/pull/1511) closed) | **+6** | Recognition only; body cache key TBD |
| [**Envoy**](https://github.com/envoyproxy/envoy) | ❓ Nothing | 28,606 | none found | n/a | No public RFC 10008 tracking found |
| [**Cloudflare workerd**](https://github.com/cloudflare/workerd) | ⚠️ Open | 8,411 | [Issue #6849](https://github.com/cloudflare/workerd/issues/6849) — open | **+14** | Body-keyed QUERY caching (Cache API) |
| [**HAProxy**](https://github.com/haproxy/haproxy) | ❓ Nothing | 6,713 | none found | n/a | No public RFC 10008 tracking found |
| [**Varnish**](https://github.com/varnishcache/varnish-cache) | ❓ Nothing | 4,049 | none found | n/a | Cache key for QUERY body untracked |
| [**Apache httpd**](https://github.com/apache/httpd) | ❓ Nothing | 4,034 | none found | n/a | Passthrough / proxy path; discuss on [dev@httpd](https://lists.apache.org/list.html?dev@httpd.apache.org) |
| [**Squid**](https://github.com/squid-cache/squid) | ❓ Nothing | 3,027 | none found | n/a | No public RFC 10008 tracking found |
| **Managed CDNs** (CloudFront, Fastly, Akamai, ALB, …) | ❓ Opaque | — | vendor docs / changelogs | n/a | Hard to track via GitHub; verify per product |

---

## Specs & documentation

| Stack | Status | ★ Stars | PR / issue | Days after RFC | Notes |
|---|---|---:|---|---|---|
| [**OpenAPI**](https://github.com/OAI/OpenAPI-Specification) | ✅ Spec-level | 31,098 | [3.2.0 announcement](https://www.openapis.org/blog/2025/09/23/announcing-openapi-v3-2) | **−266** | Documents QUERY operations (client + server codegen) |
| [**MDN**](https://github.com/mdn/content) | ⚠️ Open | 10,886 | [PR #44568](https://github.com/mdn/content/pull/44568) — open · [Issue #44665](https://github.com/mdn/content/issues/44665) — open | **+8** / **+22** | QUERY method + `Accept-Query` docs |
| [**WHATWG HTML**](https://github.com/whatwg/html) | ⚠️ Open | 9,329 | [Issue #12594](https://github.com/whatwg/html/issues/12594) — open | **+1** | `<form method="query">` |
| [**Browsers / fetch()**](https://github.com/whatwg/fetch) | ✅ Works, unofficial | 2,243 | [Issue #1938](https://github.com/whatwg/fetch/issues/1938) — open | **+14** | Client surface in browsers; [Mozilla #1430](https://github.com/mozilla/standards-positions/issues/1430) open · [WebKit #692](https://github.com/WebKit/standards-positions/issues/692) closed invalid |
| [**RFC 10008**](https://datatracker.ietf.org/doc/rfc10008/) | ✅ Published | — | [datatracker](https://datatracker.ietf.org/doc/rfc10008/) · [HTTP WG](https://datatracker.ietf.org/wg/httpbis/) | **0** | IESG approval Nov 20, 2025 = −208; [`query-method`](https://github.com/httpwg/http-extensions/labels/query-method) |

---

## Related trackers

- [jeswr/http-query-adoption](https://github.com/jeswr/http-query-adoption)
- Digest-based QUERY cache negotiation (proposal): [httpwg/http-extensions#3469](https://github.com/httpwg/http-extensions/issues/3469) → HTTP WG list
