Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def solution(brown, yellow):
    total = brown + yellow
    answer = []

    for width in range(1,total+1):
        if total % width == 0:
            height = total//width
            if (2*width+2*height-4 == brown) and (width >= height):
                answer.append(width)
                answer.append(height)
    return answer