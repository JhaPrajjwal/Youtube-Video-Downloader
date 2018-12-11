import pytube

link = input("Enter Video Link: ")

obj = pytube.YouTube(link)
result = obj.streams.all()
print("Processing......")

for i in range(len(result)):
    print(str(i+1)+".",result[i])

option = int(input("Select the option of stream for download: "))
selected = obj.streams.get_by_itag(result[option-1].itag)

print("Please wait. You will be prompted when the video gets Downloaded.")

selected.download()

print("The video has been Downloaded in the same folder where this script exists.")
