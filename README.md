# ℞大狗拼音 Daagor Integration

基于中州韵输入法引擎 (RIME) 构建的带调拼音方案集合。

目前支持：
- 基于北方官话的[拼音注音方案输入](lang-cmn-pan/README-cmn-pan.md) (ISO 639-3 cmn)
- 基于标准粤语的[粤语拼音方案输入](lang-yue-yyef/README-yue-yyef.md) (ISO 639-3 yue)

警告：所有方案及词库无法跨 ISO 639-3 语言代码使用！

~~已经沉浸在自己的艺术中无法自拔的~~ AI 辅助解析： [![Deepwiki Generated Documentation](https://deepwiki.com/badge.svg)](https://deepwiki.com/KobeArthurScofield/rime-daagor-integration)

## 下载及部署

一般情况下到 [Release](releases/latest) 下载即可。

如果需要下载开发中版本，请到 Actions 下载（保存期限为 90 日）。

1. 将下载的文件包解压；`base` 为基础文件，`extension` 为补充的 Daagor Experience 文件、特殊配置补丁以及额外方案文件。
2. 将以下文件复制到 RIME 前端设定的用户文件夹：

  * `lib.shared`
  * `lib.asciichar`、`lib.asciiphrase`及`lib.quickphrase`
  * `lib.babel-<ISO 639-3>`
    * 视需要使用的拼音方案对应的语言区复制即可
  * `lib.scribe-<ISO 639-3>`
    * 视需要使用的拼音方案对应的语言区复制即可
  * `lib.icon`
    * 将所需图标文件复制至与其以上文件同一个文件夹
      * `lib.icon.ascii`：键盘直接字符模式图标，所有方案使用
      * `lib.icon.cn`：输入法转换模式图标，大陆流行方案使用
      * `lib.icon.hk`：输入法转换模式图标，港澳流行方案使用
      * `lib.icon.tw`：输入法转换模式图标，台湾流行方案使用
  * `opencc`
    * 将 opencc 文件夹连同内含文件复制至与其以上文件同一个文件夹
      * 建议按照使用词库的繁体/简体属性复制，其中：
        * `hk2*`：词库类型为香港繁体时使用
        * `s2*`：词库类型为简体时使用
        * `t2*`：词库类型为大陆传统体时使用
        * `tw2*`：词库类型为台湾正体时使用
        * `noop`：所有方案必须，当词库及输入方案默认字型相同时使用，表示“不转换”
      * 由于各发行版可能存在机制缺陷，OpenCC **可能**无法识别文件中指向的 OCD2 文件，此种情况需要自行建立到发行版自带的 OCD2 文件链接，或者自行编译，或替换 `lib.shared` 中的转换配置为发行版自带配置
        * 如果没有遇到简繁转换不生效的问题则无需做此操作
  * `customize`
    * 若为初次安装，将 customize 内含文件复制至与其以上文件同一个文件夹
    * 若自己已有相关自定义文件内容，切勿直接覆盖文件以免造成内容丢失
  * `rscm.<期望使用的方案名称>`
  * `dictionary/<使用词库名称>/<所有文件>`
    * 复制自己所需的词库调用文件，与以上文件置于同一个文件夹
  * `experience`
    * 如果希望使用非 RIME 默认自带的输入体验，可以按需复制其中文件与以上文件置于同一个文件夹：
      * `lib.shared` 必须与 `lib.keybinder` 与 `lib.punctuation` 与 `lib.extchar` 一并复制
  * `supplimental`
    * 如果有需要，复制自己所需的库文件及方案文件，与以上文件置于同一个文件夹

3. 复制选用方案所需的词典文件及语法模型文件；
4. Windows 下使用小狼毫，进入“小狼毫设置”勾取自己需要的输入方案并确定，等待部署完成。
5. 非小狼毫用户，需在用户文件夹下的 `default.custom.yaml` 中添加以下内容（以添加使用地球拼音词库的小鹤双拼及全拼为例，格式为 `daagornt.rscm.<方案名>`），保存后部署：
``` yaml
patch:
  schema_list/+:
    - {schema: "daagornt.rscm.flypy"}
    - {schema: "daagornt.rscm.hanyu-pinyin"}
```

## 文件解析

- `lib.shared`： **（必需）** 输入方案通用基础组件
- `lib.asciichar`、`lib.asciiphrase`及`lib.quickphrase`
  - 特殊词典文件，用于快速输入符号及短语
- `lib.babel-<ISO 639-3>`： **（根据调用输入法必需）** 输入方案跨拼音规范转换库
- `lib.scribe-<ISO-936-3>`： **（根据调用输入法必需）** 输入方案拼音形态转换库
- `lib.icon`： 对应输入法的指示器图标
- `opencc`：繁简转换方案
- `customize`: 输入法可自定义内容
  - `custom.custom_phrase`: 自定义短语，该短语可跨布局及 ISO 639-3 使用，直接输入编码即可
    - 更新时注意：如果自己已有自定义短语内容，切勿使用解包后文件直接替换！会造成内容丢失！
- `experience`：Daagor Integration Experience，用于取代输入方案默认体验
  - `lib.shared`：提供经过调整的 RIME 发行版默认以外的体验
    - `daagorxp.lib.keybinder`：非默认按键组合体验
    - `daagorxp.lib.punctuation`：非默认标点输入体验
    - `daagorxp.lib.extchar`：字符输入扩展功能，包括 GB 区码输入、BIG5 内码输入、HKSCS 内码输入、电报码输入、郑码输入、仓颉输入、苍颉输入及笔画输入
- `dictionary`： **（根据调用词库必需）** 词典处理库，用于对接需要使用的拼音词库；选用的词库对所有方案全局生效
- `rscm.*`：基于以上文件组成的输入方案
- `supplimental`：用于提供额外方案。

## 特殊内容输入

以下为特殊内容输入指示符：

### 即时输入

- `｀`：一般符号输入，详细可输入内容见 `rime-prelude` （标准版）或 `daagorxp.lib.punctuation` （Daagor Experience）
- `prev`：历史输入记录
- `gr`：输入希腊字母
- `cr`：输入现代西里尔字母
- `kn`：输入现代日语假名
- `em`：输入现代韩语谚文字符（含有动态组字字符及兼容单字块字符）
- `ar`：输入亚美尼亚字符
- `gg`：输入格鲁吉亚字符
- `ab`：输入阿拉伯字符
- `hb`：输入希伯来字符
- `mg`：输入传统蒙古文字符
- `zd`：星座符号
- `mn`：月份符号
- `wk`：星期曜日符号

### 转换输入

使用时主键盘区数字列用于输入无法选词，需小键盘数字或导航键辅助

- `Pa`：北约字母表
- `Di`：易经、八卦、六十四卦文字及字符
- `Dt`：太玄经文字及字符
- `LC`：代日韵目、时间及日期字符（电码字母）
- `LD`：代日韵目、时间及日期字符（电码文字本身数字）
- `Nt`：中文大写数字（传统字形）
- `Ns`：中文大写数字（简化字形）
- `Nc`：通讯用读法数字
- `Nf`：苏州码子
- `A`：通用简写输入月份及星期
- `TM`：输入月份
- `TD`：输入日数
- `TW`：输入星期
- `TH`：输入小时
- `Ss`：节气
- `SHE`：天干
- `SEA`：地支
- `SSEG`：干支
- `TCLM`：农历月份
  - `TCLML`：农历闰月
- `TCLD`：农历日子
- `Dz`：十二生肖（陆港澳台）
- `SSEY`：干支纪年
- `SSEM`：地支/干支纪月
- `SSED`：干支纪日
- `SEAY`：地支纪年
- `SSEH`：地支/干支纪时
  - `SSEHB`：纪初
  - `SSEHM`：纪正
- `SSEQ`：纪刻
  - `SSEQF`：顺序纪刻
  - `SSEQ0`/`SSEQ1`：
- `Mc`：摩斯电码
- `Ci`/`Cq`/`Cz`：电码简码
- `Ca`：ARRL 简码

### 查码表

该功能仅限 Daagor Experience

使用时主键盘区数字列用于输入无法选词，需小键盘数字或导航键辅助

- `CM`：电报明码（中国大陆）
- `CT`：电报明码（台湾）
- `CH`：电报明码（香港）
- `HC`：香港增补字符集内码
- `B5`：大五码内码
- `G0`：GB-2312 区位码
- `GK`：GBK 内码（含 GB-2312 内码）
- `C5`：仓颉五代检字码
- `C6`：苍颉检字码
- `ZM`：郑码检字码
- `ST`：笔画检字码
  - 横：h
  - 竖：u
  - 撇：m
  - 捺/点：k
  - 折：j

## 致谢

- [RIME 输入引擎](https://github.com/rime)
