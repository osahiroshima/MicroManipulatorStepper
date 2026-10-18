# セットアップガイド

> 日本語訳（MSH-LAB による参考訳）。英語の原文は [setup_guide.en.md](setup_guide.en.md)。

このガイドでは、新しく組み立てた **Open Micro-Manipulator** のセットアップ手順を説明します。

## 新しい装置のチェックリスト

1. **ローターに機械式のリミットピン（ストッパーのピン）を付けましたか？**
   装置を正しく原点復帰（ホーミング）させるのに、このピンが必要です。

    <div style="display: flex;">
        <img src="mechanical_limit_pin.jpg" alt="Mechanical Limit Pin" width="40%">
    </div>


2. **ローターをモーター軸に固定するネジは付いていますか？**
   ローターがしっかり固定されていないと、原点復帰や移動のときに気づかないほど少しずつ滑り、キャリブレーションや原点復帰がうまくいかない原因になります。

3. **原点復帰の向きは正しいですか？**
   原点復帰の命令（`G28`）を送ると、先端（エンドエフェクター）はベースの方へ動くはずです。
   逆の方向へ動く場合は、モーターの配線をつなぎ替えて回転方向を逆にしてください。

   <div style="display: flex;">
       <img src="homing_direction.jpg" alt="Mechanical Limit Pin" width="40%">
   </div>


## キャリブレーションとエンコーダーの確認

キャリブレーションのグラフ表示ツール（calibration plotter）を使うと、エンコーダーが正しく動いているか確認できます。
左がうまくいったキャリブレーション、右がうまくいかなかったキャリブレーションの例です。

| <img src="good_calibration.jpg"> | <img src="bad_calibration.jpg"> |
:--:|:--:
| **良いキャリブレーション** | **悪いキャリブレーション** |

この文書は未完成で、作成中です…

> **補足（MSH-LAB）**：グラフ表示ツールは `software/PythonAPI/calibration_plotter.py` です。使い方は [Python API の README](../../software/PythonAPI/README.md) を参照してください。
