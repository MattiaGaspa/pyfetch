# pyfetch
![alt text](https://github.com/MattiaG-afk/pyfetch/blob/main/pyfetch.png)

A revisited python version of neofetch

## Installation
Type:
```shell
git clone https://github.com/MattiaG-afk/pyfetch.git
cd pyfetch
sudo python3 setup.py install
```

## Customization
In case you don't want to see some variables in the terminal or want to change the value of these (in case they are not shown correctly) you can edit the **/etc/pyfetch/pyfetch.conf** file. Here you can find all the variable, with the syntax (remember the space before and after the = character):
```shell
<variable name> = <his value>
```
As you can see, the file is already pre-compiled with default options, these are:
* auto: will use the default configuration. If you want to change the value of a variable that defaults to auto you have two other options:
  * your custom value: for example: I want modify the os_name variable from auto to kali linux, so I have to modify it to os_name = kali;
  * no: not to print its value.
* yes: will show its value by default. In this case they are variables which you can only change the visibility and not the value, to do this just change its value from yes to no.
Variables that are not expected will not be considered (all available variables are listed in the file).
### Exception: at the moment it you can't disable variable, like cpu current clock and swap percent, because they are in the same line with other values. You can only disable the whole line
