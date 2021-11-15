# test.describe("kata tests")
# test.it("example tests")
# test.assert_equals(find_missing_letter(['a','b','c','d','f']), 'e')
# test.assert_equals(find_missing_letter(['O','Q','R','S']), 'P')
#

def find_missing_letter(chars):
    alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new = set(alph[alph.index(chars[0]):alph.index(chars[-1]) + 1])
    return ''.join(new - set(chars))
