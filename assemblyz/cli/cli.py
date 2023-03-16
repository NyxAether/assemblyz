import argparse

from assemblyz.downloader import Downloader



def main()->None:
    parser = argparse.ArgumentParser(description="Manipule les données de l'assemblée nationale")
    subparsers = parser.add_subparsers(dest='command',help="Sous commandes")
    download_parser = subparsers.add_parser(
        "download", help="Télécharge les dernières données de l'assemblée"
    )
    download_parser.add_argument("--data",default="votes")
    download_parser.add_argument("--legislature",type=int)
    download_parser.add_argument("--format",default="xml")
    args = parser.parse_args()
    if args.command == "download":
        downloader = Downloader(args.data, args.legislature, args.format)
        downloader.download()


    

if __name__ == '__main__':
    main()