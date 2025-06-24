# Flask + Render

このリポジトリは [Render](https://render.com/) 上で動作する Flask 3 のサンプルです。

## 仕組み

WSGI アプリケーションとして Flask を利用しており、`gunicorn` などの WSGI サーバーで実行できます。

## ローカルでの実行

```bash
FLASK_APP=api/index.py flask run
```

ブラウザで `http://localhost:5000` を開くとアプリが確認できます。

## Diary API

`/diary/diaries` 以下のエンドポイントで Diary テーブルへの CRUD 操作を行えます。

- `GET /diary/diaries` - すべてのダイアリーを取得
- `GET /diary/diaries/<id>` - 指定 ID のダイアリーを取得
- `POST /diary/diaries` - 新規ダイアリーを作成
- `PUT /diary/diaries/<id>` - 既存ダイアリーを更新
- `DELETE /diary/diaries/<id>` - ダイアリーを削除

## Render へのデプロイ

Render で Web サービスを作成し、以下の Start Command を指定します。

```bash
gunicorn api.index:app
```

これだけで Flask アプリが起動します。
