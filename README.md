# msg88
 Encrypted communication through python

**Figure 1.**

Communication between B and C are facilitated by A. Passphrases are known in advance and can there own algorythm for how they are selected. See below.

<img src="https://raw.githubusercontent.com/Curt-Lucas/msg88/main/fig1.png"/>

**Workflow**
 - A (COMSEC) executes a.py
 - B (ASSET) executes b.py and enters passphrase
 - C (HANDLER) executes c.py and enters passphrase
 - B and C can now communicate securely

**Passphrases**

Used to encrypt messages being sent through commercial internet infrastructure. This needs to be complex.

Client/Server from https://github.com/patmwoo/python-client-server
