import requests
import re
import time

CAP_EXAM_URL = 'https://www.cap.ca/programs/medals-and-awards/prizes-students/university-prize-exam/'
IFTTT_URL = 'https://maker.ifttt.com/trigger/2023_happened/json/with/key/Y8PV4q9Q5XZ9dv5b1Ce3m'
OLD_NEWS = 20 # this many unrelated 2023's
SLEEP = 24 * 60 * 60

# get and check website text daily
def scan():
    capsite = requests.get(CAP_EXAM_URL).text
    cnt = re.findall('2023', capsite)
    return cnt != OLD_NEWS

# notify when new 2023 detected
def main():
    while True:
        if scan():
            requests.post(IFTTT_URL)
        time.sleep(SLEEP)

if __name__ == '__main__':
    main()