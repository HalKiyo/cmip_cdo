# cmip_cdo

CMIP6 historical 実験の月平均データ (mrso, pr, snc, tos, tsl) を CDO で 1°×1° 格子に内挿するスクリプト群です。

## 構成

```
cmip_remap.py                   共通モジュール (Remap クラス, run(), chunks())
<MODEL>/regrid_r1i1p1f1_<var>.py  各モデル・各変数の設定だけを書いた薄いラッパー (44 モデル × 5 変数)
ICON-ESM-LR/griddes_1x1.txt     CDO 用グリッド記述ファイル (現在どのスクリプトからも参照されていません)
```

ファイル名は歴史的経緯で `r1i1p1f1` ですが、実際の variant (r1i1p1f2, r1i1p1f3, r1i1p2f1, r101i1p1f1, r1i1p4f2 など) は各ラッパーの `variant=` で指定しています。

## 入出力

* 入力: `/work/kajiyama/data/cmip6/raw/<MODEL>/<var>/<var>_<realm>_<MODEL>_historical_<variant>_<grid>_<YYYY>01-<YYYY>12.nc`
  * IPSL-CM5A2-INCA と IPSL-CM6A-LR-INCA の tos のみ `/work/kajiyama/nco/cmip6/...` (`data_dir=NCO_DIR`)
* 出力: `/work/kajiyama/cdo/cmip6/<MODEL>/<var>/<var>_<begin>-<end>.nc`
* 処理: `cdo remapbil,r360x180 -seltimestep,1/<月数> -selvar,<var> <入力>`
  * AWI-ESM-1-1-LR の tos と ICON-ESM-LR の全変数は `remapycon,global_1`
* 最後に `plot_period` (省略時は最初の期間) の第 1 タイムステップを内挿して地図表示します。

## 実行方法

従来どおり、各ラッパーをそのまま実行します (どのディレクトリから実行しても動きます)。

```bash
python CESM2/regrid_r1i1p1f1_pr.py
```

必要パッケージ: `cdo` (python-cdo と CDO 本体), `cartopy`, `matplotlib`, `numpy`, `xarray`

## ラッパーで指定できる主な引数 (`cmip_remap.run`)

| 引数 | 既定値 | 内容 |
|---|---|---|
| `variable`, `realm`, `model` | 必須 | 変数名, テーブル名 (Amon/Lmon/LImon/Omon), モデル名 |
| `periods` | 必須 | 入力ファイルの (開始年, 終了年) のリスト。この順に処理します |
| `variant`, `grid` | `'r1i1p1f1'`, `'gn'` | ファイル名中のメンバー名・格子ラベル |
| `plot_period` | `periods[0]` | 確認用に描画する期間 |
| `method`, `target` | `'remapbil'`, `'r360x180'` | CDO の内挿オペレータと出力格子 |
| `data_dir` | `RAW_DIR` | 入力のルートディレクトリ |
| `plot_mode` | `'full'` | `'first'` は `[0, 0, :, :]`, `'mean'` は axis=1 の平均を描画 (tsl 用) |
| `save_flag` | `True` | `False` にすると内挿・保存をせずメッセージだけ表示 |

`chunks(start, stop, step)` は `[(i, i + step - 1) for i in range(start, stop, step)]` を返すヘルパーです。

## 変更履歴メモ

以前は各ラッパーに同じ Remap クラスや plot 関数がコピーされており、他の変数のスクリプトは
`from regrid_r1i1p1f1_mrso import Remap` で同じディレクトリの mrso スクリプトに依存していました。
現在は共通処理を `cmip_remap.py` に集約し、各ラッパーは設定値だけを持ちます。
CDO に渡すコマンド・入出力パス・処理順・描画内容は全 220 スクリプトで以前と同一です。
