def print_all_tables() -> None:
    for dan in range(2, 21):
        print(f"[{dan}단]")
        for num in range(1, 10):
            print(f"{dan} x {num} = {dan * num}")
        print()


def print_single_table(dan: int) -> None:
    if dan < 2 or dan > 20:
        print("2부터 20 사이의 숫자를 입력하세요.")
        return

    print(f"[{dan}단]")
    for num in range(1, 10):
        print(f"{dan} x {num} = {dan * num}")


def main() -> None:
    raw = input("원하는 단을 입력하세요(전체는 엔터): ").strip()
    if raw == "":
        print_all_tables()
        return

    if not raw.isdigit():
        print("숫자를 입력하세요.")
        return

    print_single_table(int(raw))


if __name__ == "__main__":
    main()
