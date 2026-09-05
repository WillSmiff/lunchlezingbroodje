### Generation helper for index.html

from .. import file as util_file
from .. import csv as util_csv
import shutil


def generate(templatedir, destinationdir, templateFilename):
    """Main generation function for index.html generation helper.

    templatedir -- the relative path of the template html file's directory\n
    destinationpath -- the directory where index.html should be generated\n
    templateFilename -- the filename of the index template (always index.html)\n
    """

    # Copy template to appropriate directory
    shutil.copy(f"{templatedir}/{templateFilename}", destinationdir)

    # Read categories and config csv files
    idName = "tk_category_dashname"
    categories = util_csv.dictReaderMultiRow("../csv/categories.csv", idName)
    runs = util_csv.dictReaderMultiRow("../csv/runs.csv", "tk_run_id")
    config = util_csv.dictReaderFirstRow("../csv/config.csv")

    # Replace config tk placeholders with values
    for key in config.keys():
        util_file.replaceTextInFile(f"{destinationdir}/index.html", key, config[key])

    # lk_categories handler
    tk_category_dashname = "tk_category_dashname"
    tk_category_name = "tk_category_name"
    for category in categories:
        util_file.replaceTextInFile(
            f"{destinationdir}/index.html",
            "lk_categories",
            f'<a class="categoryLink" href="categories/{categories[category][tk_category_dashname]}">{categories[category][tk_category_name]}</a>lk_categories',
        )
    util_file.replaceTextInFile(f"{destinationdir}/index.html", "lk_categories", "")

    # lk_sandwiches_eaten handler
    sandwiches_eaten = sum(
        1
        for run in runs.values()
    )
    util_file.replaceTextInFile(
        f"{destinationdir}/index.html",
        "lk_sandwiches_eaten",
        f"Aantal broodjes gegeten: <strong>{sandwiches_eaten}</strong>",
    )

    # lk_costs_made handler
    costs_made = sum(
        3.71
        for run in runs.values()
    )
    util_file.replaceTextInFile(
        f"{destinationdir}/index.html",
        "lk_costs_made",
        f"Euro's verspild: <strong>€{costs_made}</strong>",
    ) 