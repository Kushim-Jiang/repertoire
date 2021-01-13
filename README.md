# 说明

## G 源

这一部分企图整理全体 G 源中可以被表述为结构化文本的部分。

- 第一列：序号（单位：无）。
- 第二列：汉字（单位：无）。
- 第三列：来源参考资料值（单位：无）或伪来源参考资料值（单位：无）。
- 第四列：描述（单位：无）。

进度：

- 【已完成】G0、G1、G7、G8、GE、GK、GCE、GH、GT
- 【待完成】G3、G5、G4K、GGH、GXC、GXH、GZH、GCH、GCY、GKX、GHZ、GHZR、GFC、GOCD、GXHZ、GHF、GZFY、GZJW、GFZ、GGFZ、GLK、GZ
- 【无法完成】GS、GDZ、GRM、GWZ、GBK、GHC、GIDC、GLGYJ、GPGLG、GCYY、GJZ、GKJ、GZYS


## 汉字频度统计_1988.txt

【核心参考文献】贝贵琴，张学涛．汉字频度统计——速成识读优选表．电子工业出版社，1988-04．（[全图联盟](http://book.ucdrs.superlib.net/views/specific/2929/bookDetail.jsp?dxNumber=000001081892&d=F354F677C912576BA20CE537E3431A70&fenlei=08011304)）

- 第一列：序号（单位：无）。对应参考文献正文第一列。
- 第二列：汉字（单位：无）。对应参考文献正文第二列。如果属于同一字位的字形出现在 GB/T 2312-1980 中，则使用 GB/T 2312-1980 中的字形，否则使用简化字，原书字形与简化字不一致的全体字形列举如下。
    - 1693「颜」，原文为「顔」。
    - 2174「峡」，原文为「峽」。
    - 4771「毐」，原文为「⿱士母」。
    - 5289「伫」，原文为「⿰亻宁」。
    - 5368「𫘧」，原文为「⿰马彔」。
    - 5883「盝」，原文为「⿱彔皿」。
    - 5972「𩽾」，原文为「鮟」。
    - 5974「鲯」，原文为「鯕」。
- 第三列：单字出现次数（类型一）（单位：个）。
- 第四列：累计出现次数（类型一）（单位：个）。对应参考文献正文第六列。
- 第五列：累计出现比例（类型一）（单位：%）。对应参考文献正文第七列。
- 第六列：单字出现次数（类型二）（单位：个）。对应参考文献正文第五列。
- 第七列：累计出现次数（类型二）（单位：个）。
- 第八列：累计出现比例（类型二）（单位：%）。
    - 两个类型的区分基于参考文献的字频累加错误。由于无法确认单字出现次数和累计出现次数何者更可靠，本文档基于分别假设单字出现次数或累计出现次数正确的前提下重新计算，其结果分别为类型二和类型一。

参考资料第三列给出了汉字的拼音，第四列给出了汉字的总笔画数。二者都有一些错误，但其与字频无关，且 Unihan 数据库中存在相关数据，因而不在此列举。关于参考资料的其它评论列举如下。
-   参考资料按单字出现字频降序排列，但 18「个」、231「立」、443「话」和 982「疗」的字频均大于上一字的字频。此外，如果假定累计出现次数正确，则 670「某」和 818「协」的字频也大于上一字的字频。
-   4326「軎」出现于 GB/T 2312-1980 中，其对应的简化字为「𰹲」。	
-   4914「朊」出现于 GB/T 2312-1980 中，归月部，但按其含义应归肉部，从而其实际指代「䏓」。

## 按字音查汉字频度表_1980.txt

【核心参考文献】郑林曦［主编］，高景成［主编］．按字音查汉字频度表（字音照汉字拼音字母顺序排列）．中国文字改革委员会，1980-08．（[全图联盟](http://book.ucdrs.superlib.net/views/specific/2929/bookDetail.jsp?dxNumber=000000924233&d=E2662B8B2432107B60EEBE62D0EB3F31&fenlei=0802070404)）

- 第一列：序号（单位：无）。由本人添加的流水号，按字头出现在书中的顺序排列。
- 第二列：汉字（单位：无）。对应参考文献正文第三列。
- 第三列：级别（单位：级）。对应参考文献正文第一列。原文的「Ⅰa、Ⅰ、Ⅱ、Ⅲ、Ⅳ、Ⅴ」均改为「1a、1、2、3、4、5」。改动了部分值，即按出现次数降序，原编号分别为 42、560、1367、2400、4170 及其之前的汉字的级别设定为 1a、1、2、3、4 级汉字，其余汉字为 5 级汉字。
- 第四列：原编号（单位：无）。对应参考资料正文第二列。原《汉字频度表》中〈综合频度表〉的编号。原文的「a、b、c」均改为「.1、.2、.3」。
- 第五列：出现次数（单位：个）。对应参考资料正文第四列。
- 第六列：注释（单位：无）。主要包括对字头的简繁修正、按附录对各数据的修正细节等。
