def createAccount(account_list):
    print("--------------")
    print("계좌생성")
    print("--------------")
    ano = input("계좌번호: ")
    owner = input("계좌주: ")
    balance = int(input("초기입금액: "))

    # 계좌 생성 및 정보 저장
    account = {"ano": ano, "owner": owner, "balance": balance}
    account_list.append(account)  # 계좌 정보를 리스트에 저장

    print("계좌를 등록했습니다.")
    return account_list
