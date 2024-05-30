# Introduction

this project is to load rdf serialized file into neo4j database

# Usage

## install prerequisite

```shell
python3 -m pip install -r requirements.txt
```

## download serialized rdf file

download and unzip the following files from [MatKG 1.3](https://zenodo.org/records/10022727) and extract the nt file.

| file | url |
|------|-----|
| ENTPTNERDOI.nt.tar.gz | https://zenodo.org/records/10022727/files/ENTPTNERDOI.nt.tar.gz?download=1 |
| SUBRELOBJ.nt.tar.gz   |https://zenodo.org/records/10022727/files/SUBRELOBJ.nt.tar.gz?download=1 |

## convert to neo4j

```shell
python3 load.py --password <password> --input_rdf <path/to/ENTPTNERDOI.nt>
python3 load.py --password <password> --input_rdf <path/to/SUBRELOBJ.nt>
```

## browse the KG

visit **http://localhost:7474**, browse with cypher.
