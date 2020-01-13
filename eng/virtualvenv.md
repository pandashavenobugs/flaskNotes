# why do we need to use virtualenv?
* because we need to use different interpreter(python2 or python3)

* to install virtualvenv
    ```bash
    sudo apt-get install python3-venv
    ```

## how to use virtualvenv
```bash
python3 -m venv <name of virtualvenv-environment>
```
* for instance :

```bash
python3 -m venv flaskproject1
```
* but you want not to think of giving a speical name to virtualenv. You may give a name venv to it. for instance:
```bash
python3 -m venv venv
```
# How to activate venv system
* if you want to activate venv system in ubuntu

    ```bash
    source <the name you give>/bin/activate
    ```
* I have named berat to venv. So I am supposed to use "berat" name for example:
    ```bash
    source berat/bin/activate
    ```
* if you leave virtualvenv:
    ```bash
    deactive
    ```

