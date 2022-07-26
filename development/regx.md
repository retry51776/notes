# Regx

> If there is complex regex, try to break into [reg1, reg2 ....], better to maintain multi simple regx than a complex one
```bash

# zip
^[0-9]{5}(?:-[0-9]{4})?$

# example group
[^a-Z0-9]

# Integer
'^[\-\+]?[0-9]+'

start indicator *  = ?+
optional test?

\w is word
\d is digit
\s is space

{4} is word only with 4 char
\w{5,10} is word with 5 to 10 char

[abc]at means any word starts with (a, b, c)

group is []
captor group is (), add name is (?<groupname>\d{3})
look behind selector ?<=
negative look behind  ?<!
(?<=[(t|T)he ])word will match the book, the world

look ahead selector ?=
.(?=at) will match cat, mat

none capture group is (?:[a-d])zzzz is match zzzz from azzzz
```