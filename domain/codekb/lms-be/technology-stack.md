# Technology Stack — lms-be

> Skim `package.json` gốc và file build ở `origin/staging` @ `1051114`. Version là range khai báo, không phải bản lock.

## Languages & Runtime

| Thành phần | Version | Bằng chứng |
|---|---|---|
| TypeScript | `~5.1.3` | `package.json:166` |
| Node.js | 20 (alpine) | `docker.runtime-base.Dockerfile:1` |
| Package manager | yarn (thư mục `.yarn/`, `.yarnrc`) | repo root |

## Frameworks

| Framework | Version | Mục đích | Bằng chứng |
|---|---|---|---|
| NestJS core/common | `^10.0.2` | Framework HTTP + DI | `package.json:40,42` |
| `@nestjs/platform-express` | `^10.0.2` | HTTP adapter | `package.json:46` |
| `@nestjs/microservices` + `kafkajs` | `^10.1.0` / `^2.2.4` | Kafka giữa service | `package.json:45,111` |
| `@nestjs/schedule` | `^3.0.4` | `@Cron` ở background-job | `package.json:48` |
| `@nestjs/bull` + `bull` | `^10.0.1` / `^4.10.4` | Hàng đợi Redis (dùng ở vài module Ops) | `package.json:38,89`; `libs/modules/src/lib/queues/queue.module.ts:9` |
| `@nestjs/websockets`, `@nestjs/platform-socket.io`, `socket.io` | `^10.3.9`, `^10.3.8`, `^4.7.5` | Khai báo nhưng **không có gateway** | `package.json:47,52,132` |
| `@nestjs/swagger` | `^7.1.7` | Docs + metadata quyền | `package.json:49` |
| Nx | `16.5.1` (plugin 16.10.0) | Monorepo build | `package.json:53-60,123` |

## Data & Infrastructure

| Thành phần | Version | Mục đích | Bằng chứng |
|---|---|---|---|
| TypeORM + `@nestjs/typeorm` | `0.3.20` / `^10.0.2` | ORM, migration | `package.json:136,51` |
| PostgreSQL driver `pg` | `^8.11.1` | DB, RLS theo tenant | `package.json:125` |
| `nestjs-cls` | `^4.4.1` | Context tenant/connection theo request | `package.json:119`; `database.module.ts:24` |
| `@nestjs/cache-manager` + `cache-manager` + `cache-manager-redis-yet` | `^2.1.0` / `4.1.0` / `^4.1.2` | Cache Redis cho `@Cache` | `package.json:39,90,91` |
| `ioredis` | `^5.4.1` | Client Redis thô (`REDIS_CLIENT`) | `package.json:106`; `redis-cache.module.ts:39-64` |
| Keycloak (HTTP, `jsonwebtoken 9.0.0`) | — | IdP; verify token + admin API | `package.json:109`; `libs/services/src/lib/keycloak/` |
| `casbin` | `^5.26.2` | Model quyền (enforcer không dùng lúc request, xem `dependencies.md`) | `package.json:92` |
| Elasticsearch | `^8.15.0` | Tìm kiếm (ngoài lát) | `package.json:34,43` |
| `firebase-admin` | `^11.11.1` | FCM push | `package.json:100` |
| AWS S3 SDK | `^3.608.0` | File | `package.json:31-33` |
| Lark SDK | `^1.71.1` | Đồng bộ Lark | `package.json:36` |

## Utility Libraries

| Lib | Version | Ghi chú | Bằng chứng |
|---|---|---|---|
| `moment` | `^2.30.1` | Xử lý ngày; dùng `utcOffset(7)` literal, không có `moment-timezone` | `package.json:115`; `apps/ops/src/schedules/schedule.service.ts:173` |
| `class-validator`, `class-transformer` | `^0.14.0`, `^0.5.1` | DTO validation | `package.json:94,93` |
| `lodash` | `^4.17.21` | — | `package.json:112` |
| `nest-commander` | `^3.13.0` | Lệnh CLI (`apps/*/src/commanders/`) | `package.json:118` |
| `pino`, `nestjs-pino` | `^10.3.1`, `^4.6.1` | Logging | `package.json:127,120` |

## Build & Quality Tools

| Tool | Version | Bằng chứng |
|---|---|---|
| Jest + ts-jest + `@nestjs/testing` | `^29.4.1`, `^29.1.0`, `^10.0.2` | `package.json:158,164,148`; `jest.config.ts`, `jest.preset.js` |
| ESLint (`@nx`, `jsdoc` plugin) | `~8.15.0` | `package.json:154`; `.eslintrc.json:4` |
| Prettier | `^2.6.2` | `package.json:163` |
| Husky + lint-staged + commitlint | `^8.0.3` | `package.json:157,168-175`; `commitlint.config.js` |
| Docker (runtime-base + app image) | — | `docker.runtime-base.Dockerfile`, `docker.app.Dockerfile` |
| GitHub Actions | — | `.github/workflows/deploy-staging.yml`, `deploy-production.yml` |

## Ghi chú cho lát
- Không có thư viện múi giờ (`moment-timezone`, `dayjs/plugin/timezone`, `luxon`) trong dependencies → tính "ngày theo múi giờ tổ chức" (PRD `C9`) cần thêm lib hoặc làm ở Postgres (`AT TIME ZONE`) [suy ra].
- `cache-manager 4.1.0` đi cùng `@nestjs/cache-manager ^2.1.0` và `cache-manager-redis-yet` (thiết kế cho cache-manager v5) — chưa kiểm hành vi TTL thực tế [chưa kiểm].
