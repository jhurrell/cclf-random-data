# CCLF File Layouts

This set of scripts generates fake files and data to adhere to the
specifications outlined in the CMS Accountable Care Organization – Operational
System (ACO-OS) Claim and Claim Line Feed (CCLF) Information Packet (IP) Version
38.0, dated 02/02/2024

The PDF for this specification can be
[downloaded here](https://www.cms.gov/files/document/cclf-information-packet.pdf).

Each of the file types is generated using a Python script that generates random
data based on the specifications provided in the IP. The scripts are located in
the current directory and can be run from the command line using the following
commands:

```bash
python3 main.py
```

This will generate fake CCLF files for each of the file types listed in the IP.

The generated files are located in the `cclf` directory and have a filename that
includes the date, time, and type of file. The filenames follow the formats
specified in the requirements.

Each file contains random data based on the specifications provided in the IP.
The scripts use Python's built-in random number generator to generate fake data
for each field in the file. There is no intent to create realistic data, as this
would require a significant amount of time and resources. Instead, the scripts
generate random data that adheres to the specifications provided in the IP.
