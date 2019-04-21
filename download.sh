#!/bin/bash
## Download only train dataset. [!] Threre's only train csv in csv directory.
# For 221 server
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStrain_1 --fourcc mp4v --start 280000 --end 290000 > ./log/log_11 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStrain_2 --fourcc mp4v --start 290000 --end 300000 > ./log/log_12 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStrain_3 --fourcc mp4v --start 300000 --end 310000 > ./log/log_13 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStrain_4 --fourcc mp4v --start 310000 --end 320000 > ./log/log_14 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStrain_5 --fourcc mp4v --start 320000 --end 330000 > ./log/log_15 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStrain_6 --fourcc mp4v --start 330000 --end 340000 > ./log/log_16 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVStrain_7 --fourcc mp4v --start 340000 --end 350000 > ./log/log_17 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVStrain_8 --fourcc mp4v --start 350000 --end 360000 > ./log/log_18 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVStrain_9 --fourcc mp4v --start 360000 --end 370000 > ./logsh /log_19 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVStrain_10 --fourcc mp4v --start 370000 --end 380000 > ./log/log_20 &