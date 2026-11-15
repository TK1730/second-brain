# アーキテクチャ・Next.js 構成

- [Next.js の app/ と features/ の分担](nextjs-app-and-features.md) - Next.js の App Router で、app/ をルーティング専用の薄い入口にし、機能のコードを features/ にまとめる指針。
- [React と Next.js のデータ取得の置き場所](react-data-fetching.md) - React と Next.js（App Router）で、データ取得をどこに置き、どう無駄なく速く表示し、リクエストの関数をどう整理するかの考え方（Server Component での取得、コロケーション、直列取得と重複の回避、ストリーミング、N+1、Client Component での取得、Effect の要不要、API 層）。
- [React アプリのディレクトリ構成](react-project-structure.md) - React アプリのディレクトリを機能ごとに分けるときの 2 つの方式の考え方（Bulletproof React の構成、Feature-Sliced Design のレイヤーとスライスとセグメント、import の規則、公開 API、バレルファイル）。
- [Server Components と Client Components の分け方](react-server-and-client-components.md) - React と Next.js の App Router で、UI を Server Component と Client Component に分けるときの判断をまとめる（役割の分担、use client の境界、データの渡し方、children での差し込み、Context、サードパーティの部品、サーバー専用コードの保護）。
