import platform
import multiprocessing
import socket
from psutil import virtual_memory


def main():
    """ This function prints out system information such as the machine's name, OS name and version etc. """

    print("----- System Information -----")
    print("Machine Name: ", platform.node())
    print("Operating System Platform: ", platform.platform())
    print("Operating System Version: ", platform.release())
    print("Number of CPUs: ", multiprocessing.cpu_count())

    # Display total memory in GB
    total_memory = virtual_memory().total / 1e9
    print("Total Memory (GB): ", total_memory)

    host_ip = socket.gethostbyname(socket.gethostname())
    print("IP Address: ", host_ip)


if __name__ == '__main__':
    main()

