import sys
import datetime
import json
import csv

# track-it start "Fixing serialization bug"

def StorageLogs():
    logs = []
    title = ""
    
    while True :
        command = input().split(' ')
        if command[0] == "track-it":
            if len(command) > 1:
                if command[1] == "start":
                    if len(command) > 2:
                        for x in range(len(command)):
                            if x >= 2:
                                title = title + " " + command[x]
                        time = datetime.datetime.now()
                        logs.append([time.day,time.month,time.year,time.hour,time.minute, time.second,"start", title])
                        title = ""
                elif command[1] == "stop":
                        if len(command) > 2:
                            for x in range(len(command)):
                                if x >= 2:
                                    title = title + " " + command[x]
                            time = datetime.datetime.now()
                            logs.append([time.day,time.month,time.year,time.hour,time.minute, time.second,"stop", title])
                            title = ""
                elif command[1] == "export":
                    if command[2] == "--format=csv":
                        with open("logs.csv", mode='w', newline='') as file:
                            header = ["Day", "Month", "Year", "Hour", "Minute", "Second", "Action", "Title"]
                            writer = csv.writer(file)
                            writer.writerow(header)
                            writer.writerows(logs)
                    elif command[2] == "--format=json":
                        pass
                    else:
                        print("ERROR : this format doesnt worked (--format=json, --format=csv)")
                else:
                    print("ERROR : the command has to use start or stop")
                print(logs)
            else:
                print("ERROR : the command has to use start or stop")
        else :
            print("ERROR : the command has to start with track-it")
def main():
    StorageLogs()

if __name__ == '__main__':
    main()