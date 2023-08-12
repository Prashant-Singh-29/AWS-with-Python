import boto3
s3 = boto3.resource('s3')
# bucket name - prashantsinghbucket1
my_bucket = s3.Bucket('prashantsinghbucket1')



# uploading a single file to s3 bucket
data = open("file1.txt", "rb")
my_bucket.put_object(Key='file1.txt', Body=data)

#uploading multiple files to s3 bucket using for loop
files = ['file2.txt', 'file3.txt']
for file in files:
    my_bucket.put_object(Key=file, Body=data)

# Download a single file from s3 bucket
my_bucket.download_file(Key="file1.txt", Filename="file4.txt")

# Download files of similar patterns
files = []
for file in my_bucket.objects.all():
    files.append(file.key)
for file_name in files:
    if ".txt" in file_name:
        name = file_name.split(".")[0] + "_download.txt"
        my_bucket.download_file(Key=file_name, Filename=name)

# Download all files
files = []
for file in my_bucket.objects.all():
    files.append(file.key)
for file_name in files:
    name = file_name.split(".")[0] + "_download." + file_name.split(".")[1]
    my_bucket.download_file(Key=file_name, Filename=name)


# Delete a file
s3.Object(my_bucket.name, "file2.txt").delete()

# upload a file
data = open("14mb_file.pdf", "r")
my_bucket.put_object(Key='14mb_file.pdf', Body=data)

