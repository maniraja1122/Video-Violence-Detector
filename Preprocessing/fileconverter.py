count=0
for img in os.listdir(data_dir+"/violence"):
    img = keras.preprocessing.image.load_img(data_dir+"/violence/"+img, target_size=(im_size, im_size))
    img.save(f"drive/MyDrive/new_violence/violence/{count}.jpg")
    count+=1
    print(f"{count} Images Saved")
    clear_output()
count=0
for img in os.listdir(data_dir+"/non_violence"):
    img = keras.preprocessing.image.load_img(data_dir+"/non_violence/"+img, target_size=(im_size, im_size))
    img.save(f"drive/MyDrive/new_violence/non_violence/{count}.jpg")
    count+=1    
    print(f"{count} Images Saved")
    clear_output()