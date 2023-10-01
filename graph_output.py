def ascii_colorful_horizontal_bar_chart(time_labels, values):
    max_value = max(values)
    scale_factor = 40 / max_value if max_value > 0 else 1

    for i in range(len(time_labels)):
        bar_width = int(values[i] * scale_factor)

        bar = '*' * bar_width

        color = 31 + (i % 7)
        colored_bar = f"\x1b[{color}m{bar}\x1b[0m"
        colored_percent = f"\x1b[{color}m{bar_width}%\x1b[0m"

        print(f"{time_labels[i]} | {colored_bar} {colored_percent}")

