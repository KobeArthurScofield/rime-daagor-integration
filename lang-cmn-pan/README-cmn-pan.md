# ℞大狗拼音（北方官话） Daagor Integration (ISO 639-3 cmn-pan)

目前包含：
- 带调标准汉语拼音 (HanYu PinYin, hanyu-pinyin)
- 带调双拼
  - 自然码双拼 (ZiRanMa, ziranma)
  - 小鹤双拼 (Fly PinYin, flypy)
  - 拼音加加双拼 (PinYinJiaJia, pinyinjiajia)
  - 汉心龙双拼 (HanXin Long, hanxinlong)
  - 自然龙双拼 (ZiRan Long, ziranlong)
  - 小浪双拼 (Xiao Lang, xiaolang)
  - 冰雪四拼/声笔四拼 (Snow Si-pin, snowsipin)
  - 简龙（原作暂定名龙三） (Jian Long, jianlong)
- 帶聲調通用拼音 (Tongyong Pinyin, tongyong-pinyin)
- 國語注音符號第二式，國音二式 (Phonetic Symbols II (MPS II), mpsii)
- 注音輸入法
  - 大千鍵盤排布 (Bopomofo Dachen, dachen)
  - 許氏鍵盤排布 (Bopomofo Hsu, bpmfhsu)
  - 倚天 41 鍵排布 (Eten 41 keys, eten41)
  - 倚天忘形 26 鍵排布 (Eten 26 keys, eten26)
  - IBM 鍵盤排布 (Bopomofo IBM, bpmfibm)
  - 精業鍵盤排布 (Ching-yeh, chingyeh)
  - 神通鍵盤排布 (MiTAC, mitac)
- 國語羅馬字 (Gwoyeu Romatzyh, gwoyeu)

