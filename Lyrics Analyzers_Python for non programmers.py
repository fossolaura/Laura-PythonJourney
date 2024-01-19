# SPLITTING A STRING

from re import split


text = """Lying, thinking
Last night
How to find my soul a home
Where water is not thirsty
And bread loaf is not stone
I came up with one thing
And I don’t believe I’m wrong
That nobody,
But nobody
Can make it out here alone.

Alone, all alone
Nobody, but nobody
Can make it out here alone.

There are some millionaires
With money they can’t use
Their wives run round like banshees
Their children sing the blues
They’ve got expensive doctors
To cure their hearts of stone.
But nobody
No, nobody
Can make it out here alone.

Alone, all alone
Nobody, but nobody
Can make it out here alone.

Now if you listen closely
I'll tell you what I know
Storm clouds are gathering
The wind is gonna blow
The race of man is suffering
And I can hear the moan,
'Cause nobody,
But nobody
Can make it out here alone.

Alone, all alone
Nobody, but nobody
Can make it out here alone."""

print(text)
print(len(text)) # Gives the # of characyers not words.

# To count the words, you first need to seprate each word using the split fxn
print(text.split())
# once the words are sussecfully split, count the lenght of the split fxn
print(len(text.split())) # 164 words

# COUNTING THE WORDS
# Lets try with a simple example

text = """
a b c A a b
"""
print(text.split())

word_count = {}

for word in text.lower().split():
  if word in word_count:
    word_count[word] += 1
  else:  
   word_count[word] = 1
print(word_count)

#Now lets try this with our poem
text = """
Lying, thinking
Last night
How to find my soul a home
Where water is not thirsty
And bread loaf is not stone
I came up with one thing
And I don’t believe I’m wrong
That nobody,
But nobody
Can make it out here alone.

Alone, all alone
Nobody, but nobody
Can make it out here alone.

There are some millionaires
With money they can’t use
Their wives run round like banshees
Their children sing the blues
They’ve got expensive doctors
To cure their hearts of stone.
But nobody
No, nobody
Can make it out here alone.

Alone, all alone
Nobody, but nobody
Can make it out here alone.

Now if you listen closely
I'll tell you what I know
Storm clouds are gathering
The wind is gonna blow
The race of man is suffering
And I can hear the moan,
'Cause nobody,
But nobody
Can make it out here alone.

Alone, all alone
Nobody, but nobody
Can make it out here alone.
"""
print(text.split())

word_count = {}

for word in text.lower().split():
  if word in word_count:
    word_count[word] += 1
  else:  
   word_count[word] = 1
print(word_count)