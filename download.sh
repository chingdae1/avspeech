#!/bin/bash
## Download only train dataset. [!] Threre's only train csv in csv directory.
# For 221 server
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStest_1 --fourcc mp4v --start 0 --end 10000 > ./log/log_1 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStest_2 --fourcc mp4v --start 10000 --end 20000 > ./log/log_2 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStest_3 --fourcc mp4v --start 20000 --end 30000 > ./log/log_3 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStest_4 --fourcc mp4v --start 30000 --end 40000 > ./log/log_4 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStest_5 --fourcc mp4v --start 40000 --end 50000> ./log/log_5 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd1/AVStest_6 --fourcc mp4v --start 50000 --end 60000 > ./log/log_6 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVStest_7 --fourcc mp4v --start 60000 --end 70000 > ./log/log_7 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVStest_8 --fourcc mp4v --start 70000 --end 80000 > ./log/log_8 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVStest_9 --fourcc mp4v --start 80000 --end 90000 > ./log/log_9 &
nohup python3 main.py --csv_dir ./csv --result_dir /ssd2/AVStest_10 --fourcc mp4v --start 90000 --end 100000 > ./log/log_10 &