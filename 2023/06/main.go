package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

// returns number of ways we can beat it
func calcWays(t, d int) int {
	// determine halfway point
	half := (t - 1) / 2
	ways := 0
	for true {
		// track all the ways we can beat the old distance score
		if half*(t-half) > d {
			ways++
			half--
		} else {
			break
		}
	}
	ways *= 2
	// add one if we're even stevens
	if t%2 == 0 {
		ways++
	}

	return ways
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	// Get times
	scanner.Scan()
	times := strings.Fields(scanner.Text())
	megaTime, _ := strconv.Atoi(strings.ReplaceAll(strings.Split(scanner.Text(), ": ")[1], " ", ""))

	// get distances
	scanner.Scan()
	distances := strings.Fields(scanner.Text())
	megaDistance, _ := strconv.Atoi(strings.ReplaceAll(strings.Split(scanner.Text(), ": ")[1], " ", ""))

	total := 1

	for i := 1; i < len(times); i++ {
		t, _ := strconv.Atoi(times[i])
		d, _ := strconv.Atoi(distances[i])
		total *= calcWays(t, d)
	}

	fmt.Println(total)

	fmt.Printf("Mega ways: %d\n", calcWays(megaTime, megaDistance))
}
