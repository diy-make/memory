import psutil
import torch
import time
import os

def get_memory_usage():
    """
    Gets the current memory usage (RAM and VRAM).
    """
    # RAM usage
    ram_usage = psutil.virtual_memory()

    # VRAM usage
    vram_usage = None
    if torch.cuda.is_available():
        vram_usage = torch.cuda.memory_stats()

    return ram_usage, vram_usage

def format_bytes(bytes_val):
    """
    Formats bytes into a human-readable string (KB, MB, GB).
    """
    if bytes_val is None:
        return "N/A"
    power = 1024
    n = 0
    power_labels = {0: '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while bytes_val > power:
        bytes_val /= power
        n += 1
    return f"{bytes_val:.2f} {power_labels[n]}B"

def log_memory_usage(interval=5, duration=60):
    """
    Logs the memory usage at a specified interval for a specified duration.
    """
    print(f"--- Starting Memory Profiler (Interval: {interval}s, Duration: {duration}s) ---")
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        ram_usage, vram_usage = get_memory_usage()

        # RAM
        print(f"\n--- {time.strftime('%Y-%m-%d %H:%M:%S')} ---")
        print("RAM Usage:")
        print(f"  - Total: {format_bytes(ram_usage.total)}")
        print(f"  - Available: {format_bytes(ram_usage.available)}")
        print(f"  - Used: {format_bytes(ram_usage.used)}")
        print(f"  - Percentage: {ram_usage.percent}%")

        # VRAM
        if vram_usage:
            print("VRAM Usage:")
            for key, value in vram_usage.items():
                if "bytes" in key:
                    print(f"  - {key}: {format_bytes(value)}")
        else:
            print("VRAM Usage: Not available (PyTorch not built with CUDA support or no CUDA device found)")

        time.sleep(interval)

    print("\n--- Memory Profiler Finished ---")

if __name__ == "__main__":
    log_memory_usage()
