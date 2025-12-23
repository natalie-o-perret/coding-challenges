package main

import (
"fmt"
"os"
"path/filepath"
"runtime"
"strings"
)

func countHousesWithRobo(directions string) int {
	santaX, santaY := 0, 0
	roboX, roboY := 0, 0
	visited := make(map[string]bool)
	visited["0,0"] = true
	
	for i, char := range directions {
		if i%2 == 0 {
			switch char {
			case '^':
				santaY++
			case 'v':
				santaY--
			case '>':
				santaX++
			case '<':
				santaX--
			}
			key := fmt.Sprintf("%d,%d", santaX, santaY)
			visited[key] = true
		} else {
			switch char {
			case '^':
				roboY++
			case 'v':
				roboY--
			case '>':
				roboX++
			case '<':
				roboX--
			}
			key := fmt.Sprintf("%d,%d", roboX, roboY)
			visited[key] = true
		}
	}
	
	return len(visited)
}

func main() {
	if countHousesWithRobo("^v") != 3 {
		panic("Test failed: countHousesWithRobo(\"^v\") != 3")
	}
	if countHousesWithRobo("^>v<") != 3 {
		panic("Test failed: countHousesWithRobo(\"^>v<\") != 3")
	}
	if countHousesWithRobo("^v^v^v^v^v") != 11 {
		panic("Test failed: countHousesWithRobo(\"^v^v^v^v^v\") != 11")
	}

	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	inputPath := filepath.Join(dir, "..", "input.txt")
	content, err := os.ReadFile(inputPath)
	if err != nil {
		panic(err)
	}
	directions := strings.TrimSpace(string(content))
	
	result := countHousesWithRobo(directions)
	fmt.Printf("Go: %d\n", result)
}
