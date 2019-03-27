#!/bin/bash
## Download only train dataset. [!] Threre's only train csv in csv directory.
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStrain_1 --fourcc mp4v --start 0 --end 2000 > ./log/log_1 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStrain_2 --fourcc mp4v --start 2000 --end 4000 > ./log/log_2 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStrain_3 --fourcc mp4v --start 4000 --end 6000 > ./log/log_3 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStrain_4 --fourcc mp4v --start 6000 --end 8000 > ./log/log_4 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStrain_5 --fourcc mp4v --start 8000 --end 10000 > ./log/log_5 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStrain_6 --fourcc mp4v --start 10000 --end 12000 > ./log/log_6 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVStrain_7 --fourcc mp4v --start 12000 --end 14000 > ./log/log_7 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVStrain_8 --fourcc mp4v --start 14000 --end 16000 > ./log/log_8 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVStrain_9 --fourcc mp4v --start 16000 --end 18000 > ./log/log_9 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVStrain_10 --fourcc mp4v --start 18000 --end 20000 > ./log/log_10 &