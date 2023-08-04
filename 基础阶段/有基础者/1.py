import time
import functools

def decorder(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print(f"{func.__name__}")

        t_start =time.time()
        result =func(*args,**kwargs)
        t_end =time.time()
        print(f"{func.__name__} start time:{time.ctime(t_start)},\t{func.__name__} end time:{time.ctime(t_end)},\tlasting time:{t_end -t_start}")
        return result
    return wrapper
@decorder
def main():
    time.sleep(1)
if __name__ == '__main__':
   main()