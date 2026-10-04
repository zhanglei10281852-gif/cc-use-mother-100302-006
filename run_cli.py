"""具身机器人能力集成门禁命令行冒烟入口。"""

import json
import sys
from dataclasses import asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from robot_integration import CapabilityRelease


def main() -> None:
    item = CapabilityRelease(**{'release_code': 'release-code-001', 'robot_family': 'robot-family-001', 'capability': 'capability-001', 'state': 'draft'})
    print(json.dumps({"item": asdict(item), "fingerprint": item.fingerprint()}, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
