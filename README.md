# CCLF File Layouts

This set of scripts generates fake files and data to adhere to the
specifications outlined in the CMS Accountable Care Organization – Operational
System (ACO-OS) Claim and Claim Line Feed (CCLF) Information Packet (IP) Version
38.0, dated 02/02/2024

The PDF for this specification can be
[downloaded here](https://www.cms.gov/files/document/cclf-information-packet.pdf).

Each of the file types is generated using a Python script that generates random
data based on the specifications provided in the PDF.

Open `main.py` and change the `number_of` properties as desired, then execute
`main.py` to generate the files. For example:

```bash
python3 main.py
```

This will generate fake CCLF files for each of the file types listed in the PDF.

The generated files will be written to the `_output` directory and have a
filename that includes the date, time, and type of file. The filenames follow
the formats specified in the requirements.

Each file contains random data based on the specifications provided in the PDF.

The scripts use [Faker](https://faker.readthedocs.io/en/master/) to produce
pseudo-random data for fields such as dates and names. The Faker library is used
to generate realistic looking data, but it does not guarantee that the data will
be realistic or accurate in any way.

## Resources

- [Beneficiary Dual Status Code](https://resdac.org/cms-data/variables/edual1-12)
- [Carrier Claim Payment Denial Code](https://resdac.org/cms-data/variables/carrier-claim-payment-denial-code)
- [Claim Diagnosis Code I Diagnosis Present on Admission (POA) Indicator Code (FFS)](https://resdac.org/cms-data/variables/claim-diagnosis-code-i-diagnosis-present-admission-poa-indicator-code-ffs)
- [Claim Frequency Code (FFS)](https://resdac.org/cms-data/variables/claim-frequency-code-ffs)
- [Claim Medicare Non-Payment Reason Code](https://resdac.org/cms-data/variables/claim-medicare-non-payment-reason-code)
- [Claim Service Classification Type Code Table](https://resdac.org/cms-data/variables/claim-service-classification-type-code-ffs)
- [Claim Source Inpatient Admission Code (FFS)](https://resdac.org/cms-data/variables/claim-source-inpatient-admission-code-ffs)
- [Line CMS Provider Specialty Code](https://resdac.org/cms-data/variables/line-cms-provider-specialty-code)
- [Line CMS Type Service Code](https://resdac.org/cms-data/variables/line-cms-type-service-code)
- [Line Place Of Service Code (FFS)](https://resdac.org/cms-data/variables/line-place-service-code-ffs)
- [Line Primary Payer Code (if not Medicare)](https://resdac.org/cms-data/variables/line-primary-payer-code-if-not-medicare)
- [Line Processing Indicator Code](https://resdac.org/cms-data/variables/line-processing-indicator-code)
- [NCH Primary Payer Code (if not Medicare)](https://resdac.org/cms-data/variables/nch-primary-payer-code-if-not-medicare)
- [Patient Discharge Status Code (FFS)](https://resdac.org/cms-data/variables/patient-discharge-status-code-ffs)
- [Revenue Center APC or HIPPS Code](https://resdac.org/cms-data/variables/revenue-center-apc-or-hipps-code)
- [Revenue Center Code (FFS)](https://resdac.org/cms-data/variables/revenue-center-code-ffs)
- [FIPS State and County Codes](https://transition.fcc.gov/oet/info/maps/census/fips/fips.txt)

## Outstanding questions

- CLM_LINE_CVRD_PD_AMT: specified as X(15) but reads like a dollar amount
- CLM_LINE_ALOWD_CHRG_AMT: specified as X(17) but reads like a dollar amount
- FIPS Codes for State and County are zero-prefixed but we treat them as int in Athena. This might not be ideal if we use lookups.
- CCLF0, Table 26 indicates that start position is 70, end position is 70 but length is 1. I filled it with a space but the Lambda assumes there is no data. Which is correct?


## Todo:

[ ] Months is awkward. All we're doing is starting with 2024-01-01 and adding 1
month and replicating all the data across the files. Instead, here's what we
should do:

1. Create Beneficiaries
2. Create Providers
3. Starting with current month, create claims that take place in that month.
4. Subtract one month and create claims that take place in THAT month.
5. Repeat until we've satisfied the number of months desired.

Claim number should be YYYYMMDD###### so we have unique claim numbers no matter
what.

That, or we ignore months and do something else. Maybe we specify a month and
all claims take place in that month.

- ./output/cache
- ./output/YYYYMMDD/CCLF1/
- ./output/YYYYMMDD/CCLF2/
