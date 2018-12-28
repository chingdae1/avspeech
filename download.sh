#!/bin/bash
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVS_1 --fourcc mp4v --start 0 --end 30000 > ./log/log_1 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVS_2 --fourcc mp4v --start 30000 --end 60000 > ./log/log_2 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVS_3 --fourcc mp4v --start 60000 --end 90000 > ./log/log_3 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVS_4 --fourcc mp4v --start 90000 --end 120000 > ./log/log_4 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVS_5 --fourcc mp4v --start 120000 --end 150000 > ./log/log_5 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVS_6 --fourcc mp4v --start 150000 --end 180000 > ./log/log_6 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVS_7 --fourcc mp4v --start 180000 --end 210000 > ./log/log_7 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVS_8 --fourcc mp4v --start 210000 --end 240000 > ./log/log_8 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVS_9 --fourcc mp4v --start 240000 --end 270000 > ./log/log_9 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVS_10 --fourcc mp4v --start 270000 --end 300000 > ./log/log_10 &
