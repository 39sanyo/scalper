import time

def 30_timer:
    print("Test text")
    seconds = 30
    while seconds > 0:
        print(f"\rTime remaining {seconds}...", end="")
        time.sleep(1)
        seconds -= 1
    print("done... redirected")


if __name__ == "__main__":
    main()
