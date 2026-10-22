---
name: next-word
description: Workshop demo of how Copilot writes text. Use only when the user types /next-word followed by an unfinished sentence; it replies with the one most likely next word and its chance, and changes nothing.
argument-hint: "an unfinished sentence, like: What a nice day, let's go to the"
user-invocable: true
disable-model-invocation: true
---

# Next Word

Show how a language model writes: it picks the most likely next word, one word at a time, like
the predictive text on a phone. Every word of the sentence counts: a place or a person in it can
change which word is most likely.

1. Use only the unfinished sentence typed after /next-word, and ignore earlier messages.
2. Reply with exactly one line: the one word you predict comes next, in bold, then its chance in
   whole percent in brackets. For "I would like a cup of", the whole reply is: **coffee** (70%)
3. Write nothing else: no explanation, no other words or options, no note, no question. The
   percentage is your own rough estimate, not a measurement; the guide tells people so.
4. Never explain, and do not read or change files, use tools, or run commands.
