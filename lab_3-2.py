int(a)
# "a" is not defined
# after run: "a" was not defined

int('a')
# "a" is not defined
# after run: terminal ignores the statement

'a' + 2
# 'a' has no variable set
# after run: nothing happens, nothing was set to = 'a'

import date
# "date" has nothing attatched to import
# after run: nothing happens

print("I'm a happy camper!)
# no second quotation mark, statement does not go through
# after run: whole line is typed out, including "print"