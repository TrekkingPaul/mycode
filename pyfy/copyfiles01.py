#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Coping files on the local system"""

# standard library
import shutil

def main():
    shutil.copyfile('/home/student/mycode/pyfy/ciscoex.json', '/home/student/mycode/pyfy/ciscoex.json.bkup')
    # that was easy!

if __name__ == "__main__":
    main()

