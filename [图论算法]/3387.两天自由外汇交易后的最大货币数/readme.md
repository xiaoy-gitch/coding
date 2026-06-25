给你一个字符串 initialCurrency，表示初始货币类型，并且你一开始拥有 1.0 单位的 initialCurrency。
另给你四个数组，分别表示货币对（字符串）和汇率（实数）：
- pairs1[i] = [startCurrency(i), targetCurrency(i)] 表示在 第 1 天，可以按照汇率 rates1[i] 将 startCurrency(i) 转换为 targetCurrency(i)。
- pairs2[i] = [startCurrency(i), targetCurrency(i)] 表示在 第 2 天，可以按照汇率 rates2[i] 将 startCurrency(i) 转换为 targetCurrency(i)。
- 此外，每种 targetCurrency 都可以以汇率 1 / rate 转换回对应的 startCurrency。
你可以在 第 1 天 使用 rates1 进行任意次数的兑换（包括 0 次），然后在 第 2 天 使用 rates2 再进行任意次数的兑换（包括 0 次）。
返回在两天兑换后，最大可能拥有的 initialCurrency 的数量。
注意：汇率是有效的，并且第 1 天和第 2 天的汇率之间相互独立，不会产生矛盾。
示例 1：
输入： initialCurrency = "EUR", pairs1 = [["EUR","USD"],["USD","JPY"]], rates1 = [2.0,3.0], pairs2 = [["JPY","USD"],["USD","CHF"],["CHF","EUR"]], rates2 = [4.0,5.0,6.0]
输出： 720.00000
解释：
根据题目要求，需要最大化最终的 EUR 数量，从 1.0 EUR 开始：
- 第 1 天：
  - 将 EUR 换成 USD，得到 2.0 USD。
  - 将 USD 换成 JPY，得到 6.0 JPY。
- 第 2 天：
  - 将 JPY 换成 USD，得到 24.0 USD。
  - 将 USD 换成 CHF，得到 120.0 CHF。
  - 最后将 CHF 换回 EUR，得到 720.0 EUR。
