# The Complete System: 1/2.1/3.1/2.2/3.2/3.3
## Hosting Information
Run docker using ```docker compose up --build -d```.

2.2: give link for web interface
## Challenge Layout
```
1 -> 2.1 -> 2.2
  -> 3.1 -> 3.2 -> 3.3
```
## Topics
1.0: SSH Spray

2.1: Reversing

2.2: Malicious File Upload
     PHP RCE

3.1: PCAP Analysis

3.2: NMAP
     Request Forgery

3.3: Cryptographic Analysis
## Difficulty
- 1: Easy
- 2.1: Easy
- 2.2: Medium
- 3.1: Easy
- 3.2: Medium
- 3.3: Hard
## Flag
- 1: Intake{bubbles}
- 2.1: Intake{c2c4ctf_changeme}
- 2.2: Intake{dragon}
- 3.1: Intake{192.168.1.74}
- 3.2: Intake{SECRET_doNotOpen_onPainOfDeath.txt}
- 3.3: Intake{Th3Gre4testC0unt3rH4ck}
## Category
- 1: Misc
- 2.1: Rev
- 2.2: Web
- 3.1: Forensics
- 3.2: Misc
- 3.3: Crypto
## Descriptions
1   Jeremy believes his PC has been hacked and had his password changed. Can you access it?
    He rememebers that his username is jeremy, and his PC has a static IP of 192.168.1.10.
    We have set you up on a laptop on the same network, which you can SSH into with guest:guest.
    The flag is in the format: Intake{*password*}

2.1 Now that you've got access to Jeremy's PC, can you find what the attacker uploaded and what it does?
    Jeremy's antivirus noticed a virus upload - but could not contain it in time.
    Surely the virus will have to be activated somehow - and where does it communicate with?
    The flag is in the format: Intake{*subdomain*}

2.2 Now that you've found the webserver, can you have a look around?
    We've managed to isolate a local copy so you don't arouse suspicion, running on port 80.
    The flag is in the format: Intake{*password*}

3.1 Now you've accessed Jeremy's PC, can you find the IP of the original attacker PC?
    Some logs would be really useful wouldn't they?
    Shame the attacker deleted them all ¯\\_(ツ)_/¯
    The flag is in the format: Intake{*IP Address*}

3.2 You've got the IP - can you get in, or do they keep their machine up-to-date?
    The flag is in the format: Intake{*filename.ext*}

3.3 What is in that file? Our best codebreakers don't understand it - but do you?
