def start_end_dec(fun):
    def wrapper():
        print("start")
        fun()
        print("end")

    return wrapper


def print_name():
    print("alex")


# print_name = start_end_dec(print_name)
# print_name()

# The above lines can be re-written as the
@start_end_dec
def print_name():
    print("Alex!!")


print_name()