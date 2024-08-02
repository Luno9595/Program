import psutil
import subprocess

def get_disk():
    partitions = pautil.disk_partitions()
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"Free: {usage.free / (1024 ** 3):.2f} GB")
        
def get_swap():
    result = subprocess.run(["swapon", "-s"], capture_output=True, text=True)
    print(result.stdout)
        
get_swap_info()
get_disk()
