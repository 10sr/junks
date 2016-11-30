package main

import (
	"fmt"
	"path/filepath"
	"os"
)

func main() {
	fmt.Printf("hello, world\n")

	p, e := filepath.Abs("")

	fmt.Printf("%v\n", p)
	fmt.Printf("%v\n", e)

	stat, _ := os.Stat("parent")
	if stat != nil {
		fmt.Printf("Stat name: %s", stat.Name())
		fmt.Printf("Stat isdir: %v", stat.IsDir())
	}
}
