def deposit(account_list):
    print("--------------")
    print("예금")
    print("--------------")
    ano = input("계좌번호: ")
    money = int(input("예금액: "))

    for account in account_list:
        if account["ano"] == ano:
            account["balance"] += money
            print("결과: 예금이 성공되었습니다.")
            print(f"잔액: {account['balance']}")
            break
    else:
        print("해당하는 계좌가 없습니다.")