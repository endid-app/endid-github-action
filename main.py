#!/usr/bin/python3

import os
import endid

def main():
    token = os.environ["INPUT_TOKEN"]
    message = os.environ["INPUT_MESSAGE"]

    endid_output = endid.call(token=token, message=message, writeprefs=False, readprefs=False, printoutput=True)

    print(f"::set-output name=response::{endid_output}")

if __name__ == "__main__":
    main()
