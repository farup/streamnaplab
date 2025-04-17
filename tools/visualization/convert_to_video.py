import argparse

import os



import cv2

import sys 

sys.path.append("/cluster/home/terjenf/naplab")

def parse_args():
    parser = argparse.ArgumentParser(
        description='Visualize groundtruth and results')
    
    parser.add_argument(
        '--image-folder',
        help='path to folder with predictions (images)'
    )
   
    
    parser.add_argument(
        '--pred', 
        default=True, 
        help='If semantic predictions or not'
    )
    args = parser.parse_args()

    return args



def sort_func(e):
    return e.split("_")[-1]


def sort_func_pred(e):
    return int(e.split("_map_")[-1].split(".")[0])


def get_img_paths(file_path, pred=False): 
    if os.listdir(file_path):

        
        img_paths = [os.path.abspath(os.path.join(file_path, f)) for f in os.listdir(file_path)]

        if pred: 
            img_paths.sort(key=sort_func_pred)
        else:
            img_paths.sort(key=sort_func)

        return img_paths 
       
    
def convert_images_to_video(image_files, output_file, fps=8):
    # Get the list of image files in the input folder
    # Read the first image to get its dimensions
    first_image = cv2.imread(image_files[0])
    height, width, _ = first_image.shape

    # Create a VideoWriter object to save the video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Specify the codec for the output video file
    video = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    # Iterate over each image and write it to the video
    for image_file in image_files:
        
        frame = cv2.imread(image_file)
        video.write(frame)
    
    # Release the video writer and close the video file
    video.release()
    cv2.destroyAllWindows()
    print("Saved video to", output_file)


if __name__ == "__main__": 

    args = parse_args()

    files = get_img_paths(args.image_folder, eval(args.pred))

    name = f"{(args.image_folder).split('visualizations')[1].split('pred')[0].replace('/', '')}.mp4"

    convert_images_to_video(files, os.path.join(args.image_folder.split("pred")[0], name))


