from Read_and_Parse import read

def main():
    test_list = [("assign", 3), ("python", 9), ("recur", 1)]
    run_batch(test_list)

def run_batch(test_list):
    print("batch mode start")
    tests_passed = True
    res = 279923
    for test in test_list:
        (name, num) = test
        for n in range(1, num+1):
            f='programs/' + str(name) + str(n)+ '.py'
            new_res = read(f)
            if res != new_res:
                tests_passed = False
                print(f + "failed, program returns" + str(new_res))
    if tests_passed:
        print("All tests passed!")
    print("batch mode end")

if __name__ == "__main__":
    main()