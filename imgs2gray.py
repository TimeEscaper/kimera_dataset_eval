import argparse
from pathlib import Path

import cv2


def main():
    parser = argparse.ArgumentParser(description="Converts RGB frames to greyscale")
    parser.add_argument("--dir", "-d", required=True)
    args = parser.parse_args()
    dir_path = Path(args.dir)

    dir_files = dir_path.glob('*.png')
    dir_files = [it for it in dir_files if it.is_file()]

    new_dir = dir_path / "grey"
    new_dir.mkdir(parents=False, exist_ok=True)

    for img_file in dir_files:
        img = cv2.imread(str(img_file))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        new_path = new_dir / img_file.name
        cv2.imwrite(str(new_path), img)

if __name__ == '__main__':
    main()
