# Python API

> 日本語訳（MSH-LAB による参考訳）。英語の原文は [README.en.md](README.en.md)。

このフォルダには、Open Micro-Manipulator のシリアル通信プロトコル用の軽量な Python インターフェースと、2 つの小さなサンプルスクリプトが入っています。

- `usage_example.py`：装置を原点復帰させ、簡単な移動をして、装置の状態を表示する。
- `calibration_plotter.py`：最初の 3 つのアクチュエーター（駆動部）の関節キャリブレーションを実行し、返ってきたデータをグラフにする。

## 必要なもの

Python の依存パッケージを次のコマンドで入れます：

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

API 本体は `open_micro_stage_api.py` にあります。

## シリアルポートの選択

どちらのスクリプトも、次のオプションに対応しています：

- `--list-ports`：見つかったシリアル機器の一覧を表示して終了する
- `--port <ポート>`：使うシリアルポートを指定する

`--port` を指定しない場合、スクリプトは次の順でポートを自動で選びます：

1. 名前に `Pico` を含む機器がちょうど 1 つ見つかれば、そのポートを使う。
2. そうでなく、シリアル機器がちょうど 1 つだけ見つかれば、そのポートを使う。
3. それ以外の場合は、使えるポートの一覧を表示して終了する。

## サンプルスクリプトを実行する

このフォルダで：

```bash
python usage_example.py --list-ports
python usage_example.py --port /dev/ttyACM0
```

Windows の場合は、たとえば次のようになります：

```bash
python usage_example.py --port COM3
```

> **補足（MSH-LAB）**：Mac では `--port /dev/cu.usbmodemXXXX` のような名前になります。まず `--list-ports` で確認してください。Mac では `python` の代わりに `python3` を使う場合があります。

## キャリブレーションのグラフ表示ツールを実行する

このフォルダで：

```bash
python calibration_plotter.py --list-ports
python calibration_plotter.py --port /dev/ttyACM0
```

キャリブレーションのスクリプトは、測定したキャリブレーション曲線を matplotlib のウィンドウに表示します。

## リポジトリのルートから実行する

リポジトリの一番上のフォルダから実行したい場合は、次のようにします：

```bash
python software/PythonAPI/usage_example.py --port /dev/ttyACM0
python software/PythonAPI/calibration_plotter.py --port /dev/ttyACM0
```
