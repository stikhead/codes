# before our data ever touches pytorch or bert, it must go through a tokenizer.
# A tokenizer is basically a massive, pre-compiled dictionary that chops sentences into pieces (called tokens)
# and assign a specific ID  number to each piece

from transformers import AutoTokenizer

# download the massive multilingual dictionary
model_name = "bert-base-multilingual-cased"
tokenizer = AutoTokenizer.from_pretrained(model_name)

text = "Kinda surrealistic second half tbh But if it's screening in your city you can watch it imo Very heavy swearing tho btw 1st half was really good But surrealistic =/= bad if you're into surrealistic or endings open to interpretation"

# translate the string into bert's numbers
output = tokenizer(text)
print("what bert sees (numbers):")
print(output['input_ids'])

# reverse engineer it to see exactly hwo it chopped the text up
print("\n how bert chopped it up:")
print(tokenizer.convert_ids_to_tokens(output['input_ids']))

# we will see things like [CLS], [SEP] and words split apart with ##
# [CLS] (clasification): BERT automatically injects this at the absolute begging of every sentence.
# it stands for "classification". when we fine tune bert later to classify text,
# pytorch actually only looks at the math associatted with this specific [cls] token to make its final decision

# [SEP] (seperator): bert injects this at the end to say "the sentence stops here".
# if we feed it two sentences at once, it puts [sep] between them so it knows were one ends and the next begins.

# ## symbol (subword tokenization): if bert doesnt know a massive, complex word, it doesnt crash.
# it aggresively chops the word into smaller syllables that it does know and put ## in front of the pieces to reminds itself,
# that specific piece belongs attached to the word before it. 
# thisw is how it bandles over 100 languages without running out of ram
