#!/bin/bash
#This command, takes a URL,dislays the size of the response.
curl -sI $1 | grep Content-Length | cut -d " " -f 2
