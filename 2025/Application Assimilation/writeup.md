# Application Assimilation
An OSINT challenge about recognising and researching interfaces!

## 1

The interface is clearly split into three sections:
- horizontal lines at the top, various colours
- lines of grey text in the bottom left
- text in the bottom right, with some highlighted

Other notes:
- The interface appears to be in dark mode.
- Small green icon in the top-left of the application.

<details>
<summary>Reveal Application</summary>

The application is **Wireshark**.
</details>

## 2

The interface is split into windows, each containing different content:
- the top one appears to show a small snippet of code
- the bottom one looks like data, or variables
- the right-hand one looks like code

Given that we can see the state and type of variables outside of runtime, alongside the code, we can conclude this is a decompiler.

Researching common decompilers, we can see this matches a very common one.

<details>
<summary>Reveal Application</summary>

The application is **Ghidra**.
</details>

## 3

Getting to the hard ones now!

In the top left, there appears to be a textual logo - 5 letters long.

In the centre top, there are again lines of text, similar to the first challenge. If we assume these are packets, like the first challenge, and that the red box at the top of the screen displays that the packets have been stopped...

This is then likely a proxy application, potentially allowing the editing of HTTP requests - such as at the bottom.

This one will require a little more research, given how new the tool is.

<details>
<summary>Reveal Application</summary>

The application is **Caido**.
</details>

## 4

If you've ever done risk - then you know that's what this is. Also - because she has her head in her hands: clear sign of doing risk.

The red-green scale shows the scale used to evaluate risks in this application.

She also appears to have a map of risks on her screen, with each stemming from another, like an attack tree.

Finally, the logo in the top left looks to be a red triangle with some white text.

When searching for "*risk attack tree*"...

<details>
<summary>Reveal Application</summary>

The application is **RiskTree**.
</details>



<hr />

Created by **Peter Walker**<br />
President | Warwick Cyber Security Society<br />
[https://www.linkedin.com/in/p3ter-w/](https://www.linkedin.com/in/p3ter-w/)