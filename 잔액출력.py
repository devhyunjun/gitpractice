import pandas as pd
def accountList(account_list):
    print("--------------")
    print("계좌목록")
    print("--------------")

    if len(account_list) == 0:
        print("등록된 계좌가 없습니다.")
    else:
        for account in account_list:
            print(f"계좌번호: {account['ano']}")
            print(f"계좌주: {account['owner']}")
            print(f"잔액: {account['balance']}")
            print("--------------------")