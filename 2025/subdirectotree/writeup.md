# SubDirectoTree
I'm sure I left it somewhere around here..?
<hr />

A file-traversal forensics challenge where it's a huge tree of directories! But somewhere, maybe, there might be a flag hidden...

## MS Windows

**Using the ```tree``` command** in Command Prompt, you can see all subdirectories and files of the current directory.

How you want to do it from there is personal preference, but here's what I thought of (no-one said it had to be elegant!):
- Pipe output to file (```tree > tree.txt```) and scroll across on the file to the bottom directory. Scroll down until something sticks out. :P

**Using File Explorer** to check the size of directory contents to find the correct one at each stage.

## Linux

Using the command ``` find . -type f -exec stat -c%s%n {} + | sort -rh``` will show you all the files from the current directory downwards, sorted by filesize (presumably the flag is a decent size!).

- ```find . -type f```: shows all files from the current directory recursively.
- ```stat -c%s%n```: gets filesize of each of the files.
- ```sort -rh```: sorts in reverse, so biggest files first, using the human-readable format.

Or, use ```find``` to find only files, and hope there aren't loads of duds (*uh oh*)!

``` 
find ./ -type f -print
```

## Final Processing

After finding the flag, you have to flip the text. You can do this using an online tool (e.g. [https://www.textreverse.com/](https://www.textreverse.com/)), or by writing custom code to do it for you.

If you're curious... there are about **1500** folders in total!

## Solution

<details>
  <summary>Click to reveal solution</summary>
The flag (backwards) is in this file:
   ```
   ./doorway/52f4/e15d/6f64/b05a/,
   ```

   Then, flip it!
</details>

<hr />

Created by **Peter Walker**<br />
President | Warwick Cyber Security Society<br />
[https://www.linkedin.com/in/p3ter-w/](https://www.linkedin.com/in/p3ter-w/)
