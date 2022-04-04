##Compare ALT branches
This library compares binary packages for ALT Linux distributions 'sisyphus' and 'p10'.  
Comparison is made for all available architectures.

There are several features of interest:
1. Packages present in 'p10' distribution, but absent in 'sisyphus'.
2. Packages present in 'sisyphus', but absent in 'p10'.
3. Packages that have a higher version in 'sisyphus' than in 'p10'.

Results are returned as a JSON structure of the following format:
```JSON
[   
    {"type": "only_in_second_branch",   
    "packages": []},   
    {"type": "only_in_first_branch",   
    "packages": [ ]},   
    {"type": "version_higher_in_first_branch",   
    "packages": [ ]}   
]
```   
A mock example of a resulting structure:
```JSON
[
{"type": "only_in_p10", "packages": [{"arch": "armh", "name": "libnpth-debuginfo", "version": "1.6"},
                                     {"arch": "x86_64", "name": "libsmokeqtopengl4", "version": "4.14.3"}]},
{"type": "only_in_sisyphus", "packages": [{"arch": "armh", "name": "curlftpfs-debuginfo", "version": "0.9.2"}]},  
{"type": "version_higher_in_sisyphus", "packages": [{"arch": "ppc64le", "name": "qtscriptgenerator", "version": "0.2.0"}]}
]
```
##Use
When using the library in a python script it is recommended to only use the main module, and the function `comp()` that
returns the JSON structure on the request. By default, the utility compares branches *'sisyphus'* and *'p10'*,
but it's possible to compare custom branches. To do so, call the `comp()` function with branch names passed as a comma-separated string:
```python
import compare_alt_branches
result = compare_alt_branches.comp()
```
The library is available as a CLI utility, tested on Unix systems.   
To run the utility, make the file *compare_alt_branches.py* executable and run it:  
```bash
$ chmod +x compare_alt_branches.py
$ ./compare_alt_branches.py
```
Help is available through the console argument `-h` or `--h`:
```bash
$ ./compare_alt_branches.py -h
```
By default, the utility compares branches *'sisyphus'* and *'p10'*, but it's possible to compare custom branches using 
the console argument `-b` or `--branch` and providing branches as a comma-separated string:
```bash
$ ./compare_alt_branches.py -b "p9, p10"
```