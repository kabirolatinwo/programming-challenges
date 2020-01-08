"""
Decrypt String from Alphabet to Integer Mapping (Easy)

Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.

 

Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
Example 2:

Input: s = "1326#"
Output: "acz"
Example 3:

Input: s = "25#"
Output: "y"
Example 4:

Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
Output: "abcdefghijklmnopqrstuvwxyz"
 

Constraints:

1 <= s.length <= 1000
s[i] only contains digits letters ('0'-'9') and '#' letter.
s will be valid string such that mapping is always possible.
"""

"""
function that converts digits to characters
KNOWN LIMITATIONS - solution can be optimized
"""
def freqAlphabets(s):
    if (type(s) != str):
        return "Invalid Input"
    decrypted_string = ""
    last_hash_pos = 0
    for i in range(len(s)):
        #if we get to a #, convert all digits from last # pos until you get to the two digits
        #   right before the #
        #Then concatenate the two digits and convert to the respective character
        if (s[i] == '#'):
            for x in range(last_hash_pos, (i-2)):
                decrypted_string += chr(int(s[x])+96)
            decrypted_string += chr(int(s[i-2:i])+ 96)
            last_hash_pos = i+1
        elif (not s[i].isdigit()):
            return "Invalid Input"
        else:
            continue
    #after going through the string, convert any digits after the last # pos to characters
    if (last_hash_pos-1 != len(s)):
        for i in range(last_hash_pos, len(s)):
            decrypted_string += chr(int(s[i])+96)
    return decrypted_string

"""
function that declares and initializes strings to be tested
"""
def test_freqAlphabets():
    #initialize input strings. for testing purposes, i have created multiple valid and invalid tuples.
    # the input string is in index 0 and the expected output is in index 1
    test_num = 0
    empty_string = ("","")
    non_int_string = ("abcd","Invalid Input")
    single_char_invalid = ('k', "Invalid Input")
    simple_invalid_string = ("12.345", "Invalid Input")
    mixed_invalid_string = ("1*2c4?.d", "Invalid Input")
    simple_string = ("12345", "abcde")
    one_letter_string = ("9", "i")
    double_digit_letter = ("25#", "y")
    simple_string_2 = ("10#11#12", "jkab")
    long_string = ("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#", "abcdefghijklmnopqrstuvwxyz")

    for test_list in (empty_string,
                      non_int_string,
                      single_char_invalid,
                      simple_invalid_string,
                      mixed_invalid_string,
                      simple_string,
                      one_letter_string,
                      double_digit_letter,
                      simple_string_2,
                      long_string):
        test_num+=1
        print ("================ Test ", test_num, " ================")
        print ("Input: ", test_list[0])
        print ("Expected: ", test_list[1])
        print ("Output: ", freqAlphabets(test_list[0]))
        if (test_list[1] == freqAlphabets(test_list[0])):
            print ("PASS")
        else:
            print ("FAIL")

if __name__ == '__main__':    
    test_freqAlphabets()