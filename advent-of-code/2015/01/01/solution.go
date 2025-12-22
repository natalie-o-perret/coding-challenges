package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func calculateAndPrintFloor(source string) {
	floor := 0
	for _, char := range source {
		switch char {
		case '(':
			floor++
		case ')':
			floor--
		}
	}
	fmt.Println(floor)
}

func main() {
	// both result in floor 0
	calculateAndPrintFloor("(())")
	calculateAndPrintFloor("()()")

	// both result in floor 3.
	calculateAndPrintFloor("(((")
	calculateAndPrintFloor("(()(()(")

	// also results in floor 3.
	calculateAndPrintFloor("))(((((")

	// both result in floor -1 (the first basement level).
	calculateAndPrintFloor("())")
	calculateAndPrintFloor("))(")

	// both result in floor -3.
	calculateAndPrintFloor(")))")
	calculateAndPrintFloor(")())())")

	execPath, _ := os.Executable()
	execDir := filepath.Dir(execPath)
	inputPath := filepath.Join(execDir, "..", "input.txt")
	input, _ := os.ReadFile(inputPath)
	calculateAndPrintFloor(string(input))
}
