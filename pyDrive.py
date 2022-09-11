from googleApi import Drive
from input import  InputParams

def main():
    input_params  = InputParams()
    args = input_params.parse_args()
    drive = Drive(args.credentials)
    # if args.download:
    #     drive.download_file(args.files, args.destination)
    # else:
    #     drive.upload_file(args.files, args.destination)

if __name__ == '__main__':
    main()
