#!/bin/bash
# This script displays body of the response of a JSOn Post request
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
