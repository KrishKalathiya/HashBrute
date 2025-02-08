# HashBrute

Credit to BearcatCTF 2025 for making the challenge which inspired this code.

## Description

It is a simple python script that convert words given in an input file to every possible leet speek variant. Each variant is then hashed, and the hash value is compared against 
an input hash value.

### Which hashing algorithms can I use?
Any! I have it set to SHA1 by default.

### How reliable is it?
I have used it in BearcatCTF 2025 to be the 8th quickest team (out of ~15 who got it overall, in a competition of ~120teams) to retrieve the flag for 850 points.
As long as the word and word list are reasonably short, it should give you a result in a few minutes.
If you find that the leetspeek conversions you are looking for are missing, you can always update the dictionary to check for your specific conversion patterns.

#### Only for educational use.
