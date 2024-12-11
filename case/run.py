import GENERAL
from util import read

general_api_list = read.api_list('../api_data/general')
scenario_api_list = read.api_list('../api_data/scenario/image')
all_list = read.api_list('../api_data')


## 고정
def tc_valid_one():
    tc = GENERAL.GENERAL()
    tc.para_loop_2('valid')


def tc_invalid_one():
    tc = GENERAL.GENERAL()
    tc.para_loop_2('invalid')


def tc_header_one():
    tc = GENERAL.GENERAL()
    tc.header_loop()


## 전체
def tc_valid_general():
    for api_list in general_api_list:
        tc = GENERAL.GENERAL(api_list)
        tc.para_loop_2('valid')


def tc_invalid_general():
    for api_list in general_api_list:
        tc = GENERAL.GENERAL(api_list)
        tc.para_loop_2('invalid')


def tc_header_general():
    for api_list in general_api_list:
        tc = GENERAL.GENERAL(api_list)
        tc.header_loop()


if __name__ == "__main__":
    tc_valid_general()
    # tc_invalid_general()
    # tc_header_general()
