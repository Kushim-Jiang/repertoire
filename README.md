# Description

## Tibetan > 20542-22238.txt

The Tibetan data is maintained in [`tibtfontbuilder`](https://github.com/kushim-Jiang/tibtfontbuilder/).

## KhitanSmall > khitan-words.txt

- Column 1: Serial number.
- Column 2: Number sequence.
- Column 3: Codepoint sequence.

The vocabulary in the document is taken from 契丹小字词汇索引 and has not been proofread nor has the filler been added to fit the character set model.

## G-Source

This section attempts to collate the parts of the overall G-source that can be represented as structured text.

- Column 1: Serial number.
- Column 2: Character.
- Column 3: Source reference or pseudo source reference.
- Column 4: Description.

Progress:

- [Finished] G0, G1, G7, G8, GE, GK, GCE, GH, GT
- [Not finished] G3, G5, G4K, GGH, GXC, GXH, GZH, GCH, GCY, GKX, GHZ, GHZR, GFC, GOCD, GXHZ, GHF, GZFY, GZJW, GFZ, GGFZ, GLK, GZ
- [Cannot be finished] GS, GDZ, GRM, GWZ, GBK, GHC, GIDC, GLGYJ, GPGLG, GCYY, GJZ, GKJ, GZYS

## 字频 (Frequency)

### 字频 > 汉字频度统计\_1988.txt

[Core Reference] 贝贵琴, 张学涛. 汉字频度统计——速成识读优选表. 电子工业出版社, 1988-04. ([全图联盟](http://book.ucdrs.superlib.net/views/specific/2929/bookDetail.jsp?dxNumber=000001081892&d=F354F677C912576BA20CE537E3431A70&fenlei=08011304))

- Column 1: Serial number. Corresponds to the Column 1 of the body of the reference.
- Column 2: Character. Corresponds to the Column 2 in the body of the reference. If the forms belonging to the same character position appear in GB/T 2312—1980, the glyphs in GB/T 2312—1980 are used; otherwise, simplified characters are used. All forms in the original book that do not agree with the simplified characters are listed below.

  - 1693 “颜”, original “顔”.
  - 2174 “峡”, original “峽”.
  - 4771 “毐”, original “⿱士母”.
  - 5289 “伫”, original “⿰亻宁”.
  - 5368 “𫘧”, original “⿰马彔”.
  - 5883 “盝”, original “⿱彔皿”.
  - 5972 “𩽾”, original “鮟”.
  - 5974 “鲯”, original “鯕”.

- Column 3: Character frequency (type A) (times).
- Column 4: Accumulate frequency (type A) (times). Corresponds to the sixth column in the body of the reference.
- Column 5: Accumulate frequency ratio (type A) (%). Corresponds to the seventh column in the body of the reference.
- Six column: Character frequency (type B) (times). Corresponds to the Column 5 in the body of the reference.
- Seventh column: Accumulate frequency (type B) (times).
- Eighth column: Accumulate frequency ratio (type B) (%).

The distinction between the two types is based on the incorrect accumulate frequencies in the references. As it is not possible to confirm which is more reliable, the number of single word occurrences or cumulative occurrences, this document is recalculated based on the assumption that the number of single word occurrences or cumulative occurrences are correct, respectively, and the results are type two and type one.

The Column 3 of the reference gives the pinyin of the character and the Column 4 gives the total number of strokes of the character. Both have some errors, and they are not related to the frequency of the characters and similar data exist in the Unihan database, so they are not listed here. Other comments on the references are listed below.

- The references are listed in descending order of character frequency, but the frequency of 18 “个”, 231 “立”, 443 “话”and 982 “疗”are all greater than the frequency of the previous character. In addition, if the cumulative number of occurrences is assumed to be correct, the character frequencies for 670 “某”and 818 “协”are also greater than the frequency of the previous character.
- 4326 “軎”appears in GB/T 2312—1980 and its corresponding simplified character is “𰹲”.
- 4914 “朊”appears in GB/T 2312—1980 under 月 radical, but by implication should be under 肉 radical, so that it actually refers to “䏓”.

### 字频 > 按字音查汉字频度表\_1980.txt

[Core Reference] 郑林曦 (chief), 高景成 (chief). 按字音查汉字频度表 (字音照汉字拼音字母顺序排列). 中国文字改革委员会, 1980-08. ([全图联盟](http://book.ucdrs.superlib.net/views/specific/2929/bookDetail.jsp?dxNumber=000000924233&d=E2662B8B2432107B60EEBE62D0EB3F31&fenlei=0802070404))

- Column 1: Serial number.
- Column 2: Character. Corresponds to the Column 3 in the body of the reference.
- Column 3: Level (level). Corresponds to the Column 1 in the body of the reference. The original “Ⅰa, Ⅰ, Ⅱ, Ⅲ, Ⅳ, Ⅴ”have been changed to “1a, 1, 2, 3, 4, 5”. Some of the values have been changed, i.e. the characters originally numbered 42, 560, 1367, 2400, 4170 and earlier have been set in descending order of occurrence as level 1a, 1, 2, 3 and 4 characters, while the rest are level 5 characters.
- Column 4: original serial number. Corresponds to the Column 2 in the body of the reference. The number of the 综合频度表 in the original 汉字频度表. For “a, b, c”in the original text, read “.1, .2, .3”.
- Column 5: Frequency (times). Corresponds to the Column 4 in the body of the reference.
- Column 6: Notes. Mainly includes corrections to headers for simplified/traditional form, details of corrections to individual data by appendix, etc.

## 字盘 (Cases)

### 字盘 > 新华字目表\_1976.txt

[Core Reference] 北京新华字模厂字目表. 1976-05. ([孔夫子](https://book.kongfz.com/28596/3131848582/1632580369/))

- Column 1: Serial number.
- Column 2: Character.
- Column 3: Radical.
- Column 4: Level (level).
- Column 5: Page number.
- Column 6: Pseudo source reference.

### 字盘 > 新字盘样本\_1967.txt

[Core Reference] 上海字模一厂新字盘样本. 1967. ([孔夫子](https://book.kongfz.com/231815/1391608848/1632580621/))

- Column 1: Serial number.
- Column 2: Character.
- Column 3: Case number.
- Column 4: Pseudo source reference.

### 字盘 > 标题字盘书\_1975.txt

[Core Reference] 标题字盘书. 荆州印刷厂. 1975-10. ([孔夫子](https://book.kongfz.com/17731/2107892434/1636599860/))

- Column 1: Serial number.
- Column 2: Character.
- Column 3: Pseudo source reference.
