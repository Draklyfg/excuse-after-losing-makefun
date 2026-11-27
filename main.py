"""Write one original excuse an agent gives after losing a bounty."""

import os


ENTRY = "I lost the bounty, but my post-loss analysis confirms I would lose it again in 97% of parallel universes."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
