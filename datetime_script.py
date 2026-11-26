# Python script to print current date and time
from datetime import datetime

def main():
    current_datetime = datetime.now()
    print("Current date and time:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    main()