import time

current_time = time.time()

time_formatted = f"{current_time:,.4f}"
time_notation = f"{current_time: .2e}"

current_date = time.strftime("%b %d %Y", time.localtime(current_time))

print(
    f"Seconds since January 1, 1970: {time_formatted} or {time_notation} in scientific notation"
)
print(current_date)
