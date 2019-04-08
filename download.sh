#!/bin/bash
## Download only train dataset. [!] Threre's only train csv in csv directory.
# For 221 server
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStrain_1 --fourcc mp4v --start 140000 --end 142000 > ./log/log_1 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStrain_2 --fourcc mp4v --start 142000 --end 144000 > ./log/log_2 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStrain_3 --fourcc mp4v --start 144000 --end 146000 > ./log/log_3 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStrain_4 --fourcc mp4v --start 146000 --end 148000 > ./log/log_4 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStrain_5 --fourcc mp4v --start 148000 --end 150000 > ./log/log_5 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStrain_6 --fourcc mp4v --start 150000 --end 152000 > ./log/log_6 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVStrain_7 --fourcc mp4v --start 152000 --end 154000 > ./log/log_7 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVStrain_8 --fourcc mp4v --start 154000 --end 156000 > ./log/log_8 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVStrain_9 --fourcc mp4v --start 156000 --end 158000 > ./log/log_9 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVStrain_10 --fourcc mp4v --start 158000 --end 1600000 > ./log/log_10 &