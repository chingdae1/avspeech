#!/bin/bash
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVS_1 --fourcc mp4v --start 0 --end 3000 > ./log/log_1 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVS_2 --fourcc mp4v --start 3000 --end 6000 > ./log/log_2 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVS_3 --fourcc mp4v --start 6000 --end 9000 > ./log/log_3 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVS_4 --fourcc mp4v --start 9000 --end 12000 > ./log/log_4 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVS_5 --fourcc mp4v --start 12000 --end 15000 > ./log/log_5 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVS_6 --fourcc mp4v --start 15000 --end 18000 > ./log/log_6 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVS_7 --fourcc mp4v --start 18000 --end 21000 > ./log/log_7 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVS_8 --fourcc mp4v --start 21000 --end 24000 > ./log/log_8 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVS_9 --fourcc mp4v --start 24000 --end 27000 > ./log/log_9 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVS_10 --fourcc mp4v --start 27000 --end 30000 > ./log/log_10 &
