# HTTP QUERY (RFC 10008) — ecosystem adoption

Day **0** = RFC publication **2026-06-16**. Last refreshed **2026-08-03** (day **+48**). ★ Stars are approximate (fetched ~2026-08-03).

Tracking is split by role: **servers** (inbound), **clients** (outbound), **edge** (proxies/caches), and **specs/docs**. The same monorepo can appear in more than one table when server and client surfaces differ (e.g. Spring Framework). Stack names link to the project home when available.

---

## Servers & frameworks (inbound)

Stacks that **accept** or **route** QUERY.

| Stack | Lang | Status | ★ Stars | PR / issue | Days after RFC | Notes |
|---|---|---|---:|---|---|---|
| [**Go (net/http)**](https://github.com/golang/go) | Go | ⚠️ Manual | 135,565 | [Issue #80058](https://github.com/golang/go/issues/80058) — open · [PR #80134](https://github.com/golang/go/pull/80134) — open | **+2** issue · PR **+8** · active **+37** | Raw method strings work; `MethodQuery` now in [active proposal review](https://go.dev/s/proposal-status#active), discussed **+43** |
| [**Node.js (core)**](https://github.com/nodejs/node) | JS / C++ | ✅ Shipped | 118,687 | [v21.7.2 release](https://github.com/nodejs/node/releases/tag/v21.7.2) (llhttp 9.2.0) | **−804** | Earliest shipper (parse/route QUERY) |
| [**Deno**](https://github.com/denoland/deno) | Rust / TS | ⚠️ Open | 107,972 | [Issue #36186](https://github.com/denoland/deno/issues/36186) — open | **+34** | Feature request; `Deno.serve` may accept method string |
| [**FastAPI**](https://github.com/tiangolo/fastapi) | Python | ❓ Nothing | 101,265 | none found | n/a | No dedicated RFC 10008 tracking found |
| [**Bun**](https://github.com/oven-sh/bun) | Zig / TS | ✅ Works (generic) | 95,248 | [Issue #34839](https://github.com/oven-sh/bun/issues/34839) — closed | **+34** | `Bun.serve` + body verified; not full RFC semantics |
| [**Django**](https://github.com/django/django) | Python | ❓ Nothing | 88,320 | none found | n/a | No dedicated RFC 10008 tracking found |
| [**CPython (`http.server`)**](https://github.com/python/cpython) | Python / C | ⚠️ Open | 74,123 | [Issue #153309](https://github.com/python/cpython/issues/153309) — open · [PR #153310](https://github.com/python/cpython/pull/153310) — open | **+22** | Stdlib HTTP support / method constant; awaiting reviewer (ping **+37**) |
| [**Express**](https://github.com/expressjs/express) | JavaScript | ✅ Works | 69,298 | [Issue #5615](https://github.com/expressjs/express/issues/5615) — closed completed | **−787** | Works on QUERY-capable Node |
| [**Spring MVC / WebFlux**](https://github.com/spring-projects/spring-framework) | Java | ❌ Not shipped | 60,144 | [PR #34993](https://github.com/spring-projects/spring-framework/pull/34993) — open; [#32975](https://github.com/spring-projects/spring-framework/issues/32975) closed not-planned; [#36988](https://github.com/spring-projects/spring-framework/issues/36988) / [#37056](https://github.com/spring-projects/spring-framework/issues/37056) closed duplicates | **−378** · revived +15–17 | `RequestMethod` / `@RequestMapping` QUERY; community-approved Jul 3, but PR idle since **+31** |
| [**Rails**](https://github.com/rails/rails) | Ruby | ⚠️ PR open | 58,669 | [PR #57973](https://github.com/rails/rails/pull/57973) — open ([forum](https://discuss.rubyonrails.org/t/proposal-support-for-the-http-query-method-rfc-10008/91255)) | **~+6** → PR **+17** | Core reviewed +30; no new discussion since |
| [**PHP (CLI server)**](https://github.com/php/php-src) | PHP / C | ✅ Merged | 40,270 | [PR #22615](https://github.com/php/php-src/pull/22615) — merged | **+20** · merged **+22** | Built-in dev server accepts QUERY (was 501) |
| [**ASP.NET Core**](https://github.com/dotnet/aspnetcore) | C# | ⚠️ Preview | 38,347 | [PR #65714](https://github.com/dotnet/aspnetcore/pull/65714) — shipped in 11 Preview 4 | **−35** | Server + OpenAPI operation type |
| [**Fastify**](https://github.com/fastify/fastify) | JavaScript | ✅ Released | 36,917 | [PR #6832](https://github.com/fastify/fastify/pull/6832) — merged · closes [#6807](https://github.com/fastify/fastify/issues/6807) | **+5** · merged **+30** · release **+44** | First-class QUERY routing; shipped in [v5.11.0](https://github.com/fastify/fastify/releases/tag/v5.11.0) |
| [**Laravel (routing)**](https://github.com/laravel/framework) | PHP | ⚠️ Merged for L14 | 34,835 | [PR #60655](https://github.com/laravel/framework/pull/60655) — merged to `master`; [#60810](https://github.com/laravel/framework/pull/60810) closed | **+20** | `Route::query()` on master → ships with Laravel 14; client helper separate (13.x) |
| [**Axum**](https://github.com/tokio-rs/axum) | Rust | ⚠️ In review | 26,765 | [Issue #3799](https://github.com/tokio-rs/axum/issues/3799) — open · [PR #3801](https://github.com/tokio-rs/axum/pull/3801) — open (also [#3837](https://github.com/tokio-rs/axum/pull/3837)) | **0** / **+1** | QUERY routing; MSRV blocker cleared by `http` v1.5.0, active review **+48** |
| [**Vapor**](https://github.com/vapor/vapor) | Swift | ⚠️ Approved, held | 26,174 | [PR #3489](https://github.com/vapor/vapor/pull/3489) — open, approved | **+42** · approved **+43** | Router QUERY methods; merge held until `swift-http-types` 1.7.0 ships |
| [**Tornado**](https://github.com/tornadoweb/tornado) | Python | ❌ Closed unmerged | 22,192 | [PR #3697](https://github.com/tornadoweb/tornado/pull/3697) — closed | **+42** | Opened and closed the same day without merge |
| [**GoFr**](https://github.com/gofr-dev/gofr) | Go | ⚠️ Approved | 21,065 | [PR #3760](https://github.com/gofr-dev/gofr/pull/3760) — open · [Issue #3756](https://github.com/gofr-dev/gofr/issues/3756) — open | **+38** | `App.QUERY` routes + client `Query`; approved pending a docs update |
| [**aiohttp (server)**](https://github.com/aio-libs/aiohttp) | Python | ✅ Released | 16,510 | [Issue #13160](https://github.com/aio-libs/aiohttp/issues/13160) — closed · [PR #13174](https://github.com/aio-libs/aiohttp/pull/13174) — merged | **+30** · merged **+34** | C parser recognizes QUERY; shipped in **3.14.2** (+34) |
| [**Slim**](https://github.com/slimphp/Slim) | PHP | ⚠️ PR open | 12,270 | [PR #3461](https://github.com/slimphp/Slim/pull/3461) — open (4.x) | **+43** | `query()` route method; deliberately excluded from `any()`; no review yet |
| [**Frappe**](https://github.com/frappe/frappe) | Python | ✅ Merged | 10,504 | [PR #41135](https://github.com/frappe/frappe/pull/41135) — merged | **+35** | Merged to `develop` |
| [**Tomcat**](https://github.com/apache/tomcat) | Java | ✅ Committed (12.x) | 8,217 | [PR #1026](https://github.com/apache/tomcat/pull/1026) — closed **unmerged**; reimplemented by committer | **+15** | Landed by hand "based on PR #1026… with a few minor variations"; **Tomcat 12 only** (needs Servlet API change) |
| [**Armeria**](https://github.com/line/armeria) | Java | ✅ Merged | 5,126 | [PR #6861](https://github.com/line/armeria/pull/6861) — merged | **+31** · merged **+48** | Server + client surfaces |
| [**Jetty**](https://github.com/jetty/jetty.project) | Java | ⚠️ Open | 4,091 | [PR #15316](https://github.com/jetty/jetty.project/pull/15316) — open | **+5** | Targeted at Jetty 13.0.x (not 12.x); idle since +29 |
| [**Undertow**](https://github.com/undertow-io/undertow) | Java | ❓ Nothing | 3,759 | none found | n/a | Servlet container (Spring Boot option); no RFC tracking found |
| [**Jakarta Servlet**](https://github.com/jakartaee/servlet) | Java (spec) | ✅ Completed | 325 | [Issue #1068](https://github.com/jakartaee/servlet/issues/1068) — closed completed · [#1069](https://github.com/jakartaee/servlet/issues/1069) | **+9** · closed ≤+34 | Spec-level container contract; cited by the Tomcat 12 work |
| [**W3C LWS**](https://github.com/w3c/lws-protocol) | Spec | ✅ Merged, contested | 26 | [PR #179](https://github.com/w3c/lws-protocol/pull/179) — merged · [Issue #205](https://github.com/w3c/lws-protocol/issues/205) — open | **+10** · merged **≈+34** | QUERY for Search / Type Index; GET/POST fallback must resolve before CR |

---

## Clients (outbound)

Stacks that **send** QUERY.

| Stack | Lang | Status | ★ Stars | PR / issue | Days after RFC | Notes |
|---|---|---|---:|---|---|---|
| [**Go (net/http)**](https://github.com/golang/go) | Go | ⚠️ Manual | 135,565 | [Issue #80058](https://github.com/golang/go/issues/80058) · [PR #80134](https://github.com/golang/go/pull/80134) · [Issue #80488](https://github.com/golang/go/issues/80488) — redirects | **+2** · **+8** · **+35** | `NewRequest("QUERY", …)` works; constant pending; §2.5 301/302 fix mailed as [CL 803520](https://go.dev/cl/803520) |
| [**Deno (`fetch`)**](https://github.com/denoland/deno) | Rust / TS | ⚠️ Open | 107,972 | [Issue #36186](https://github.com/denoland/deno/issues/36186) — open | **+34** | Feature request; method string may already work |
| [**Bun (`fetch` / node:http)**](https://github.com/oven-sh/bun) | Zig / TS | ✅ Works (generic) | 95,248 | [Issue #34839](https://github.com/oven-sh/bun/issues/34839) — closed | **+34** | Client + body verified |
| [**CPython (`http.client`)**](https://github.com/python/cpython) | Python / C | ⚠️ Open | 74,123 | [Issue #153309](https://github.com/python/cpython/issues/153309) — open · [PR #153310](https://github.com/python/cpython/pull/153310) — open | **+22** | Stdlib client / method constant |
| [**Spring RestClient / WebClient**](https://github.com/spring-projects/spring-framework) | Java | ❓ Via mapping PR | 60,144 | Same Framework track as server ([#34993](https://github.com/spring-projects/spring-framework/pull/34993)); no RestClient-specific issue found | **−378**+ | Fluent clients (`spring-web`); often on JDK HC / Apache HC5 / Netty |
| [**requests**](https://github.com/psf/requests) | Python | ❌ Declined | 54,202 | [Issue #7558](https://github.com/psf/requests/issues/7558) — closed not planned · [PR #7577](https://github.com/psf/requests/pull/7577) — closed unmerged | **+18** / **+24** | No first-class `requests.query()` |
| [**Cypress**](https://github.com/cypress-io/cypress) | JavaScript | ⚠️ PR open | 50,655 | [PR #34459](https://github.com/cypress-io/cypress/pull/34459) — open | **+47** | `cy.request()` / `cy.intercept()` method validation; opened by a maintainer |
| [**curl**](https://github.com/curl/curl) | C | ✅ Generic | 42,518 | none needed | n/a | `-X QUERY` works today |
| [**Laravel `Http::query()`**](https://github.com/laravel/framework) | PHP | ✅ Merged | 34,835 | [PR #60663](https://github.com/laravel/framework/pull/60663) — merged | **+17** | Client helper on 13.x (routing separate, L14) |
| [**Guzzle**](https://github.com/guzzle/guzzle) | PHP | ✅ Works + redirects | 23,459 | [Issue #3699](https://github.com/guzzle/guzzle/issues/3699) — closed · [PR #3702](https://github.com/guzzle/guzzle/pull/3702) — merged | **+8** | Method string + redirect middleware fixed for QUERY |
| [**JDK `HttpClient`**](https://github.com/openjdk/jdk) (`java.net.http`) | Java | ✅ Generic | 23,183 | none found | n/a | Java 11+; `HttpRequest.newBuilder().method("QUERY", body)` — arbitrary methods with body |
| [**aiohttp (client)**](https://github.com/aio-libs/aiohttp) | Python | ✅ Released | 16,510 | [Issue #13160](https://github.com/aio-libs/aiohttp/issues/13160) · [PR #13174](https://github.com/aio-libs/aiohttp/pull/13174) — merged | **+30** · **+34** | Shared parser fix benefits client + server; shipped in **3.14.2** |
| [**hyper**](https://github.com/hyperium/hyper) | Rust | ✅ Via `http` | 16,250 | inherits [hyperium/http#798](https://github.com/hyperium/http/pull/798) | **0** | Low-level client/server; `http::Method::QUERY`, released in `http` v1.5.0 (+43) |
| [**httpx**](https://github.com/encode/httpx) | Python | ❓ Nothing | 15,388 | none found | n/a | Arbitrary methods usually work |
| [**reqwest**](https://github.com/seanmonstar/reqwest) | Rust | ❌ Declined | 11,756 | [Issue #3056](https://github.com/seanmonstar/reqwest/issues/3056) — closed not planned | **0** | High-level async (on hyper); uses `http` crate methods |
| [**resty**](https://github.com/go-resty/resty) | Go | ✅ Merged | 11,740 | [PR #1187](https://github.com/go-resty/resty/pull/1187) — merged | **+35** · merged **+38** | Merged to the `v3` branch |
| [**JMeter**](https://github.com/apache/jmeter) | Java | ⚠️ Open | 9,485 | [Issue #6743](https://github.com/apache/jmeter/issues/6743) — open | **+42** | HTTP sampler method list; to-triage, no PR yet |
| [**Node.js / undici**](https://github.com/nodejs/undici) | JavaScript | ✅ Shipped | 7,654 | [Issue #5454](https://github.com/nodejs/undici/issues/5454) · [PR #5459](https://github.com/nodejs/undici/pull/5459) — merged | **+11** / **+13** · npm 8.6.0 at +16 | Node's `fetch` implementation; body-aware cache key work |
| [**ofetch**](https://github.com/unjs/ofetch) | TypeScript | ⚠️ PR open | 5,341 | [PR #611](https://github.com/unjs/ofetch/pull/611) — open · [Issue #610](https://github.com/unjs/ofetch/issues/610) — open | **+30** | QUERY treated as payload-bearing (JSON body, default headers, retry class) |
| [**req**](https://github.com/imroc/req) | Go | ✅ Merged | 4,844 | [PR #508](https://github.com/imroc/req/pull/508) — merged | **+35** · merged **+44** | `Query` / `MustQuery` helpers |
| [**urllib3**](https://github.com/urllib3/urllib3) | Python | ❓ Nothing | 4,047 | none found | n/a | Underpins many Python clients |
| [**ureq**](https://github.com/algesten/ureq) | Rust | ⚠️ Open | 2,165 | [Issue #1177](https://github.com/algesten/ureq/issues/1177) — open | **+6** (Jun 22) | Blocking client; request for `ureq::query` / `Agent::query`; idle |
| [**Apache HttpClient 5**](https://github.com/apache/httpcomponents-client) | Java | ✅ Merged (master) | 1,532 | [PR #840](https://github.com/apache/httpcomponents-client/pull/840) — merged · [PR #852](https://github.com/apache/httpcomponents-client/pull/852) — **merged** | **+15** method · cache **+36** | Method/redirect **and** body-keyed HTTP cache now both on master; no release cut yet (not Commons HttpClient 3.x EOL) |
| [**Rust `http` crate**](https://github.com/hyperium/http) | Rust | ✅ Released | 1,369 | [PR #798](https://github.com/hyperium/http/pull/798) — merged · closes [#743](https://github.com/hyperium/http/issues/743) | **0** · release **+43** | `Method::QUERY`; safe + idempotent. [v1.5.0](https://github.com/hyperium/http/releases/tag/v1.5.0) unblocked axum + hyper downstream |
| [**retrofit.dart**](https://github.com/trevorwang/retrofit.dart) | Dart | ⚠️ Open | 1,184 | [Issue #922](https://github.com/trevorwang/retrofit.dart/issues/922) — open | **+34** | Client-generator feature request; a dedicated Dart QUERY SDK (`http_query`) now exists — see Purpose-built projects |
| [**isahc**](https://github.com/sagebind/isahc) | Rust | ❓ Nothing | 783 | none found | n/a | libcurl-backed; custom methods typically work |
| [**attohttpc**](https://github.com/sbstp/attohttpc) | Rust | ❓ Nothing | 294 | none found | n/a | Lightweight blocking; no RFC tracking found |
| [**Inrupt solid-client (JS)**](https://github.com/inrupt/solid-client-js) | TypeScript | ❓ Nothing | 244 | none found | n/a | Solid data client; needed once pods speak QUERY |
| [**libwww-perl**](https://github.com/libwww-perl/libwww-perl) | Perl | ⚠️ Bug open | 211 | [Issue #530](https://github.com/libwww-perl/libwww-perl/issues/530) — open | **+35** | `LWP::UserAgent` downgrades QUERY→GET on 302, contrary to RFC 10008 §2.5 |
| [**Inrupt solid-client-authn (JS)**](https://github.com/inrupt/solid-client-authn-js) | TypeScript | ❓ Nothing | 77 | none found | n/a | Authenticated `fetch` wrapper |
| [**Inrupt solid-client (Java)**](https://github.com/inrupt/solid-client-java) | Java | ❓ Nothing | 17 | none found | n/a | Java Solid client |

---

## Edge, proxies & caches

Infrastructure in front of apps. Body-aware caching and method allow-lists matter most (RFC 10008 §2.7).

| Stack | Lang | Status | ★ Stars | PR / issue | Days after RFC | Notes |
|---|---|---|---:|---|---|---|
| [**Traefik**](https://github.com/traefik/traefik) | Go | ⚠️ Declined (roadmap) | 64,254 | [Issue #13544](https://github.com/traefik/traefik/issues/13544) — open | **+34** · reply **+41** | Maintainers: "makes a lot of sense" but not on the roadmap "for a while"; community contribution invited |
| [**Kong**](https://github.com/Kong/kong) | Lua / Nginx | ⚠️ No response | 43,908 | [Discussion #14944](https://github.com/Kong/kong/discussions/14944) — open | **+34** | Proxy, plugins, body-keyed Proxy Cache; retries list missing QUERY. Zero comments since filing |
| [**nginx**](https://github.com/nginx/nginx) | C | ⚠️ Open | 31,318 | [PR #1488](https://github.com/nginx/nginx/pull/1488) — open · ([#1511](https://github.com/nginx/nginx/pull/1511) closed) | **+6** | Recognition only; body cache key TBD; idle since +9 |
| [**Envoy**](https://github.com/envoyproxy/envoy) | C++ | ⚠️ PR open | 28,686 | [Issue #46404](https://github.com/envoyproxy/envoy/issues/46404) — open · [PR #46496](https://github.com/envoyproxy/envoy/pull/46496) — open | **+41** / **+46** | HTTP/1 + /2 + /3, gated by `envoy.reloadable_features.http1_allow_query_method` (default on); deliberately excluded from `isSafeRequest()`. Awaiting code-owner review |
| [**Cloudflare workerd**](https://github.com/cloudflare/workerd) | C++ | ⚠️ Open | 8,444 | [Issue #6849](https://github.com/cloudflare/workerd/issues/6849) — open | **+14** | Body-keyed QUERY caching (Cache API) |
| [**HAProxy**](https://github.com/haproxy/haproxy) | C | ❓ Nothing | 6,747 | none found | n/a | No public RFC 10008 tracking found |
| [**Varnish**](https://github.com/varnishcache/varnish-cache) | C | ❓ Nothing | 4,050 | none found | n/a | Cache key for QUERY body untracked |
| [**Apache httpd**](https://github.com/apache/httpd) | C | ❓ Nothing | 4,048 | none found | n/a | Passthrough / proxy path; discuss on [dev@httpd](https://lists.apache.org/list.html?dev@httpd.apache.org) |
| [**Squid**](https://github.com/squid-cache/squid) | C++ | ❓ Nothing | 3,043 | none found | n/a | No public RFC 10008 tracking found |
| **Managed CDNs** (CloudFront, Fastly, Akamai, ALB, …) | — | ❓ Opaque | — | vendor docs / changelogs | n/a | Hard to track via GitHub; verify per product |

---

## Specs & documentation

| Stack | Lang | Status | ★ Stars | PR / issue | Days after RFC | Notes |
|---|---|---|---:|---|---|---|
| [**OpenAPI**](https://github.com/OAI/OpenAPI-Specification) | Spec | ✅ Spec-level | 31,130 | [3.2.0 announcement](https://www.openapis.org/blog/2025/09/23/announcing-openapi-v3-2) | **−266** | Documents QUERY operations (client + server codegen) |
| [**MDN**](https://github.com/mdn/content) | Docs | ⚠️ Open | 10,902 | [PR #44568](https://github.com/mdn/content/pull/44568) — open · [Issue #44665](https://github.com/mdn/content/issues/44665) — open | **+8** / **+22** | QUERY method + `Accept-Query` docs |
| [**WHATWG HTML**](https://github.com/whatwg/html) | Spec | ⚠️ Open | 9,344 | [Issue #12594](https://github.com/whatwg/html/issues/12594) — open | **+1** | `<form method="query">` |
| [**Swashbuckle.AspNetCore**](https://github.com/domaindrivendev/Swashbuckle.AspNetCore) | C# | ⚠️ PR open | 5,496 | [PR #4092](https://github.com/domaindrivendev/Swashbuckle.AspNetCore/pull/4092) — open | **+48** | QUERY in SwaggerGen operation map + SwaggerUI `SubmitMethod` ("Try it out") |
| [**Browsers / fetch()**](https://github.com/whatwg/fetch) | Spec | ✅ Works, unofficial | 2,245 | [Issue #1938](https://github.com/whatwg/fetch/issues/1938) — open | **+14** | Client surface in browsers; [Mozilla #1430](https://github.com/mozilla/standards-positions/issues/1430) open · [WebKit #692](https://github.com/WebKit/standards-positions/issues/692) closed invalid |
| [**RFC 10008**](https://datatracker.ietf.org/doc/rfc10008/) | Spec | ✅ Published | — | [datatracker](https://datatracker.ietf.org/doc/rfc10008/) · [HTTP WG](https://datatracker.ietf.org/wg/httpbis/) | **0** | IESG approval Nov 20, 2025 = −208; [`query-method`](https://github.com/httpwg/http-extensions/labels/query-method) |

---

## Purpose-built QUERY projects & interop testing

Greenfield projects written *for* QUERY, rather than existing stacks adding it. Tracked separately
because star counts here measure novelty, not ecosystem penetration. Contributed via
[jeswr/http-query-adoption#3](https://github.com/jeswr/http-query-adoption/pull/3) and
[#4](https://github.com/jeswr/http-query-adoption/pull/4), which were redirected to this repo.

| Project | Lang | Kind | ★ Stars | Source | Days after RFC | Notes |
|---|---|---|---:|---|---|---|
| [**Ayder**](https://github.com/A1darbek/ayder) | C | Adopter | 96 | [PR #10](https://github.com/A1darbek/ayder/pull/10) | **+31** · updated **+43** | HTTP-native durable event log / message bus. `interop/spring-query/` emits side-by-side receipts for QUERY-with-JSON-body direct vs. routed through Envoy, plus a Spring-side matching contract |
| [**rfc10008-interop**](https://github.com/A1darbek/rfc10008-interop) | — | Interop suite | 0 | [repo](https://github.com/A1darbek/rfc10008-interop) | **+31** | Evidence-first matrix: portable checks emitting machine-readable receipts (`PASS` / `FAIL` / `NOT_SUPPORTED` / `NOT_APPLICABLE` / `UNVERIFIED` / `OBSERVED`) over ETag, conditional revalidation, `Content-Location`, semantic query identity, method override, CORS preflight and cache observability. Records evidence rather than pass/fail verdicts |
| [**query-suite-example**](https://github.com/DanMat/query-suite-example) | JS (Workers) | Reference impl | 0 | [repo](https://github.com/DanMat/query-suite-example) | **+20** | Cloudflare Workers QUERY suite; one of the two implementations currently covered by the interop matrix |
| [**query-go-sdk**](https://github.com/thatwasyahya/query-go-sdk) | Go | SDK | 0 | [repo](https://github.com/thatwasyahya/query-go-sdk) | **+23** | Dependency-free client + server SDK; §2.5-conformant redirect handling |
| [**http-query**](https://github.com/thatwasyahya/http-query) | Rust | SDK | 0 | [crates.io](https://crates.io/crates/http-query) · [repo](https://github.com/thatwasyahya/http-query) | **+35** | Client + server SDK on reqwest + axum; published to crates.io |
| [**http_query**](https://github.com/thatwasyahya/http-query-dart) | Dart | SDK | 0 | [pub.dev](https://pub.dev/packages/http_query) · [repo](https://github.com/thatwasyahya/http-query-dart) | **+49** | Client + server SDK on `package:http`; published to pub.dev |

Only two independent implementations are covered by the interop matrix so far, so it is not yet a
conformance signal for the stacks in the tables above.

---

## Cross-cutting: redirect semantics (§2.5)

A recurring failure class, independent of language: clients that treat QUERY like POST on 301/302 and silently downgrade it to GET, discarding the query body.

| Stack | Status | Tracking |
|---|---|---|
| Guzzle | ✅ Fixed | [PR #3702](https://github.com/guzzle/guzzle/pull/3702) — merged (+8) |
| Go (net/http) | ⚠️ CL mailed | [Issue #80488](https://github.com/golang/go/issues/80488) (+35) · [CL 803520](https://go.dev/cl/803520) |
| libwww-perl | ⚠️ Open | [Issue #530](https://github.com/libwww-perl/libwww-perl/issues/530) (+35) |
| Apache HttpClient 5 | ✅ Fixed | part of [PR #840](https://github.com/apache/httpcomponents-client/pull/840) (+15) |

Worth checking explicitly in any stack marked "✅ Generic" above — arbitrary-method support does not imply correct redirect handling.

---

## Related trackers

- [jeswr/http-query-adoption](https://github.com/jeswr/http-query-adoption) — **retired**; content assimilated into the tables above. The owner is archiving it in favour of this repo and closed [#3](https://github.com/jeswr/http-query-adoption/pull/3) / [#4](https://github.com/jeswr/http-query-adoption/pull/4) redirecting contributors here (+48)
- Digest-based QUERY cache negotiation: [httpwg/http-extensions#3469](https://github.com/httpwg/http-extensions/issues/3469) — **closed completed** (+13)
