#!/bin/bash

python captureImages.py &
sleep 3
python sendImages.py &
