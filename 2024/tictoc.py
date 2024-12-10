import math
import time
from typing import Generator


def create_tic_toc_generator() -> Generator[float, None, None]:
    # Generator that returns time differences
    # ti = 0  # initial time
    tf = time.perf_counter()  # final time
    while True:
        ti = tf
        tf = time.perf_counter()
        yield tf - ti  # returns the time difference


tic_toc = create_tic_toc_generator()  # create an instance of the TicTocGen generator


# This will be the main function through which we define both tic() and toc()
def toc(message: str = '', print_value: bool = True) -> None:
    # Prints the time difference yielded by generator instance TicToc
    temp_time_interval = next(tic_toc)
    if print_value:
        if temp_time_interval > 1e-15:
            power = math.floor(math.log10(temp_time_interval)) + 1
            if power >= 0:
                power = 0
            else:
                power = power - power % 3
            units = ['s', 'ms', 'us', 'ns', 'ps', 'fs']
            temp_time_interval /= 10 ** power
            unit = units[- power // 3]
        else:
            unit = 's'
        print(f"[toc] {message} {temp_time_interval:.2f} {unit}")
        tic()


def tic() -> None:
    # Records a time in TicToc, marks the beginning of a time interval
    toc(print_value=False)
