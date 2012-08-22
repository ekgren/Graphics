import random
import Image
 
def get_random_start_and_end_points_in_file(file_data):
    start_point = random.randint(10, len(file_data))
    end_point = start_point + random.randint(0, len(file_data) - start_point)
 
    return start_point, end_point
 
def splice_a_chunk_in_a_file(file_data):
    start_point, end_point = get_random_start_and_end_points_in_file(file_data)
    section = file_data[start_point:end_point]
    repeated = ''
 
    for i in range(1, random.randint(1,3)):
        repeated += section
 
    new_start_point, new_end_point = get_random_start_and_end_points_in_file(file_data)
    file_data = file_data[:new_start_point] + repeated + file_data[new_end_point:]
    return file_data
   
def glitch_an_image(local_image):
    file_handler = open(local_image, 'rb')
    file_data = file_handler.read(16)
    file_handler.close()
    for i in range(1, random.randint(1,5)):
        file_data = splice_a_chunk_in_a_file(file_data)
 
    file_handler = open('data/output.bmp', 'wb')
    file_handler.write(file_data)
    file_handler.close
 
    return local_image
 
if __name__ == '__main__':
    image_glitch_file = glitch_an_image('data/test.bmp')