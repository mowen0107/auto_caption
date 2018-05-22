#!/bin/bash
# Author: HZT
# Create Date: 20180519


py.test --cov=./src --cov-report=html  --cov-config=.coveragerc --html=./test/html/pytest_report/report.html