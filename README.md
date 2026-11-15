# Open Micro-Manipulator（オープン・マイクロマニピュレーター）

> 日本語訳（MSH-LAB による学習用の参考訳）。英語の原文は [README.en.md](README.en.md)。内容に違いがある場合は原文が優先です。
> 訳注・補足は「**補足（MSH-LAB）**」と書いて原文と区別しています。

このプロジェクトは、オープンソースで低コスト、しかも組み立てやすい電動 **XYZ マイクロマニピュレーター**（微動ステージ）です。サブミクロン（1µm 未満）の精度で動かせます。
光学部品の位置合わせ、電子部品へのプロービング（針当て）、顕微鏡観察などの用途を想定しています。

装置の詳しい説明と作り方は YouTube の動画で紹介しています：<br>
[An Open Source Motorized XYZ Micro-Manipulator - Affordable sub µm Motion Control](https://youtu.be/MgQbPdiuUTw)

<div style="display: flex; gap: 2%;">
  <img src="images/overview.gif" alt="Image 1" width="49%">
  <img src="images/microscopy_die.gif" alt="Image 2" width="49%">
</div>

パラレルリンク機構と小さなボールジョイントを使っているので、機械的な剛性が高く、動ける範囲も広くなっています。
モーターは市販のステッピングモーターで、30 kHz のクローズドループ制御（位置をセンサーで測りながらの制御）と、非常に精密な PWM 信号で駆動します。
「磁気ギア」という方式で、安価な磁気式ロータリーエンコーダーの分解能を 30 倍に高めており、50nm 刻みのステップが可能です。
（**分解能と精度の違いに注意してください**。絶対的な精度はこれよりかなり劣ります。）

装置は USB シリアル経由のシンプルな G コード命令で操作できるので、ほかのプロジェクトにも簡単に組み込めます。
ファームウェアには、先読み（ルックアヘッド）付きの完全なモーションプランニング（動きの計画）機能があり、なめらかで正確に経路をたどれます。

> **補足（MSH-LAB）：用語**
> - **マイクロマニピュレーター**：顕微鏡の下などで、ごく小さな対象を µm 単位で動かしたり操作したりする装置
> - **パラレルリンク機構**：3 本の腕で先端（エンドエフェクター）を支える構造。デルタロボットと同じ仲間
> - **エンドエフェクター**：腕の先端の、道具や試料を取り付ける部分
> - **G コード**：3D プリンターや CNC で使われる、動きを指示する命令の書き方

## はじめかた

このプロジェクトを再現したい場合の、大まかな手順です。
組み立てで質問や問題があるとき、またはプロジェクトに関する話題を話し合いたいときは、プロジェクトのコミュニティ [Discord サーバー](https://discord.gg/maRvMVpa2Q) に参加してください。

1. この文書を読み、紹介している動画を見る
2. [部品表（BOM）](documentation/bom/bom.md) の部品をそろえる
3. 装置本体と電子回路を組み立てる
4. 自分の組み立てに合わせてハードウェア設定 [hw_config.h](firmware/MotionControllerRP/src/hw_config.h) を変更する
5. VSCode と PlatformIO プラグインでファームウェアを書き込む
6. 各軸のキャリブレーション（校正）をする

新しく組み立てた装置向けのセットアップガイドもあります：[セットアップガイド](documentation/setup_guide/setup_guide.md)

## ✨新登場：ハードウェア バージョン 4.0
旧設計のいくつかの問題を直した新バージョンのハードウェアを公開しました。

- 原点復帰（ホーミング）中に部品同士がぶつかる問題を修正
- ボールジョイントのブロックをネジだけで固定していたため、位置が十分に決まらず少し回転することがあった
- リンク棒（ロッド）の長さをそろえる確実な方法がなかった
- ボールジョイントに不要な摩擦があった
- ボールの正確な位置が、印刷品質や角の丸まりに大きく左右された
- 一度接着したゴムバンドを交換・取り外しできなかった

改良したボールジョイントとリンクの製作方法の動画は YouTube にあります：[Better Ball Joints for the Open Micro-Manipulator](https://www.youtube.com/watch?v=NM2KXvRGmpg)
FreeCAD のモデルも構成を整理・改良し、すべてのピンと締結部品を含めました。必要な機械部品はすべてこのモデルで確認できます。

<div style="display: flex;">
    <img src="images/Hardware-v4.0.jpg" alt="Open Micro-Manipulator GUI" width="50%">
</div>

注意：部品表（BOM）はまだ更新されていません…

## Open Micro-Manipulator GUI
Open Micro-Manipulator を手軽にテスト・利用できるように、画面で操作できる Python の制御プログラムを用意しています：[Open Micro-Manipulator GUI](https://github.com/0x23/OpenMicroManipulatorGUI)
装置を動かす簡単な操作に加えて、カメラ（顕微鏡カメラなど）のライブ映像を表示できます。ほかにも、簡単な G コード実行機能や、リアルタイムのマウス操作（生物学の用途など）があります。

<div style="display: flex;">
    <img src="images/grain_manipulation_2.jpg" alt="Open Micro-Manipulator GUI" width="50%">
</div>

## 🐍 Python API

軽量な Python API が、シリアル通信のすべてを受け持ち、命令の実行やデバッグメッセージの表示を手軽にします。
原点復帰・移動・キャリブレーション・装置情報の取得などの関数があります。
[open_micro_stage_api.py](software/PythonAPI/open_micro_stage_api.py) を自分のプロジェクトにコピーし（requirements.txt の依存パッケージも入れる）、すぐに使い始められます。

## 使用例
```python
from open_micro_stage_api import OpenMicroStageInterface

# インターフェースを作って接続する
oms = OpenMicroStageInterface(show_communication=True, show_log_messages=True)
oms.connect('/dev/ttyACM0')

# 各関節のキャリブレーションは最初に一度だけ実行する
# for i in range(3): oms.calibrate_joint(i, save_result=True)

# 原点復帰
oms.home()

# x, y, z の位置へ順に移動する [mm]
oms.move_to(0.0, 0.0, 0.0, f=10)
oms.move_to(3.1, 4.1, 5.9, f=26)
oms.move_to(0.0001, 0.0, 0.0, f=10)

# 移動が終わるまで待つ
oms.wait_for_stop()
```

> **補足（MSH-LAB）**：`/dev/ttyACM0` は Linux でのポート名です。Mac では `/dev/cu.usbmodemXXXX` のような名前になります（`ls /dev/cu.*` で確認）。

## API の関数（主なものだけ）
```python
connect(port, baud_rate=921600)                   # 接続
disconnect()                                      # 切断
set_workspace_transform(transform)                # 作業座標の変換を設定
get_workspace_transform()                         # 作業座標の変換を取得
home(axis_list=None)                              # 原点復帰
calibrate_joint(joint_index, save_result)         # 関節のキャリブレーション
move_to(x, y, z, f, move_immediately, blocking, timeout)  # 移動
set_tool_output(tool_idx, output_value, immediate)  # ツール出力の設定
set_pose(x, y, z)                                 # 現在位置を設定
dwell(time_s, blocking, timeout)                  # 一時停止
enable_motors(enable)                             # モーターの有効/無効
wait_for_stop(polling_interval_ms, disable_callbacks)  # 停止まで待つ
set_max_acceleration(linear_accel, angular_accel) # 最大加速度の設定
set_servo_parameter(pos_kp, pos_ki, vel_kp, vel_ki, vel_filter_tc)  # サーボ制御のゲイン設定
```
## ✨ ファームウェア v1.0.4

ファームウェア 1.0.4 では、多くの小さな改良とバグ修正に加え、大きな新機能が加わりました。

 - **ツール**：基板の J5 にある 2 本の GPIO ピンで、ツール（たとえばレーザー彫刻）を使えるようになりました。
              ツールはプランナー（動きの計画）に組み込まれているので、G コードの実行中も素早く、正しいタイミングで動きます。
              ツールは PWM に対応しています（ソフトウェア PWM に頼らず、PIO 機能を使ってチャンネルを増やしています）。

   使用例：
   ```
     M3 T0 S0.7  // ツール 0 の PWM 出力を 70% にする
     G4 S0.001   // 一時停止命令（ほかの移動命令でもよい）。ツールの出力を反映するために必要
   ```

- **キャリブレーション**：エンコーダーの取り付け位置ずれなど、起こりうる問題をより分かりやすく報告するエラーチェックを追加しました。
- **運動学モデルのパラメーター**：初期化コードを整理し、パラメーターのコメントを分かりやすくしました。パラメーターはハードウェア v4.0 用に設定済みですが、必要なら旧ハードウェア v3.0 用に戻せます。
- **バグ修正**：細かなバグを修正しました。

重要：**ハードウェア バージョン v3.0** を使っている場合は、[kinematic_model_delta3d.cpp](firmware/MotionControllerRP/src/kinematic_models/kinematic_model_delta3d.cpp) で旧来の運動学パラメーターに戻す必要があります（ファイル先頭に `#define` があります）。

> **補足（MSH-LAB）**：具体的には、ファイル先頭付近の `#define HW_VERSION4` の行を削除（またはコメントアウト）します。

## ファームウェア v1.0.1

このアップデートでは、キャリブレーション・原点復帰・ログ出力を改良し、G コード命令をいくつか追加しました。

### 改良点
- **原点復帰**：複数軸の同時原点復帰に対応、再現性の向上、より正確な幾何学的基準
- **関節のキャリブレーション**：手順の改良、フラッシュメモリへの保存（再起動しても再キャリブレーション不要）
- **ログ出力**：より分かりやすく詳しい出力

### 新しい G コード命令
- `G28` — 関節の原点復帰（複数軸を同時に原点復帰でき、起動が速くなる）
- `G24` — 姿勢を直接設定（モーションコントローラーを通さず、サーボの目標値を直接設定する）
- `M17/M18` — モーターの有効化 / 無効化（有効化するときはエンコーダーから姿勢を復元する）
- `M51` — エンコーダーの値を読む
- `M55` — サーボ制御ループのパラメーターを設定する
- `M56` — 関節のキャリブレーション（フラッシュに保存するオプションあり）
- `M57` — 装置の状態に関するさまざまな情報を読む
- `M58` — ファームウェアのバージョンを読む

## ⚙ CAD ファイル

CAD モデルはすべて **FreeCAD** で作っています。有料の CAD を契約しなくても、誰でも設計を見たり変更したりできるようにするためです。
ほとんどの部品は、3 軸 CNC フライスで加工しやすいように設計しています。
3D プリントで作ることもできますが、熱による寸法の変化（熱ドリフト）は避けられません（カーボン入りのフィラメントを使うとこの問題を減らせます）。

<div style="display: flex;">
    <img src="images/FreeCAD-Model.jpg" alt="FreeCAD Model" width="50%">
</div>

<br>

CAD ファイルはこちら：[CAD モデル](construction)
FreeCAD のバージョン **1.2.0dev** を使っているので、古いバージョンでは開けない場合があります。

3D プリント用の STL ファイルはこちら：[STL ファイル](construction/v4_3dprinting_stl/)

> **補足（MSH-LAB）**：原文のリンク先 `construction/STL_3D_Printing/` は存在しないため、実際のフォルダ `construction/v4_3dprinting_stl/` に直しています。

## ⚙ 運動学モデル

運動学モデル（モーターの角度と先端の位置の関係を計算する部分）はここで定義しています：[kinematic_model_delta3d.cpp](firmware/MotionControllerRP/src/kinematic_models/kinematic_model_delta3d.cpp)
自分が組み立てた装置の寸法が、コンストラクターで設定している値と合っているか確認してください。特に、腕（アーム）の長さが一致していることを確かめてください。

> **補足（MSH-LAB）**：原文のリンクはフォルダ名の綴りが `kinemtaic_models` と誤っているため、正しい `kinematic_models` に直しています。

## ⚙ 電子回路

重要：PCB のバージョン v1.2（基板にバージョン表記があります）を製造した場合は、ダイオード D1 の位置を誤って配置したビア（穴）があり、5V の電源ラインが GND とショートしています。このビアをドリルでさらってください（[修理の画像](electronics/control_board/pcb_v1.2_fix.jpg) を参照）。この問題は v1.3 で修正済みです。

> **補足（MSH-LAB）**：原文のリンク先 `electronics/pcb_v1.2_fix.jpg` は存在せず、実際の画像は `electronics/control_board/pcb_v1.2_fix.jpg` にあるため直しています。

電子回路は **KiCAD** で設計しています。一般に手に入るモジュール（モータードライバーとマイコンボード）だけを使い、シンプルな基板でつないでいます。表面実装（SMD）部品のはんだ付けは不要なので、誰でも組み立てやすくなっています。
一般的な巻線抵抗のモーターなら、電流と発熱を適度に抑えるため、装置には **5V〜6V（2A）** の電源を使ってください。

<div style="display: flex; gap: 5%;">
  <img src="images/Kicad-Board.jpg" alt="Image 1" style="flex: 1; object-fit: contain; height: 10vw;">
  <img src="images/ControllerPCB.jpg" alt="Image 2" style="flex: 1; object-fit: contain; height: 10vw;">
</div>

基板メーカーにそのままアップロードできる製造用ファイルも、リポジトリに入っています。

## ⚙ ファームウェア

ファームウェアは C++ で書かれていて、「SimpleFOC」プロジェクトから一部着想を得ています。このプロジェクトのハードウェアに絞って、余計なものがなく読みやすいことを目指しています。
先読み付きの経路計画を実装しており、ほかの多くのモーションコントローラーと違って、6 自由度（6DOF）の姿勢の補間と計画に本格的に対応しています。そのためヘキサポッド（6 本脚）のモーションプラットフォームも駆動できます。これがこのプロジェクトの次の一歩になる…かもしれません。

ピン番号・モーターの種類・その他のパラメーターの設定は [hw_config.h](firmware/MotionControllerRP/src/hw_config.h) にあります。ファームウェアを書き込む前に確認してください。

<div style="display: flex; gap: 2%;">
  <img src="documentation/firmware/firmware_overview.png" alt="Image 1" width="49%">
  <img src="documentation/firmware/path_planning.png" alt="Image 2" width="49%">
</div>

### ファームウェアのビルドと書き込み

ファームウェアのビルドと書き込みには、Visual Studio Code（Windows・Linux で無料）をおすすめします。
PlatformIO アドオンを入れて firmware フォルダを開けば、ほかの PlatformIO プロジェクトと同じようにビルドと書き込みができます。

> **補足（MSH-LAB）**：Visual Studio Code と PlatformIO は macOS でも無料で使えます。

## ⚙ G コードインターフェース

ファームウェアが対応している G コード命令は、下の表の一部だけです。
各命令には **`ok`** か **`error`** の応答が返ります。

命令が追加の情報を返す場合（例：*位置の取得* 命令）、その情報は `ok` の**前に**返ります。
次の命令を送る前に、必ず前の命令の応答を待ってください。待たずに送った場合の動作は保証されません。

| 命令           | 説明                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `G0 X Y Z F`   | 先端（エンドエフェクター）を指定した位置まで直線で動かす。<br>• `X`、`Y`、`Z`：目標位置 <br>• `F`：送り速度 |
| `G1 X Y Z F`   | `G0` と同じ。                                                              |
| `G4 S/P`       | 指定した時間だけ一時停止する。<br>• `S`：秒 <br>• `P`：ミリ秒 |
| `G24 X Y Z A B C` | サーボ制御ループの現在の姿勢を直接設定する。回転ベクトル* `A`、`B`、`C` は省略可。 |
| `G28 A-F`      | 1 つ以上の関節を原点復帰させる。<br>• 関節は `A`〜`F` で選択（省略可）。           |
| `M3`           | ツールの出力を設定する。<br>• `T`：ツール番号 <br>• `S`：出力値（0.0〜1.0） <br> 注意：新しい値は次の移動命令か一時停止命令で反映される         |
| `M17`          | モーターを有効にし、現在の姿勢を開始姿勢として読み込む。                     |
| `M18`          | モーターを無効にする。                                                            |
| `M50`          | 内部で保持している現在の姿勢を取得する（エンコーダーは読まない）。                                   |
| `M51`          | 現在のエンコーダーの角度（度）と生の値を取得する。              |
| `M52`          | プランナーの待ち行列にある命令の数を取得する。                               |
| `M53`          | 計画した動きがすべて終わったか確認する（`1` = 終了、`0` = 未終了）。 |
| `M55 A B C D F` | サーボ制御ループのパラメーターを設定する。<br>• `A`、`B`：位置 PI 制御のゲイン（P と I） <br>• `C`、`D`：速度 PI 制御のゲイン（P と I） <br>• `F`：速度フィルターの時定数 |
| `M56 J S`      | 関節をキャリブレーションする。<br>• `J`：関節番号 <br>• `S`：結果を保存する |
| `M57`          | 装置とサーボ制御ループの情報を取得する：原点復帰・キャリブレーションの状態、角度、ループ周波数、ファイル一覧。 |
| `M58`          | ファームウェアのバージョンを取得する。                                                      |
| `M204 L A`     | 直線と回転の加速度を設定する。<br>• `L`：直線の加速度 <br>• `A`：回転の加速度 |

*注：通信プロトコルでは、回転を 3 次元ベクトルで表します。ベクトルの向きが回転軸、ベクトルの長さがその軸まわりの回転角を表します。

## ❤️ 応援のお願い

このプロジェクトを応援したい場合は、次のような方法があります。

- **組み立てガイドに協力する** – プルリクエストを送ったり、提案を Issue に書いたりして、組み立て手順の改善・拡充を手伝う。
- **一般的なステッピングモーターの軸の半径方向の振れを測る** – 複数の NEMA-17 ステッピングモーターについて、軸の半径方向の振れ（ラジアル方向の誤差運動）を測定する（このテーマについては Cylos Garage を参照：https://www.youtube.com/watch?v=gt2gK-oxy5s）。
- **組み立ての感想を伝える** – うまくいったこと、いかなかったこと、ほかの人がもっとスムーズに作るにはどうすればよいかを教える。
- **Ko-fi で支援する** – このプロジェクトに価値を感じたら、[Ko-fi](https://ko-fi.com/diffractionlimited) で金銭的に支援できます ☕。

## YouTube 動画
[![動画を見る](images/video-thumbnails/01_MicroManipulator.jpg)](https://youtu.be/MgQbPdiuUTw)
[![Better Ball Joints for the Open Micro-Manipulator](images/video-thumbnails/02_BetterBallJoints.jpg)](https://www.youtube.com/watch?v=NM2KXvRGmpg)

> **補足（MSH-LAB）**：原文では 2 つ目のサムネイルも 1 本目の動画にリンクしているため、2 本目の動画（Better Ball Joints）へのリンクに直しています。
