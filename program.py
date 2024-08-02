import psutil

def get_disk():
    partitions = pautil.disk_partitions()
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"Free: {usage.free / (1024 ** 3):.2f} GB")
get_disk()
