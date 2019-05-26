#!/usr/bin/env bash

cut flightdelays1.csv -d',' -f18 | sort | uniq -c |sort -n | tail -3 | csvlook
echo 'Edith Adinku'
