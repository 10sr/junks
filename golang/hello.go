package main

import (
	"fmt"
	"path/filepath"
)

func main() {
	fmt.Printf("hello, world\n")

	p, e := filepath.Abs("")

	fmt.Printf("%v\n", p)
	fmt.Printf("%v\n", e)
}
