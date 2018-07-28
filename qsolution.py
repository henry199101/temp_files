def longest_subpalindrome_slice(text):
    "Return (i,j) such that text[i:j] is the longest palindrome in text."
    if text == '': return (0,0)

    def length(slice): a,b = slice; return b-a

    candidates = [grow(text, start, end)
                    for start in range(len(text))
                    for end in (start, start+1)]

    return max(candidates, key=length)

def grow(text, start, end):
    "Start with a 0- or 1- length palindrome; try to grow a bigger one."

    while (start > 0 and end < len(text)
            and text[start-1].upper() == text[end].upper()):
        start -= 1; end += 1

    return (start, end)

def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == L('Racecar') == L('RacecarX') == (0, 7)
    print("All test cases pass!")

if __name__ == "__main__":
	test()
else:
	print("Importing ", __name__, "...Done!")
