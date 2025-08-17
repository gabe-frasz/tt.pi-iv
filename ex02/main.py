import numpy as np

COLD = 5
HOT = 10

temperatures = np.array([2.5, 3.2, 5.1, 6.3, 7.0, 8.1, 10.5, 9.8, 8.5, 7.3,
    6.2, 5.1, 4.5, 3.8, 5.6, 6.7, 7.2, 8.3, 10.1, 9.4,
    8.2, 7.0, 6.3, 5.4, 4.7, 3.9, 5.8, 6.9, 7.4, 8.5,
    10.3, 9.6, 8.4, 7.2, 6.5, 5.6, 4.9, 4.1, 5.9, 7.0,
    7.5, 8.6, 10.4, 9.7, 8.5, 7.3, 6.6, 5.7, 5.0, 4.2,
    6.0, 7.1, 7.6, 8.7, 10.6, 9.9, 8.7, 7.5, 6.8, 5.9,
    5.2, 4.4, 6.1, 7.2, 7.7, 8.8, 10.7, 10.0, 8.8, 7.6,
    6.9, 6.0, 5.3, 4.5, 6.2, 7.3, 7.8, 8.9, 10.8, 10.2,
    9.0, 7.8, 7.1, 6.2, 5.5, 4.7, 6.3, 7.4, 7.9, 9.0,
    10.9, 10.3, 9.1, 7.9, 7.2, 6.3, 5.6, 4.8, 6.4, 7.5])

mean = np.mean(temperatures)
median = np.median(temperatures)
std_deviation = np.std(temperatures, mean=mean)
coldest_temperatures_idx = np.where(temperatures <= COLD)
hottest_temperatures_idx = np.where(temperatures >= HOT)

print("\n" + "="*40)
print("   🌡️ Temperature Analysis Report 🌡️")
print("="*40)

print("\n📊 Statistical Summary")
print("----------------------------------------")
print(f"Mean Temperature:   {mean:.2f}°C")
print(f"Median Temperature: {median:.2f}°C")
print(f"Standard Deviation: {std_deviation:.2f}°C")

print("\n" + "="*40)
print("        🧊 Temperature Extremes 🔥")
print("="*40)

print(f"\n🥶 Coldest Days (<= {COLD}°C)")
print("----------------------------------------")
if coldest_temperatures_idx[0].size > 0:
    for i in coldest_temperatures_idx[0]:
        print(f"  - Day {i + 1:<3}: {temperatures[i]:.1f}°C")
else:
    print("  - No exceptionally cold days recorded.")

print(f"\n🥵 Hottest Days (>= {HOT}°C)")
print("----------------------------------------")
if hottest_temperatures_idx[0].size > 0:
    for i in hottest_temperatures_idx[0]:
        print(f"  - Day {i + 1:<3}: {temperatures[i]:.1f}°C")
else:
    print("  - No exceptionally hot days recorded.")

print("\n" + "="*40 + "\n")
