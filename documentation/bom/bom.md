# 部品表（BOM）

> 日本語訳（MSH-LAB による参考訳）。英語の原文は [bom.en.md](bom.en.md)。
> README にあるとおり、**この部品表はハードウェア v4.0 に合わせてまだ更新されていません**。最新の部品は FreeCAD モデルで確認してください。

## 機械部品

| 名前 | 数量 | 仕様 | 備考 | 参考リンク | 画像 |
|------|-----|-------------|----------|----------------|-------|
| 鋼球 | 12 | Ø1 mm（0.04"） | 精度等級 G10 以上。小さなボールベアリングから取り出してもよい | |
| PU ストレッチコード（伸縮ひも） | 1 m | Ø1mm | 例：「Stretch Magic」や「Magic String」 | [Aliexpress](https://www.aliexpress.us/item/3256805953910514.html)| ![Pu strech cord](images/PU_StretchCord.png)|
| ネオジム円柱磁石 | 70 | Ø3mm 高さ 5 mm | N52 グレード | [NeoMagnets](https://www.buyneomagnets.com/p/3mm-dia-x-5mm-thick-n52-neodymium-rare-earth-disc-magnets-100-pack/)|
| 真鍮パイプ | 1 m | 外径 Ø2mm 内径 Ø1 mm |  | [Amazon](https://a.co/d/1pRFmtf)| ![Brass Pipe](images/BrassPipe.png)|
| 平行ピン M2×8     | 9   |             |          |                |       |
| 六角穴付きボルト（SHCS）M2×8      | 9   |             |          |                |       |
| イモネジ M3×6 | 3   |             |          |                |       |
| 皿ネジ（FHCS）M3×6      | 3   |             |          |                |       |
| 皿ネジ（FHCS）M3×10     | 9   |             |          |                |       |
| 皿ネジ（FHCS）M3×20     | 12  |             |          |                |       |
| カシメ玉（クリンプビーズ）    | 12  |             | PU コードの端を固定するのに使う |  |       |

## 電子部品

| 名前 | 数量 | 仕様 | 備考 | 参考リンク | 画像 |
|------|-----|-------------|----------|----------------|-------|
| DC-DC 降圧モジュール | 1 | 5V 固定出力の降圧（バック）コンバーター |  | [Aliexpress](https://www.aliexpress.com/item/1005008257960729.html)| ![DC-DC Step Down](images/Fixed_DC_DC-StepDown.png)|
| （1N5819）または（PMEG4010） | 1 | ダイオード（リード部品または SMD） |  | |
| Raspberry Pi Pico 2 | 1 | マイコンボード |  | | ![Raspberry Pi Pico 2](images/RaspberryPiPico2.png)|
| MT6835 磁気エンコーダーモジュール | 3 | 磁気式エンコーダー |  | [Aliexpress](https://www.aliexpress.us/item/3256808005140674.html)| ![MT6835 Magnetic Encoder Module](images/MT6835.png)|
| TB6612FNG ドライバー | 3 | モータードライバー |  | [Aliexpress](https://www.aliexpress.us/item/3256806060073976.html)| ![TB6612FNG Driver](images/TB6612FNG.png)|
| 470 µF 電解コンデンサー | 3 | 100 µF 超 | 100µF より大きければ何でもよい | |
| 10 µF セラミックコンデンサー 0603 | 3 | 任意（なくてもよい） |  | |
| 4.7 kΩ 抵抗 0603 | 2 | 任意（なくてもよい） |  | |
| NEMA 17 ステッピングモーター | 3 | 本体長 38 mm 以下 | 本体の長さが 38mm 以下のもの | |
| JST XH2.54 4P コネクター | 3 | 4P ハウジング＋ヘッダー、2.54mm ピッチ | J1、J2、J3（モーター） | [Aliexpress](https://www.aliexpress.com/item/1005007080333485.html?spm=a2g0o.order_list.order_list_main.53.3d5d1802JZg5Wb) | ![JST XH2.54 Connector](images/JST_XH2.54_Connector.png) |
| XT60H コネクター | 1 | 2P オス・メスのペア、7.5mm ピッチ | 電源コネクター | [Aliexpress](https://www.aliexpress.com/item/1005007605928815.html?spm=a2g0o.order_list.order_list_main.409.3d5d1802JZg5Wb) | ![XT60H Connector](images/XT60H_Pairs.png) |
| PH2.0 4P ハウジング <br> PH2.0 8P ハウジング | 1 <br> 1 | 4P 2mm ピッチ ハウジング <br> 8P 2mm ピッチ ハウジング | J5（ツール / I2C）<br> J4（エンコーダー） | [Aliexpress](https://www.aliexpress.com/item/1005010491403413.html?spm=a2g0o.order_detail.order_detail_item.3.2b60126a5SMahl) | ![PH2.0 Housings](images/PH2_Housings.png) |
| PH2.0 4P ヘッダー <br> PH2.0 8P ヘッダー | 1 <br> 1 | 4P 2mm ピッチ ヘッダー <br> 8P 2mm ピッチ ヘッダー | J5（ツール / I2C） <br> J4（エンコーダー） | [Aliexpress](https://www.aliexpress.com/item/1005010491403413.html?spm=a2g0o.order_detail.order_detail_item.3.2b60126a5SMahl) | ![PH2.0 Headers](images/PH2_Headers.png) |

## 基板（PCB）

| 名前                | 数量 | 仕様 | 備考 | 画像 |
| ------------------- | --- | ----------- | -------- | ----- |
| 制御基板（Control Board）       | 1   |             |          |       |
| balljoint_plate_pcb（ボールジョイント板） | 6   |             |          |       |

## 3D プリント部品

| 名前                | 数量 | 仕様 | 備考                                                        | 画像                                              |
| ------------------- | --- | ----------- | --------------------------------------------------------------- | -------------------------------------------------- |
| Motor Horn（モーターホーン）          | 3   |             | 0.4 mm 以上のノズルだと仕上げ加工が必要な場合あり                      | ![Motor Horn](images/MotorHorn.png)                |
| RubberBandCollet（ゴムバンド用コレット）    | 12  |             | 0.4 mm ノズル、積層 0.1mm 以下。仕上げ加工が必要な場合あり | ![Rubber Band Collet](images/RubberBandCollet.png) |
| Motor Mount（モーター台）         | 3   |             |                                                                 | ![Motor Mount](images/MotorMount.png)              |
| End Effector（先端部）        | 1   |             |                                                                 | ![End Effector](images/EndEffector.png)            |
| Base Block（ベースブロック）          | 1   |             |                                                                 | ![Base Block](images/BaseBlock.png)                |

# 治具：ロッド先端削り（Rod Sharpener）

## 3D プリント部品

| 名前          | 数量 | 仕様 | 備考 | 画像 |
| ------------- | --- | ----------- | -------- | ----- |
| Rod Guide（ロッドガイド）     | 1   |             |          |       |
| Blade Carrier（刃ホルダー） | 1   |             |          |       |

# 治具：ロッド長さ合わせプレス（Rod Length Setting Press）

## 基板（PCB）

| 名前                    | 数量 | 仕様 | 備考 | 画像 |
| ----------------------- | --- | ----------- | -------- | ----- |
| ball_alignment_disc_pcb（ボール位置合わせ円盤） | 1   |             |          |       |

## 3D プリント部品

| 名前                    | 数量 | 仕様 | 備考 | 画像 |
| ----------------------- | --- | ----------- | -------- | ----- |
| RodGrindingJigA（ロッド研削治具 A）         | 1   |             |          |       |
| RodGrindingJigB（ロッド研削治具 B）         | 1   |             |          |       |
| RodGuide（ロッドガイド）                | 1   |             |          |       |
| RodCollet（ロッドコレット）               | 2   |             |          |       |
| CaliperClamp（ノギス固定具）            | 2   |             |          |       |

> **補足（MSH-LAB）：日本での入手**
> - NEMA 17 ステッピングモーター・TB6612FNG・Raspberry Pi Pico 2・XH / PH コネクターは、秋月電子・スイッチサイエンス・マルツ・Amazon などで入手しやすい部品です
> - MT6835 エンコーダーモジュールと Ø1mm の精密鋼球は国内では見つけにくいので、AliExpress などの海外通販が現実的です
> - ネオジム磁石は国内でも Ø3×5mm のものが買えますが、グレード（N52 など）を確認してください
