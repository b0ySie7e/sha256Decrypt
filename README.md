# sha256Decrypt

## USO:

```python
❯ python3 decrypt.py
usage: decrypt.py [-h] -w WORDLIST -H HASHES
decrypt.py: error: the following arguments are required: -w/--wordlist, -H/--hashes

```

```python

❯ python3 decrypt.py -w /usr/share/wordlists/rockyou.txt -H user_password

Contraseña encontrada para abc: abc

```

## ¿Tienes problemas?

```python
❯ python3 decrypt.py -w /usr/share/wordlists/rockyou.txt -H user_password
Traceback (most recent call last):
  File "/home/b0ysie7e/seven/sha256Decrytp/decrypt.py", line 47, in <module>
    user_hash(args.wordlist, args.hashes)
  File "/home/b0ysie7e/seven/sha256Decrytp/decrypt.py", line 30, in user_hash
    if check_password_hash(hash_value, password):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/werkzeug/security.py", line 128, in check_password_hash
    return hmac.compare_digest(_hash_internal(method, salt, password)[0], hashval)
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/werkzeug/security.py", line 70, in _hash_internal
    raise ValueError(f"Invalid hash method '{method}'.")
ValueError: Invalid hash method 'sha256'.
```

Probablemente este problema lo presentes debido a que la version de `werkzeug` sea mayor a la 2.2, en las versionas superiores presente este problema y no invetigue a detalle de como solucionarlo haciendo uso de una versión superior, pero lo logre solucionar con un entorno virtual.

### Instalación de virtualenv

```python
> pip install virtualenv
Defaulting to user installation because normal site-packages is not writeable
Collecting virtualenv
  Downloading virtualenv-20.25.0-py3-none-any.whl (3.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.8/3.8 MB 7.6 MB/s eta 0:00:00
Collecting distlib<1,>=0.3.7
  Downloading distlib-0.3.8-py2.py3-none-any.whl (468 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 468.9/468.9 KB 9.6 MB/s eta 0:00:00
Collecting platformdirs<5,>=3.9.1
  Downloading platformdirs-4.1.0-py3-none-any.whl (17 kB)
Collecting filelock<4,>=3.12.2
  Downloading filelock-3.13.1-py3-none-any.whl (11 kB)
Installing collected packages: distlib, platformdirs, filelock, virtualenv
Successfully installed distlib-0.3.8 filelock-3.13.1 platformdirs-4.1.0 virtualenv-20.25.0
```
### Creando nuestro entorno

```python
> virtualenv -p /usr/bin/python3.8 env
created virtual environment CPython3.8.15.final.0-64 in 1529ms
  creator CPython3Posix(dest=/home/b0ysie7e/Escritorio/web/env, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/b0ysie7e/.local/share/virtualenv)
    added seed packages: pip==23.3.1, setuptools==69.0.2, wheel==0.42.0
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

```

### Activar el entorno

```python
❯ source env/bin/activate
```

### Desactivar el entorno

```python
❯ deactivate
```

Luego de activar el entorno, lo unico que debemos de hacer es dirigirnos a nuestro directorio donde creamos nuestro entorno, en mi caso `env` e installar la libreria que necesitamos.

```python
❯ pip install werkzeug==2.2
```

Y con eso puedes solucionar el problema.
