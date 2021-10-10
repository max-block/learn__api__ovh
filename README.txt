https://docs.ovh.com/gb/en/api/first-steps-with-ovh-api/
https://github.com/ovh/python-ovh

--> check learn_pypi_ovh repo!!!

--> get api token
https://eu.api.ovh.com/createToken/ Attention! Login via username only, don't user email!

--> signature
"$1$" + SHA1_HEX(AS+"+"+CK+"+"+METHOD+"+"+QUERY+"+"+BODY+"+"+TSTAMP)
