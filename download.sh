#!/bin/bash
## Download only train dataset. [!] Threre's only train csv in csv directory.
# For 221 server
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStrain_1 --fourcc mp4v --start 780000 --end 790000 > ./log/log_11 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStrain_2 --fourcc mp4v --start 790000 --end 800000 > ./log/log_12 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStrain_3 --fourcc mp4v --start 800000 --end 810000 > ./log/log_13 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStrain_4 --fourcc mp4v --start 810000 --end 820000 > ./log/log_14 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStrain_5 --fourcc mp4v --start 820000 --end 830000 > ./log/log_15 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStrain_6 --fourcc mp4v --start 830000 --end 840000 > ./log/log_16 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVStrain_7 --fourcc mp4v --start 840000 --end 850000 > ./log/log_17 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVStrain_8 --fourcc mp4v --start 850000 --end 860000 > ./log/log_18 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVStrain_9 --fourcc mp4v --start 860000 --end 870000 > ./log/log_19 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVStrain_10 --fourcc mp4v --start 870000 --end 880000 > ./log/log_20 &