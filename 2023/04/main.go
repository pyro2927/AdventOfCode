package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"sort"
	"strings"
)

func calcNext(seeds []int, lookup map[int]int) []int {
	newSeeds := []int{}
	for _, seed := range seeds {
		val, ok := lookup[seed]
		if ok {
			newSeeds = append(newSeeds, val)
		} else {
			newSeeds = append(newSeeds, seed)
		}
	}
	return newSeeds
}

func Min(array []int) int {
	var min int = array[0]
	for _, value := range array {
		if min > value {
			min = value
		}
	}
	return min
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	score := 0

	for scanner.Scan() {
		count := 0
		line := scanner.Text()
		all := strings.Split(strings.Split(line, ": ")[1], " | ")
		winners := strings.Fields(all[0])
		sort.Strings(winners)
		mine := strings.Fields(all[1])
		sort.Strings(mine)
		for _, w := range winners {
			for _, m := range mine {
				if w == m {
					count++
					break
				}
			}
		}

		if count > 0 {
			fmt.Printf("Matches: %d\n", count)
			score += int(math.Pow(2, float64(count-1)))
			fmt.Printf("Score: %d\n", score)
		}
	}

	fmt.Println(score)
}
