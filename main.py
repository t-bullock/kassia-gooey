import logging

from gooey import Gooey, GooeyParser

from kassia import Kassia


@Gooey(program_name="Kassia Simple GUI",
       show_stop_warning=False,
       show_success_modal=False,
       show_failure_modal=False,
       menu=[{
           'name': 'File',
           'items': [{
               'type': 'AboutDialog',
               'menuTitle': 'About',
               'name': 'Kassia Gooey',
               'description': 'An Simple Kassia GUI',
               'version': '0.0.1',
               'copyright': '2021',
               'website': 'https://github.com/t-bullock/kassiagooey',
               'developer': 'https://github.com/t-bullock/',
               'license': 'MIT'
           }]
        }, {
           'name': 'Help',
           'items': [{
               'type': 'Link',
               'menuTitle': 'Documentation',
               'url': 'https://github.com/t-bullock/kassia/wiki'
           }]
       }]
       )
def get_args():
    parser = GooeyParser(description="A Simple GUI for Exporting Kassia Scores")

    parser.add_argument(
        "input_file",
        help="The score to be processed (in .xml format)",
        type=str,
        widget="FileChooser",
    )

    parser.add_argument(
        "output_file",
        help="The name and location of the score to generate (in PDF format)",
        type=str,
        widget="FileSaver",
    )

    return parser.parse_args()


def main():
    args = get_args()
    Kassia(args.input_file, args.output_file)


if __name__ == "__main__":
    logging.basicConfig(level=logging.WARN, format='%(asctime)s - %(levelname)s - %(message)s')
    main()
