# hello-line-notify-localstack

[LINE Notify](https://notify-bot.line.me/ja/) の Hello world プログラムを LocalStack の Lambda にデプロイして実行するサンプル。

## Requirements

- [Python](https://www.python.org/) 3.9
- [Docker](https://www.docker.com/)
- [LocalStack](https://localstack.cloud/)
- [AWS CLI v2](https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/getting-started-install.html)
- [awscli-local](https://github.com/localstack/awscli-local)
- `zip` コマンド

動作確認は Ubuntu 22.04.1 LTS on WSL 2 で行っている。

## Installation

1. `.devcontainer` で定義された開発用コンテナを使用する場合は [Developing inside a Container using Visual Studio Code Remote Development](https://code.visualstudio.com/docs/devcontainers/containers) を参照して起動する。

2. LocalStack を起動する。

   ```bash
   docker run --rm -it -p 4566:4566 -p 4510-4559:4510-4559 localstack/localstack
   ```

3. `function/.env`を作成する。

   ```bash
   touch function/.env
   ```

4. `function/.env` に LINE Notify のアクセストークンを追記する。⚠️ アクセストークンは外部に公開しないこと。

   ```.env
   LINE_NOTIFY_ACCESS_TOKEN=<LINE Notify のアクセストークン>
   ```

5. Lambda 関数を LocalStack にデプロイする。

   ```bash
   cd function/
   make
   ```

6. 初期化する場合は `make clean` を実行する。

## Usage

awslocal コマンドで Lambda 関数を呼び出す。

```bash
# awslocal コマンドは aws コマンドと同じ使い方
# 詳しい使い方は aws help のマニュアルページを参照
awslocal lambda invoke --function-name hello-line-notify-function /dev/stdout
```

LocalStack を実行している環境から HTTP 経由で Lambda 関数を呼び出すことも可能。開発用コンテナからは実行不可。

```bash
# Get FunctionUrl: awslocal lambda get-function-url-config --function-name hello-line-notify-function
curl http://xxxxxxxxxx.lambda-url.us-east-1.localhost.localstack.cloud:4566/
```

## License

[MIT](https://github.com/ogyogy/hello-line-notify-localstack/blob/main/LICENSE)
