from datetime import datetime


def build_report(rows, errors, dups):
    lines = []

    lines.append("CSV Cleaner Report")
    lines.append(datetime.now().isoformat())
    lines.append("")
    lines.append(f"Rows: {rows}")
    lines.append("")

    if errors:
        lines.append("Errors:")
        for e in errors:
            lines.append(f"- {e}")
    else:
        lines.append("No validation errors")

    lines.append("")

    if dups:
        lines.append("Duplicates:")
        for d in dups:
            lines.append(f"- {d}")
    else:
        lines.append("No duplicates")

    return "\n".join(lines)
