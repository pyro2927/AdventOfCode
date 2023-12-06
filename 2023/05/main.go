package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Lookup struct {
	// source, destination, range
	src, dst, rng int
}

func calcNext(seeds []int, lookup []Lookup) []int {
	newSeeds := []int{}
out:
	for _, seed := range seeds {

		// iterate over available lookups to see if we can
		// find the right lookup to use
		for _, lu := range lookup {
			if seed >= lu.src && seed < lu.src+lu.rng {
				val := lu.dst + (seed - lu.src)
				newSeeds = append(newSeeds, val)
				continue out
			}
		}

		// if none match, just append existing seed
		newSeeds = append(newSeeds, seed)
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
	seeds := []int{}

	// create lookup table for conversions based on name key
	// ex: lookups["fertilizer-to-water"][98] = 50

	lookups := make(map[string][]Lookup)

	currentMap := ""

	for scanner.Scan() {
		line := scanner.Text()

		if len(line) <= 0 {
			// ignore empty lines
			continue
		} else if strings.HasPrefix(line, "seeds:") {
			// load initial seeds
			s := strings.Split(strings.Split(line, ": ")[1], " ")

			for _, seed := range s {
				i, _ := strconv.Atoi(seed)
				seeds = append(seeds, i)
			}
		} else if strings.HasSuffix(line, "map:") {
			// update map we're loading
			currentMap = strings.Split(line, " ")[0]
			//fmt.Println(currentMap)
		} else {
			// build lookup table
			values := strings.Split(line, " ")
			length, _ := strconv.Atoi(values[2])
			srcStart, _ := strconv.Atoi(values[1])
			dstStart, _ := strconv.Atoi(values[0])

			lookup := Lookup{srcStart, dstStart, length}

			lookups[currentMap] = append(lookups[currentMap], lookup)
		}
	}

	// process w/ lookup
	//fmt.Println(seeds)

	steps := []string{"seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"}
	for _, step := range steps {
		seeds = calcNext(seeds, lookups[step])
		//fmt.Println(seeds)
	}
	// find min location
	fmt.Println(Min(seeds))
}
