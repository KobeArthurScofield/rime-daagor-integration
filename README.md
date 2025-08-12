# ℞大狗拼音 Daagor Integration

基于中州韵输入法引擎 (RIME) 构建的带调拼音方案集合。

目前包含：
- 带调标准汉语拼音 (HanYu PinYin, hanyu-pinyin)
- 带调双拼
  - 自然码双拼 (ZiRanMa, ziranma)
  - 小鹤双拼 (Fly PinYin, flypy)
  - 拼音加加双拼 (PinYinJiaJia, pinyinjiajia)
  - 汉心龙双拼 (HanXin Long, hanxinlong)
  - 自然龙双拼 (ZiRan Long, ziranlong)
- 帶聲調通用拼音 (Tongyong Pinyin, tongyong-pinyin)
- 國語注音符號第二式，國音二式 (Phonetic Symbols II (MPS II), mpsii)
- 國語羅馬字 (Gwoyeu Romatzyh, gwoyeu)

同时允许使用数种带声调词库：
- RIME 发行版内置的[地球拼音方案词库](https://github.com/rime/rime-terra-pinyin)
- [冰雪拼音词库](https://github.com/rimeinn/rime-snow-pinyin)
- [万象词库](https://github.com/amzxyz/RIME-LMDG)

目前所有方案所需词库及语言模型请自行到对应的仓库下载。

AI 辅助解析： [![Deepwiki Generated Documentation](https://deepwiki.com/badge.svg)](https://deepwiki.com/KobeArthurScofield/rime-daagor-integration)

## 文件解析

- `lib.shared`： **（必需）** 输入方案通用基础组件
- `lib.babel`： **（必需）** 输入方案跨拼音规范转换库
- `lib.normalizer`： **（必需）** 输入方案拼音形态转换库
- `icon`： **（小狼毫必需）** 输入指示器图标
  - `lib.icon`： 对应输入法的指示器图标
- `opencc`：特殊繁简转换方案
  - `noop.json`：不转换
- `experience`：Daagor Integration Experience，用于取代输入方案默认体验
  - `lib.shared`：提供经过调整的 RIME 发行版默认以外的体验
    - `daagorxp.lib.keybinder`：非默认按键组合体验
    - `daagorxp.lib.punctuation`：非默认标点输入体验
    - `daagorxp.lib.recognizer`：非默认识别功能体验
  - `daagorxp.lib.comment`：提供拼音提示转换功能，使拼音提示显示为输入方案相同而非词库方案；启用后全局生效
  - `daagorxp.lib.preedit`：提供上屏字符转换功能，上屏显示为对应拼音而非输入字符；启用后全局生效
- `dictionary`： **（根据调用词库必需）** 词典处理库，用于对接需要使用的拼音词库；选用的词库对所有方案全局生效
  - `rime-terra`：调用 RIME 发行版附带的地球拼音词库
  - `rime-snow`：调用冰雪拼音词库
  - `rime-lmdg`：调用万象拼音词库
    - `dict.wanxiang.*`：词库分包文件
- `rscm.*`：基于以上文件组成的输入方案
- `supplimental`：用于提供额外方案。这些方案包含：
  - 威妥玛拼音 (wade-giles)（及邮政拼音 (postcal) 和简化威妥玛拼音 (wand-giles-simp)）
  - 法国远东学院拼音 (efeo)
  - 德国式拼音 (lessing-othmer)
  - 拉丁化新文字 (latinxua)
  - 耶鲁拼音 (yale)
  - 捷克式拼音 (cesky)

## 下载及部署

1. 将下载的代码包解压；
2. 将以下文件复制到 RIME 前端设定的用户文件夹：

  * `lib.shared`
  * `lib.babel`
  * `lib.normalizer`
  * `icon`
    * 将 icon 文件夹内所需图标文件复制至与其以上文件同一个文件夹
      * `lib.icon.ascii`：键盘直接字符模式图标，所有方案使用
      * `lib.icon.cn`：输入法转换模式图标，大陆流行方案使用
      * `lib.icon.hk`：输入法转换模式图标，港澳流行方案使用
      * `lib.icon.tw`：输入法转换模式图标，台湾流行方案使用
  * `opencc`
    * 将 opencc 文件夹连同内含文件复制至与其以上文件同一个文件夹
  * `rscm.<期望使用的方案名称>`
    * `flypy` 小鹤双拼布局
    * `gwoyeu` 国语罗马字布局
    * `gwoyeu` 国语罗马字布局
    * `hanxinlong` 汉心龙/龙码双拼布局
    * `hanyu-pinyin` 汉语拼音布局
    * `mpsii` 国音二式布局
    * `pinyinjiajia` 拼音加加双拼布局
    * `tongying-pinyin` 通用拼音布局
    * `ziranlong` 自然龙双拼布局
    * `ziranma` 自然码双拼布局
  * `dictionary/<使用词库名称>/<所有文件>`
    * 复制自己所需的词库调用文件，与以上文件置于同一个文件夹
  * `supplimental`
    * 如果有需要，复制自己所需的库文件及方案文件，与以上文件置于同一个文件夹
  * `experience`
    * 如果希望使用非 RIME 自带的默认输入体验，可以按需复制其中文件与以上文件置于他送一个文件夹：
      * `lib.comment` 与 `lib.preedit` 可以单独复制
      * `lib.shared` 必须与 `lib.keybinder`、`lib.punctuation` 与 `lib.recognizer` 一并复制

3. 复制选用方案所需的词典文件及语法模型文件；

  * 冰雪拼音语法模型使用 `amz-v2n3m1-zh-hans.gram`
  * 地球拼音语法模型使用 `zh-han?-t-essay-bg?.gram`
  * 万象拼音语法模型使用 `wanxiang-lts-zh-hans.gram`
  * 词库及语法模型下载地址在后方内容

4. Windows 下使用小狼毫，进入“小狼毫设置”勾取自己需要的输入方案并确定，等待部署完成。
5. 非小狼毫用户，需在用户文件夹下的 `default.custom.yaml` 中添加以下内容（以添加使用地球拼音词库的小鹤双拼及全拼为例，格式为 `daagornt.rscm.<方案名>`），保存后部署：
``` yaml
patch:
  schema_list:
    - {schema: "daagornt.rscm.flypy"}
    - {schema: "daagornt.rscm.hanyu-pinyin"}
```


## 输入键盘布局

布局本身不支持音调时，输入音调的方法为：在输入音节后，以主键盘上 6-0 分别代表阴平、阳平、上声、去声和轻声。不使用声调时可作普通拼音使用。

### 汉心龙键盘布局

![键盘布局](image/hxlong-2025-01.png)

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

![键盘布局](image/zrlong-2025-01.jpg)

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

## 鸣谢

- [RIME 输入引擎](https://github.com/rime)
- [汉心龙](https://hanxinma.gitlab.io/longma/hanxinlong) 作者：晡时之光
- [自然龙](https://hanxinma.gitlab.io/longma/ziranlong) 作者：小幽幽
- 自然码 作者：（周志农）
- [小鹤双拼](https://flypy.com/) 作者：散步的鹤（何海峰）
- 拼音加加双拼 原作者：（廖恒毅）
- [冰雪拼音](https://github.com/rimeinn/rime-snow-pinyin)
- [万象拼音](https://github.com/amzxyz/RIME-LMDG)
