# ToDoアプリケーション

## 概要

- アプリURL：<http://localhost:8000/todo/>
- PythonのWebアプリケーションフレームワーク「[Django](https://docs.djangoproject.com/ja/3.2/)」で開発したToDoアプリケーション
- Djangoは[MTV](https://qiita.com/kotayanagi/items/01e9a617571e2b9526bc)アーキテクチャーを採用したフルスタックWebアプリケーションフレームワーク
- [Bootstrap5.0](https://getbootstrap.com/)を使用
- データベースは[MariaDB](https://mariadb.com/kb/ja/mariadb/)を使用
- ローカルの[Docker](https://www.docker.com/)でWeb, DBコンテナをそれぞれ起動する
- アプリケーションサーバーはDjangoの開発用サーバー（[runserver](https://docs.djangoproject.com/en/3.2/ref/django-admin/)）を使用

## 各種コマンド

### Docker

#### イメージ作成

```bash
docker compose build [CONTAINER_NAME]
```

#### コンテナ作成

```bash
docker compose up -d [CONTAINER_NAME]
```

#### コンテナ削除

```bash
docker compose down [CONTAINER_NAME]
```

#### コンテナ起動

```bash
docker compose start [CONTAINER_NAME]
```

#### コンテナ停止

```bash
docker compose stop [CONTAINER_NAME]
```

#### コンテナ再起動

```bash
docker compose restart [CONTAINER_NAME]
```

### Django

#### アプリケーションを作成する

```bash
python3 manage.py startapp [APP_NAME]
```

#### マイグレーション

##### ファイル作成

```bash
python3 manage.py makemigrations [APP_NAME]
```

##### 実行

```bash
python3 manage.py migrate [APP_NAME]
```

##### 確認

```bash
python3 manage.py showmigrations [APP_NAME]
```

#### adminユーザーの作成

```bash
python3 manage.py createsuperuser
```

## 追加機能（例）

- CSS（Bootstrap）を設定しよう
- 一覧画面にソート機能を追加しよう（[django-tables2](https://django-tables2.readthedocs.io/en/latest/)）
- 任意のカテゴリー分けをしよう
- 重要度を設定しよう（例：大、中、小）
- フィルター機能（カテゴリー、重要度、日時、etc.）
- 論理削除機能を追加しよう（削除したToDoは削除済画面から確認できる。ゴミ箱。）
- 一括削除機能を追加しよう（チェックボックス等を付け、チェックが付いているものをまとめて削除）
- [ページネーション](https://docs.djangoproject.com/en/3.2/topics/pagination/)を実装しよう
- 登録画面の[カレンダー入力](https://github.com/monim67/django-bootstrap-datepicker-plus)のデバッグ（時間入力ができない）
- 本文検索機能を追加しよう（検索窓にテキストを入力すると、ToDo本文から部分一致検索等を行う）
