#!/bin/bash
#Responsible for sending JSON POST requests with passed args
curl -sX POST -H "Content-Type: Application/json" -d @$2 $1
