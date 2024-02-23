import argparse
from glob import glob
import PyPDF2


def Merge(args) -> None:
    print(f"\n> merge {args.input_dir_path}/*.pdf to {args.output_file_path}")
    merger = PyPDF2.PdfMerger()
    for input_file_name in sorted(glob(f"{args.input_dir_path}/**/*.pdf", recursive=True)):
        input_file_name = str(input_file_name).replace("\\", "/").replace("//", "/")
        merger.append(input_file_name)
    output_file_name = str(args.output_file_path).replace("\\", "/").replace("//", "/")
    merger.write(output_file_name)
    merger.close()
    print("\n> successfull completed")
    return


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser(description="thats this: cli pdf merger")
    argument_parser.add_argument(
        "-i", "--input_dir_path", required=True, type=str, metavar="", help="path to directory required"
    )
    argument_parser.add_argument(
        "-o", "--output_file_path", default="./output/main.pdf", type=str, metavar="", help="path to file required"
    )
    Merge(argument_parser.parse_args())
