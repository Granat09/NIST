import os
from shutil import copyfile


def get_class(subdir):
    (filepath, filename) = os.path.split(subdir)
    print('nazwa pliku', filename)
    return filename

def main():
    by_class_dir = "D:/inzynier/wyciete znaki/odreczne/litery"
    output_dir = "D:/inzynier/klasy/litery"
    index = 0
    class_index = -1
    counter = 0
    n_copied = 0
    classes = []
    for subdir, dirs, files in os.walk(by_class_dir):
        for file in files:

            if get_class(subdir) not in classes:
                classes.append(get_class(subdir))
                class_index = get_class(subdir)
                index=0
                print("Copied " + os.path.join(subdir, file) + " to "
                      + os.path.join(output_dir, "class_{}_index_{}.png".format(class_index, index)))

            else:

                print('index',index,'klasa',get_class(subdir))

                print("Copied " + os.path.join(subdir, file) + " to "
                      + os.path.join(output_dir, "class_{}_index_{}.png".format(class_index, index)))
            print("Copied " + os.path.join(subdir, file) + " to "
                      + os.path.join(output_dir, "class_{}_index_{}.png".format(class_index, index)))
            copyfile(os.path.join(subdir, file),
                     os.path.join(output_dir, "class_{}_index_{}.png".format(class_index, index)))

            index += 1
            n_copied += 1
            counter += 1
        a=len(classes)
        print("Total images: " + str(n_copied))
        print('liczba klas', a)


if __name__ == "__main__":

    main()

