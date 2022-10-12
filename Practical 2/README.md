# Vulnerability Scanning using Nikto in Kali Linux

### Nikto Tool
Nikto is an Open Source software written in Perl language that is used to scan a web-server for the vulnerability that can be exploited and can compromise the server. It can also check for outdated version details of 1200 server and can detect problems with specific version details of over 200 servers. It can also fingerprint server using favicon.ico files present in the server. It is not designed to be a particularly a stealth tool rather than it is designed to be fast and time-efficient to achieve the task in very little time. Because of this, a web admin can easily detect that its server is being scanned by looking into the log files. 

### Installation
Nikto is pre-installed on Kali Linux hence no seperate installation is required.

### Usage
```
$ nikto -host www.google.com
```
### Nikto Output
```
$ nikto -h

Option host requires an argument

       -config+            Use this config file
       -Display+           Turn on/off display outputs
       -dbcheck            check database and other key files for syntax errors
       -Format+            save file (-o) format
       -Help               Extended help information
       -host+              target host/URL
       -id+                Host authentication to use, format is id:pass or id:pass:realm
       -list-plugins       List all available plugins
       -output+            Write output to this file
       -nossl              Disables using SSL
       -no404              Disables 404 checks
       -Plugins+           List of plugins to run (default: ALL)
       -port+              Port to use (default 80)
       -root+              Prepend root value to all requests, format is /directory
       -ssl                Force ssl mode on port
       -Tuning+            Scan tuning
       -timeout+           Timeout for requests (default 10 seconds)
       -update             Update databases and plugins from CIRT.net
       -Version            Print plugin and database versions
       -vhost+             Virtual host (for Host header)
                + requires a value

        Note: This is the short help output. Use -H for full help text.
        
```

```
$ nikto -host vulnweb.com    

- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          44.228.249.3
+ Target Hostname:    vulnweb.com
+ Target Port:        80
+ Start Time:         2022-10-10 14:43:06 (GMT-4)
---------------------------------------------------------------------------
+ Server: nginx/1.19.0
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ ERROR: Error limit (20) reached for host, giving up. Last error: error reading HTTP response
+ Scan terminated:  20 error(s) and 3 item(s) reported on remote host
+ End Time:           2022-10-10 14:44:40 (GMT-4) (94 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

```
$ nikto -host vulnweb.com -o reuslt.html -Format html
```
   [result.html](https://github.com/Encryptor-Sec/system-security/blob/main/Practical_2/reuslt.html)
```
$ nikto -host google.com -ssl     

- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          142.251.42.110
+ Target Hostname:    google.com
+ Target Port:        443
---------------------------------------------------------------------------
+ SSL Info:        Subject:  /CN=*.google.com
                   Ciphers:  TLS_AES_256_GCM_SHA384
                   Issuer:   /C=US/O=Google Trust Services LLC/CN=GTS CA 1C3
+ Start Time:         2022-10-10 14:50:14 (GMT-4)
---------------------------------------------------------------------------
+ Server: gws
+ X-XSS-Protection header has been set to disable XSS Protection. There is unlikely to be a good reason for this.
+ Uncommon header 'alt-svc' found, with contents: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"
+ The site uses SSL and the Strict-Transport-Security HTTP header is not defined.
+ The site uses SSL and Expect-CT header is not present.
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ Root page / redirects to: https://www.google.com/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Server banner has changed from 'gws' to 'sffe' which may suggest a WAF, load balancer or proxy is in place
+ Uncommon header 'cross-origin-resource-policy' found, with contents: cross-origin
+ Cookie 1P_JAR created without the httponly flag
+ Cookie NID created without the secure flag
+ Server is using a wildcard certificate: *.google.com
+ Allowed HTTP Methods: GET, HEAD 
+ End Time:           2022-10-10 14:52:40 (GMT-4) (94 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```
