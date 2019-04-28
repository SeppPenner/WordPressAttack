# WordPressAttack

WordPressAttack is written and tested in Python 3.7.3. Its purpose is to describe how a wordpress website can be attacked.

[![Build status](https://ci.appveyor.com/api/projects/status/5vxr69c6mmgyvj7m?svg=true)](https://ci.appveyor.com/project/SeppPenner/wordpressattack)
[![GitHub issues](https://img.shields.io/github/issues/SeppPenner/WordPressAttack.svg)](https://github.com/SeppPenner/WordPressAttack/issues)
[![GitHub forks](https://img.shields.io/github/forks/SeppPenner/WordPressAttack.svg)](https://github.com/SeppPenner/WordPressAttack/network)
[![GitHub stars](https://img.shields.io/github/stars/SeppPenner/WordPressAttack.svg)](https://github.com/SeppPenner/WordPressAttack/stargazers)
[![GitHub license](https://img.shields.io/badge/license-AGPL-blue.svg)](https://raw.githubusercontent.com/SeppPenner/WordPressAttack/master/License.txt)
[![Known Vulnerabilities](https://snyk.io/test/github/SeppPenner/WordPressAttack/badge.svg)](https://snyk.io/test/github/SeppPenner/WordPressAttack)

## How does it work:

1. Find a website to attack. I will not attack the website but I chose the following just for reference: https://pcgames-download.com/
2. Find out usernames by attaching ?author=1, ?author=2 and so on at the end of the url with Wordpress, e.g. https://pcgames-download.com/?author=1 or https://pcgames-download.com/?author=2.
This will give you the real authors' names, e.g. https://pcgames-download.com/author/pcgdwadm/ or https://pcgames-download.com/author/enigma/
3. Now we got the user names pcgdwadm and enigma. Probably, pcgdwadm is an admin and more interesting.
4. Create a password list with this programm [WordPressAttackPasswordGenerate.py](https://github.com/SeppPenner/WordPressAttack/tree/master/WordPressAttackPasswordGenerate.py) or with a password list you already own.
5. Run the [WPForce](https://github.com/n00py/WPForce) projekt on Kali or any system to attack the WordPress website.

## Disclaimer:

I am neither responsible for damage on any system nor for any hacking attempts from you guys here :smile:

Another thing: If anyone really tries to hack, there are few things to notice:

1. Smart people block their attempts per IP address whenever e.g. 5 times a password is wrong. As far as I found out, https://pcgames-download.com/ doesn't!
2. Always use proper protection, e.g. VPNs and Tor in combination.

## How do you start the project:

```python
Python WordPressAttackPasswordGenerate.py
```

Please modify the following line as you like in the [WordPressAttackPasswordGenerate.py](https://github.com/SeppPenner/WordPressAttack/tree/master/WordPressAttackPasswordGenerate.py) file:

```python
generator=itertools.combinations_with_replacement('abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVW_.,;:!?ß[](){}/\%&$§"@€^°+-*', 15)
```

## Sources:

https://stackoverflow.com/questions/11747254/python-brute-force-algorithm

https://github.com/n00py/WPForce

https://gist.github.com/roachhd/1f029bd4b50b8a524f3c

https://hackertarget.com/attacking-wordpress/

https://gist.github.com/pazdera/1121315

https://stackoverflow.com/questions/11747254/python-brute-force-algorithm


Change history
--------------

* **Version 1.0.0.0 (2018-05-10)** : 1.0 release.