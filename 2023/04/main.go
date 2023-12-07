package main

import (
	"fmt"
	"os"
	"sort"
	"strings"
)

func main() {
	content, err := os.ReadFile("input.txt")
	if err != nil {
		//Do something
	}

	lines := strings.Split(string(content), "\n")

	var queue []int

	for i := 0; i < len(lines); i++ {
		queue = append(queue, i)
	}

	fmt.Println(len(queue))

	score := len(lines)

	for len(queue) > 0 {
		//fmt.Println(len(queue))
		score++
		// dequeue
		next := queue[0]
		queue = queue[1:]

		count := 0

		// load the correct line
		line := lines[next]

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

		// add our cards
		if count > 0 {
			//score += int(math.Pow(2, float64(count-1)))

			// track additional cards
			//fmt.Printf("Tracking next %d cards\n", count)
			for i := 1; i <= count; i++ {
				queue = append(queue, next+i)
			}
		}
	}

	fmt.Println(score)
}
