#问题：操作系统采用整形运算，溢出的时候怎么解决？
STRIDE_MAX – STRIDE_MIN <= PASS_MAX这是很重要的一个条件。
假设我们现在知道最小的stride值，不妨记为s，那所有的stride一定在[s,s+PASS_MAX]这个区间里。即便区间的右半部分溢出了，也不会和左半部分重叠，因此，可以看到最小stride左边的一定比stride右边的大，然后内部服从正常的数轴大小关系。
另外一个思路是，我们还知道Priority > 1的限制，所以我们有STRIDE_MAX – STRIDE_MIN <= BIG_STRIDE，因此我们可以设置BIG_STRIDE的大小，就可以了。