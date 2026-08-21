# HTTP QUERY (RFC 10008) — ecosystem adoption

Day **0** = RFC publication **2026-06-16**. Last refreshed **2026-08-21** (day **+66**). ★ Stars are approximate (fetched ~2026-08-21).

Tracking is split by role: **servers** (inbound), **clients** (outbound), **edge** (proxies/caches), and **specs/docs/tooling**. The same monorepo can appear in more than one table when server and client surfaces differ (e.g. Spring Framework). Stack names link to the project home when available.

---

## Servers & frameworks (inbound)

Stacks that **accept** or **route** QUERY.

| Stack | Lang | Status | ★ Stars | PR / issue | Days after RFC | Notes |
|---|---|---|---:|---|---|---|
| [**Go (net/http)**](https://github.com/golang/go) | Go | ⚠️ Likely accept | 136,042 | [Issue #80058](https://github.com/golang/go/issues/80058) — open · [PR #80134](https://github.com/golang/go/pull/80134) — open | **+2** issue · PR **+8** · likely accept **+65** | Raw method strings work; `MethodQuery` proposal formally moved to **[likely accept](https://go.dev/s/proposal-status#likely-accept)** (**+65**); side question open on auto-accepting future RFC methods |
| [**Node.js (core)**](https://github.com/nodejs/node) | JS / C++ | ✅ Shipped | 119,149 | [v21.7.2 release](https://github.com/nodejs/node/releases/tag/v21.7.2) (llhttp 9.2.0) | **−804** | Earliest shipper (parse/route QUERY) |
| [**Deno**](https://github.com/denoland/deno) | Rust / TS | ⚠️ Open | 108,273 | [Issue #36186](https://github.com/denoland/deno/issues/36186) — open | **+34** | Feature request; `Deno.serve` may accept method string; idle since +36 |
| [**FastAPI**](https://github.com/tiangolo/fastapi) | Python | ❓ Nothing | 101,741 | none found | n/a | No dedicated RFC 10008 tracking found |
| [**Bun**](https://github.com/oven-sh/bun) | Zig / TS | ✅ Works (generic) | 95,555 | [Issue #34839](https://github.com/oven-sh/bun/issues/34839) — closed | **+34** | `Bun.serve` + body verified; not full RFC semantics |
| [**Gin**](https://github.com/gin-gonic/gin) | Go | ⚠️ PR open | 89,094 | [PR #4806](https://github.com/gin-gonic/gin/pull/4806) — open | **+59** | First-class `router.QUERY` support; community PR, active review (**+65**) |
| [**Django**](https://github.com/django/django) | Python | ❓ Nothing | 88,619 | none found | n/a | No dedicated RFC 10008 tracking found |
| [**NestJS**](https://github.com/nestjs/nest) | TypeScript | ✅ Released | 76,417 | [PR #17162](https://github.com/nestjs/nest/pull/17162) — merged · [v11.2.0](https://github.com/nestjs/nest/releases/tag/v11.2.0) | **+3** · merged & released **+59** | QUERY routing in core + Express/Fastify platforms; e2e tests [#17310](https://github.com/nestjs/nest/pull/17310) merged; OpenAPI module PR separate (see Specs) |
| [**CPython (`http.server`)**](https://github.com/python/cpython) | Python / C | ⚠️ Open | 74,546 | [Issue #153309](https://github.com/python/cpython/issues/153309) — open · [PR #155786](https://github.com/python/cpython/pull/155786) — open | **+22** · new PR **+59** | Stdlib HTTP support / method constant; original [PR #153310](https://github.com/python/cpython/pull/153310) closed unmerged, picked up fresh by a new contributor (**+59**) |
| [**Flask**](https://github.com/pallets/flask) | Python | ✅ Merged | 72,136 | [Issue #6065](https://github.com/pallets/flask/issues/6065) — closed completed · [PR #6133](https://github.com/pallets/flask/pull/6133) — merged | **+7** · merged **+56** | `app.query()` route decorator merged after two earlier attempts closed; Werkzeug test-client `Client.query()` merged too ([#3219](https://github.com/pallets/werkzeug/pull/3219), **+44**); flask-cors QUERY-by-default PR open ([#413](https://github.com/corydolphin/flask-cors/pull/413), **+62**); unreleased (latest Flask 3.1.3) |
| [**Express**](https://github.com/expressjs/express) | JavaScript | ✅ Works | 69,385 | [Issue #5615](https://github.com/expressjs/express/issues/5615) — closed completed | **−787** | Works on QUERY-capable Node |
| [**Spring MVC / WebFlux**](https://github.com/spring-projects/spring-framework) | Java | ✅ Merged | 60,205 | [PR #34993](https://github.com/spring-projects/spring-framework/pull/34993) — closed, **applied by maintainer** | **−378** · revived +15–17 · merged **+65** | `RequestMethod.QUERY` / `@RequestMapping` support merged and "scheduled for the next milestone" (snapshots available) — ends a 14-month saga; convenience `@QueryMapping` / `@QueryExchange` / DSL follow-up [#37185](https://github.com/spring-projects/spring-framework/pull/37185) closed (**+66**): enhancements considered "one by one" as adoption shows |
| [**Rails**](https://github.com/rails/rails) | Ruby | ✅ Merged (8.2) | 58,703 | [PR #57973](https://github.com/rails/rails/pull/57973) — **merged** ([forum](https://discuss.rubyonrails.org/t/proposal-support-for-the-http-query-method-rfc-10008/91255)) | **~+6** → PR **+17** · merged **+59** | Merged to `main` by rails core, milestone 8.2.0 |
| [**PHP (CLI server)**](https://github.com/php/php-src) | PHP / C | ✅ Merged | 40,304 | [PR #22615](https://github.com/php/php-src/pull/22615) — merged | **+20** · merged **+22** | Built-in dev server accepts QUERY (was 501) |
| [**Fiber**](https://github.com/gofiber/fiber) | Go | ✅ Released (v3) | 40,070 | [PR #4436](https://github.com/gofiber/fiber/pull/4436) — merged · [#4456](https://github.com/gofiber/fiber/pull/4456) completion · [#4459](https://github.com/gofiber/fiber/pull/4459) cache body keys | **+2** · merged **+9** | Early full adopter: routing, completion follow-up and QUERY cache body-key hashing all merged to main (v3); v3.4.0 tagged **+16** |
| [**ASP.NET Core**](https://github.com/dotnet/aspnetcore) | C# | ⚠️ Preview | 38,390 | [PR #65714](https://github.com/dotnet/aspnetcore/pull/65714) — shipped in 11 Preview 4 · [Issue #68331](https://github.com/dotnet/aspnetcore/issues/68331) — open | **−35** | Server + OpenAPI operation type; original issue [#61089](https://github.com/dotnet/aspnetcore/issues/61089) closed completed (**+49**); Map/attribute-routing follow-up filed **+55** |
| [**Fastify**](https://github.com/fastify/fastify) | JavaScript | ✅ Released | 37,025 | [PR #6832](https://github.com/fastify/fastify/pull/6832) — merged · closes [#6807](https://github.com/fastify/fastify/issues/6807) | **+5** · merged **+30** · release **+44** | First-class QUERY routing; shipped in [v5.11.0](https://github.com/fastify/fastify/releases/tag/v5.11.0); empty-body fix [#6929](https://github.com/fastify/fastify/pull/6929) open (**+54**) |
| [**Laravel (routing)**](https://github.com/laravel/framework) | PHP | ⚠️ Merged for L14 | 34,876 | [PR #60655](https://github.com/laravel/framework/pull/60655) — merged to `master`; [#60810](https://github.com/laravel/framework/pull/60810) closed | **+20** | `Route::query()` on master → ships with Laravel 14; client helper separate (13.x) |
| [**Hono**](https://github.com/honojs/hono) | TypeScript | ✅ Released | 31,753 | [PR #5070](https://github.com/honojs/hono/pull/5070) — merged · [v4.13.0](https://github.com/honojs/hono/releases/tag/v4.13.0) | **+16** · release **+48** | First-class `app.query()` routing; QUERY-aware ETag ([#5111](https://github.com/honojs/hono/pull/5111)), CORS ([#5115](https://github.com/honojs/hono/pull/5115)) and cache ([#5119](https://github.com/honojs/hono/pull/5119)) all in v4.13.0; zod-openapi middleware QUERY support merged ([middleware#2086](https://github.com/honojs/middleware/pull/2086), **+58**) |
| [**Axum**](https://github.com/tokio-rs/axum) | Rust | ✅ Merged (main) | 26,919 | [Issue #3799](https://github.com/tokio-rs/axum/issues/3799) — closed completed · [PR #3801](https://github.com/tokio-rs/axum/pull/3801) — **merged** | **0** / **+1** · merged **+48** | QUERY routing merged to `main` (**+48**); still not in a release (latest 0.8.9); ecosystem: `axum-test` QUERY support merged ([#211](https://github.com/JosephLenton/axum-test/pull/211), **+65**) |
| [**Vapor**](https://github.com/vapor/vapor) | Swift | ⚠️ Approved, held | 26,191 | [PR #3489](https://github.com/vapor/vapor/pull/3489) — open, approved | **+42** · approved **+43** | Router QUERY methods; merge held until `swift-http-types` 1.7.0 ships (latest is still 1.6.0 at **+66**) |
| [**fasthttp**](https://github.com/valyala/fasthttp) | Go | ⚠️ PR open | 23,439 | [PR #2358](https://github.com/valyala/fasthttp/pull/2358) — open | **+60** | High-performance server + client lib; QUERY method support |
| [**Phoenix**](https://github.com/phoenixframework/phoenix) | Elixir | ⚠️ PR open | 23,130 | [PR #6737](https://github.com/phoenixframework/phoenix/pull/6737) — open | **+9** · active **+60** | Router QUERY support; the Plug layer underneath already merged it (see Plug row) |
| [**Tornado**](https://github.com/tornadoweb/tornado) | Python | ❌ Closed unmerged | 22,180 | [PR #3697](https://github.com/tornadoweb/tornado/pull/3697) — closed | **+42** | Opened and closed the same day without merge |
| [**GoFr**](https://github.com/gofr-dev/gofr) | Go | ⚠️ Approved | 20,982 | [PR #3760](https://github.com/gofr-dev/gofr/pull/3760) — open · [Issue #3756](https://github.com/gofr-dev/gofr/issues/3756) — open | **+38** | `App.QUERY` routes + client `Query`; approved pending a docs update; last touched **+56** |
| [**SvelteKit**](https://github.com/sveltejs/kit) | TypeScript | ✅ Merged (v3) | 20,751 | [PR #16782](https://github.com/sveltejs/kit/pull/16782) — merged (`version-3`) | **+58** | QUERY handlers in `+server.js`; ships with SvelteKit 3 |
| [**aiohttp (server)**](https://github.com/aio-libs/aiohttp) | Python | ✅ Released | 16,527 | [Issue #13160](https://github.com/aio-libs/aiohttp/issues/13160) — closed · [PR #13174](https://github.com/aio-libs/aiohttp/pull/13174) — merged | **+30** · merged **+34** | C parser recognizes QUERY; shipped in **3.14.2** (+34); `METH_QUERY` + idempotent classification merged for 3.15 ([#13301](https://github.com/aio-libs/aiohttp/pull/13301), **+48**; backport **+56**; 3.15 not yet out) |
| [**Yii2**](https://github.com/yiisoft/yii2) | PHP | ⚠️ PR open | 14,299 | [Issue #21062](https://github.com/yiisoft/yii2/issues/21062) — open · [PR #21063](https://github.com/yiisoft/yii2/pull/21063) — open | **+59** · PR **+61** | Framework QUERY support; `QUERY` method constant PR in `yiisoft/http` too ([#71](https://github.com/yiisoft/http/pull/71), **+59**) |
| [**Slim**](https://github.com/slimphp/Slim) | PHP | ⚠️ PR open | 12,280 | [PR #3461](https://github.com/slimphp/Slim/pull/3461) — open (4.x) | **+43** · maintainer review **+54** | `query()` route method; maintainers agreed to adopt (**+54**), targeting a 4.16.0 minor; interface-vs-docblock API question open |
| [**gqlgen**](https://github.com/99designs/gqlgen) | Go | ⚠️ Open | 10,750 | [Issue #4295](https://github.com/99designs/gqlgen/issues/4295) — open | **+66** | First GraphQL server library tracking QUERY (natural fit for GraphQL-over-HTTP reads) |
| [**Frappe**](https://github.com/frappe/frappe) | Python | ✅ Merged | 10,607 | [PR #41135](https://github.com/frappe/frappe/pull/41135) — merged | **+35** | Merged to `develop` |
| [**Django Ninja**](https://github.com/vitalik/django-ninja) | Python | ⚠️ PR open | 9,170 | [PR #1754](https://github.com/vitalik/django-ninja/pull/1754) — open | **+57** | `@api.query()` operation support; Django itself still tracks nothing |
| [**Tomcat**](https://github.com/apache/tomcat) | Java | ✅ Committed (12.x) | 8,233 | [PR #1026](https://github.com/apache/tomcat/pull/1026) — closed **unmerged**; reimplemented by committer | **+15** | Landed by hand "based on PR #1026… with a few minor variations"; **Tomcat 12 only** (needs Servlet API change) |
| [**Armeria**](https://github.com/line/armeria) | Java | ✅ Merged | 5,133 | [PR #6861](https://github.com/line/armeria/pull/6861) — merged | **+31** · merged **+48** | Server + client surfaces |
| [**Jetty**](https://github.com/jetty/jetty.project) | Java | ⚠️ Open | 4,092 | [PR #15316](https://github.com/jetty/jetty.project/pull/15316) — open | **+5** | Targeted at Jetty 13.0.x (not 12.x); no discussion since +29, but touched again **+65** |
| [**Kemal**](https://github.com/kemalcr/kemal) | Crystal | ✅ Merged | 3,905 | [Issue #762](https://github.com/kemalcr/kemal/issues/762) — open · [PR #769](https://github.com/kemalcr/kemal/pull/769) — **merged** | **+13** · merged **+59** | QUERY routing merged to `master` by the maintainer; Crystal stdlib client PR separate (see Clients) |
| [**Helidon**](https://github.com/helidon-io/helidon) | Java | ⚠️ PR open | 3,811 | [PR #12178](https://github.com/helidon-io/helidon/pull/12178) — open | **+29** · active **+65** | Oracle's microservices framework; WebServer + WebClient QUERY support |
| [**Undertow**](https://github.com/undertow-io/undertow) | Java | ❓ Nothing | 3,758 | none found | n/a | Servlet container (Spring Boot option); no RFC tracking found |
| [**Plug**](https://github.com/elixir-plug/plug) | Elixir | ✅ Merged | 3,013 | [PR #1319](https://github.com/elixir-plug/plug/pull/1319) — merged | **+9** | Among the earliest post-RFC merges; the HTTP layer under Phoenix (whose router PR is still open) |
| [**Servant**](https://github.com/haskell-servant/servant) | Haskell | ⚠️ PR open | 1,965 | [PR #1907](https://github.com/haskell-servant/servant/pull/1907) — open | **+57** | Type-level QUERY verb; upstream `http-types` still lacks the constant (only a small fork merged it, [Vlix#34](https://github.com/Vlix/http-types/pull/34), **+64**) |
| [**Koa (`@koa/bodyparser`)**](https://github.com/koajs/bodyparser) | JavaScript | ⚠️ PR open | 1,325 | [PR #177](https://github.com/koajs/bodyparser/pull/177) — open | **+58** | Parse QUERY request bodies; routing already works on QUERY-capable Node (`http.METHODS`) |
| [**Vert.x Web**](https://github.com/vert-x3/vertx-web) | Java | ⚠️ In review | 1,151 | [PR #2921](https://github.com/vert-x3/vertx-web/pull/2921) — open | **+21** | In the maintainers' review queue; caching-impact explanation requested (**+66**) |
| [**Hanami**](https://github.com/hanami/hanami-router) | Ruby | ⚠️ PR open | 361 | [PR #307](https://github.com/hanami/hanami-router/pull/307) — open | **+64** | Conditional QUERY support in the router; follows Rails' merge |
| [**Jakarta Servlet**](https://github.com/jakartaee/servlet) | Java (spec) | ✅ Completed | 325 | [Issue #1068](https://github.com/jakartaee/servlet/issues/1068) — closed completed · [#1069](https://github.com/jakartaee/servlet/issues/1069) | **+9** · closed ≤+34 | Spec-level container contract; cited by the Tomcat 12 work |
| [**W3C LWS**](https://github.com/w3c/lws-protocol) | Spec | ✅ Merged, contested | 30 | [PR #179](https://github.com/w3c/lws-protocol/pull/179) — merged · [Issue #205](https://github.com/w3c/lws-protocol/issues/205) — open | **+10** · merged **≈+34** | QUERY for Search / Type Index; GET/POST fallback must resolve before CR; fallback issue quiet since **+34** |

---

## Clients (outbound)

Stacks that **send** QUERY.

| Stack | Lang | Status | ★ Stars | PR / issue | Days after RFC | Notes |
|---|---|---|---:|---|---|---|
| [**Go (net/http)**](https://github.com/golang/go) | Go | ⚠️ Likely accept | 136,042 | [Issue #80058](https://github.com/golang/go/issues/80058) · [PR #80134](https://github.com/golang/go/pull/80134) · [Issue #80488](https://github.com/golang/go/issues/80488) — **closed completed** | **+2** · **+8** · fix **+64** | `NewRequest("QUERY", …)` works; `MethodQuery` **likely accept** (+65); §2.5 redirect fix ([CL 803520](https://go.dev/cl/803520)) landed (**+64**) |
| [**Deno (`fetch`)**](https://github.com/denoland/deno) | Rust / TS | ⚠️ Open | 108,273 | [Issue #36186](https://github.com/denoland/deno/issues/36186) — open | **+34** | Feature request; method string may already work |
| [**Bun (`fetch` / node:http)**](https://github.com/oven-sh/bun) | Zig / TS | ✅ Works (generic) | 95,555 | [Issue #34839](https://github.com/oven-sh/bun/issues/34839) — closed | **+34** | Client + body verified |
| [**CPython (`http.client`)**](https://github.com/python/cpython) | Python / C | ⚠️ Open | 74,546 | [Issue #153309](https://github.com/python/cpython/issues/153309) — open · [PR #155786](https://github.com/python/cpython/pull/155786) — open | **+22** · new PR **+59** | Stdlib client / method constant; replacement PR after [#153310](https://github.com/python/cpython/pull/153310) closed (**+59**) |
| [**Spring RestClient / WebClient**](https://github.com/spring-projects/spring-framework) | Java | ✅ Merged | 60,205 | Framework-wide [PR #34993](https://github.com/spring-projects/spring-framework/pull/34993) — applied (**+65**) | **−378** → merged **+65** | Core QUERY support merged with the server work (next milestone); `@QueryExchange` / client DSL shortcuts deferred ([#37185](https://github.com/spring-projects/spring-framework/pull/37185) closed **+66**) |
| [**requests**](https://github.com/psf/requests) | Python | ❌ Declined | 54,247 | [Issue #7558](https://github.com/psf/requests/issues/7558) — closed not planned · [PR #7577](https://github.com/psf/requests/pull/7577) — closed unmerged | **+18** / **+24** | No first-class `requests.query()` |
| [**Cypress**](https://github.com/cypress-io/cypress) | JavaScript | ✅ Released | 50,977 | [PR #34459](https://github.com/cypress-io/cypress/pull/34459) — **merged** · in [v15.20.0](https://github.com/cypress-io/cypress/releases/tag/v15.20.0) | **+47** · merged **+48** · release **+49** | `cy.request()` / `cy.intercept()` QUERY support; 2023-era issue [#28282](https://github.com/cypress-io/cypress/issues/28282) closed completed; follow-up [#34576](https://github.com/cypress-io/cypress/pull/34576) merged **+57** |
| [**curl**](https://github.com/curl/curl) | C | ✅ Generic | 42,654 | none needed | n/a | `-X QUERY` works today |
| [**Laravel `Http::query()`**](https://github.com/laravel/framework) | PHP | ✅ Merged | 34,876 | [PR #60663](https://github.com/laravel/framework/pull/60663) — merged | **+17** | Client helper on 13.x (routing separate, L14) |
| [**Symfony HttpClient**](https://github.com/symfony/symfony) | PHP | ✅ Merged (8.2) | 31,132 | [PR #64874](https://github.com/symfony/symfony/pull/64874) — merged | **+25** · merged **+58** | `CachingHttpClient` QUERY support (body-aware) on the 8.2 branch; arbitrary methods already worked; docs issue open ([symfony-docs#22642](https://github.com/symfony/symfony-docs/issues/22642), **+58**) |
| [**Guzzle**](https://github.com/guzzle/guzzle) | PHP | ✅ Works + redirects | 23,458 | [Issue #3699](https://github.com/guzzle/guzzle/issues/3699) — closed · [PR #3702](https://github.com/guzzle/guzzle/pull/3702) — merged | **+8** | Method string + redirect middleware fixed for QUERY |
| [**JDK `HttpClient`**](https://github.com/openjdk/jdk) (`java.net.http`) | Java | ⚠️ Minor internal semantics changes outstanding | 23,255 | [JDK-8276958](https://bugs.openjdk.org/browse/JDK-8276958) | n/a | Java 11+; `HttpRequest.newBuilder().method("QUERY", body)` — arbitrary methods with body; JBS ticket untouched since Jan 2025 |
| [**Crystal (`HTTP::Client`)**](https://github.com/crystal-lang/crystal) | Crystal | ⚠️ PR open | 20,380 | [PR #17265](https://github.com/crystal-lang/crystal/pull/17265) — open | **+64** | Stdlib client `query` method; pairs with Kemal's merged server support |
| [**.NET `HttpClient`**](https://github.com/dotnet/runtime) (`System.Net.Http`) | C# | ⚠️ API approved | 18,222 | [Issue #113522](https://github.com/dotnet/runtime/issues/113522) — open, **API approved** · [#132092](https://github.com/dotnet/runtime/issues/132092) — open · [#130671](https://github.com/dotnet/runtime/issues/130671) — closed duplicate | **−459** proposal · approved **+56** | `QueryAsync` surface passed .NET API review (**+56**); JSON extension methods split out to #132092 (**+55**); arbitrary methods already work via `HttpRequestMessage` |
| [**aiohttp (client)**](https://github.com/aio-libs/aiohttp) | Python | ✅ Released | 16,527 | [Issue #13160](https://github.com/aio-libs/aiohttp/issues/13160) · [PR #13174](https://github.com/aio-libs/aiohttp/pull/13174) — merged | **+30** · **+34** | Shared parser fix benefits client + server; shipped in **3.14.2**; `METH_QUERY` + idempotent treatment merged for 3.15 (**+48**) |
| [**hyper**](https://github.com/hyperium/hyper) | Rust | ✅ Via `http` | 16,282 | inherits [hyperium/http#798](https://github.com/hyperium/http/pull/798) | **0** | Low-level client/server; `http::Method::QUERY`, released in `http` v1.5.0 (+43) |
| [**httpx**](https://github.com/encode/httpx) | Python | ❓ Unmaintained | 15,426 | none found | n/a | Arbitrary methods usually work, but the project is unmaintained — no release since 2024. pydantic's **httpx2** fork (below) is its QUERY-capable successor; see [issue #4](https://github.com/ebremer/RFC10008support/issues/4) |
| [**reqwest**](https://github.com/seanmonstar/reqwest) | Rust | ❌ Declined | 11,784 | [Issue #3056](https://github.com/seanmonstar/reqwest/issues/3056) — closed not planned | **0** | High-level async (on hyper); uses `http` crate methods |
| [**resty**](https://github.com/go-resty/resty) | Go | ✅ Merged | 11,759 | [PR #1187](https://github.com/go-resty/resty/pull/1187) — merged | **+35** · merged **+38** | Merged to the `v3` branch |
| [**OpenFeign**](https://github.com/OpenFeign/feign) | Java | ✅ Merged | 9,797 | [PR #3454](https://github.com/OpenFeign/feign/pull/3454) — merged | **+11** · merged **+42** | Declarative Java client; QUERY in the method template |
| [**JMeter**](https://github.com/apache/jmeter) | Java | ⚠️ Open | 9,516 | [Issue #6743](https://github.com/apache/jmeter/issues/6743) — open | **+42** | HTTP sampler method list; to-triage, no PR yet |
| [**Node.js / undici**](https://github.com/nodejs/undici) | JavaScript | ✅ Shipped | 7,669 | [Issue #5454](https://github.com/nodejs/undici/issues/5454) · [PR #5459](https://github.com/nodejs/undici/pull/5459) — merged | **+11** / **+13** · npm 8.6.0 at +16 | Node's `fetch` implementation; body-aware cache key work |
| [**ofetch**](https://github.com/unjs/ofetch) | TypeScript | ⚠️ Two PRs open | 5,350 | [PR #611](https://github.com/unjs/ofetch/pull/611) — open · [PR #623](https://github.com/unjs/ofetch/pull/623) — open · [Issue #610](https://github.com/unjs/ofetch/issues/610) — open | **+30** · second PR **+61** | QUERY as payload-bearing method; a second, competing PR appeared (**+61**) with neither reviewed; sibling `ocache` PR closed unmerged ([#31](https://github.com/unjs/ocache/pull/31), **+63**) |
| [**req**](https://github.com/imroc/req) | Go | ✅ Merged | 4,854 | [PR #508](https://github.com/imroc/req/pull/508) — merged | **+35** · merged **+44** | `Query` / `MustQuery` helpers |
| [**urllib3**](https://github.com/urllib3/urllib3) | Python | ❓ Nothing | 4,050 | none found | n/a | Underpins many Python clients |
| [**ureq**](https://github.com/algesten/ureq) | Rust | ⚠️ Open | 2,172 | [Issue #1177](https://github.com/algesten/ureq/issues/1177) — open | **+6** (Jun 22) | Blocking client; request for `ureq::query` / `Agent::query`; idle |
| [**Apache HttpClient 5**](https://github.com/apache/httpcomponents-client) | Java | ✅ In 5.7-alpha1 | 1,535 | [PR #840](https://github.com/apache/httpcomponents-client/pull/840) — merged · [PR #852](https://github.com/apache/httpcomponents-client/pull/852) — **merged** | **+15** method · cache **+36** · alpha **+52** | Method/redirect support released in **5.7-alpha1** (Maven Central, **+52**); body-keyed HTTP cache (#852) missed the alpha1 cut — next release |
| [**Rust `http` crate**](https://github.com/hyperium/http) | Rust | ✅ Released | 1,375 | [PR #798](https://github.com/hyperium/http/pull/798) — merged · closes [#743](https://github.com/hyperium/http/issues/743) | **0** · release **+43** | `Method::QUERY`; safe + idempotent. [v1.5.0](https://github.com/hyperium/http/releases/tag/v1.5.0) unblocked axum + hyper downstream |
| [**retrofit.dart**](https://github.com/trevorwang/retrofit.dart) | Dart | ✅ Merged | 1,183 | [Issue #922](https://github.com/trevorwang/retrofit.dart/issues/922) — closed completed · [PR #926](https://github.com/trevorwang/retrofit.dart/pull/926) — **merged** | **+34** · merged **+58** | Generator QUERY support merged by the maintainer (**+58**); duplicate PRs #924/#925 closed; a dedicated Dart QUERY SDK (`http_query`) also exists — see Purpose-built projects |
| [**httpx2**](https://github.com/pydantic/httpx2) | Python | ✅ Released | 967 | [PR #1055](https://github.com/pydantic/httpx2/pull/1055) — merged · [v2.6.0](https://github.com/pydantic/httpx2/releases/tag/v2.6.0) | **+28** | pydantic's maintained fork / successor of httpx and the natural migration path for httpx users who need QUERY — already ~a quarter of httpx's downloads and climbing ([pypistats](https://pypistats.org/packages/httpx2)); QUERY merged & released same day in v2.6.0 |
| [**isahc**](https://github.com/sagebind/isahc) | Rust | ❓ Nothing | 788 | none found | n/a | libcurl-backed; custom methods typically work |
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
| [**Caddy**](https://github.com/caddyserver/caddy) | Go | ❓ Nothing | 75,070 | none found | n/a | No RFC 10008 tracking found. Built on Go's `net/http`, so raw QUERY requests likely pass through untouched today, but nothing in Caddy's repo/forum addresses QUERY explicitly; closed, pre-RFC #5166 shows unrecognized methods historically fell back rather than returning 501 |
| [**Traefik**](https://github.com/traefik/traefik) | Go | ⚠️ Community PR | 64,528 | [Issue #13544](https://github.com/traefik/traefik/issues/13544) — open · [PR #13667](https://github.com/traefik/traefik/pull/13667) — open | **+34** · reply **+41** · PR **+55** | Maintainers invited contribution; community PR (QUERY in metrics labeling) moved to "review" status (**+58**) |
| [**Kong**](https://github.com/Kong/kong) | Lua / Nginx | ⚠️ No response | 44,016 | [Discussion #14944](https://github.com/Kong/kong/discussions/14944) — open | **+34** | Proxy, plugins, body-keyed Proxy Cache; retries list missing QUERY. Still zero comments at **+66** |
| [**nginx**](https://github.com/nginx/nginx) | C | ⚠️ Open | 31,463 | [PR #1488](https://github.com/nginx/nginx/pull/1488) — open · ([#1511](https://github.com/nginx/nginx/pull/1511) closed) | **+6** | Recognition only; body cache key TBD; idle since +9 |
| [**Envoy**](https://github.com/envoyproxy/envoy) | C++ | ⚠️ Awaiting final review | 28,808 | [Issue #46404](https://github.com/envoyproxy/envoy/issues/46404) — open · [PR #46496](https://github.com/envoyproxy/envoy/pull/46496) — open | **+41** / **+46** · LGTM **+56** | HTTP/1 + /2 + /3, gated by `envoy.reloadable_features.http1_allow_query_method` (default on); senior LGTM (**+56**), nits addressed (**+57**); second maintainer pinged for review (**+65**) |
| [**Cloudflare workerd**](https://github.com/cloudflare/workerd) | C++ | ⚠️ Open | 8,618 | [Issue #6849](https://github.com/cloudflare/workerd/issues/6849) — open | **+14** | Body-keyed QUERY caching (Cache API); idle since +18 |
| [**HAProxy**](https://github.com/haproxy/haproxy) | C | ❓ Nothing | 6,796 | none found | n/a | No public RFC 10008 tracking found |
| [**Apache httpd**](https://github.com/apache/httpd) | C | ❓ Nothing | 4,051 | none found | n/a | Passthrough / proxy path; discuss on [dev@httpd](https://lists.apache.org/list.html?dev@httpd.apache.org) |
| [**Varnish**](https://github.com/varnishcache/varnish-cache) | C | ❓ Nothing | 4,048 | none found | n/a | Cache key for QUERY body untracked |
| [**Squid**](https://github.com/squid-cache/squid) | C++ | ❓ Nothing | 3,070 | none found | n/a | No public RFC 10008 tracking found |
| [**APISIX (lua-resty-radixtree)**](https://github.com/api7/lua-resty-radixtree) | Lua | ⚠️ PR open | 282 | [PR #159](https://github.com/api7/lua-resty-radixtree/pull/159) — open | **+56** · active **+66** | The route-matching library under Apache APISIX; QUERY in the method bitmap |
| **Managed CDNs** (CloudFront, Fastly, Akamai, ALB, …) | — | ❓ Opaque | — | vendor docs / changelogs | n/a | Hard to track via GitHub; verify per product |

---

## Specs, docs & tooling

| Stack | Lang | Status | ★ Stars | PR / issue | Days after RFC | Notes |
|---|---|---|---:|---|---|---|
| [**OpenAPI**](https://github.com/OAI/OpenAPI-Specification) | Spec | ✅ Spec-level | 31,165 | [3.2.0 announcement](https://www.openapis.org/blog/2025/09/23/announcing-openapi-v3-2) | **−266** | Documents QUERY operations (client + server codegen) |
| [**MDN**](https://github.com/mdn/content) | Docs | ⚠️ Open | 10,948 | [PR #44568](https://github.com/mdn/content/pull/44568) — open · [Issue #44665](https://github.com/mdn/content/issues/44665) — open | **+8** / **+22** | QUERY method + `Accept-Query` docs; PR idle since +41 |
| [**WHATWG HTML**](https://github.com/whatwg/html) | Spec | ⚠️ Open | 9,358 | [Issue #12594](https://github.com/whatwg/html/issues/12594) — open | **+1** | `<form method="query">` |
| [**Swashbuckle.AspNetCore**](https://github.com/domaindrivendev/Swashbuckle.AspNetCore) | C# | ⚠️ PR open | 5,498 | [PR #4092](https://github.com/domaindrivendev/Swashbuckle.AspNetCore/pull/4092) — open | **+48** | QUERY in SwaggerGen operation map + SwaggerUI `SubmitMethod` ("Try it out"); no review since +48 |
| [**Browsers / fetch()**](https://github.com/whatwg/fetch) | Spec | ✅ Works, unofficial | 2,250 | [Issue #1938](https://github.com/whatwg/fetch/issues/1938) — open | **+14** | Client surface in browsers; [Mozilla #1430](https://github.com/mozilla/standards-positions/issues/1430) open · WebKit position **re-requested** ([#709](https://github.com/WebKit/standards-positions/issues/709) — open, **+61**) after [#692](https://github.com/WebKit/standards-positions/issues/692) was closed unresolved |
| [**NestJS Swagger**](https://github.com/nestjs/swagger) | TypeScript | ⚠️ PR open | 1,887 | [PR #4007](https://github.com/nestjs/swagger/pull/4007) — open | **+28** · active **+65** | OpenAPI module catch-up for NestJS's released QUERY routing |
| [**zod-to-openapi**](https://github.com/asteasolutions/zod-to-openapi) | TypeScript | ⚠️ Open | 1,611 | [Issue #393](https://github.com/asteasolutions/zod-to-openapi/issues/393) — open | **+57** | OpenAPI 3.2 QUERY operations from Zod schemas |
| [**OWASP Noir**](https://github.com/owasp-noir/noir) | Crystal | ✅ Merged | 1,375 | [Issue #2232](https://github.com/owasp-noir/noir/issues/2232) — closed completed · [PR #2563](https://github.com/owasp-noir/noir/pull/2563) — merged | **+9** · merged **+60** | Endpoint-discovery / attack-surface tool now detects QUERY routes in scanned code |
| [**RFC 10008**](https://datatracker.ietf.org/doc/rfc10008/) | Spec | ✅ Published | — | [datatracker](https://datatracker.ietf.org/doc/rfc10008/) · [HTTP WG](https://datatracker.ietf.org/wg/httpbis/) | **0** | IESG approval Nov 20, 2025 = −208; [`query-method`](https://github.com/httpwg/http-extensions/labels/query-method) |

---

## Purpose-built QUERY projects & interop testing

Greenfield projects written *for* QUERY, rather than existing stacks adding it. Tracked separately
because star counts here measure novelty, not ecosystem penetration. Contributed via
[jeswr/http-query-adoption#3](https://github.com/jeswr/http-query-adoption/pull/3) and
[#4](https://github.com/jeswr/http-query-adoption/pull/4), which were redirected to this repo.

| Project | Lang | Kind | ★ Stars | Source | Days after RFC | Notes |
|---|---|---|---:|---|---|---|
| [**Ayder**](https://github.com/A1darbek/ayder) | C | Adopter | 96 | [PR #10](https://github.com/A1darbek/ayder/pull/10) — merged | **+31** · merged **+43** | HTTP-native durable event log / message bus. `interop/spring-query/` emits side-by-side receipts for QUERY-with-JSON-body direct vs. routed through Envoy, plus a Spring-side matching contract |
| [**rfc10008-interop**](https://github.com/A1darbek/rfc10008-interop) | — | Interop suite | 0 | [repo](https://github.com/A1darbek/rfc10008-interop) | **+31** | Evidence-first matrix: portable checks emitting machine-readable receipts (`PASS` / `FAIL` / `NOT_SUPPORTED` / `NOT_APPLICABLE` / `UNVERIFIED` / `OBSERVED`) over ETag, conditional revalidation, `Content-Location`, semantic query identity, method override, CORS preflight and cache observability. Records evidence rather than pass/fail verdicts |
| [**query-suite-example**](https://github.com/DanMat/query-suite-example) | JS (Workers) | Reference impl | 0 | [repo](https://github.com/DanMat/query-suite-example) | **+20** | Cloudflare Workers QUERY suite; one of the two implementations currently covered by the interop matrix |
| [**query-go-sdk**](https://github.com/thatwasyahya/query-go-sdk) | Go | SDK | 0 | [repo](https://github.com/thatwasyahya/query-go-sdk) | **+23** · v0.2.1 **+49** | Dependency-free client + server SDK; §2.5-conformant redirect handling; v0.2.1 (**+49**) fixes media-type matching |
| [**http-query**](https://github.com/thatwasyahya/http-query) | Rust | SDK | 0 | [crates.io](https://crates.io/crates/http-query) · [repo](https://github.com/thatwasyahya/http-query) | **+35** · v0.2.0 **+49** | Client + server SDK on reqwest + axum; published to crates.io; v0.2.0 (**+49**) adds §2.5 redirect handling |
| [**http_query**](https://github.com/thatwasyahya/http-query-dart) | Dart | SDK | 0 | [pub.dev](https://pub.dev/packages/http_query) · [repo](https://github.com/thatwasyahya/http-query-dart) | **+49** | Client + server SDK on `package:http`; published to pub.dev; 0.2.0 (**+49**) adds §2.5 redirect handling |

Only two independent implementations are covered by the interop matrix so far, so it is not yet a
conformance signal for the stacks in the tables above.

---

## Cross-cutting: redirect semantics (§2.5)

A recurring failure class, independent of language: clients that treat QUERY like POST on 301/302 and silently downgrade it to GET, discarding the query body.

| Stack | Status | Tracking |
|---|---|---|
| Guzzle | ✅ Fixed | [PR #3702](https://github.com/guzzle/guzzle/pull/3702) — merged (+8) |
| Go (net/http) | ✅ Fixed | [Issue #80488](https://github.com/golang/go/issues/80488) — closed completed (+64) · [CL 803520](https://go.dev/cl/803520) landed |
| libwww-perl | ⚠️ Open | [Issue #530](https://github.com/libwww-perl/libwww-perl/issues/530) (+35) |
| Apache HttpClient 5 | ✅ Released | part of [PR #840](https://github.com/apache/httpcomponents-client/pull/840) (+15); in 5.7-alpha1 (+52) |

Worth checking explicitly in any stack marked "✅ Generic" above — arbitrary-method support does not imply correct redirect handling.

---

## Related trackers

- [jeswr/http-query-adoption](https://github.com/jeswr/http-query-adoption) — **retired & archived** (+48); content assimilated into the tables above. The owner closed [#3](https://github.com/jeswr/http-query-adoption/pull/3) / [#4](https://github.com/jeswr/http-query-adoption/pull/4) redirecting contributors here
- Digest-based QUERY cache negotiation: [httpwg/http-extensions#3469](https://github.com/httpwg/http-extensions/issues/3469) — **closed completed** (+13)
