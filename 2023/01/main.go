package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func main() {
	// Specify the file path
	filePath := "input.txt"

	lookup := map[string]string{
		"one":   "1",
		"two":   "2",
		"three": "3",
		"four":  "4",
		"five":  "5",
		"six":   "6",
		"seven": "7",
		"eight": "8",
		"nine":  "9",
	}
	// Open the file
	file, err := os.Open(filePath)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close() // Close the file when done

	pattern := `(one|two|three|four|five|six|seven|eight|nine|\d)`
	greedy := `.*(one|two|three|four|five|six|seven|eight|nine|\d)`

	regex, err := regexp.Compile(pattern)
	gregex, err := regexp.Compile(greedy)

	if err != nil {
		fmt.Println("Error compiling regex:", err)
		return
	}
	// Create a scanner to read the file line by line
	scanner := bufio.NewScanner(file)

	// Read and print each line
	sum := 0

	for scanner.Scan() {
		//fmt.Println(scanner.Text())
		matches := regex.FindAllString(scanner.Text(), -1)
		greedyMatches := gregex.FindStringSubmatch(scanner.Text())

		first := matches[0]

		// song and dance
		if len(first) > 1 {
			first = lookup[first]
		}

		last := greedyMatches[1]
		fmt.Println(last)

		if len(last) > 1 {
			last = lookup[last]
		}

		fmt.Println(first + last)
		i, err := strconv.Atoi(first + last)
		if err != nil {
			// ... handle error
			panic(err)
		}
		sum += i
	}

	fmt.Println(sum)

	// Check for errors during scanning
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
	}
}
