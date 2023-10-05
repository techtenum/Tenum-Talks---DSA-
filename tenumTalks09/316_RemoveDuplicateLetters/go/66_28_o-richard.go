package main

import (
	"fmt"
	"strings"
	"slices"
)

func removeDuplicateLetters(s string) string {
	// Build the least lexicographical string.
	var unique []rune
	var charCount int
	for i, v := range s {
		// Incase of no character, add it to the end of the array
		if charCount == 0 {
			unique = append(unique, v)
			charCount++
		} else {
			// Ensure the unique array lacks the current character.
			if !slices.Contains(unique, v) {
				lastChar := unique[charCount - 1]
				// Perform a replacement of the last item only if the previous last character is present in the unexplored part of the input string.
				if lastChar > v && strings.Contains(s[i:], string(lastChar)) {
					unique[charCount - 1] = v
					// Rebuild the array from the recently swaped backwards. Example: input string: thesqtitxyetpxloeevdeqifkz
					// Base Conditions: 1. Don't exceed zero 
					// Base Conditions: 2. The value to swap should exist in the unexplored part of the input string.
					// Base Conditions: 3. The value to replace has a lesser value than what to remove.
					for x := charCount - 2; x > -1; x = x - 1 {
						if strings.Contains(s[i:], string(unique[x])) && unique[x + 1] < unique[x]{
							// Remove the value at unique[x] from the array.
							unique = append(unique[:x], unique[x + 1:]...)
							charCount--
						} else {
							break
						}
					}
				} else {
					unique = append(unique, v)
					charCount++
				}
			}
		}
	}
	var answer string
	// Convert the runes to a string
	for _, v := range unique {
		answer += string(v)
	}
	return answer
}

func main()  {
	fmt.Println(removeDuplicateLetters("thesqtitxyetpxloeevdeqifkz"))
	fmt.Println(removeDuplicateLetters("cbacdcbc"))
}