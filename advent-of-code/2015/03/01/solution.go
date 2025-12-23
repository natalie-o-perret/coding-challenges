package main

import (
	"fmt"
	"os"
	"path/filepath"
	"runtime"
	"strings"
)

func countHouses(directions string) int {
	x, y := 0, 0
	visited := make(map[string]bool)
	visited["0,0"] = true

	for _, char := range directions {
		switch char {
		case '^':
			y++
		case 'v':
			y--
		case '>':
			x++
		case '<':
			x--
		}
		key := fmt.Sprintf("%d,%d", x, y)
		visited[key] = true
	}

	return len(visited)
}

func main() {
	// Test cases with assertions
	if countHouses(">") != 2 {
		panic("Test failed: countHouses(\">\") != 2")
	}
	if countHouses("^>v<") != 4 {
		panic("Test failed: countHouses(\"^>v<\") != 4")
	}
	if countHouses("^v^v^v^v^v") != 2 {
		panic("Test failed: countHouses(\"^v^v^v^v^v\") != 2")
	}

	// Read input and calculate result
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	inputPath := filepath.Join(dir, "..", "input.txt")
	content, err := os.ReadFile(inputPath)
	if err != nil {
		panic(err)
	}
	directions := strings.TrimSpace(string(content))

	result := countHouses(directions)
	fmt.Printf("Go: %d\n", result)
}
