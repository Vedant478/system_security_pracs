# Static Code Analysis using Open Source Tool - Flawfinder

### What is Flawfinder
FlawFinder is a python based tool that helps in finding vulnerabilities in a C/C++ source code. It examines the source code and gives the list of possible vulnerabilities/flaws in the code as the output.

### Installation of Flawfinder
```
pip install flawfinder
```
### Usage 
```
flawfinder vulnerable_code.py
```
### Vulnerable Code Output with Flawfinder 

```
ANALYSIS SUMMARY:

Hits = 2
Lines analyzed = 11 in approximately 0.02 seconds (522 lines/second)
Physical Source Lines of Code (SLOC) = 10
Hits@level = [0]   1 [1]   0 [2]   1 [3]   0 [4]   1 [5]   0
Hits@level+ = [0+]   3 [1+]   2 [2+]   2 [3+]   1 [4+]   1 [5+]   0
Hits/KSLOC@level+ = [0+] 300 [1+] 200 [2+] 200 [3+] 100 [4+] 100 [5+]   0
Minimum risk level = 1
```

### Patched Code Output with Flawfinder

```
ANALYSIS SUMMARY:

No hits found.
Lines analyzed = 11 in approximately 0.02 seconds (663 lines/second)
Physical Source Lines of Code (SLOC) = 10
Hits@level = [0]   1 [1]   0 [2]   0 [3]   0 [4]   0 [5]   0
Hits@level+ = [0+]   1 [1+]   0 [2+]   0 [3+]   0 [4+]   0 [5+]   0
Hits/KSLOC@level+ = [0+] 100 [1+]   0 [2+]   0 [3+]   0 [4+]   0 [5+]   0
Minimum risk level = 1
```
