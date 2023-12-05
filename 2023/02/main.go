package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
	"regexp"
	"strings"
	"strconv"
)

func main() {
    file, err := os.Open("input.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)
    //r, _ := regexp.Compile(`Game (\d+)`)
	r2, _ := regexp.Compile(`(\d+) (blue|green|red)`)

	/*
	maxes := map[string]int{
		"red": 12,
		"green": 13,
		"blue": 14,
	}*/

	count := 0
	index := 0

	// loop all lines
	//outer:
    for scanner.Scan() {
		index++
		line := scanner.Text()
		//fmt.Println(r.FindStringSubmatch(line)[1])
		sets := strings.Split(strings.Split(line, ":")[1], ";")

		totals := map[string]int{
			"red": 0,
			"green": 0,
			"blue": 0,
		}
		// track this outer loop
		//works := true
		for _, round := range sets {
			counts := r2.FindAllStringSubmatch(round, -1)
			//fmt.Println(counts)

			// check to see if we exceed
			for _, color := range counts {
				i, _ := strconv.Atoi(color[1])
				/*
				if i > maxes[color[2]] {
					works = false
				}*/
				// Track the number we absolutely need
				if i > totals[color[2]]{
					totals[color[2]] = i
				}
			}
		}

		mc := 1
		for _, num := range totals {
			mc *= num
		}

		count += mc
    }

	fmt.Println(count)
}