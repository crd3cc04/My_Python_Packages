# my_lambdata/my_mod.py or my_lambdata.my_script
# file for functions

def enlarge(n):
        return n * 100

if __name__ == "__main__":
        # only if run from the comman line, invoke the following code:
        #otherwise, don't

        print("Junk")
        print("Global Scope")

        y = float(input("Please Input A Number To Enlarge:"))
        print(enlarge(y))