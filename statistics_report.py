def print_statistics(stats):

    print("\n" + "=" * 50)
    print("SECURITY ANALYTICS SUMMARY")
    print("=" * 50)

    print(
        f"Total Events Analyzed : "
        f"{stats['total_events']}"
    )

    print(
        f"Critical Events       : "
        f"{stats['critical']}"
    )

    print(
        f"High Events           : "
        f"{stats['high']}"
    )

    print(
        f"Medium Events         : "
        f"{stats['medium']}"
    )

    print(
        f"Low Events            : "
        f"{stats['low']}"
    )

    print(
        f"Most Common Event     : "
        f"{stats['most_common_event']}"
    )

    print(
        f"Most Common Tactic    : "
        f"{stats['most_common_tactic']}"
    )

    print("=" * 50)
