import glob
from PIL import Image

# jpg 파일명 경로 받기
imglist_jpg = glob.glob('C:/Users/82109/Desktop/PythonWorkspace/khuthon/피카츄/*.jpg')
# png 파일명 경로 받기
# imglist_png = glob.glob('C:/Users/82109/Desktop/PythonWorkspace/khuthon/고라파덕/*.png')

# 각각 파일 불러서 리스트에 저장
img_jpg = Image.open(imglist_jpg[0])
# img_png = Image.open(imglist_png[0])

# 가로, 세로 변환 크기 설정
width = 150
height = 150

# jpg 파일 변환
for img_path in imglist_jpg:
    img_jpg = Image.open(img_path)
    resize_img = img_jpg.resize((width, height), Image.ANTIALIAS)
    resize_img.save(img_path)

# png 파일 변환
# for img_path in imglist_png:
#     img_png = Image.open(img_path)
#     resize_img = img_png.resize((width, height), Image.ANTIALIAS)
#     resize_img.save(img_path)