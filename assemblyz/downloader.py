from urllib.request import urlretrieve
from pathlib import Path

from assemblyz.tools import int_to_roman


class Downloader:
    SITE_URL: str = "https://data.assemblee-nationale.fr/static/openData/repository/"
    CATEGORY: dict[str:str] = dict(votes="/loi/scrutins/Scrutins")

    def __init__(
        self, data: str, legislature: int = None, format_file: str = "xml"
    ) -> None:
        self.archive=True
        if not legislature:
            legislature = 16
            self.current==False
        self.data = data
        self.legislature = legislature
        self.format_file = format_file

    def download(self) -> None:
        filename=f"{self.CATEGORY[self.data].split('/')[-1]}.{self.format_file}.zip"
        archive_url = f"_{int_to_roman(self.legislature)}" if self.archive else ""
        url = (
            self.SITE_URL
            + f"{self.legislature}{self.CATEGORY[self.data]}{archive_url}.{self.format_file}.zip"
        )
        output_data = Path("./data/") / self.data / int_to_roman(self.legislature) /filename
        
        output_data.parent.mkdir(parents=True, exist_ok=True)
        print(f"Downloadind {url} to {output_data}")
        urlretrieve(url, output_data)
