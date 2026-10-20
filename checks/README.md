# Checks for Your Website

This folder holds the tests you write on Day 3. A test is a short file that checks your page
for you, so you do not have to look again after every change.

- Tests live in files named `test_<something>.py` in this folder, for example `test_us1.py`.
- `website.py` is a ready-made helper that reads your page. Do not change it.
- Run every test from the terminal with `pytest checks`. Green means pass; red shows what failed.

A test checks what is written in your files: titles, buttons, sample data, and that every
picture and style the page uses exists. Clicking and counting stays your own manual check in
the Website preview. Write those in your requirements file as **Manual checks**.

Ask Copilot, for example:

> Write tests in checks/test_us1.py for the acceptance criteria of US-1 in my requirements file
> that can be checked from the files, using `from website import Page`. List the others under
> "Manual checks" in the requirements file. Then run `pytest checks` and show me the result.
