#!/bin/bash
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVS_2 --fourcc mp4v --start 3000 --end 6000 > ./log/log_2 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVS_4 --fourcc mp4v --start 9000 --end 12000 > ./log/log_4 &
