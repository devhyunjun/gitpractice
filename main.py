from 회원정보_입력 import createAccount
from 잔액입금 import deposit
from 잔액출력 import accountList

account_list = []


def main():
    run = True

    while run:
        print("-----------------------------------------------------------------")
        print("1.계좌생성 | 2.계좌목록 | 3.예금 |")
        print("-----------------------------------------------------------------")
        choice = input("선택> ")

        if choice == "1":
            createAccount(account_list)
        elif choice == "2":
            accountList(account_list)
        elif choice == "3":
            deposit(account_list)

        else:
            print("올바른 선택을 입력해주세요.")


if __name__ == "__main__":
    main()
