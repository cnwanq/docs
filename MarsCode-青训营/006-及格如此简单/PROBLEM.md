# 问题描述

为了响应国家全面发展的响应，学校提供了“德”、“智”、“体”、“美”、“劳” 等多门课程供同学们选择学习。

每位同学必修 3 门课程，可选修其他 3 门及以上课程。

小 A 同学选了 `n` 门选修课程，马上要期末考核了，请你帮小 A 同学算一算，如果小 A 同学要及格的话，他所学所有课程的成绩共有多少种组合的方式。

**注意**：
1. 同学的所有学习课程的平均分 >= 60 分 即为及格
2. 每门课程满分 100 分，只有 20 道选择题，每题 5 分，答错 0 分，答对 5 分
3. 成绩的总组合数对 202220222022 取模

## 输入

整数 `n` （`3 <= n <= 1000`）小 A 同学选修的课程数

## 输出

一个整数，表示小 A 同学所学课程能及格的成绩组合方式个数（对 202220222022 取模即可）