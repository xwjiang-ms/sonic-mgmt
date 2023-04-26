import re
import sys
from typing import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    stage_files = sys.argv[1:]
    retval = 0
    for stage_file in stage_files:
        conditions = []
        with open(stage_file, 'r') as f:
            file_contents = f.readlines()
            if not file_contents:
                continue
            for line in file_contents:
                if re.match('^[a-zA-Z]', line):
                    conditions.append(line.strip().rstrip(":"))
            sorted_conditions = conditions[:]
            sorted_conditions.sort()
            if conditions != sorted_conditions:
                print("The entries in tests/common/plugins/conditional_mark/tests_mark_conditions*.yaml are not sorted in alphabetic order.")
                retval = 1
    return retval


if __name__ == "__main__":
    raise SystemExit(main())
