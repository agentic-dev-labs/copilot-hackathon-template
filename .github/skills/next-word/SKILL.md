---
name: next-word
description: Workshop demo of how Copilot writes text. Use only when the user types /next-word followed by an unfinished sentence; it guesses the next word with rough chances and changes nothing.
argument-hint: "an unfinished sentence, like: What a nice day, let's go to the"
user-invocable: true
disable-model-invocation: true
---

# Next Word

Show how a language model writes: it picks a likely next word, one word at a time, like the
predictive text on a phone.

1. Use only the unfinished sentence typed after /next-word, and ignore earlier messages.
2. On the first line, write the one word you predict comes next, in bold, with a rough chance in
   whole percent, for example: **beach** (about 45%)
3. On the second line, write `Also possible:` and the next two likely words, most likely first,
   each with a rough chance in whole percent. The three chances add up to less than 100%.
4. On the third line, write exactly: These percentages are my own rough estimate, not a
   measurement. Other words share the rest.
5. Stop there. Do not explain, and do not read or change files, use tools, or run commands.
