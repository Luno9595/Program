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

def get_memory():
    memory = psutil.virtual_memory()
    print(f"Used RAM: {memory.used / (1024 ** 3):.2f} GB")
        
get_memory()
get_swap()
get_disk()
