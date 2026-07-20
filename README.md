| Stack | Status | Repo | PR / issue | Days after RFC (Jun 16 = day 0) | Notes |
|---|---|---|---|---|---|
| **RFC 10008** | ✅ Published | IETF HTTP WG | [RFC 10008 (datatracker)](https://datatracker.ietf.org/doc/rfc10008/) | **0** (Jun 16, 2026) | IESG approval Nov 20, 2025 = −208 |
| **Node.js (core)** | ✅ Shipped | nodejs/node | [v21.7.2 release](https://github.com/nodejs/node/releases/tag/v21.7.2) (llhttp 9.2.0 bump, no single PR) | **−804** (Apr 3, 2024) | Earliest shipper |
| **undici** | ✅ Shipped | nodejs/undici | [PR #5459](https://github.com/nodejs/undici/pull/5459) — merged | **+13** (Jun 29) · first npm **8.6.0** at +16 | Still present in 8.8.0 (+34) |
| **Browsers / fetch()** | ✅ Works, unofficial | whatwg/fetch | [Issue #1938](https://github.com/whatwg/fetch/issues/1938) — open | **+14** (Jun 30) | Plus [Mozilla position request #1430](https://github.com/mozilla/standards-positions/issues/1430) |
| **OpenAPI** | ✅ Spec-level | OAI/OpenAPI-Specification | [3.2.0 announcement](https://www.openapis.org/blog/2025/09/23/announcing-openapi-v3-2) | **−266** (Sep 23, 2025) | — |
| **Express** | ✅ Works | expressjs/express | [Issue #5615](https://github.com/expressjs/express/issues/5615) — closed completed, no code PR | **−787** (Apr 20, 2024) | Filed 17 days after Node shipped parsing |
| **Fastify** | ✅ Shipped (main) | fastify/fastify | [PR #6832](https://github.com/fastify/fastify/pull/6832) — merged · closes [#6807](https://github.com/fastify/fastify/issues/6807) | **+5** issue (Jun 21) · merged **+30** (Jul 16) | First-class QUERY (not only `addHttpMethod`); release tag TBC |
| **nginx** | ⚠️ Open | nginx/nginx | [PR #1488](https://github.com/nginx/nginx/pull/1488) — open · ([#1511](https://github.com/nginx/nginx/pull/1511) closed, not merged) | **+6** (Jun 22) | Recognition only; body cache key TBD |
| **Apache httpd** | ❓ Nothing | apache/httpd | none found | n/a | Passthrough only |
| **Tomcat** | ✅ Merged | apache/tomcat | [PR #1026](https://github.com/apache/tomcat/pull/1026) — merged | **+15** (Jul 1) | Release placement TBC |
| **Jakarta Servlet** | ✅ Completed | jakartaee/servlet | [Issue #1068](https://github.com/jakartaee/servlet/issues/1068) — closed completed | **+9** (Jun 25) · closed ≤+34 | Cites Tomcat PR |
| **Jetty** | ⚠️ Open | jetty/jetty.project | [PR #15316](https://github.com/jetty/jetty.project/pull/15316) — open | **+5** (Jun 21) | Retargeted to Jetty 13.0.x |
| **Bun** | ❓ Unverified | oven-sh/bun | none found | n/a | — |
| **Deno** | ❓ Unverified | denoland/deno | none found | n/a | — |
| **Go (net/http)** | ⚠️ Manual | golang/go | none verified | n/a | Raw method strings work |
| **ASP.NET Core** | ⚠️ Preview | dotnet/aspnetcore | [PR #65714](https://github.com/dotnet/aspnetcore/pull/65714) — shipped in 11 Preview 4 | **−35** (May 12, 2026) | OpenAPI recognizes QUERY as operation type |
| **Spring** | ❌ Not shipped | spring-projects/spring-framework | [PR #34993](https://github.com/spring-projects/spring-framework/pull/34993) — open (fixes [#32975](https://github.com/spring-projects/spring-framework/issues/32975)) | **−378** (Jun 3, 2025) · revived +15–17 | Community-approved Jul 3; still open |
| **Rails** | ⚠️ PR open | rails/rails | [PR #57973](https://github.com/rails/rails/pull/57973) — open ([proposal thread](https://discuss.rubyonrails.org/t/proposal-support-for-the-http-query-method-rfc-10008/91255)) | **~+6** proposal → **+17** PR (Jul 3) | Rails core reviewed +30; active through +31 |
| **curl** | ✅ Generic | curl/curl | none needed | n/a | `-X QUERY` works today |
| **W3C LWS** | ✅ Merged, contested | w3c/lws-protocol | [PR #179](https://github.com/w3c/lws-protocol/pull/179) — merged | **+10** · merged **≈+34** | Fallback debate = your thread |