同时允许使用数种带声调词库：
- RIME 发行版内置的[地球拼音方案词库](https://github.com/rime/rime-terra-pinyin)
- [冰雪拼音词库](https://github.com/rimeinn/rime-snow-pinyin)
- [万象词库](https://github.com/amzxyz/RIME-LMDG)

目前所有方案所需词库及语言模型请自行到对应的仓库下载。

## 文件解析

- `lib.babel-cmn-pan`： **（必需）** 输入方案跨拼音规范转换库
- `lib.scribe-cmn-pan`： **（必需）** 输入方案拼音形态转换库
- `lib.icon`： 对应输入法的指示器图标
  - `icon.ascii`： 输入法键盘直接输入模式图标
  - `icon.imecn`： 输入法模式中国大陆方案图标
  - `icon.imetw`： 输入法模式台湾方案图标
- `experience`：Daagor Integration Experience，用于取代输入方案默认体验
  - `daagorxp.lib.preedit-cmn-pan`：提供上屏字符转换功能，上屏显示为对应拼音而非输入字符；启用后全局生效
- `dictionary`： **（根据调用词库必需）** 词典处理库，用于对接需要使用的拼音词库；选用的词库对所有方案全局生效
  - `cmn-pan-rime-terra`：调用 RIME 发行版附带的地球拼音词库
  - `cmn-pan-rime-snow`：调用冰雪拼音词库
  - `cmn-pan-rime-lmdg`：调用万象拼音词库
    - `dict.wanxiang`：词库合包文件
- `rscm.*`：基于以上文件组成的输入方案
    - `bpmfhsu` 注音（許氏）布局
    - `bpmfibm` 注音（IBM）布局
    - `bpmfliu` 注音（劉氏）布局
    - `chewing` 注音（酷音大千二十六鍵）布局
    - `chingyeh` 注音（精業）布局
    - `dachen` 注音（大千）布局
    - `eten26` 注音（倚天忘形 26 鍵）布局
    - `eten41` 注音（倚天 41 鍵）布局
    - `flypy` 小鹤双拼布局
    - `gwoyeu` 国语罗马字布局
    - `gwoyeu-num` 国语罗马字数字音调布局
    - `hanxinlong` 汉心龙/龙码双拼布局
    - `hanyu-pinyin` 汉语拼音布局
    - `jianlong` 简龙/龙三双拼布局
    - `mitac` 注音（神通）布局
    - `mpsii` 国音二式布局
    - `pinyinjiajia` 拼音加加双拼布局
    - `snowsipin` 冰雪四拼布局
    - `starlight` 注音（星光排布）布局
    - `tongying-pinyin` 通用拼音布局
    - `xiaolang` 小浪双拼布局
    - `ziranlong` 自然龙双拼布局
    - `ziranma` 自然码双拼布局
- `supplimental`：用于提供额外方案。这些方案包含：
  - 威妥玛拼音 (wade-giles)（及邮政拼音 (postcal) 和简化威妥玛拼音 (wand-giles-simp)）
  - 法国远东学院拼音 (efeo)
  - 德国式拼音 (lessing-othmer)
  - 拉丁化新文字 (latinxua)
  - 耶鲁拼音 (yale)
  - 捷克式拼音 (cesky)

## 方案所需的词典文件及语法模型文件；

  * 冰雪拼音语法模型使用 `amz-v2n3m1-zh-hans.gram`
  * 地球拼音语法模型使用 `zh-han?-t-essay-bg?.gram`
  * 万象拼音语法模型使用 `wanxiang-lts-zh-hans.gram`
  * 词库及语法模型下载地址在后方内容

## 输入键盘布局

布局本身不支持音调时，输入音调的方法为：在输入音节后，以主键盘上 7-0 以及 - = 两个符号分别代表阴平、阳平、上声、去声、轻声和入声。不使用声调时可作普通拼音使用。

### 汉心龙键盘布局

![键盘布局](https://github.com/KobeArthurScofield/rime-daagor-integration/blob/main/image/hxlong-2025-01.png)

新增按键见下：

#### ExtK-HX-01 标准

| 拼音成份 | 按键（12345 声） |
|--------|----------------|
| 轻声 | 所有轻声的按键与其第一声相同 |
| ê | LUICL |
| 空韵母 h | MNCLM |
| 空韵母 m | ULNIU |
| 空韵母 n | CLTKC |
| 空韵母 ng | CIGUC |

#### ExtK-HX-02 标准

| 拼音成份 | 按键（12345 声） |
|--------|----------------|
| 轻声 | 所有轻声的按键与其第一声相同 |
| ê | LUICL |
| 声母 v | G |
| 声母 gn | L |
| 声母 ng | Y |
| 空韵母 h | MNCLM |
| 空韵母 m | ULNIU |
| 空韵母 n | CLTKC |
| 空韵母 ng | CIGUC |
| 韵母 iai | AJRBA |
| 韵母 io | TQJFT |
| 韵母 üo | SSPXS |

### 自然龙键盘布局

![键盘布局](https://github.com/KobeArthurScofield/rime-daagor-integration/blob/main/image/zrlong-2025-01.jpg)

新增按键见下：

#### ExtK-ZR-01 标准

| 拼音成份 | 按键（12345 声） |
|--------|----------------|
| 轻声 | 所有轻声的按键与其第一声相同 |
| ê | YATQY |
| 空韵母 h | VZNXV |
| 空韵母 m | AYBTA |
| 空韵母 n | QYZBQ |
| 空韵母 ng | QTJAQ |

#### ExtK-ZR-02 标准

| 拼音成份 | 按键（12345 声） |
|--------|----------------|
| 轻声 | 所有轻声的按键与其第一声相同 |
| ê | YATQY |
| 声母 v | W |
| 声母 gn | G |
| 声母 ng | N |
| 空韵母 h | VZNXV |
| 空韵母 m | AYBTA |
| 空韵母 n | QYZBQ |
| 空韵母 ng | QTJAQ |
| 韵母 iai | BDUOB |
| 韵母 io | PEIGP |
| 韵母 üo | SLLPS |

### 简龙/龙三键盘布局

![键盘布局](https://github.com/KobeArthurScofield/rime-daagor-integration/blob/main/image/jianlong-2025-09.jpg)

新增按键见下：

#### ExtK-ZR-02 标准

| 拼音成份 | 按键（12345 声） |
|--------|----------------|
| 轻声 | 所有轻声的按键与其第一声相同 |
| ê | ERRYE |
| 声母 v | W |
| 声母 gn | G |
| 声母 ng | N |
| 空韵母 h | RYYOR |
| 空韵母 m | OAAGO |
| 空韵母 n | TPPHT |
| 空韵母 ng | LBBEL |
| 韵母 iai | FCCHF |
| 韵母 io | VWWXV |
| 韵母 üo | KOOJK |

## 词库及语法模型

注意：不同词库之间会存在拼写差异。

- 八股文模型（繁体）： https://github.com/lotem/rime-octagram-data/tree/hant
- 冰雪拼音词库： https://github.com/rimeinn/rime-snow-pinyin (*.dict.yaml)
- 万象词库： https://github.com/amzxyz/RIME-LMDG/releases/tag/dict-nightly
- 万象通用模型： https://github.com/amzxyz/RIME-LMDG/releases/tag/v2n3
- 万象原子模型： https://github.com/amzxyz/RIME-LMDG/releases/tag/LTS

## 注意

### 拼音表示方式转换

将音调转换至输入方案支持的范围，一种是仅转换音调而保留所有拼写，另一种是将拼写压缩到常用拼音拼写组合（limited）；前者适用于所用布局能支持词库中所有拼写（如扩展后的汉心龙、自然龙），后者适用于所用布局仅能支持常见拼写（如一般双拼）。

示例如下（以汉语拼音示例）：

| 原形式 | 完全拼写 | 受限拼写 |
|----|----|----|
| ê | ê | eh |
| m | m | mu |
| n | n | en |
| ng | ng | eng |
| 空韵母 -h | -h | -e |
| 空韵母 -m | -m | -un |
| 空韵母 -n | -n | -en |
| 空韵母 -ng | -ng | -eng |
| 声母 ng- | ng- | n- |
| 声母 gn- | gn- | g- |
| 声母 v- | v- | w- |
| 韵母 -iai | -iai | -ai |
| 韵母 -io | -io | -o |
| 韵母 -üo | -üo | -uo |

- 目前该框架可以正常支持包含但不限于《现代汉语词典》中存在的拼写，而压缩拼写组合则支持范围为《现代汉语词典中》存在的拼写。

### 为何部分方案没有特定音节

需要对应的词库支持该拼写。

## 致谢

- [RIME 输入引擎](https://github.com/rime)
- [汉心龙](https://hanxinma.gitlab.io/longma/hanxinlong) 作者：晡时之光
- [自然龙](https://hanxinma.gitlab.io/longma/ziranlong) 作者：小幽幽
- [简龙](https://hanxinma.gitlab.io/longma/longsan)/[龙三] 作者：青蛙
- 自然码 作者：（周志农）
- [小鹤双拼](https://flypy.com/) 作者：散步的鹤（何海峰）
- 拼音加加双拼 原作者：（廖恒毅）
- 小浪双拼 原作者：小浪
- [冰雪四拼](https://input.tansongchen.com/snow4/)/[声笔四拼](https://sbxlm.github.io/sbsp/) 原作者：谭淞宸
- 許氏鍵盤 原作者：許聞廉
- IBM 注音鍵盤 原作者：IBM
- 精業鍵盤 原作者：精業資訊
- 倚天 41 鍵、倚天忘形 26 鍵 原作者：倚天資訊
- 神通鍵盤 原作者：神通電腦
- 劉氏鍵盤 原作者：劉又銘
- 星光鍵盤 原作者：聽雨客
- 酷音大千二十六鍵鍵盤 原作者：新酷音
- [冰雪拼音](https://github.com/rimeinn/rime-snow-pinyin)
- [万象拼音](https://github.com/amzxyz/RIME-LMDG)
