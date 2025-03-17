# ℞大狗拼音核心版 Daagor Integration Core

基于带调拼音的方案集合。核心版即功能仅有打字。（如需丰富功能欢迎基于此仓库开建新仓库添加功能）

包含带调自然码双拼、带调小鹤双拼、汉心龙双拼及自然龙双拼，同时允许使用内置的地球拼音方案词库，或者冰雪拼音词库或万象词库。

目前所有方案所需词库及语言模型请自行到对应的仓库下载。

## 文件解析

`lib.component`： **（必需）** 输入法基础组件。

`lib.experience`： **（必须）** 输入法体验组件。

`lib.bridge`：（必需）提供词库及代码格式转换。

`lib.dict`： **（根据调用词库必需）** 输入法调用词库所需配置。

`lib.layout`： **（根据使用拼音方案必需）** 输入法键盘映射所需配置。

`rscm`：基于以上文件组成的输入方案。

`opencc/noop.json`：特殊繁简转换方案（阻止转换）。

`terra-*`：基于地球拼音词库及八股文繁体字模型

`snow-*`：基于冰雪拼音词库及万象通用模型

`wanxiang-*`：基于万象原子词库及万象原子模型

## 输入键盘布局

- [汉心龙](https://hanxinma.gitlab.io/longma) 原作者：晡时之光
- [自然龙](https://hanxinma.gitlab.io/longma/zrl) 原作者：晡时之光
- 自然码 原作者：周志农
- [小鹤双拼](https://flypy.com/) 原作者：何海峰
- 拼音（或称全拼、标准拼音）

布局本身不支持音调时，输入音调的方法为：在输入音节后，以主键盘上 6-0 分别代表阴平、阳平、上声、去声和轻声。不使用声调时可作普通拼音使用。

### 汉心龙键盘布局

![键盘布局](image/hxlong-2025-01.png)

新增按键见下：

#### ExtK-HX-01

| 拼音成份 | 按键（12345 声） |
|--------|----------------|
| 轻声 | 所有轻声的按键与其第一声相同 |
| ê | LUICL |
| 空韵母 h | MNCLM |
| 空韵母 m | ULNIU |
| 空韵母 n | CLTKC |
| 空韵母 ng | CIGUC |

### 自然龙键盘布局

![键盘布局](image/zrlong-2025-01.jpg)

新增按键见下：

#### ExtK-ZR-01

| 拼音成份 | 按键（12345 声） |
|--------|----------------|
| 轻声 | 所有轻声的按键与其第一声相同 |
| ê | YATQY |
| 空韵母 h | VZNXV |
| 空韵母 m | AYBTA |
| 空韵母 n | QYZBQ |
| 空韵母 ng | QTJAQ |

## 词库及语法模型

- 八股文模型（繁体）： https://github.com/lotem/rime-octagram-data/tree/hant
- 冰雪拼音词库： https://github.com/rimeinn/rime-snow-pinyin (*.dict.yaml)
- 万象词库： https://github.com/amzxyz/RIME-LMDG/releases/tag/dict-nightly （需要同时下载 https://github.com/amzxyz/RIME-LMDG/blob/main/wanxiang.dict.yaml ）
- 万象通用模型： https://github.com/amzxyz/RIME-LMDG/releases/tag/v2n3
- 万象原子模型： https://github.com/amzxyz/RIME-LMDG/releases/tag/LTS

## 注意

### 拼音表示方式转换

将音调转换至末尾标注时的转换方向，一种是仅转换音调而保留所有拼写（normal），另一种是将拼写压缩到常用拼音拼写组合（limited）；前者适用于所用布局能支持词库中所有拼写（如扩展后的汉心龙、自然龙），后者适用于所用布局仅能支持常见拼写（如一般双拼）。

示例如下：

| 原形式 | normal | limited |
|----|----|----|
| ê | ê | eh |
| hm | hm | hun |
| hng | hng | heng |
| m | m | mu |
| n | n | en |
| ng | ng | eng |

- 目前该框架可以正常支持包含但不限于《现代汉语词典》中存在的拼写，而压缩拼写组合则支持范围为《现代汉语词典中》存在的拼写。

### 为何部分方案没有特定音节

需要对应的词库支持该拼写。
