# ℞大狗拼音（标准粤语） Daagor Integration (ISO 639-3 yue-yyef)

目前包含：
- 香港語言學學會粵語拼音方案 (Jyutping, jyutping)
- 教育學院拼音方案 (ILE Romanization, ile)
- 劉錫祥拼音方案 (Sidney Lau Romanization, slr)
- 广州话拼音方案 (Guangdong Romanization, gdr)
- 耶魯拼音方案 (Yale, yale-yue)

同时允许使用词库：
- [粵語拼音方案](https://github.com/rime/rime-cantonese)

目前所有方案所需词库及语言模型请自行到对应的仓库下载。

## 文件解析

- `lib.babel-yue-yyef`： **（必需）** 输入方案跨拼音规范转换库
- `lib.scribe-yue-yyef`： **（必需）** 输入方案拼音形态转换库
- `lib.icon`： 对应输入法的指示器图标
  - `icon.ascii`： 输入法键盘直接输入模式图标
  - `icon.imecn`： 输入法模式中国大陆方案图标
  - `icon.imehk`： 输入法模式香港方案图标
- `dictionary`： **（根据调用词库必需）** 词典处理库，用于对接需要使用的拼音词库；选用的词库对所有方案全局生效
  - `yue-yyef-rime-terra`：调用粵語拼音方案词库
- `rscm.*`：基于以上文件组成的输入方案
  - `gdr` 广州话拼音方案
  - `ile` 教育學院拼音方案
  - `jyutping` 香港語言學學會粵語拼音方案
  - `slr` 劉錫祥拼音方案
  - `yale-yue` 粵語耶魯拼音方案
- `supplimental`：用于提供额外方案。这些方案包含：
  - 廣州話拉丁化新文字輸入方案 (latinfa)

## 方案所需的词典文件及语法模型文件；

  * 粵語拼音方案模型使用 `zh-hant-t-essay-bg?.gram`
  * 词库及语法模型下载地址在后方内容

## 输入键盘布局

输入音调的方法为：在输入音节后，以主键盘上 7-0 以及 - = 两个符号分别粤语 1-6 声，其中入声中高阴入为 7，中阴入为 9，阳入为 =。不使用声调时可作普通拼音使用。

## 词库及语法模型

注意：不同词库之间会存在拼写差异。

- 八股文模型（繁体）： https://github.com/lotem/rime-octagram-data/tree/hant
- 粵語拼音方案词库： https://github.com/rime/rime-cantonese (*.dict.yaml)

## 致谢

- [RIME 输入引擎](https://github.com/rime)
- [粵語拼音方案](https://github.com/rime/rime-cantonese)
