package main


type MyStack struct {
    values []int
    itemCount int
}


func Constructor() MyStack {
    return MyStack{}
}


func (this *MyStack) Push(x int)  {
    this.values = append(this.values, x)
    this.itemCount++
}


func (this *MyStack) Pop() int {
    if this.itemCount == 0 {
        return 0
    }

    val := this.values[this.itemCount - 1]
    this.values = this.values[:this.itemCount - 1]
    this.itemCount--
    return val
}


func (this *MyStack) Top() int {
    if this.itemCount == 0 {
        return 0
    }
    
    val := this.values[this.itemCount - 1]
    return val
}


func (this *MyStack) Empty() bool {
    return this.itemCount == 0
}

func main() {
    // Sample Usage

	// obj := Constructor();
 	// obj.Push(x);
 	// param_2 := obj.Pop();
 	// param_3 := obj.Top();
 	// param_4 := obj.Empty();
}