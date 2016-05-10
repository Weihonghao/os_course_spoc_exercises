#Q: 请在lab7-answer中分析:

##cvp->count含义是什么？cvp->count是否可能<0, 是否可能>1？请举例或说明原因。

cvp->count含义是等待条件变量的进程个数。
因为cvp->count永远是先加后减，所以cvp->count不可能<0
因为等待的进程数可能有多个，所以cvp->count可能>1。

##cvp->owner->next_count含义是什么？cvp->owner->next_count是否可能<0, 是否可能>1？请举例或说明原因。
cvp->owner->next_count含义是因发出signal进入睡眠的进程个数。
因为cvp->owner->next_count永远是先加后减，所以cvp->owner->next_count不可能<0。
cvp->owner->next_count不可能>1，因为一旦 cvp->owner->next_count += 1，变成1，进程A发出signal唤醒进程B后睡眠，B执行结束后，必然会通过cvp->owner->next_count>0的判断，执行signal操作，，又会唤醒A，此时cvp->owner->next_count -= 1。


##目前的lab7-answer中管程的实现是Hansen管程类型还是Hoare管程类型？请在lab7-answer中实现另外一种类型的管程。
目前的lab7-answer中管程的实现是Hoare管程类型。


