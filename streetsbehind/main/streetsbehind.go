package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

var cache map[[4]int]int

func solve(n, k, a, b int) int {
	key := [4]int{n, k, a, b}
	if val, ok := cache[key]; ok {
		return val
	}

	c := 0
	y := n * (b - a) / a
	if y == 0 {
		c = -1
	} else {
		for k > 0 {
			y = n * (b - a) / a
			x := int(math.Ceil(float64(a*(y+1)) / float64(b-a)))
			d := x - n
			s := int(math.Ceil(float64(d) / float64(y)))
			if k-d <= 0 {
				s = int(math.Ceil(float64(k) / float64(y)))
			}
			c += s
			n += s * y
			k -= s * y
		}
	}
	cache[key] = c
	return c
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	scanner.Scan()
	t, _ := strconv.Atoi(scanner.Text())

	cache = make(map[[4]int]int)

	for i := 0; i < t; i++ {
		scanner.Scan()
		line := scanner.Text()
		parts := strings.Split(line, " ")
		n, _ := strconv.Atoi(parts[0])
		k, _ := strconv.Atoi(parts[1])
		a, _ := strconv.Atoi(parts[2])
		b, _ := strconv.Atoi(parts[3])

		fmt.Println(solve(n, k, a, b))
	}
}
