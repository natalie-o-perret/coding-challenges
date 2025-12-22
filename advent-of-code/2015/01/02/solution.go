package main

import (
	"fmt"
	"os"
)

func findAndPrintBasementPosition(source string) {
	floor := 0
	for position, char := range source {
		switch char {
		case '(':
			floor++
		case ')':
			floor--
		}

		if floor == -1 {
			fmt.Println(position + 1) // 1-indexed
			break
		}
	}
}

func main() {
	// causes him to enter the basement at character position 1
	findAndPrintBasementPosition(")")

	// causes him to enter the basement at character position 5
	findAndPrintBasementPosition("()())")

	data, err := os.ReadFile("../input.txt")
	if err != nil {
		panic(err)
	}
	findAndPrintBasementPosition(string(data))
}
