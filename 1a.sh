#!/usr/bin/env bash


cut -d',' -f15,17 flightdelays1.csv |grep SFO | head -3 | cut -d',' -f1 > first3sfo.csv

cat first3sfo.csv | csvlook